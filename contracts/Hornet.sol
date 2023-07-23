// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract Hornet is ChainlinkClient {
    using Chainlink for Chainlink.Request;
    uint256 public volume;
    address public oracle;
    bytes32 public jobId;
    uint256 public fee;

    event DataFullfilled(uint256 volume);

    constructor(address _oracle, bytes32 _jobId, uint256 _fee, address _link) {
        if (_link == address(0)) {
            setPublicChainlinkToken();
        } else {
            setChainlinkToken(_link);
        }
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
    }

    /**
     * Create a Chainlink request to retrieve API response and find the target
     * data.
     */
    function requestVolumeData() public returns (bytes32 requestId) {
        Chainlink.Request memory request = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfill.selector
        );

        // Set the URL to perform the GET request on
        request.add(
            "get",
            "https://ipfs.io/ipfs/QmXhHY63grvCCyg6CEkCiNcyTCKxLHCF5kgLWDcYXhQr1E"
        );

        request.add("path", "0x9538D438d506Fc426dB37fb83daC2a0752A02757,index");

        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }

    /**
     * Receive the response in the form of uint256
     */
    function fulfill(
        bytes32 _requestId,
        uint256 _volume
    ) public recordChainlinkFulfillment(_requestId) {
        volume = _volume;
        emit DataFullfilled(volume);
    }
}
