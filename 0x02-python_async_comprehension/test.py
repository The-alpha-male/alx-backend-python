import asyncio


async def square(x):
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    return x * x


async def main():
    numbers = [1, 2, 3, 4, 5]
    squares = [await square(num) for num in numbers]
    print(squares)

asyncio.run(main())
