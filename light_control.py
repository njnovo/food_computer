from kasa import Discover, Device

async def main():
    device = await Discover.discover_single(
        "10.0.0.40",
        username="Niels.novotny@gmail.com",
        password="q-XLdbs0_XG578p",
    )
    print(device.alias)

# If you are using a script, you need to run the async function using an event loop
import asyncio
asyncio.run(main())
