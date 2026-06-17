import sys

def solve():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        
        arr = []
        curr = 1
        for idx in range(n):
            arr.append(curr)
            # Alternate the step size between 1 and 2
            if idx % 2 == 0:
                curr += 1
            else:
                curr += 2
                
        # Format the array as a space-separated string
        out.append(" ".join(map(str, arr)))
        
    # Print all outputs separated by newlines
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()
