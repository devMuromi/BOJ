def solution() -> None:
    MAXVALUE = 10**6
    N = int(input())

    cache = [[0, []] for _ in range(MAXVALUE+1)]
    cache[1][0] = 0
    cache[1][1] = [1]

    for i in range(2, N+1):
        cache[i][0] = cache[i-1][0] + 1
        cache[i][1] = cache[i-1][1] + [i]

        if i % 2 == 0 and cache[i//2][0] + 1 < cache[i][0]:
            cache[i][0] = cache[i//2][0] + 1
            cache[i][1] = cache[i//2][1] + [i]

        if i % 3 == 0 and cache[i//3][0] + 1 < cache[i][0]:
            cache[i][0] = cache[i//3][0] + 1
            cache[i][1] = cache[i//3][1] + [i]
    
    print(cache[N][0])
    print(" ".join(list(map(str, cache[N][1][::-1]))))

solution()