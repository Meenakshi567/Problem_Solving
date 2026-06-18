import sys

def solve():
    # Read all tokens from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # Parse initial cards
    A = [int(x) for x in input_data[2:2+N]]
    
    # Parse operations as (Value, Count) pairs
    ops = []
    idx = 2 + N
    for _ in range(M):
        b = int(input_data[idx])
        c = int(input_data[idx+1])
        ops.append((c, b))  # Store as (C_j, B_j) to sort by replacement value
        idx += 2
        
    # Sort initial cards in ascending order
    A.sort()
    # Sort operations by replacement value in descending order
    ops.sort(key=lambda x: x[0], reverse=True)
    
    curr_a_idx = 0
    for c, b in ops:
        if curr_a_idx >= N:
            break
            
        # Replace the smallest cards with the highest available multiplier
        count = 0
        while curr_a_idx < N and count < b and A[curr_a_idx] < c:
            A[curr_a_idx] = c
            curr_a_idx += 1
            count += 1
            
        # If the current smallest card is already >= c, smaller future values won't help
        if curr_a_idx < N and A[curr_a_idx] >= c:
            break
            
    print(sum(A))

if __name__ == '__main__':
    solve()
