# 문제 꼼꼼히 읽자!!!

n = int(input())

if n >= 3:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    print(dp[n])
else:
    print(n)