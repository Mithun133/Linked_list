class Node:
    def __init__(self, data='Head', next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def get_length(self):
        count = 0
        n = self.head
        while n:
            count = count + 1
            n = n.next
        return count


    def print_LL(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.next

    def add_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  


    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node 


    def search(self, search_data):
        n = self.head.next

        while n != None:
            if n.data == search_data:   
                print("Data found in linked list.")
                return

            n = n.next  
        print("Data not found")  


ll = LinkedList()
print("Linked list : ")
ll.add_end(5)
ll.add_end(10)
ll.add_end(15)
ll.add_end(20)
ll.print_LL()

ll.search(15)
ll.search(40)
