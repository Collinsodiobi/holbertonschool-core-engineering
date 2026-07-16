#!/usr/bin/env python3
"""ASGI WebSocket server using Starlette."""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    """Serve the homepage.

    Args:
        request: the HTTP request object

    Returns:
        HTMLResponse with a simple web page
    """
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    """Handle WebSocket connections with echo behavior.

    Args:
        websocket: the WebSocket connection object
    """
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except Exception:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
