import sys

def solve():
    # Fast I/O to handle up to 200,000 characters efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        s = input_data[idx+2]
        idx += 3
        
        # Track the count of '1's for each of the k modulo chains
        ones_count = [0] * k
        
        for i in range(n):
            if s[i] == '1':
                ones_count[i % k] += 1
        
        # If any chain has an odd number of '1's, it's impossible to clear
        possible = True
        for count in ones_count:
            if count % 2 != 0:
                possible = False
                break
        
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
