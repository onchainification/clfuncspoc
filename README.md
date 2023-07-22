# title

## STEPS

0. TODO: somehow in ci, auto update votium submodule whenever a
    `MerkleRootUpdated` is transmitted by votium's `MultiMerkleStash`
    (0x378Ba9B73309bE80BF4C2c027aAD799766a7ED5A). eg 0x7753669d2e6418aa013bfdaf28f1603f1c6254d6fc03af5bfc397e885e38ea03

1. python backend script [`build_api_json`](scripts/build_api_json.py) consolidates the whole votium repo into one single json

2. host json on the graph network (or permissioned central host)

2. cl funcs calls this api endpoint and grabs claims object for its own address

3. it can now call `MultiMerkleStash.claimMulti(address(this), claims)`

4. profit

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

### url
https://thegraph.com/hosted-service/subgraph/onchainification/json-subgraph-poc


## REFERENCES
- https://docs.chain.link/chainlink-functions
- https://github.com/GalloDaSballo/vested-cvx
