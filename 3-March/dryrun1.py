def dis(arr, n, d):
    t = []
    i = 0
    while (i < d):
        t.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + t
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]

print(dis(arr, len(arr), 2))

#Bhool se bhi termnal mein run mat krna
