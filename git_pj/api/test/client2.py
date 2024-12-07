import asyncio

async def main(host='127.0.0.1', port=65432):
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(1024)
        print(f"Получено от сервера: {data.decode()}")

if __name__ == "__main__":
    asyncio.run(main())