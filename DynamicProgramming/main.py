class SurroundedRegions:
    def helper(self, i, j, board, visited):
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == 'X' or visited[i][j]:
            return
        visited[i][j] = True

        self.helper(i - 1, j, board, visited)
        self.helper(i + 1, j, board, visited)
        self.helper(i, j - 1, board, visited)
        self.helper(i, j + 1, board, visited)

    def solve(self, board):
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(n):
            if board[0][i] == "O":
                self.helper(0, i, board, visited)
        for i in range(m):
            if board[i][0] == "O":
                self.helper(i, 0, board, visited)
        for i in range(n):
            if board[m - 1][i] == "O":
                self.helper(m - 1, i, board, visited)
        for i in range(m):
            if board[i][n - 1] == "O":
                self.helper(i, n - 1, board, visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"


class HouseRobber:
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[size-1]


def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


def longest_common_subsequence_helper(i, j, text1, text2):
    if i == len(text1) or j == len(text2):
        return 0
    if text1[i] == text2[j]:
        return 1 + longest_common_subsequence_helper(i+1, j+1, text1, text2)
    else:
        option1 = longest_common_subsequence_helper(i+1, j, text1, text2)
        option2 = longest_common_subsequence_helper(i, j + 1, text1, text2)
        return max(option1, option2)


def longestCommonSubsequenceAlternate(text1, text2):
    """
    https://getsdeready.com/courses/design-dsa-combined/lesson/longest-common-subsequence-2/
    """
    return 1 + longest_common_subsequence_helper(0, 0, text1, text2)


def max_profit_dp(prices):
    n = len(prices)
    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = 0  # No profit on the first day

    for i in range(1, n):
        # Calculate the profit if selling on the current day
        dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], 0)

    # Return the maximum profit
    return max(dp)


def max_profit_dp_daily(prices):
    n = len(prices)
    if n == 0:
        return 0

    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        if min_price < prices[i]:
            max_profit += prices[i] - min_price
        min_price = prices[i]

    return max_profit
