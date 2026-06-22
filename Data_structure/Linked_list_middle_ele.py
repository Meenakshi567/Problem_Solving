class EmployeeNode:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id      
        self.name = name          
        self.next = None
class EmployeeRoster:
    def __init__(self):
        self.head = None         
    def add_employee(self, emp_id, name):
        new_employee = EmployeeNode(emp_id, name)
        if not self.head:
            self.head = new_employee
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_employee

    def find_middle_employee(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next       
            fast = fast.next.next  
        return slow
    def display_roster(self):
        if not self.head:
            print("The roster is currently empty.")
            return
        current = self.head
        while current:
            print(f"[{current.emp_id}: {current.name}]", end=" -> ")
            current = current.next
        print("End")
if __name__ == "__main__":
    print("     HR MANAGEMENT SYSTEM - MID-POINT PERFORMANCE REVIEW     ")
    roster = EmployeeRoster()
    
    print("Enter employees in their chronological order of joining.")
    emp_count = 1
    while True:
        print(f"\nEntering details for Employee #{emp_count}:")
        e_id = input("  Enter Employee ID (e.g., EMP101) or 'done' to finish: ").strip()
        
        if e_id.lower() == 'done':
            if emp_count == 1:
                print("  [Alert] Please register at least one employee.")
                continue
            break
            
        e_name = input("  Enter Employee Name: ").strip()
        
        roster.add_employee(e_id, e_name)
        print(f"  [Success] Registered {e_name} (ID: {e_id}).")
        emp_count += 1
    print("CURRENT CHRONOLOGICAL ROSTER:")
    roster.display_roster()

    # Execute the single-pass middle identification algorithm
    print("\n[SYSTEM] Calculating mid-point roster balance...")
    middle_emp = roster.find_middle_employee()

    if middle_emp:
        print(" TARGET EMPLOYEE IDENTIFIED FOR PERFORMANCE REVIEW ")
        print(f"  Employee ID:   {middle_emp.emp_id}")
        print(f"  Employee Name: {middle_emp.name}")
        if emp_count % 2 == 1:
            print("Note: The roster has an even number of employees.")
            print("The system naturally picked the second middle element.")
