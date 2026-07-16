#!/usr/bin/env python3
"""WebSocket client that sends a message and prints the response."""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket server, send a message, and return the response.

    Args:
        uri: the WebSocket server URI
        text: the message to send

    Returns:
        the response received from the server
    """
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Send a message to the echo server and print the response."""
    uri = "ws://localhost:8765"
    text = "Hello WebSocket"
    response = await connect_and_send(uri, text)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
