def factorials(n: int):
    factorial_nums = {}
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        factorial_nums[i] = factorial
    return factorial_nums
