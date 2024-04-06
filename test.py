import asyncio
import sys


coeff = 0.01


buying_time_wait_time, gift_name_choice_pack_time = list(), list()
buying_time_wait_time = [[int(el.strip()) * coeff for el in elem.split()] for elem in buying_time_wait_time]
thread = True
for elem in sys.stdin:
    if elem == "\n":
        thread = False
        continue
    if thread:
        buying_time_wait_time += [list(map(lambda elem: int(elem) * coeff, elem.split()))]
    else:
        gift_name_choice_pack_time += [[elem.split()[0], int(elem.split()[1]) * coeff, int(elem.split()[2]) * coeff]]
gift_name_choice_pack_time.sort(key=lambda elem: (elem[-1] + elem[-2]), reverse=True)


async def delay(delay_time):
    await asyncio.sleep(delay_time)


async def got_bought(name, delay_time):
    await asyncio.sleep(delay_time)
    print(f"Got {name}")


async def buy_gift(buying_time=None):
    try:
        name, choice_time, pack_time = gift_name_choice_pack_time[0]
    except IndexError:
        return
    iteration = 0
    while buying_time is not None and choice_time + pack_time > buying_time:
        iteration += 1
        try:
            name, choice_time, pack_time = gift_name_choice_pack_time[iteration]
        except IndexError:
            return
    del gift_name_choice_pack_time[iteration]
    print(f"Buy {name}")
    await asyncio.sleep(choice_time)
    tasks = [asyncio.create_task(got_bought(name, pack_time)), asyncio.create_task(buy_gift(buying_time - choice_time
                                                                                            if buying_time is not None
                                                                                            else None))]
    await asyncio.gather(*tasks)


async def main():
    for i, (buying_time, wait_time) in enumerate(buying_time_wait_time):
        i += 1
        print(f"Buying gifts at {i} stop")
        tasks = list()
        tasks.append(asyncio.create_task(delay(buying_time)))
        tasks.append(asyncio.create_task(buy_gift(buying_time)))
        await asyncio.gather(*tasks)
        print(f"Arrive from {i} stop")
        await asyncio.sleep(wait_time)
    if gift_name_choice_pack_time:
        print("Buying gifts after arrival")
        await buy_gift()


asyncio.run(main())
