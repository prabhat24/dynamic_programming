import sys
def max_revenue(hi_len, pos, rev, N, T):
    dp = [0] * N
    dp[0] = rev[0]
    global_maxa = dp[0]
    for k in range(1, N):
        maxa = 0
        for j in range(0, k):
            if pos[k] - pos[j] > T:
                maxa = max(maxa, dp[j])
        dp[k] = maxa + rev[k]
        global_maxa = max(global_maxa, dp[k])
    return global_maxa


if __name__ == '__main__':
    hi_len = int(input())
    N = int(input())
    pos = [int(k) for k in sys.stdin.readline().split()]
    rev = [int(k) for k in sys.stdin.readline().split()]
    T = int(input())
    print(max_revenue(hi_len, pos, rev, N, T))