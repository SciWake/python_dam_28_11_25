import time

# print(1)
# start_time = time.time()
# time.sleep(2)
# end_time = time.time()
# print(end_time - start_time)
# print(2)


def get_numbers_comp(n):
    return [f"#{i}" for i in range(n)]


def get_numbers_for(n):
    data = []
    for i in range(n):
        data.append(f"#{i}")
    return data


start_time = time.time()
get_numbers_comp(1_000_000)
end_time = time.time()
print(f"get_numbers_comp time = {end_time - start_time}")

start_time = time.time()
get_numbers_for(1_000_000)
end_time = time.time()
print(f"get_numbers_for time = {end_time - start_time}")
