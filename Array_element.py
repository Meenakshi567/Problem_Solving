class Solution:
    def search(self, A: list, key: int) -> int:
        low, high = 0, len(A) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if A[mid] == key:
                return mid
            
            # Check if the left half is sorted
            if A[low] <= A[mid]:
                if A[low] <= key < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right half must be sorted
            else:
                if A[mid] < key <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
