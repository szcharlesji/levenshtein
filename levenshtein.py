def calc_levenshtein_distance(string_a, string_b):
    # Convert to lower cases
    string_a = string_a.lower()
    string_b = string_b.lower()

    # Initialize DP
    a_len = len(string_a)
    b_len = len(string_b)
    dp = [[0] * (a_len + 1) for i in range((b_len + 1))]

    for i in range(a_len + 1):
        dp[0][i] = i
    for j in range(b_len + 1):
        dp[j][0] = j

    # Bottom up
    for i in range(b_len):
        for j in range(a_len):
            # Distance of a, b, c, meaning respectively the distance between substring a - 1 and substring b
            # substring a and substring b - 1, and substring a and b
            d_a = dp[i][j+1] + 1
            d_b = dp[i+1][j] + 1
            if string_a[j] == string_b[i]:
                d_c = dp[i][j]
            else:
                d_c = dp[i][j] + 2
            dp[i+1][j+1] = min(d_a, d_b, d_c)

    return dp[b_len][a_len]