'''
Input:
A list of intervals. Each interval is represented as a tuple (start, finish, weight).

Output:
An integer representing the maximum total weight of non-overlapping intervals.
'''

import math

def weighted_interval_scheduling(intervals):    
    # sort intervals in increasing order of end times
    sortedIntervals = sorted(intervals, key = lambda t:t[1])
    n = len(sortedIntervals)

    # dp[i] represents the max weight achievable upto interval i; optimal substructure 🧱
    dp = [1] * n
    dp[0] = sortedIntervals[0][2]   # base case

    for i in range(1, n):
        weight = sortedIntervals[i][2]
        # 2 options: include current interval or don't include it
        dp[i] = max(weight + findLastCompatibleIntervalWeightBinary(sortedIntervals, dp, i), dp[i-1]) 
    
    return dp[n-1]



# O(logn) for this algo, and O(n) * O(logn) for caller function
def findLastCompatibleIntervalWeightBinary(sortedIntervals, dp, i):
    targetStart = sortedIntervals[i][0]
    left = 0
    right = i-1
    compatibleIntervalWeight = 0

    while(True):
        if(left > right):
            break

        mid = math.floor((left + right)/2)
        currEnd = sortedIntervals[mid][1]

        if(currEnd > targetStart):
            right = mid - 1

        if(currEnd <= targetStart):
            compatibleIntervalWeight = dp[mid]
            left = mid + 1

    return compatibleIntervalWeight

# O(n) for this algo, and O(n) * O(n) for caller function
def findLastCompatibleIntervalWeightLinear(sortedIntervals, dp, i):
    currStart = sortedIntervals[i][0]
    for j in range(i-1, -1, -1):
        prevEnd = sortedIntervals[j][1]
        if(currStart >= prevEnd):
            return dp[j]
        
    return 0

def main():
    intervals = [
        (1, 4, 4),
        (3, 6, 20),
        (5, 7, 5),
        (8, 10, 5),
    ]
    
    max_weight = weighted_interval_scheduling(intervals)
    print("maximum total weight of non-overlapping intervals:", max_weight)

if __name__ == "__main__":
    main()
