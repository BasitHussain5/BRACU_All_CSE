# Name: Basit Hussain
# ID: 21141064

class CircularArray:
    def __init__(self, lin, st, sz):
        # Initializing Variables
        self.lin = lin
        self.start = st
        self.size = sz
        self.cir = [None] * len(lin)


        # if lin = [10, 20, 30, 40, None]
        # then, CircularArray(lin, 2, 4) will generate
        # cir = [40, null, 10, 20, 30]
        # To Do. 
        # Hints: set the values for initialized variables
        i = 0
        while i < sz:
            self.cir[st] = self.lin[i]
            st = (st + 1) % len(self.cir)
            i = i + 1
        #0 < 4 => self.cir[2] = self.lin[0]=> [None, None, 10, None, None]
        #1 < 4 => self.cir[3] = self.lin[1]=> [None, None, 10, 20, None]
        #2 < 4 => self.cir[4] = self.lin[2]=> [None, None, 10, 20, 30]
        #1 < 4 => self.cir[0] = self.lin[3]=> [40, None, 10, 20, 30]
 
    # Print from index 0 to len(cir) - 1
    def printFullLinear(self): #Easy
    # To Do
        for i in range(len(self.cir)):
            if i != len(self.cir) - 1:
                print(self.cir[i], end = ", ")
            else:
                print(self.cir[i])
                

    # Print from start index and total size elements
    def printForward(self): #Easy
        self.st = self.start
        i = 0
        while i < self.size:
            if i != self.size - 1:
                print(self.cir[self.st], end = ", ")
            else:
                print(self.cir[self.st])
                
            self.st = (self.st + 1) % len(self.cir)
            i = i + 1
            
    def printBackward(self): #Easy
    # To Do
        self.st_ind = (self.start + self.size - 1) % len(self.cir)
        i = 0
        while i < self.size:
            if i != self.size - 1:
                print(self.cir[self.st_ind], end = ", ")
            else:
                print(self.cir[self.st_ind])
            self.st_ind = self.st_ind - 1
            if self.st_ind < 0:
                self.st_ind = len(self.cir) -1
            #self.st_ind = (self.st_ind - 1) % len(self.cir)
            i = i + 1
            
    # With no null cells
    def linearize(self): #Medium 
        self.linearize = [0] * self.size
        self.st = self.start
        i = 0
        while i < self.size:
            self.linearize[i] = self.cir[self.st]
            self.st = (self.st + 1) % len(self.cir)
            i = i + 1
        self.cir = self.linearize
        
    # Do not change the Start index
    def resizeStartUnchanged(self, newcapacity): #Medium [40, 50, 10, 20, 30] [0, 0, 0, 0, 0, 0, 0, 0]
    # To Do
        self.newcapacity = newcapacity
        self.resiz = [None] * self.newcapacity
        self.k = self.start
        self.l = self.start
        i = 0
        while i < self.size:
            self.resiz[self.k] = self.cir[self.l]
            self.l = (self.l + 1) % len(self.cir)
            self.k += 1
            i = i + 1
        self.cir = self.resiz
        
    # This method will check whether the array is palindrome or not
    def palindromeCheck(self): #Hard
        self.st_ind = self.start
        self.last_ind = (self.st_ind+self.size-1)%len(self.cir)
        check = 0
        i = 0
        while i < self.size//2:
            if self.cir[self.st_ind] == self.cir[self.last_ind]:
                check += 0
            else:
                check += 1

            self.st_ind += 1
            if self.st_ind > len(self.cir):
                self.st_ind = (self.st_ind+self.size-1)%len(self.cir)
            self.last_ind -= 1
            if self.last_ind< 0:
                self.last_ind = len(self.cir)-1
            i += 1
        if (check==0):
            print("This array is a palindrome")
        else:
            print("This array is NOT a palindrome")
        
    # This method will sort the values by keeping the start unchanged
    def sort(self): #[-30, 20, 50, 30, None, 10, 20]   -30, 10, 20, 20, 30, 50  
        self.st = self.start
        i = 0
        while i < self.size:
            j = i +1
            while j < self.size:
                if self.cir[(j+self.st)%len(self.cir)] < self.cir[(i+self.st)%len(self.cir)]:
                    temp = self.cir[(self.st+i)%len(self.cir)]
                    self.cir[(self.st+i)%len(self.cir)] = self.cir[(self.st+j)%len(self.cir)]
                    self.cir[(self.st+j)%len(self.cir)] =  temp

                j += 1
            i += 1

    # This method will check the given array across the base array and if they are equivalent interms of values return true, or else return false
    def equivalent(self, cir_arr):
        self.cir_arr = cir_arr
        flag = False
        self.s1 = self.start
        self.s2 = cir_arr.start
        i = 0
        while i < self.size:
            if self.cir[self.s1] == cir_arr.cir[self.s2]:
                flag = True
            else:
                flag = False
                break
            self.s1 = (self.s1 +1) % len(self.cir)
            self.s2 = (self.s2 +1) % (len(cir_arr.cir))
            i += 1
        return flag

    # the method take another circular array and returns a linear array containing the common elements between the two circular arrays.
    def intersection(self, c2): 
        self.s1 = self.start
        self.cir1 = [0] * self.size
        i = 0
        while i <self.size:
            self.cir1[i] = self.cir[self.s1]
            self.s1 = (self.s1+1) % len(self.cir)
            i +=1
        self.s2 = c2.start    
        self.cir2 = [0] * c2.size
        j = 0
        while j < c2.size:
            self.cir2[j] = c2.cir[self.s2]
            self.s2 = (self.s2+1) % len(c2.cir)
            j += 1
        self.intersec_array = []
        for i in self.cir1:
            if i in self.cir2:
                self.intersec_array.append(i)
        return self.intersec_array







# Tester class. Run this cell after completing methods in the upper cell and
# check the output


lin_arr1 = [10, 20, 30, 40, None]

print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10


print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40


print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None


print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None] #[10, None, None, 10, 20, 30, 20]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome


print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome


print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50


print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None] #[30, None, 10, 20, -30, 20, 50]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True


print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True


print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False


print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]
