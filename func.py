import random
import time
class func:
    def __init__(self):
        self.cont = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.lose = False
        self.score = 0
        self.add()
        
    def add(self):
        add_list = [2,2,2,4]
        zero_list = []
        for i in range(len(self.cont)):
            for j in range(len(self.cont[i])):
                if self.cont[i][j] == 0:
                    zero_list.append([i,j])
        if len(zero_list) != 0:  
            self.random_add = random.choice(zero_list)
            self.cont[self.random_add[0]][self.random_add[1]]=random.choice(add_list)
        
    def check_lose(self):
        zero_list = []
        for i in range(len(self.cont)):
            for j in range(len(self.cont[i])):
                if self.cont[i][j] == 0:
                    zero_list.append([i,j])
        if len(zero_list) == 0:
            samenum = False
            for i in range(4):
                for j in range(3):
                    if self.cont[i][j] == self.cont[i][j+1]:
                        samenum = True
            for i in range(3):
                for j in range(4):
                    if self.cont[i][j] == self.cont[i+1][j]:
                        samenum = True
            if samenum: return 0
            else: return "lose"
        return 0
    def up(self):
        first_check = ""
        for x in self.cont:
            first_check += ",".join(list(map(str,x))) + ","
        for i in range(4):
            #remove 0
            temp_arr = []
            for x in self.cont:
                temp_arr.append(x[i])
            temp_arr = list(filter(lambda a: a != 0, temp_arr))
            while len(temp_arr) < 4:
                temp_arr.append(0)
            #sum up same num
            for j in range(3):
                if temp_arr[j] == temp_arr[j+1]:
                    temp_arr[j]*=2
                    self.score += temp_arr[j]
                    for k in range(j+1,3):
                        temp_arr[k] = temp_arr[k+1]
                    temp_arr[3] = 0
            for j in range(4):
                self.cont[j][i] = temp_arr[j]
        second_check = ""
        for x in self.cont:
            second_check += ",".join(list(map(str,x))) + ","
        if first_check != second_check: 
            self.add()
            return self.check_lose(),True
        return self.check_lose(),False
    def down(self):
        first_check = ""
        for x in self.cont:
            first_check += ",".join(list(map(str,x))) + ","
        for i in range(4):
            #remove 0
            temp_arr = []
            for x in self.cont:
                temp_arr.append(x[i])
            temp_arr = list(filter(lambda a: a != 0, temp_arr))
            temp_arr.reverse()
            while len(temp_arr) < 4:
                temp_arr.append(0)
            #sum up same num
            for j in range(3):
                if temp_arr[j] == temp_arr[j+1]:
                    temp_arr[j]*=2
                    self.score += temp_arr[j]
                    for k in range(j+1,3):
                        temp_arr[k] = temp_arr[k+1]
                    temp_arr[3] = 0
            temp_arr.reverse()
            for j in range(4):
                self.cont[j][i] = temp_arr[j]
        second_check = ""
        for x in self.cont:
            second_check += ",".join(list(map(str,x))) + ","

        if first_check != second_check: 
            self.add()
            return self.check_lose(),True
        return self.check_lose(),False
    def left(self):
        first_check = ""
        for x in self.cont:
            first_check += ",".join(list(map(str,x))) + ","
        for i in range(4):
            #remove 0
            self.cont[i] = list(filter(lambda a: a != 0, self.cont[i]))
            while len(self.cont[i]) < 4:
                self.cont[i].append(0)
            #sum up same num
            for j in range(3):
                if self.cont[i][j] == self.cont[i][j+1]:
                    self.cont[i][j]*=2
                    self.score += self.cont[i][j]
                    for k in range(j+1,3):
                        self.cont[i][k] = self.cont[i][k+1]
                    self.cont[i][3] = 0
        second_check = ""
        for x in self.cont:
            second_check += ",".join(list(map(str,x))) + ","
        if first_check != second_check: 
            self.add()
            return self.check_lose(),True
        return self.check_lose(),False
    def right(self):
        first_check = ""
        for x in self.cont:
            first_check += ",".join(list(map(str,x))) + ","
        for x in self.cont:
            x.reverse()
        for i in range(4):
            #remove 0
            self.cont[i] = list(filter(lambda a: a != 0, self.cont[i]))
            while len(self.cont[i]) < 4:
                self.cont[i].append(0)
            #sum up same num
            for j in range(3):
                if self.cont[i][j] == self.cont[i][j+1]:
                    self.cont[i][j]*=2
                    self.score += self.cont[i][j]
                    for k in range(j+1,3):
                        self.cont[i][k] = self.cont[i][k+1]
                    self.cont[i][3] = 0
        for x in self.cont:
            x.reverse()
        second_check = ""
        for x in self.cont:
            second_check += ",".join(list(map(str,x))) + ","
        if first_check != second_check: 
            self.add()
            return self.check_lose(),True
        return self.check_lose(),False