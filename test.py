from db.session import config, check_connection
import asyncio

status = asyncio.run(check_connection())

if status:
    print("connection estabilished")