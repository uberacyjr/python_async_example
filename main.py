import asyncio
import time
import requests as rs
import requests_async as requests


def request_sync(aux):
    print('INICIOU SYNC--- >' + str(aux))
    rs.get('https://httpbin.org/delay/3')
    print('FINALIZOU---- > ' + str(aux))

async def request(aux):
    print('INICIOU --- >' + str(aux))
    response = await requests.get('https://httpbin.org/delay/3')
    print('FINALIZOU---- > ' + str(aux))
    

async def main():
       start = time.time()
       task = asyncio.gather(request(1),request(2),request(3),request(4),request(5),request(6)) 
       await task
       print('FINALIZOU ASYNC ---- > ' + str(time.time() - start))

def main_sync():
    start = time.time()
    request_sync(1)
    request_sync(2)
    request_sync(3)
    request_sync(4)
    request_sync(5)
    request_sync(6)
    print('FINALIZOU SYNC ---- > ' + str(time.time() - start))

asyncio.run(main())
main_sync()

