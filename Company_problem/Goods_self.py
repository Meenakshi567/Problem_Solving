import sys

def solve():
    # Fast I/O to read all test cases efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    output = []
    
    for _ in range(t):
        n = int(input_data[idx])
        a = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # Step 1: Coordinate Compression
        unique_vals = sorted(list(set(a)))
        val_to_id = {v: i for i, v in enumerate(unique_vals)}
        a_comp = [val_to_id[x] for x in a]
        
        num_types = len(unique_vals)
        blocks = [[] for _ in range(num_types)]
        cntb = [0] * num_types
        
        # Step 2: Extract block boundaries
        i = 0
        while i < n:
            j = i
            val = a_comp[j]
            while i < n and a_comp[i] == val:
                i += 1
            # Add boundary elements and their immediate neighbors
            blocks[val].extend([i, i - 1, j, j - 1])
            cntb[val] += 1
            
        # Helper function to validate a simulated swap
        def check(x, y):
            if x < 0 or x >= n or y < 0 or y >= n:
                return False
            
            # Simulate the swap
            a_comp[x], a_comp[y] = a_comp[y], a_comp[x]
            
            # Count the resulting blocks
            cnt = [0] * num_types
            k = 0
            while k < n:
                curr_val = a_comp[k]
                while k < n and a_comp[k] == curr_val:
                    k += 1
                cnt[curr_val] += 1
                
            # Restore original state
            a_comp[x], a_comp[y] = a_comp[y], a_comp[x]
            
            # Check if all blocks are unified (count <= 1)
            for c in cnt:
                if c > 1:
                    return False
            return True

        ans = "YES"
        for t_id in range(num_types):
            if cntb[t_id] > 1:
                # Impossible to fix more than 3 segments with 1 swap
                if cntb[t_id] > 3:
                    ans = "NO"
                    break
                
                # Filter valid inside-bounds and unique indices
                candidates = sorted(list(set([pos for pos in blocks[t_id] if 0 <= pos < n])))
                
                ok = False
                for idx_x in range(len(candidates)):
                    for idx_y in range(idx_x + 1, len(candidates)):
                        if check(candidates[idx_x], candidates[idx_y]):
                            ok = True
                            break
                    if ok:
                        break
                
                if not ok:
                    ans = "NO"
                break  # Only need to attempt to fix the first fragmented block
                
        output.append(ans)
        
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
