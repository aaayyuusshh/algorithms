def max_wage(wages):
    n = len(wages)
    dp = [0] * n 

    #base cases
    dp[0] = wages[0]
    dp[1] = max(wages[0], wages[1])

    for i in range(2, n):
        dp[i] = max(wages[i] + dp[i-2], dp[i-1])    
    
    return dp[n - 1]

def main():
    wages = [7, 2, 4, 5, 3]
    result = max_wage(wages)
    print("maximum wage possible:", result)

if __name__ == "__main__":
    main()
