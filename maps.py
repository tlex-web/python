if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    arr.sort()
    arr.reverse()
    max = arr[0]
    for i in range(1, n):
        if arr[i] < max:
            max = arr[i]
            break
    print(max)
