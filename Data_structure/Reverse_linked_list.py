class CoachNode:
    def __init__(self, coach_id):
        self.coach_id = coach_id        
        self.next = None               
class TrainSequence:
    def __init__(self, train_number):
        self.train_number = train_number
        self.engine_head = None        
    def attach_coach(self, coach_id):
        new_coach = CoachNode(coach_id)
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
        
        current = self.engine_head
        while current:
            print(f"{current.coach_id}", end=" -> ")
            current = current.next
        print("[End]")



if __name__ == "__main__":
    
    kerala_express = TrainSequence("12626")

    
    kerala_express.attach_coach("HA1")
    kerala_express.attach_coach("A1")
    kerala_express.attach_coach("B1")
    kerala_express.attach_coach("S1")
    kerala_express.attach_coach("S2")
    kerala_express.attach_coach("GS")
    print("\n Original Departure Sequence:")
    kerala_express.display_manifest()
    kerala_express.reverse_train_direction()
    print("\n[SUCCESS] New Flipped Departure Sequence:")
    kerala_express.display_manifest()
