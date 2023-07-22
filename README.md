# title

## steps

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

## references
- https://docs.chain.link/chainlink-functions
- https://github.com/GalloDaSballo/vested-cvx
