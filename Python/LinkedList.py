"""
Expanded exercise/problem skeleton from Udacity:
Instructions:
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        index = 1
        while (current) :
             if (index == position):
                 return current.value
             index = index + 1
             current = current.next 
        return None        
                
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        if new_element == None:
            return;
        
        current = self.head
        prev = self
        index = 1
       
        while (current) :
            if position == index:
               if index == 1 : 
                   prev.head = new_element
               else:
                   prev.next = new_element     
               new_element.next = current
               break 
            else:
               prev = current 
               current = current.next 
               index = index + 1
            
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = self
        while (current):
            if (current.value == value):
                if prev == self:
                   prev.head = current.next 
                else :   
                   prev.next = current.next 
                current = None
                break
            prev = current
            current = current.next

    def print(self):
        """Added this for printing the whole list
        Useful for debugging."""
        
        cur  = self.head
        while cur:
            print(cur.value)
            cur = cur.next
                
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


ll.print()
    

# Test get_position
# Should print 3
#print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3))

# Test insert
ll.insert(e4,3)


ll.print()

# Should print 4 now
#print(ll.get_position(3).value)

# Test delete
ll.delete(3)

print(ll.get_position(1))


#print(ll.get_position(2).value)

#print(ll.get_position(3).value)
