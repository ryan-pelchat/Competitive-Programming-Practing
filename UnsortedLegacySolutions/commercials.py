values = list(map(int, input().split()))
viewers = list(map(int,input().split()))

# array with the worth of an item
for i in range(len(viewers)):
    viewers[i] = int(viewers[i])-int(values[1])


dp = [0] * (len(viewers))
# represents maximum profit using first i items
dp[0] = viewers[0]
max_profit = dp[0]
for i in range(1,len(viewers)):
    # can keep the current max profit | keep are old subsequence and its profit
    # or add the worth of the next commercial | extending our subsequence taking its profit
    # or set it to the worth of the next commercial | starting a new subsequence taking its profit
    dp[i] = max(dp[i-1]+viewers[i], viewers[i])
    max_profit = max(dp[i], max_profit)

print(max_profit)
