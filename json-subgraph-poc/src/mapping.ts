import { JSON } from "assemblyscript-json";
import { BigInt } from "@graphprotocol/graph-ts";
import { MerkleRootUpdated } from "../generated/MultiMerkleStash/MultiMerkleStash";
import { Bytes } from "@graphprotocol/graph-ts";
import { ClaimParam } from "../generated/schema";
import { data } from "./data";

// ref: https://bounties.gitcoin.co/issue/23514
// const CODE = includeBytes("../../../build/release/meme.wasm")

export function handleMerkleRootUpdated(event: MerkleRootUpdated): void {
    let jsonObj: JSON.Obj = <JSON.Obj>(JSON.parse(data));

    let addressOrNull: JSON.Str | null = jsonObj.getString("address");
    if (addressOrNull != null) {
        let address: Bytes = Bytes.fromHexString(addressOrNull.valueOf());
        let claimParam = ClaimParam.load(address);
        if (claimParam == null) {
            claimParam = new ClaimParam(address);
        }

        let tokenOrNull: JSON.Str | null = jsonObj.getString("token");
        if (tokenOrNull != null) {
            let token: Bytes = Bytes.fromHexString(tokenOrNull.valueOf());
            claimParam.token = token;
        }
        let indexOrNull: JSON.Str | null = jsonObj.getString("index");
        if (indexOrNull != null) {
            let index: BigInt = BigInt.fromString(indexOrNull.valueOf());
            claimParam.index = index;
        }
        let amountOrNull: JSON.Str | null = jsonObj.getString("amount");
        if (amountOrNull != null) {
            let amount: BigInt = BigInt.fromString(amountOrNull.valueOf());
            claimParam.amount = amount;
        }
        // let merkleProofOrNull: JSON.Arr | null = jsonObj.getArr("merkleProof");
        // if (merkleProofOrNull != null) {
        //     let merkleProof: Bytes[] = <JSON.Arr>JSON.from<Bytes[]>(merkleProofOrNull);
        //     claimParam.merkleProof = merkleProof;
        // }

        claimParam.save();
    }

    // primArr = <JSON.Arr>JSON.from<i32[]>([42]);
}
