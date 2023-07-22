import json
import os
from pprint import pprint

from brownie import interface, web3


DIRECTORY = "data/Votium/merkle/"
MULTI_MERKLE_STASH = interface.IMultiMerkleStash(
    "0x378Ba9B73309bE80BF4C2c027aAD799766a7ED5A"
)


def main(address="0x9f6e831c8f8939dc0c830c6e492e7cef4f9c2f5f"):
    claims = generate_claims(address)
    print(f"Trying MultiMerkleStash.claimParam[] array for {address}:")
    pprint(claims)
    try:
        tx = MULTI_MERKLE_STASH.claimMulti(address, claims, {"from": address})
        if tx.status == 1:  # successful
            tx.call_trace(True)
            print("Success!")
            return json.dumps(claims)
    except:
        print("Failed!")
        return None


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
    if len(result) > 0:
        return result


if __name__ == "__main__":
    main()
