def even_numbers(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
