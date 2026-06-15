class Solution:
    # Function to find starting point where the truck can cover the circle
    def tour(self, petrol, distance):
        n = len(petrol)
        start_idx = 0
        current_surplus = 0
        total_surplus = 0
        
        for i in range(n):
            net_petrol = petrol[i] - distance[i]
            total_surplus += net_petrol
            current_surplus += net_petrol
            
            # If we cannot reach the next pump from the current start_idx
            if current_surplus < 0:
                # Reset current pool and pick the next pump as the new starting candidate
                start_idx = i + 1
                current_surplus = 0
                
        # If total petrol is less than total distance, no solution exists
        return start_idx if total_surplus >= 0 else -1
