import sys

def solve():
    # Read input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    # Tracks maximum points for activities [A, B, C]
    dp = [0, 0, 0]
    
    idx = 1
    for _ in range(N):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        # Prevent consecutive repeats during selection
        new_dp = [
            a + max(dp[1], dp[2]),
            b + max(dp[0], dp[2]),
            c + max(dp[0], dp[1])
        ]
        dp = new_dp
        
    print(max(dp))

if __name__ == '__main__':
    solve()
