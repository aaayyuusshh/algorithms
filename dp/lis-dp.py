# longest increasing subsequence
'''
Input:
A list of integers.

Output:
An integer representing the length of the longest increasing subsequence.
'''

def longest_increasing_subsequence(nums):
    n = len(nums)
    # let dp[i] be the lis ending in nums[i]
    dp = [1] * n    # base case

    for i in range(n):
        for j in range(i):
            if(nums[i] > nums[j]):
                dp[i] = max(dp[j] + 1, dp[i])
                '''
                dp[i] is considered in the max bc what if nums[i] is a part of another prev longer subsequence
                that it found previously
                '''
    return max(dp)

def main():
    sample_nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8]
    lis_length = longest_increasing_subsequence(sample_nums)
    print("length of longest increasing subsequence:", lis_length)

if __name__ == "__main__":
    main()
