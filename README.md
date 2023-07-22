# title

## STEPS

1. run python backend script [`build_api_json`](scripts/build_api_json.py) to consolidate the whole votium repo into one single json. can be called manually or hook that runs it whenever the repo is committed to

2. host json on the graph's decentralised network (or permissioned central host)

3. a contract can now call this api endpoint via chainlink functions, to grab the claims object for its own address

4. it can then call `MultiMerkleStash.claimMulti(address(this), claims)` and receive rewards

5. the whole process of claiming votium bribes is now possible on-chain!

6. profit

## SUBGRAPH

- this subgraph acts as a decentralised, open source alternative to solutions that host json files as api endpoints (eg jsonbin.io, jsonkeeper.com)
- current poc is able to read the custom formatted json file in [`data.ts`](json-subgraph-poc/src/data.ts) and convert it to a subgraph entity
- serialisation of multiple objects should be possible according to the docs of the package (https://www.npmjs.com/package/assemblyscript-json?activeTab=readme)
- near platform also added an `includeBytes` into their assemblyscript release which enables direct reading of `.json` files from disk to memory (https://bounties.gitcoin.co/issue/23514)
- future work: upload a single json file through the graph cli or ui and have it deployed on the graph's decentralised network. no indexing necessary, just serve data.

### install
```
cd json-subgraph-poc
yarn
```

### dev
```
yarn codegen && yarn build
```

### deploy
```
yarn lfg
```

### urls
- https://thegraph.com/hosted-service/subgraph/onchainification/json-subgraph-poc
- https://testnet.thegraph.com/explorer/subgraphs/GEWddKhHEf7tASNRoLzJSEopTv5woSGzQMxijVyBRBFk

## REFERENCES
- https://docs.chain.link/chainlink-functions
- https://github.com/smartcontractkit/functions-hardhat-starter-kit
- https://github.com/GalloDaSballo/vested-cvx
