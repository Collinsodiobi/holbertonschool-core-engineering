#!/usr/bin/env python3
"""WebSocket client that sends a message and prints the response."""

import asyncio
import os
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
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
