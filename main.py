import aiohttp
import asyncio



async def whois_info(domain):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://ip-api.com/json/{domain}') as response:

            html = await response.json()
            if html['status'] =='success':
                result = (f"Country:{html['country']}\nRegion:{html['regionName']}\nzip:{html['zip']}\nisp:{html['isp']}\nip:{html['query']}\n")
                print(result)
            else:
                print("None domain")






if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(whois_info(input("Enter the ip or domain to display the whois:")))