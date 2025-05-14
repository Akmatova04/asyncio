# Керектүү модулдарды импорттоо
import asyncio      # Асинхрондук операциялар үчүн
import aiohttp      # Асинхрондук HTTP сурамдарын жасоо үчүн китепкана

# Асинхрондук функция (корутина) URL'ден мазмун алуу үчүн
async def url_мазмунун_алуу(session, url):
    """
    Берилген URL'ге асинхрондук GET сурамын 'session' аркылуу жасап,
    жооптун мазмунун текст түрүндө кайтарат.
    """
    print(f"{url} дарегине сурам жөнөтүлүүдө...")
    try:
        # 'async with' конструкциясы сессияны жана жоопту туура жабууну камсыздайт.
        # 'session.get(url)' асинхрондук GET сурамын жасайт.
        async with session.get(url) as response:
            # response.raise_for_status() - эгер HTTP статусу ката болсо
            # (мисалы, 404 Not Found, 500 Server Error), бул жерде exception ыргытылат.
            response.raise_for_status()
            print(f"{url} дарегинен жооп алынды, статусу: {response.status}")
            # await response.text() - жооптун мазмунун (body) асинхрондук түрдө
            # текст катары окуйт. Эгер JSON күтсөңүз, await response.json() колдонсоңуз болот.
            return await response.text()
    except aiohttp.ClientError as e: # aiohttp менен байланышкан каталарды кармоо
        print(f"{url} дарегине сурам жасоодо ката кетти: {e}")
        return None # Ката болсо, None кайтаруу

# Негизги асинхрондук функция
async def main():
    """
    Бул функция эки башка URL'ге 'aiohttp' аркылуу асинхрондук
    HTTP сурамдарын жасап, алардын мазмунун чыгарат.
    """
    # Сурам жөнөтүлө турган URL'дердин тизмеси
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/posts/1"
    ]

    # 'async with aiohttp.ClientSession() as session:'
    # 'ClientSession' түзөт. Бир нече сурам үчүн бир эле сессияны
    # колдонуу сунушталат (туташууларды кайра колдонуу үчүн натыйжалуу).
    async with aiohttp.ClientSession() as session:
        # Ар бир URL үчүн 'url_мазмунун_алуу' корутинасын түзүп, тизмеге сактоо.
        # Бул учурда корутиналар дароо аткарылбайт, алар 'Task' объектилерине
        # айланып, 'asyncio.gather' аркылуу ишке кирет.
        сурам_тапшырмалары = [url_мазмунун_алуу(session, url) for url in urls]

        # 'asyncio.gather(*сурам_тапшырмалары)' - бардык сурам корутиналарын
        # бир учурда (конкуренттүү) аткарат. '*' оператору тизмени
        # өзүнчө аргументтерге "чачат".
        жооптор = await asyncio.gather(*сурам_тапшырмалары)

    print("\n--- Сурамдардын жыйынтыктары ---")
    # Алынган жоопторду чыгаруу
    for i, url in enumerate(urls):
        print(f"\nМазмун {url} дарегинен:")
        if жооптор[i]:
            # Мазмун өтө узун болсо, алгачкы 300 символун гана чыгаруу
            print(жооптор[i][:300] + "..." if len(жооптор[i]) > 300 else жооптор[i])
        else:
            print("Мазмун алынган жок.")

if __name__ == "__main__":
    asyncio.run(main())