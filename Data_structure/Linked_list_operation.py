class Node:
   def __init__ (self,data):
      self.data = data
      self.next = None
class Linked_List:
   def __init__(self):
      self.head = None
   def insert_at_first(self,data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
   def insert_at_last(self,data):
      new_node = Node(data)
      if not self.head:
         self.head = new_node
         return
      current = self.head
      while current.next:
         current = current.next
      current.next = new_node
   def delete_value(self,key):
       current = self.head
       if current and current.data == key:
           self.head = current.next
           current = None
           return
       prev = None
       while current and current.data != key:
           prev = current
           current = current.next
       if not current:
           print("The value is not found")
       prev.next = current.next
       current = None
   def display(self):
       if not self.head:
           print("The list is empty")
           return
       current = self.head
       while current:
           print(current.data, end = "->")
           current = current.next
       print("None")
llist = Linked_List()
while True:
    print("\n==============================")
    print("   LINKED LIST OPERATIONS   ")
    print("==============================")
    print("1. Insert at Beginning")
    print("2. Append to End")
    print("3. Delete a Value")
    print("4. Display Linked List")
    print("5. Exit")
    print("==============================")
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue
    if choice == 1:
        try:
            data = int(input("Enter integer value to insert at beginning: "))
            llist.insert_at_last(data)
        except ValueError:
            print("Invalid data type. Please input an integer.")
                
    elif choice == 2:
        try:
            data = int(input("Enter integer value to append to end: "))
            llist.insert_at_last(data)
        except ValueError:
            print("Invalid data type. Please input an integer.")
                
    elif choice == 3:
        if not llist.head:
            print("The list is empty. Nothing to delete.")
            continue
        try:
            key = int(input("Enter the value you want to delete: "))
            llist.delete_value(key)
        except ValueError:
            print("Invalid data type. Please input an integer.")
                
    elif choice == 4:
        print("\n--- Current Linked List State ---")
        llist.display()
            
    elif choice == 5:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please pick an option from 1 to 5.")
    
