#!/usr/bin/python3
import epson_projector as epson
from epson_projector.const import (POWER)

import sys
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)


async def run(websession):
    projector = epson.Projector(
        host='192.168.10.62',
        websession=websession,
        port=80,
        encryption=False)

    cmdmapping = {
    "on": "TURN_ON",
    "off": "TURN_OFF",
    "day": "CMODE_BRIGHT",
    "night": "CMODE_NATURAL",
    }

    mode = sys.argv[1]
    if mode in cmdmapping:
        print("sending cmd "+cmdmapping[mode])
        data = await projector.send_command(cmdmapping[mode])
    else:
        print("unknown command")
#    data = await projector.get_property(POWER)
#    data = await projector.send_command("TURN_OFF")
    print(data)

asyncio.get_event_loop().run_until_complete(main())


