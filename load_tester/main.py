import requests
import asyncio
import aiohttp
import time
import argparse


APP_URL = "http://localhost:8000"
RESOURCES = ["slow", "fast", "stuck"]


def requests_test(r, resource) -> requests.Response:
    start_time = time.time()
    for _ in range(r):
        response = requests.get(f"{APP_URL}/{resource}")
        print(response.text, response.elapsed.total_seconds())
    end_time = time.time()
    print(f"total time elapsed: {end_time - start_time}")


async def fetch(url: str, session: aiohttp.ClientSession):
    start_time = time.time()
    async with session.get(url) as response:
        result = await response.text()
        end_time = time.time()
        return (result, end_time - start_time)


async def run(r, resource):
    tasks = []
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        for _ in range(r):
            task = asyncio.ensure_future(
                fetch(url=f"{APP_URL}/{resource}", session=session)
            )
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        for x in responses:
            print(x)
    end_time = time.time()
    print(f"total time elapsed: {end_time - start_time}")


if __name__ == "__main__":
    # create the parser
    parser = argparse.ArgumentParser(description="Running the load tester...")
    # add the arguments
    parser.add_argument(
        "resource",
        metavar="resource",
        type=str,
        help="the resource, which can be: slow, fast, stuck",
    )
    parser.add_argument(
        "--hits", metavar="hits", type=int, help="the number of hits", default=10
    )
    args = parser.parse_args()
    print(f"testing config {args.hits, args.resource}")

    # requests_test(args.Hits, args.Resource)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(args.hits, args.resource))
    loop.run_until_complete(future)
