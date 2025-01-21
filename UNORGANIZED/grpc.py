"""
This file is to explain GRPC briefly

GRPC: Google Remote Procedure Call

Alternatives (used before GRPC):
    - REST
    - SOAP
    - GraphQL

Types:
    - Unary:
        - Client sends a single request to the server and gets a single response back.
        - Daily life example: Requesting a webpage.
    - Server streaming
        - Client sends a single request to the server and gets a stream (multiple, continuous) of responses back.
        - Daily life example: Watching a video.
    - Client streaming
        - Client sends a stream (multiple, continuous) of requests to the server and gets a single response back.
        - Daily life example: Uploading a file, or streaming a video.
    - Bidirectional streaming
        - Both client and server send a stream of requests and responses.
        - Daily life example: Chat application.

"""