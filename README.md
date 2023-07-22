# title

## STEPS

0. TODO: somehow in ci, auto update votium submodule whenever a
    `MerkleRootUpdated` is transmitted by votium's `MultiMerkleStash`
    (0x378Ba9B73309bE80BF4C2c027aAD799766a7ED5A). eg 0x7753669d2e6418aa013bfdaf28f1603f1c6254d6fc03af5bfc397e885e38ea03

1. python backend api endpoint (TODO: implement in anvil.works?):
    - loops local merkle tree proofs
    - generates claims object
    - tests claimMulti call onfork
    - returns claims object in json if successful

2. cl funcs call custom api endpoint and grabs claims object

3. it can now call `MultiMerkleStash.claimMulti(address(this), claims)`

4. profit

## SUBGRAPH

- this subgraph can act as a decentralised, open source alternative to solutions host json files as api endpoints (eg jsonbin.io, jsonkeeper.com)
- current poc is able to read the converted json file in [`data.ts`](json-subgraph-poc/src/data.ts) and convert it to a subgraph entity
- serialisation of multiple objects should be possible according to the docs (https://www.npmjs.com/package/assemblyscript-json?activeTab=readme)
- near also added a `includeBytes` into their assemblyscript release which should enable direct reading of `.json` files from disk to memory (https://bounties.gitcoin.co/issue/23514)
- future work: upload a single json file through cli or ui and have it deployed on the graph's decentralised network

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
