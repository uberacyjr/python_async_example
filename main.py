import asyncio
import time
import requests as rs

# Request lib must be async
import requests_async as requests

DELAY_URL = 'https://httpbin.org/delay/3'

def request_sync(aux):
    print('START SYNC MAIN -> ' + str(aux))
    rs.get(DELAY_URL)
    print('END SYNC MAIN -> ' + str(aux))


async def request_async(aux):
    print('START ASYNC MAIN -> ' + str(aux))
    await requests.get(DELAY_URL)
    print('END ASYNC MAIN -> ' + str(aux))
    


async def main():
       print('----START ASYNC MAIN----')
       start = time.time()
       task = asyncio.gather(request_async(1), 
                             request_async(2), 
                             request_async(3), 
                             request_async(4), 
                             request_async(5), 
                             request_async(6)) 
       await task
       print('----FINALIZOU ASYNC MAIN----' + str(time.time() - start))


def main_sync():
    print('----START SYNC MAIN----')
    start = time.time()
    request_sync(1)
    request_sync(2)
    request_sync(3)
    request_sync(4)
    request_sync(5)
    request_sync(6)
    print('----END SYNC MAIN----' + str(time.time() - start))

# Async main
asyncio.run(main())
# Sync main
main_sync()

