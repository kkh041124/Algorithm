def dist_squared(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def min_distance(arr):
    min_dist = float('inf')
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            temp = dist_squared(arr[i][0], arr[i][1], arr[j][0], arr[j][1])
            if temp < min_dist:
                min_dist = temp
    return min_dist

def strip_closest(strip, min_dist):
    strip.sort(key=lambda point: point[1])
    
    strip_min = min_dist
    size = len(strip)
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j][1] - strip[i][1]) ** 2 >= strip_min:
                break
            temp = dist_squared(strip[i][0], strip[i][1], strip[j][0], strip[j][1])
            if temp < strip_min:
                strip_min = temp
    return strip_min

def Closepair(arr):
    n = len(arr)
    
    if n <= 3:
        return min_distance(arr)

    mid = n // 2
    mid_point = arr[mid]

    left = arr[:mid]
    right = arr[mid:]

    left_min = Closepair(left)
    right_min = Closepair(right)

    min_dist = min(left_min, right_min)

    strip = []
    for i in range(n):
        if abs(arr[i][0] - mid_point[0]) ** 2 < min_dist:
            strip.append(arr[i])

    strip_min = strip_closest(strip, min_dist)

    return min(min_dist, strip_min)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])

min_dist_squared = Closepair(arr)

print(min_dist_squared)
