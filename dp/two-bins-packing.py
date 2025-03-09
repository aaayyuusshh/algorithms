'''
You are given a set of n items with positive weights. 
Your task is to partition these items into two bins such that the difference between the total weights of the two bins is minimized. 
In other words, you want to split the set of weights into two subsets such that the absolute difference between the sum of weights in 
each subset is as small as possible.

Input:
A list of integers representing the weights of the items.

Output:
An integer representing the minimum possible difference between the total weights of the two bins.

analysis
----------
let S be the total sum
S = s1 + s2
s1 = closest sum possible to n/2
s2 = S - s1
absolute difference = s1 - s2 = s1-(S-s1) = -S-2s1 = S - 2s1
- now all we need to find is s1
- the problem becomes: find s1, the closest possible subset sum to S/2 and plug it into the derived difference formula
'''

def packing(weights):
    totalWeight = sum(weights)
    print("total weight: ", totalWeight)
    n = len(weights)

    # dp[i][j] represents if sum j is possible upto item i
    dp = [[False for _ in range(totalWeight//2 + 1)] for _ in range(len(weights) + 1)]

    # handling base case
    dp[0][0] = True
    for i in range(1, n + 1):
        dp[i][0] = True

    for item in range(1, n + 1):
        for runningWeight in range(1, totalWeight//2 + 1):
            # case 1
            if(weights[item - 1] == runningWeight):
                dp[item][runningWeight] = True

            # case 2
            elif(weights[item - 1] > runningWeight):
                dp[item][runningWeight] = dp[item-1][runningWeight]

            # case 3
            elif(weights[item - 1] < runningWeight):
                # dp = prev i can already achieve running weight so just use that OR
                # if not, dp = see if this i can achieve running weight
                dp[item][runningWeight] = dp[item-1][runningWeight] or dp[item-1][runningWeight - weights[item - 1]]

    # find the subset sum that is the closest to n/2
    closestSubsetSum = 0
    for runningWeight in range(totalWeight//2, -1, -1):
        if(dp[n][runningWeight]):
            closestSubsetSum = runningWeight
            break
                
    print(f'closest subset sum: {closestSubsetSum}')
    return totalWeight - (2 * closestSubsetSum)

def main():
    weights = [9, 5, 5]
    min_diff = packing(weights)    
    print("minimum possible difference:", min_diff)

if __name__ == "__main__":
    main()
