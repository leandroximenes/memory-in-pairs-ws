#!/usr/bin/env python

import asyncio
import signal
import os

import websockets


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    port = int(os.environ.get("PORT", "5678"))
    async with websockets.serve(
        echo,
        host="",
        port=port,
    ):
        await stop


if __name__ == "__main__":
    asyncio.run(main())