from asyncio.exceptions import TimeoutError
from modules.printer import clout

async def test_string(session, url, data):
    try:
        response = await session.get(url)
        if response.status == 404:
            pass
        elif response.status not in codes:
            print(f'{R}[-] {Y}[{url}] {W}[{response.status}]')
        else:
            resp_body = await response.text()
            if data in resp_body:
                pass
            else:
                await clout(response.url)
    except TimeoutError:
        #print(f'{Y}[!] Timeout :{C} {url}{W}')
        return
    except Exception as exc:
        #print(f'{Y}[!] Exception [test_string] [{url}] :{W} {exc}')
        return