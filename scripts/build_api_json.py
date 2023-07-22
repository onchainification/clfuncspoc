import json
import os
from pprint import pprint

from brownie import interface, web3
from rich.progress import track


DIRECTORY = "data/Votium/merkle/"
MULTI_MERKLE_STASH = interface.IMultiMerkleStash(
    "0x378Ba9B73309bE80BF4C2c027aAD799766a7ED5A"
)


def main():
    address_list = compile_address_list()
    result = {}
    for address in track(
        address_list,
        description="Generating claims object for all addresses...",
    ):
        claims = generate_claims(address)
        if len(claims) == 0:
            continue
        result[address] = claims
    json.dump(result, open("result.json", "w"), indent=4)


def compile_address_list(sample=None):
    """
    Unique addresses as per 2023-07-22: 5927 (took ~16 minutes).
    Can also pass a `sample` argument to only compile a subset of addresses.
    """
    unique_addresses = set()
    with open(os.path.join(DIRECTORY, "activeTokens.json")) as fp:
        active_tokens = json.load(fp)
    for token in track(
        active_tokens,
        description="Compiling list of all unique addresses with unclaimed incentives...",
    ):
        last_json = sorted(os.listdir(DIRECTORY + token["symbol"]))[-1]
        with open(os.path.join(DIRECTORY, token["symbol"], last_json)) as f:
            claims = json.load(f)["claims"]
            for address in claims:
                leaf = claims[address]
                if not MULTI_MERKLE_STASH.isClaimed(token["value"], leaf["index"]):
                    unique_addresses.add(address)
                if sample and len(unique_addresses) >= sample:
                    return list(unique_addresses)
    return list(unique_addresses)


def generate_claims(address):
    """
    Loop over all directories in the latest version of the official Votium
    repository (https://github.com/oo-00/Votium) and build the
    MultiMerkleStash.claimParam[] array for given `address`.
    """
    address = web3.toChecksumAddress(address)

    with open(os.path.join(DIRECTORY, "activeTokens.json")) as fp:
        active_tokens = json.load(fp)

    result = []
    for token in active_tokens:
        last_json = sorted(os.listdir(DIRECTORY + token["symbol"]))[-1]
        with open(os.path.join(DIRECTORY, token["symbol"], last_json)) as f:
            claims = json.load(f)["claims"]
            if address in claims:
                leaf = claims[address]
                if not MULTI_MERKLE_STASH.isClaimed(token["value"], leaf["index"]):
                    result.append(
                        [
                            token["value"],
                            leaf["index"],
                            int(leaf["amount"], 0),
                            leaf["proof"],
                        ]
                    )
    return result


def verify_claims(address, claims):
    """
    Simulate a claimMulti() call to Votium's MultiMerkleStash on-fork to verify
    that the claims object is valid.
    """
    print(f"Trying MultiMerkleStash.claimParam[] array for {address}:")
    pprint(claims)
    try:
        tx = MULTI_MERKLE_STASH.claimMulti(address, claims, {"from": address})
        if tx.status == 1:
            # tx.call_trace(True)  # times out too often :(
            return True
    except:
        return False


if __name__ == "__main__":
    main()
