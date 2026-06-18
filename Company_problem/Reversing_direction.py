# cook your dish here
import sys

def solve():
    # Fast I/O: Read all lines from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    T = int(input_data[0].strip())
    line_idx = 1
    
    for _ in range(T):
        if line_idx >= len(input_data):
            break
        N = int(input_data[line_idx].strip())
        line_idx += 1
        
        turns = []
        roads = []
        
        # Parse each instruction into directional turn and road name
        for _ in range(N):
            line = input_data[line_idx]
            line_idx += 1
            # Split only at the first occurrence of " on "
            parts = line.split(" on ", 1)
            turns.append(parts[0])
            roads.append(parts[1])
            
        # The reversed route always begins on the very last road
        print(f"Begin on {roads[-1]}")
        
        # Process the remaining roads and flip the matching turns
        for i in range(1, N):
            orig_turn = turns[N - i]
            opp_turn = "Right" if orig_turn == "Left" else "Left"
            print(f"{opp_turn} on {roads[N - i - 1]}")
            
        # Print a blank line after each test case as required
        print()

if __name__ == '__main__':
    solve()
