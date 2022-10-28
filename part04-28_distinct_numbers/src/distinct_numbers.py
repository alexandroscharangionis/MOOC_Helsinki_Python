def distinct_numbers(numbers):
    distinct = []
    for num in sorted(numbers):
        if num in distinct:
            continue
        distinct.append(num)
    return distinct
