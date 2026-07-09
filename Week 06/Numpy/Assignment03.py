import numpy as np

np.random.seed(42) 
arr = np.random.randint(1, 501, 1000)

print("Original Array:")
print(arr)

perfect_square_mask = np.sqrt(arr) % 1 == 0
perfect_square_count = np.sum(perfect_square_mask)

print("\nNumber of Perfect Squares:", perfect_square_count)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_mask = np.array([is_prime(num) for num in arr])
prime_count = np.sum(prime_mask)

print("Number of Prime Numbers:", prime_count)

modified_arr = arr.astype(float)

multiple_of_7_mask = modified_arr % 7 == 0
modified_arr[multiple_of_7_mask] = np.sqrt(modified_arr[multiple_of_7_mask])

print("\nArray after replacing multiples of 7 with square roots:")
print(modified_arr)

sorted_arr = np.sort(arr)

gaps = np.diff(sorted_arr)

largest_gap = np.max(gaps)

print("\nLargest Gap Between Consecutive Sorted Values:", largest_gap)
cumulative_sum = np.cumsum(arr)

print("\nCumulative Sum:")
print(cumulative_sum)

index = np.argmax(cumulative_sum > 100000)
print("\nFirst Index Where Cumulative Sum Exceeds 100000:", index)
print("Cumulative Sum at that Index:", cumulative_sum[index])