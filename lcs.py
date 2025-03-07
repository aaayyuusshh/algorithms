# longest common subsequence
'''
Input:
Two strings

Output:
An integer representing the length of the longest common subsequence between the two strings.
'''

def longest_common_subsequence(seq1, seq2):
    # let dp[i][j] represent the lcs between ith idx of seq1 and jth idx of seq2
    dp = [[0 for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            print(i, j)
            if(seq1[i-1] == seq2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[len(seq1)][len(seq2)]

def main():
    sequence1 = "abcde"
    sequence2 = "bankd"

    lcs_length = longest_common_subsequence(sequence1, sequence2)    
    print("length of longest common subsequence:", lcs_length)

if __name__ == "__main__":
    main()
