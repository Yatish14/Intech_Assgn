def count(n):
    count = 0
    start = 1
    while start <= n // 2:
        sum_of_nums = 0
        end = start
        while sum_of_nums < n:
            sum_of_nums += end
            end += 1
            if sum_of_nums == n and end - start > 1:
                count += 1
        start += 1
    return count

n = int(input("Enter a natural number: "))
print(count(n))
