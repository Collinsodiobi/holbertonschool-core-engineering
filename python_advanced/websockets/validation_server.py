#!/usr/bin/env python3
"""WebSocket server with message validation."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Handle incoming WebSocket connections with message validation.

    Args:
        websocket: the WebSocket connection object
    """
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """Start the WebSocket validation server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
