

import asyncio


async def Керемет_банк():
    print("🏦 Керемет Банкка кош келиңиз!")
    print("💳 Сураныч, картаңызды салыңыз...")
    await asyncio.sleep(2)  
    print("✅ Карта кабыл алынды.")
    print("💵 Накталай акча алуу мүмкүнчүлүгү!")


async def иштетүү():
    print("📋 Кызмат тандоо менюсу жүктөлүп жатат...")
    await asyncio.sleep(2)  
    print("📱 Кызмат тандадыңыз.")
    print("✅ Иштетүү ийгиликтүү аяктады!")

async def main():
    await asyncio.gather(
        Керемет_банк(),
        иштетүү()
    )


asyncio.run(main())
