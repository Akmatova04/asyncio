# import asyncio

# async def task1():
#     print("Task 1 башталды")
#     await asyncio.sleep(2)
#     print("Task 1 бүттү")

# async def task2():
#     print("Task 2 башталды")
#     await asyncio.sleep(1)
#     print("Task 2 бүттү")

# async def main():
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())



# import asyncio

# # Асинхрондуу функция түзөбүз
# async def салам_бер():
#     print("Салам!")
#     await asyncio.sleep(2)  # 2 секунд күт
#     print("Кандайсың?")

# # Бул функцияны иштетиш үчүн атайын цикл керек
# asyncio.run(салам_бер())

# import asyncio
# async def назира_акматова():
#     print('ATAMBEKOVNA')
#     await asyncio.sleep(3)
#     print('Саламатсызбы')
# asyncio.run(назира_акматова())


# import asyncio
# async def func1():
#     print('start!')
#     await asyncio.sleep(1)
#     print('end')

# async def func2():
#     print('start2')
#     await asyncio.sleep(2)
#     print('end2')

# async def main():
#     await asyncio.gather(func1(),func2())

# asyncio.run(main())
 
import asyncio

async def суу_кайнатуу():
    print("Суу коюлду кайнап баштады...")
    await asyncio.sleep(3)  
    print("Суу кайнап бүттү!")


async def чай_салуу():
    print("Чай салынды...")
    await asyncio.sleep(1)  
    print("Чай даяр!")


async def main():
    
    await asyncio.gather(
        суу_кайнатуу(),
        чай_салуу()
    )


asyncio.run(main())
