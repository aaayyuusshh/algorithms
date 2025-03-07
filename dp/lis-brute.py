# longest increasing subsequence
'''
Input:
A list of integers.

Output:
An integer representing the length of the longest increasing subsequence.
'''

def longest_increasing_subsequence(nums):
    # we don't even need a dp arr, we could just track curr length and compare it with max length
    
    n = len(nums)
    dp = [[1 for _ in range(n)] for _ in range(n)]
   
    for i in range(n):
        for j in range(n):
            if j > i and nums[i] < nums[j]:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1]

    return max(max(row) for row in dp)

def main():
    sample_nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8]
    lis_length = longest_increasing_subsequence(sample_nums)
    print("length of longest increasing subsequence:", lis_length)

if __name__ == "__main__":
    main()
