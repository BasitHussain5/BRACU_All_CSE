# CSE220 LAB_05
# 21141064
# Basit Hussain
# Sec: 13



class  ArrayStack:
  def __init__(self, sz):
    self.bracketsTracker_stack = [None] * sz
    self.indexTracker_stack = [None] * sz
    self.size1 = 0
    self.size2 = 0
  def push(self, e):
    if self.size1 == len(self.bracketsTracker_stack):
        print("No space in array")
    else:
        if str(e) in "({[":
            self.bracketsTracker_stack[self.size1] = e
            self.size1 += 1
        else:
            self.indexTracker_stack[self.size2] = e
            self.size2 += 1
  def pop(self):
    if self.size1 == 0:
      return ("Array is empty")
    else:
      temp1 = self.bracketsTracker_stack[self.size1-1]
      self.bracketsTracker_stack[self.size1-1] = 0
      temp2 = self.indexTracker_stack[self.size2-1]
      self.indexTracker_stack[self.size2-1] = 0
      self.size1 -= 1
      self.size2 -= 1
      return temp1, temp2
  def peek(self):
    if self.size1 == 0:
      return ("Array is empty")
    else:
      temp = self.bracketsTracker_stack[self.size-1]
      return temp
  def is_empty(self):
    return self.size1 == 0
    
  def balancing(self, string):
    check = True
    for i in range(len(string)):
        if string[i] in "({[":
            self.push(string[i])
            self.push(i)
        else:
            if string[i] in ")}]":
                if self.is_empty() == True:
                    check = "This expression is NOT correct."
                    error = "\nError at character # " + str(i+1) + ". " + str(string[i]) + "- not opened."
                    output = "{} {}". format(check, error)
                    return output
                top = self.pop()
                if top == "(":
                    if string[i] != ")":
                        check = False
                if top == "{":
                    if string[i] != "}":
                        check =  False
                if top == "[":
                    if string[i] != "]":
                         check =  False
    if self.is_empty() == True and check == True:
        return "This expression is correct."
    else:
        check = "This expression is NOT correct."
        error = "\nError at character # " + str(top[0]) + ". " + str(top[1]+1) + "- not closed." 
        output = "{} {}". format(check, error)
        return output
        
        
        
print("==========Test 1==========")
string = "1+2*(3/4)"
s1 = ArrayStack(len(string))
print(s1.balancing(string))




class Node:
  def __init__(self, e):
    self.e = e
    self.next = None

class LinklistStack:
  def __init__(self):
      self.head1 = None
      self.size1 = 0
      self.head2 = None
      self.size2 = 0
  def push(self, val):
    if self.head1 == None:
        if str(val) in "({[":
            self.head1 = Node(val)
            self.size1 += 1
        else:
            self.head2 = Node(val)
            self.size2 += 1  
    else:
        if str(val) in "({[":
            n1 = Node(val)
            n1.next = self.head1
            self.head1 = n1
            self.size1 += 1
        else:
            n2 = Node(val)
            n2.next = self.head2
            self.head2 = n2
            self.size2 += 1
  def pop(self):
    if self.head1 == None:
        return ("LinkList is empty")
    else:
        h1 = self.head1
        t1 = h1.e
        self.head1 = h1.next
        h1 = None
        self.size1 -= 1
        
        h2 = self.head2
        t2 = h2.e
        self.head2 = h2.next
        h2 = None
        self.size2 -= 1
        return t1, t2
  def peek(self):
    if self.head1 == None:
        return ("LinkList is empty")
    else:
        return self.head1.e
  def is_empty(self):
    return self.size1 == 0
    
  def balancing(self, string):
    check = True
    for i in range(len(string)):
        if string[i] in "({[":
            self.push(string[i])
            self.push(i)
        else:
            if string[i] in ")}]":
                if self.is_empty() == True:
                    check = "This expression is NOT correct."
                    error = "\nError at character # " + str(i+1) + ". " + str(string[i]) + "- not opened."
                    output = "{} {}". format(check, error)
                    return output
                top = self.pop()
                if top == "(":
                    if string[i] != ")":
                        check =  False
                if top == "{":
                    if string[i] != "}":
                        check =  False
                if top == "[":
                    if string[i] != "]":
                        check =  False
    if self.is_empty() == True and check == True:
        return "This expression is correct."
    else:
        check = "This expression is NOT correct."
        error = "\nError at character # " + str(top[1]+1) + ". " + str(top[0]) + "- not closed." 
        output = "{} {}". format(check, error)
        return output
        
print("==========Test 1==========")        
l = LinklistStack()
string = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
print(l.balancing(string))
