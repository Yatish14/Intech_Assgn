def trap_rain_water(heights):
    n = len(heights)
    
    if n <= 2:
        return 0
    
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    trapped_water = 0
    for i in range(1, n - 1):
        trapped_water += max(min(left_max[i], right_max[i]) - heights[i], 0)

    return trapped_water

arr = list(map(int, input("Enter the array: ").split()))

print("Trapped water:", trap_rain_water(arr))
