class CoachNode:
    def __init__(self, coach_id, coach_type):
        self.coach_id = coach_id        
        self.coach_type = coach_type    
        self.next = None               
class TrainSequence:
    def __init__(self, train_number):
        self.train_number = train_number
        self.engine_head = None        
    def attach_coach(self, coach_id, coach_type):
        new_coach = CoachNode(coach_id, coach_type)
        if not self.engine_head:
            self.engine_head = new_coach
            return
        current = self.engine_head
        while current.next:
            current = current.next
        current.next = new_coach

    def reverse_train_direction(self):
    
        prev_coach = None
        current_coach = self.engine_head
        
        while current_coach is not None:
            next_coach = current_coach.next   
            current_coach.next = prev_coach    
            prev_coach = current_coach         
            current_coach = next_coach        
        self.engine_head = prev_coach

    def display_manifest(self):
        if not self.engine_head:
            print(f"Train {self.train_number} has no coaches attached.")
            return
        
        print(f"[Engine {self.train_number}]", end=" -> ")
        current = self.engine_head
        while current:
            print(f"({current.coach_id}: {current.coach_type})", end=" -> ")
            current = current.next
        print("[End]")



if __name__ == "__main__":
    
    kerala_express = TrainSequence("12626")

    
    kerala_express.attach_coach("HA1", "First AC")
    kerala_express.attach_coach("A1", "AC 2-Tier")
    kerala_express.attach_coach("B1", "AC 3-Tier")
    kerala_express.attach_coach("S1", "Sleeper Class")
    kerala_express.attach_coach("S2", "Sleeper Class")
    kerala_express.attach_coach("GS", "General Second Class")
    print("  RAILWAY MANAGEMENT SYSTEM - COUPLING MANIFEST             ")
    print("\n[ALERT] Original Departure Sequence:")
    kerala_express.display_manifest()
    print("\n[SYSTEM] Route Change Exception Triggered! Reversing operational orientation...")
    kerala_express.reverse_train_direction()
    print("\n[SUCCESS] New Flipped Departure Sequence:")
    kerala_express.display_manifest()
