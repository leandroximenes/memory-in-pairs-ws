
#!/usr/bin/env python

import asyncio
import websockets
from datetime import datetime
from pytz import timezone
import signal
import os

async def handler(websocket):
    while True:
        format = "%Y-%m-%d %H:%M:%S"
        now_utc = datetime.now(timezone('America/Sao_Paulo'))
        await websocket.send(now_utc.strftime(format))
        await asyncio.sleep(1)


async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    port = int(os.environ.get("PORT", "5678"))
    async with websockets.serve(
        handler,
        host="",
        port=port,
    ):
        await stop


if __name__ == "__main__":
    asyncio.run(main())