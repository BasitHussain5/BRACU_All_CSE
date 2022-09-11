# CSE220 LAB 06
# NAME: BASIT HUSSAIN
# ID: 21141064
# SEC: 13


# TASK 01

class keyIndex:
    def __init__(self, a):
        self.a = a

        # Find Min Val
        self.min_val = self.a[0]
        i = 1
        while i < len(self.a):
            if self.a[i] < self.min_val:
                self.min_val = self.a[i]
            i = i + 1
            
        # check negative values are present or not
        if self.min_val < 0:
            x = self.min_val * -1
            for i in range(len(self.a)):
                self.a[i] = self.a[i] + x

        # Find Max Val
        max_val = self.a[0]
        i = 1
        while i < len(self.a):
            if self.a[i] > max_val:
                max_val = self.a[i]
            i = i + 1
        
        
        # creat Aux Array
        self.Aux = [0] * (max_val +1)

        
        
        # Scan over Array
        i = 0
        while i < len(self.a):
            x = self.a[i]
            self.Aux[x] = self.Aux[x] + 1 
            i = i + 1

        
        

    def search(self, k):
        if self.min_val >= 0: 
            if k >= 0 and k < len(self.Aux):
                if self.Aux[k] > 0:
                    return True
            return False
    
        else:
            if k >= self.min_val and k < len(self.Aux)+self.min_val:
                if self.Aux[k+abs(self.min_val)] > 0:
                    return True
            return False
        
        
        
    def sort(self):
        k = 0
        i = 0
        while i < len(self.Aux):
            if self.min_val >= 0: 
                if self.Aux[i] != 0:
                    for s in range(self.Aux[i]):
                        self.a[k] = i
                        k +=1
            else:
                if self.Aux[i] != 0:
                    for s in range(self.Aux[i]):
                        self.a[k] = i+self.min_val
                        k += 1
                    
            i += 1
        return (self.a)
    
    
    
    
print("==========Test 1==========")      
list_1 =[4, 0, 3, 4, 2, 9, 7]
key_indx = keyIndex(list_1)
print(key_indx.search(0))
print(key_indx.sort())

print("==========Test 2==========")  

list_2 =[4, 0, -3, 4, -2, 9, 7]
key_indx = keyIndex(list_2)
print(key_indx.search(-2))
print(key_indx.sort())






# TASK 02

vowels_letters = ["A", "E", "I", "O", "U"]
consonants_letters = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S","T", "V", "W", "X","Y", "Z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

class Hashstring:
    def __init__(self, s):
        self.s = s
    def string_get(self):
        return self.s
        
    def s_key(self):
        v = 0
        n = 0
        for x in self.s:
            if x in consonants_letters:
                v += 1
            if x not in consonants_letters and x not in vowels_letters:
                n += int(x)
        skey = ((v*24) +n)
        return skey
    

class Hashtable:
    def __init__(self, size = 9):
        self.size = size
        self.lis = [0] * size

    def func(self, s_key):
        return s_key % self.size

    def linear_probing(self, s):
        v = s.s_key()
        pos = self.func(v)
        j = 1
        while j < self.size:
            if self.lis[pos] == 0:
                self.lis[pos] = s.string_get()
                break
            else:
                pos = (v + j) % self.size
            j += 1
                

    def print_sorted_HS(self):
        i = 0
        while i < (self.size):
            print(self.lis[i])
            i += 1

            
            
print("==========Test 1==========")  
h = Hashtable()
l = ["X9ZAR2JD6F7", "ZJO9V49NDOU", "G94F5SMC2DG", "KD9LNX46TT2",
        "WN2NY54F22D", "YVRFKVUOH6Y", "NJ89I7DN7V8", "5W8UWJSDCJH", "5YLHRBO79CT"]
i = 0
while i < len(l):
    v = Hashstring(l[i])
    h.linear_probing(v)
    i+=1
h.print_sorted_HS()
                

