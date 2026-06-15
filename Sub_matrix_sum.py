class Solution:
    def maximumSumRectangle(self, R: int, C: int, M: list[list[int]]) -> int:
        max_sum = float('-inf')
        
        # Fix the left column
        for left in range(C):
            temp = [0] * R
            # Move the right column
            for right in range(left, C):
                # Accumulate elements row-wise
                for i in range(R):
                    temp[i] += M[i][right]
                
                # Apply 1D Kadane's algorithm
                current_max = temp[0]
                max_so_far = temp[0]
                for i in range(1, R):
                    current_max = max(temp[i], current_max + temp[i])
                    max_so_far = max(max_so_far, current_max)
                
                max_sum = max(max_sum, max_so_far)
                
        return max_sum
