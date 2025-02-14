def count_details(N, K, M):
    n_details = 0
    if N * K * M != 0 and N >= K and K >= M:
        while N > 0 and  N // K > 0:
            n_prereq = N // K
            delta = N % K
            n_details += n_prereq * (K // M)
            delta += n_prereq * (K % M)
            N = delta
    return n_details


def main():
    # assert count_details(10, 5, 2) == 4
    # assert count_details(13, 5, 3) == 3
    # assert count_details(14, 5, 3) == 4
    # assert count_details(0, 0, 0) == 0
    # assert count_details(200, 200, 200) == 1
    N, K, M = map(int, input().split())
    print(count_details(N, K, M))


if __name__ == "__main__":
    main()
