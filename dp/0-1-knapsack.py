'''
Input:
- A list of integers representing the weights of the items.
- A list of integers representing the values of the items.
- An integer representing the maximum capacity of the knapsack.

Output:
- An integer representing the maximum total value achievable without exceeding the knapsack capacity.
'''

def knapsack(weights, values, capacity):
    numOfItems = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(numOfItems + 1)]

    for i in range(1, numOfItems + 1):
        for c in range(1, capacity + 1):
            # current capacity <= item weight
            if(c < weights[i-1]):
                dp[i][c] = dp[i-1][c]

            # current capacity >= item weight
            else:
                # 2 options: add this current item or don't add the item
                dp[i][c] = max(values[i-1] + dp[i-1][c - weights[i-1]], dp[i-1][c])
    
    return dp[numOfItems][capacity]

def main():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    max_value = knapsack(weights, values, capacity)

    print("maximum value achievable:", max_value)

if __name__ == "__main__":
    main()
