# Lab: 08
# Name: Basit Hussain
# ID: 21141064
# Sec: 13


# 1

def swap(Array, i, min_ind):
    temp = Array[i]
    Array[i] = Array[min_ind]
    Array[min_ind] = temp
    
def selection_sorting(Array, i, n):
    min_ind = i
    j = i+1
    while j < n:
        if Array[j] < Array[min_ind]:
            min_ind = j
        j += 1
            
    swap(Array, min_ind , i)
    
    if i+1 < n:
         selection_sorting(Array, i+1, n)
        
    
Array = [9,-3,2,5]    
selection_sorting(Array, 0, len(Array))

print(Array)


# 2
def insert_sort(Array, i):
    n = len(Array)
    if i == n:
        return -1
    if i < n:
        j = i -1
        k = Array[i]
        while j >= 0 and k < Array[j]:
            Array[j+1] = Array[j]
            j = j-1
            Array[j+1] = k
            insert_sort(Array, i+1)
            
Array = [9,-3,2,5]    
insert_sort(Array,1)

print(Array)




# 3

class Node:
    def __init__(self, e):
        self.element = e
        self.next = None
    
class LinkedList:
    def __init__(self, a):
        self.head = None
        tail = None
        for i in a:
            new_node = Node(i)
            if self.head is None:
                self.head = new_node
                tail = new_node 
            else:
                tail.next = new_node
                tail = new_node
    def printList(self):
        x = self.head
        if x is None:
            print("List is Empty!")
        else:
            while x is not None:
                if x.next is None:
                    print(x.element)
                    break
                else:
                    print(x.element, end = ", ")
                    x = x.next
                    
    def bubble_sort(self):
        head = self.head
        tail = None
        if self.head is None:
            return
        else:
            while head is not None:
                tail = head.next
                while tail is not None:
                    if tail.element < head.element:
                        head.element, tail.element = tail.element, head.element
                    tail = tail.next
                head = head.next
                          
a1 = [9,-3,2,5]  
h1 = LinkedList(a1)
print("Before Sorting")
h1.printList()
h1.bubble_sort()
print("After Sorting")
h1.printList()




# 4

class Node:
    def __init__(self, e):
        self.element = e
        self.next = None
    
class LinkedList:
    def __init__(self, a):
        self.head = None
        tail = None
        for i in a:
            new_node = Node(i)
            if self.head is None:
                self.head = new_node
                tail = new_node 
            else:
                tail.next = new_node
                tail = new_node
    def printList(self):
        x = self.head
        if x is None:
            print("List is Empty!")
        else:
            while x is not None:
                if x.next is None:
                    print(x.element)
                    break
                else:
                    print(x.element, end = ", ")
                    x = x.next
                    
    def selection_sort(self):
        head = self.head
        if self.head is None:
            return
        else:
            while head.next is not None:
                tail = head
                element = head.element
                n_element = head.next
                while n_element is not None:
                    if element > n_element.element:
                        element = n_element.element
                        tail = n_element
                    n_element = n_element.next
                head.element, tail.element = tail.element, head.element
                head = head.next
                    
                    
a1 = [9,-3,2,5]  
h1 = LinkedList(a1)
print("Before Sorting")
h1.printList()
h1.selection_sort()
print("After Sorting")
h1.printList()




# 5
class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p
class DoublyList:
    def __init__(self, a):
        self.head = Node(a[0],None,None)
        tail = self.head
        for i in range(1, len(a)):
            new_node = Node(a[i], None, tail)
            tail.next = new_node
            tail = new_node
    
  # prints the elements in the list
    def printList(self):
        if self.head.next is None:
            print("Empty list")
        else:
            head = self.head
            while self.head is not None:
                if head.next is None:
                    print(head.element)
                    break
                else:
                    print(head.element, end =" ")
                    head = head.next
    
    
    def insert_sort(self):
        head = self.head
        if head is None:
            return
        else:
            while head is not None:
                tail = head.next
                while tail and tail.prev != None and tail.element < tail.prev.element:
                    tail.element, tail.prev.element = tail.prev.element, tail.element
                    tail = tail.prev
                head = head.next
 
a1 = [9,-3,2,5]  
h1 = DoublyList(a1)
print("Before Sorting")
h1.printList()
h1.insert_sort()
print("After Sorting")
h1.printList()



# 6
def recursive_binary_search(a, l, r,v):
    if l > r:
        return -1
    else:
        m_v = int((l+r)//2)
        if a[m_v] < v:
            return recursive_binary_search(a, m_v+1, r, v)
        elif a[m_v] > v:
            return recursive_binary_search(a, l, m_v-1, v)
        else:
            return m_v
        
a = [1,2,3,4,5,6,7]
print(recursive_binary_search(a, 0, len(a),4))
                
