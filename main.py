import aiohttp
import asyncio



class whois_ip:
    async def info_choice(domain, choi):
        if choi == "json":
            send_task = asyncio.create_task(whois_ip.whois_json(domain))
            await send_task
        elif choi == "info":
            send_task = asyncio.create_task(whois_ip.whois_inf(domain))
            await send_task
        else:
            print("NONE")



    async def whois_json(domain):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://ip-api.com/json/{domain}') as response:

                html = await response.json()
                if html['status'] =='success':
                    print(html)
                else:
                    print("None domain")


    async def whois_inf(domain):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://ip-api.com/json/{domain}') as response:

                html = await response.json()
                if html['status'] =='success':
                    result = (f"Country:{html['country']}\nRegion:{html['regionName']}\nzip:{html['zip']}\nisp:{html['isp']}\nip:{html['query']}\n")
                    print(result)
                else:
                    print("None domain")








if __name__ == "__main__":
    domain = input("Enter the ip or domain to display the whois: ")
    choice = input("Enter the info or json: ")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(whois_ip.info_choice(domain=domain, choi=choice))