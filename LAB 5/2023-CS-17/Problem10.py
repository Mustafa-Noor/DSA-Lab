import time

numbers = []
start_time = time.time()

for i in range(1, 101):
    start = time.time()
    numbers.append(i)
    end = time.time()
    print(f"Appending {i} took {end - start:.10f} seconds")

total_time = time.time() - start_time
print(f"Total time to append 100 numbers: {total_time:.10f} seconds")
