'''
Given a set of positive integers and a target sum S, determine if there exists a subset of numbers whose sum is exactly S.

Input: nums = [3, 34, 4, 12, 5, 2], target = 9
Output: True (Because subset [4, 5] sums to 9)

Some quick analysis
--------------------
At item 5 for running sum 9 --> okay we can make 5 here... remaining is 4.. could we make 4 at a previous index.. if yes,
ofc, we can make 9 bc we can make 5 here and we can make 4 with a prev subset.. 5+4 = 9
'''

def subset_sum(nums, target):
    n = len(nums)
    # let dp[i][j] represent if running sum of j is possible at index i
    # j: running sum, 0<= j <=target
    # i: ith index/weight of input array
    dp = [[False for _ in range(target + 1)] for _ in range(n+1)]

    # base cases
    dp[0][0] = True # sum of 0 is possible at 0 index(doesn't exist in reality)
    # sum of 0 is possible at all indexes so just use a for loop
    for i in range(n+1):
        dp[i][0] = True
    
    # dp table population step
    for index in range(1, n+1):
        for runningSum in range(1, target+1):
            currNum = nums[index-1]

            # case 1
            if(currNum == runningSum):
                dp[index][runningSum] = True

            # case 2
            if(currNum < runningSum):
                # remaining trick
                dp[index][runningSum] = dp[index-1][runningSum] or dp[index-1][runningSum - currNum]

            # case 3
            if(currNum > runningSum):
                dp[index][runningSum] = dp[index-1][runningSum]  

    return dp[n][target]

def main():
    nums = [1,1,1,1,1,1,1,1,1]
    target = 9
    print(subset_sum(nums, target))

if __name__ == "__main__":
    main()
