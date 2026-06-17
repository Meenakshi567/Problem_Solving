# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read n, x, and s from the first line of the test case
    n, x, s = map(int, input().split())
    
    # Read the personality string
    u = input()
    
    # Count how many Ambiverts ('A') are in the line
    cnt_A = u.count('A')
    
    max_seated = 0
    
    # Try every possible number of leading Ambiverts to act as Introverts
    for p in range(cnt_A + 1):
        rem_empty = x  # Empty tables left
        U = 0          # Tables with at least one person
        P = 0          # Total people seated
        seated = 0     # People seated in this specific simulation
        a_ptr = 0      # Track which Ambivert we are currently looking at
        
        for ch in u:
            # Decide the current person's role
            if ch == 'A':
                if a_ptr < p:
                    curr_type = 'I'
                else:
                    curr_type = 'E'
                a_ptr += 1
            else:
                curr_type = ch
            
            # Apply the seating rules based on role
            if curr_type == 'I':
                if rem_empty > 0:
                    rem_empty -= 1
                    U += 1
                    P += 1
                    seated += 1
            elif curr_type == 'E':
                if U * s > P:
                    P += 1
                    seated += 1
                    
        # Update the maximum seated count if this simulation did better
        if seated > max_seated:
            max_seated = seated
            
    # Print the final result for this test case
    print(max_seated)
