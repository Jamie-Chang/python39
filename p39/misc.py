## asyncio
import asyncio, datetime, time

SEC = datetime.timedelta(seconds=1)


def sleep(length: datetime.timedelta):
    time.sleep(length / SEC)
    print("Awaken")


async def lecture():
    while True:
        print("$%^&")
        await asyncio.sleep(0.15)


async def main():
    await asyncio.gather(
        lecture(),
        asyncio.to_thread(sleep, datetime.timedelta(minutes=45)),
        asyncio.to_thread(sleep, datetime.timedelta(seconds=4)),
        asyncio.to_thread(sleep, datetime.timedelta(seconds=10)),
        asyncio.to_thread(sleep, datetime.timedelta(seconds=2)),
    )


## math
import math

assert math.lcm(5, 7) == 35
assert math.lcm(2, 3, 4, 6) == 12


## http
import http

print(http.HTTPStatus.IM_A_TEAPOT.value)
