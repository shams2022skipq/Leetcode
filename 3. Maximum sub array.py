def maxSubArray(nums) -> int:
    dp = [0] * len(nums)
    for i, num in enumerate(nums):
        dp[i] = max(dp[i - 1] + num, num)
    return max(dp)


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
