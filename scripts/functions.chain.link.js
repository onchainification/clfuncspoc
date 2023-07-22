const request = {
    // decentralised live node (needs to be picked up by indexer):
    // url: "https://gateway.testnet.thegraph.com/api/f6cb1e63b04b4966d0566d57e42a7814/subgraphs/id/GEWddKhHEf7tASNRoLzJSEopTv5woSGzQMxijVyBRBFk",
    // centralised (hosted) node:
    // url: "https://api.thegraph.com/subgraphs/name/onchainification/json-subgraph-poc",
    // decentralised test node:
    url: "https://api.studio.thegraph.com/query/50162/json-subgraph-poc/version/latest",
    method: "POST",
    data: {
      query: `{
        claimParam(id: "0x0012a7f00af8a643ba5a6aa187f915b4c13289df") {
          token
          index
          amount
        }
      }`,
    },
  }

  const response = await Functions.makeHttpRequest(request)
  console.log(JSON.stringify(response, null, 2))

  return Functions.encodeString(response.data.data.claimParam.index)

  return Functions.encodeUint256(response.data.data.claimParam.index)
