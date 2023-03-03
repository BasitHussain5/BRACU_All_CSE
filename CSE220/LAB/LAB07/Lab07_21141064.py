# Lab 07 CSE220
# Name: Basit Hussain
# ID: 21141064
# Sec: 13

# Task 01

# a) Implement a recursive algorithm to find factorial of n. 


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))



# b) Implement a recursive algorithm to find the n-th Fibonacci number.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))


# c) Print all the elements of a given array recursively.

def print_array(array, ind):
    if ind < len(array):
        print(array[ind])
        print_array(array, ind + 1)
print_array([1,2,3,4,5], 0)


# d)

def power(x, y):
    if y > 0:
        return x * power(x , y - 1)
    else:
        return 1
        
print(power(3, 3))


# Task 02

# a)

def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decimal_to_binary(n // 2)
    
print(decimal_to_binary(13))



# b

class Node:
    def __init__(self, e):
        self.e = e
        self.next = None
        
class LinkedList:
    def __init__(self, array):
        self.head = Node(array[0])
        tail = self.head
        i = 1
        while i < len(array):
            new_node = Node(array[i])
            tail.next = new_node
            tail = tail.next
            i += 1
                      
    def add(self, head):
        if head.next == None:
            return head.e
        else:
            return head.e + self.add(head.next)
    def print_add(self):
        return self.add(self.head)

              
lst = [1,2,3,4,5,6,7,8,9]
L1 = LinkedList(lst)
print(L1.print_add())


# c)


class Node:
    def __init__(self, e):
        self.e = e
        self.next = None
        
class LinkedList:
    def __init__(self, array):
        self.head = Node(array[0])
        tail = self.head
        i = 1
        while i < len(array):
            new_node = Node(array[i])
            tail.next = new_node
            tail = tail.next
            i += 1
            
    def reverse(self, head):
        if head.next == None:
            print(head.e)
        else:
            self.reverse(head.next)
            print(head.e)
    def rev_print(self):
        return self.reverse(self.head)
    
a = [1,2,3,4,5,6,7,8,9]
L = LinkedList(a)
L.rev_print()



# Task 03


def hocBuilder(height): 
    if height == 0:
        return 0
    if height == 1:
        return 8
    else:
        return 5 + hocBuilder(height - 1)
    
print(hocBuilder(3))


# Task 4


# a)

def pattrn(n):
    if n == 0:
        return 0
    else:
        pattrn(n-1)
        print(n, end = "")
        
def p(n):
    if n == 0:
        return n
    else:
        p(n-1)
    pattrn(n)
    print()
        
p(5)     




# b)

def pattrn(n):
    if n == 0:
        return 0
    else:
        pattrn(n-1)
        print(n, end="")
        
def p(n, x):
    if n == 0:
        return 0
    else:
        s(n-1)
        pattrn((x)-n+1)
        print()
        p(n-1, x)
    
def s(n):
    if n == 0:
        return 0
    else:
        s(n - 1)
        print("", end=" ")
    
p(5,5)




# Task 05

class final_question:
    def prnt(self, array, i):
        if (i < len(array)):
            print(f"{str(i+1)}. Investment: {array[i]} Profit: {self.calc_profit(array[i])}")
            self.prnt(array, i+1)
                  
    def calc_profit(self, inves):
        if inves <= 25000:
            return 0.0
        elif inves > 25000 and inves <= 100000:
            return 45 + self.calc_profit(inves - 1000)
        elif inves > 100000:
            return 80 + self.calc_profit(inves - 1000)
        else:
            return 0     
                  
array = [25000, 100000, 250000,350000]
obj = final_question()
obj.prnt(array, 0)

