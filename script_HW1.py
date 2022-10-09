
#######################################################################
#                    Homework 1 - Gian Alvin Guico                    #
#######################################################################


#### Problem 1
''' 1) Introduction'''

#1.1) Say "Hello, World!" With Python
print("Hello, World!")

#1.2) Python If-else
n = int(input().strip())
    
if n%2 != 0:
    print("Weird")
if n%2==0 and (n >= 2 and n <= 5):
    print("Not Weird")
if n%2==0 and (n >= 6 and n <= 20):
    print("Weird")
if n%2==0 and n> 20:
        print("Not Weird")

#1.3) Arithmetic Operators
a = int(input())
b = int(input())
    
sum = int(a+b)
dif = int(a-b)
prod = int(a*b)
    
print(sum)
print(dif)
print(prod)

#1.4) Python: Division
a = int(input())
b = int(input())
    
int_div = int(a//b)
float_div = float(a/b)
    
print(int_div)
print(float_div)

#1.5) Print Function
n = int(input())
    
for i in range(1,n+1):
    print(i,end="")

#1.6) Write a function
def is_leap(year):
    leap = False
    
    if year%4 == 0:
        leap = True
    if year%100 == 0:
        leap = False
    if year%400 == 0:
        leap = True  
            
    return leap

#1.7) Loops
n = int(input())
    
for i in range(0,n):
    print(i*i)

'''2) Basic Data Types'''

#2.1) List Comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    permutations = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    
    print(permutations)

#2.2) Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    new_arr = sorted(arr, reverse = True)
    
    first = new_arr[0]
    second = 0
    
    for i in range(len(new_arr)):
        if new_arr[i] < first:
            second = new_arr[i]
            break
    print(second)

#2.3) Nested Lists
if __name__ == '__main__':
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input() #number of students
        name_list.append(name)
        score = float(input())
        score_list.append(score)

    lowest_grade = 1000
    second_lowest_grade = 1000
    
    for grade in sorted(score_list):
        if grade < lowest_grade:
            second_lowest_grade = lowest_grade
            lowest_grade = grade
        elif grade > lowest_grade and grade < second_lowest_grade:
            second_lowest_grade = grade
    
    students = list(zip(name_list, score_list))
    second_lowest_grade_students = []
    
    for i in range(len(students)):
        if students[i][1] == second_lowest_grade:
            second_lowest_grade_students.append(students[i][0])
    
    for stud in sorted(second_lowest_grade_students):
        print(stud)

# 2.4) Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg = sum(student_marks[query_name])/len(student_marks[query_name])
    print("{:.2f}".format(avg))

#2.5) Lists
if __name__ == '__main__':
    N = int(input()) #number of commands
    
    L = [] #init list
    
    for i in range(N):
        action = input().split()
        #print(action)
        if action[0] == "insert":
            L.insert(int(action[1]), int(action[2]))
        elif action[0] == "print":
            print(L)
        elif action[0] == "remove":
            L.remove(int(action[1]))
        elif action[0] == "append":
            L.append(int(action[1]))
        elif action[0] == "sort":
            L.sort()
        elif action[0] == "pop":
            L.pop()
        else:
            L.reverse()

#2.6) Tuples
if __name__ == '__main__':
  n = int(input())
  integer_list = map(int, input().split())
  
  t = tuple(integer_list)
  print(hash(t))

'''3) Strings'''

#3.1) sWAP cASE
def swap_case(s):
    string = ""
    for c in s:
        if c.isupper():
            string += c.lower()
        else:
            string += c.upper()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#3.2) String Split and Join
def split_and_join(line):
    # write your code here
    new_string = line.split(" ")
    new_string = "-".join(new_string)
    
    return new_string
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#3.3) What's your name?
def print_full_name(first, last):
    print("Hello " + first, last+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#3.4) Mutations
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#3.5) Find a string
def count_substring(string, sub_string):
    occurrences = 0
    
    for i in range(len(string)):
        s = string[i:i+len(sub_string)]
        if s == sub_string:
            occurrences += 1

    return occurrences

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#3.6)String Validators
if __name__ == '__main__':
    s = input()
    
    flag_alnum = False
    flag_alpha = False
    flag_digit = False
    flag_lower = False
    flag_upper = False
    string_validator_list = []
    
    #.isalnum() check
    for i in range(len(s)):
        if s[i].isalnum():
            flag_alnum = True
            break
        else:
            flag_num = False
    string_validator_list.append(flag_alnum)
    
    #.isalpha() check
    for i in range(len(s)):
        if s[i].isalpha():
            flag_alpha = True
            break
        else:
            flag_alpha = False
    string_validator_list.append(flag_alpha)
    
    #is.digit() check
    for i in range(len(s)):
        if s[i].isdigit():
            flag_digit = True
            break
        else:
            flag_digit = False
    string_validator_list.append(flag_digit)
    
    #.islower() check
    for i in range(len(s)):
        if s[i].islower():
            flag_lower = True
            break
        else:
            flag_lower = False
    string_validator_list.append(flag_lower)
    
    #is.upper() check
    for i in range(len(s)):
        if s[i].isupper():
            flag_upper = True
            break
        else:
            flag_upper = False
    string_validator_list.append(flag_upper)
    
    for i in string_validator_list:
        print(i)



#3.7) Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



#3.8)Text Wrap
import textwrap

def wrap(string, max_width):
    new_string_list = textwrap.wrap(string, max_width)
    new_string_list = "\n".join(new_string_list)
    return new_string_list

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#3.9) Designer Door Mat
if __name__ == '__main__':
    N, M = map(int, input().split())
    
    # part above the word welcome
    for i in range(1,N,2):
        print((i * ".|.").center(M,"-"))
    
    # center line
    print("WELCOME".center(M,"-"))
    
    # part under the word welcome
    for i in range(N-2,-1 ,-2):
        print((i * ".|.").center(M,"-"))

#3.10) String Formatting
def print_formatted(number):
    
    #talue of the space between the outputs
    width = len(bin(number)[2:])

    for i in range(1,number+1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#3.11) Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    width  = size*4-3
    string = ''

    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):    
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
        string = ''

    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
 

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



#3.12) Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    str = ""
    for i in range(len(s)):
    
        if (i == 0 and s[i].islower()) or s[i-1] == " ":
            str += s[i].upper()
        else:
            str += s[i]
    return str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



#3.13) The Minion Game
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    length = len(string)
    vow = 0
    cons = 0
    
    for i in range(length):
        if string[i] in vowels:
            vow += (length - i)
        else:
            cons += (length - i)
            
    if vow < cons:
        print("Stuart", cons)
    elif vow > cons:
        print("Kevin", vow)
    else:
        print("Draw")
        
        

if __name__ == '__main__':
    s = input()
    minion_game(s)


#3.14) Merge the tools!
def merge_the_tools(string, k):
    # your code goes here
    
    l = []
    length = 0
    for item in string:
        length += 1
        
        if item not in l:
            l.append(item)
        if length == k:
            print(''.join(l))
            l = []
            length = 0
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)



''' 4) Sets'''

#4.1) Introduction to sets
def average(array):
    l = set(array)
    avg = sum(l)/len(l)
   
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#4.2)No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n,m = map(int,input().split())
    
arr = input().split()

A = set(input().split())
B = set(input().split())
happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)


#4.3) Symmetric difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    M = int(input())
    a = list(map(int, input().split()))
    
    N = int(input())
    b = list(map(int, input().split()))
    
    A = set(a)
    B = set(b)
    
    not_in_B = list(A.difference(B))
    not_in_A = list(B.difference(A))
    
    diff = not_in_B + not_in_A
    
    for i in sorted(diff):
        print(i)

#4.4) Set.add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    countries = set()
    
    for i in range(N):
        countries.add(input())
    
    print(len(countries))

#4.5) Set.discard(), .remove() and .pop()
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input()) #number of elements in the set
    s = set(input())
    N = int(input())
    
    for i in range(N):
        action = input().split()
        print(action)
        if action[0] == "pop":
            s.pop()
        elif action[0] == "remove":
            s.remove(int(action[1]))
        elif action[0] == "discard":
            s.discard(int(action[1]))
    
    print(len(s))

#4.6) Set.union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input()) #number of students subscribed to the english newspaper
    english_roll_numbers = set(map(int, input().split()))
    b = int(input()) #number of students subscribe to the french newspaper
    french_roll_numbers = set(map(int, input().split()))
    
    print(len(english_roll_numbers.union(french_roll_numbers)))


#4.7) Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    #number of students subscribed to the English newspaper
    n = int(input())
    english_roll_numbers = set(map(int, input().split()))
    #number of students subscribed to the French newspaper
    b = int(input())
    french_roll_numbers = set(map(int, input().split()))
    
    print(len(english_roll_numbers.intersection(french_roll_numbers)))

#4.8) Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    english_roll_numbers = set(map(int, input().split()))
    
    b = int(input())
    french_roll_numbers = set(map(int, input().split()))
    
    print(len(english_roll_numbers.difference(french_roll_numbers)))

#4.9) Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    english_roll_numbers = set(map(int, input().split()))
    
    b = int(input())
    french_roll_numbers = set(map(int, input().split()))
    
    print(len(english_roll_numbers.symmetric_difference(french_roll_numbers)))


#4.10) Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    A = set(map(int, input().split()))
    N = int(input()) #number of other sets
    
    for i in range(N):
        action = input().split()
        other_set = set(map(int, input().split()))
        if action[0] == 'intersection_update':
            A.intersection_update(other_set)
        elif action[0] == 'update':
            A.update(other_set)
        elif action[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(other_set)
        else:
            A.difference_update(other_set)
    
    print(sum(A))


#4.11) The captain's room
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    K = int(input()) #size of each group
    room_number_list = list(map(int, input().split()))
    
    room_set = set()
    capt_room = set()
    
    for room in room_number_list:
        if room not in room_set:
            room_set.add(room)
            capt_room.add(room)
        else:
            capt_room.discard(room)
            
    print(list(capt_room)[0])
    


#4.12) check subset
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    T = int(input()) #number of test cases
    
    for test in range(T):
        
        elements_A = int(input())
        A = set(map(int, input().split()))
        elements_B = int(input())
        B = set(map(int, input().split()))
        
        print(A.issubset(B))

#4.13) check strick superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    A = set(map(int, input().split())) #elements of set A
    n = int(input())
    superset_flag = False
    l = []
    
    for i in range(n):
        other_set = set(map(int, input().split()))
        if len(A) > len(other_set):
            if A.issuperset(other_set):
                superset_flag = True
                l.append(superset_flag)
            else:
                superset_flag = False
                l.append(superset_flag)
                
    if all(l):
        print("True")
    else:
        print("False")
    
'''5) Math'''

#5.1) Polar coordinates
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
if __name__ == "__main__":
    
    z = complex(input())
    
    print(abs(z))
    print(cmath.phase(z))

#5.2) Find Angle MBC
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    
    theta = str(round(math.degrees(math.atan(AB/BC))))
    degree_sign = chr(176)
    theta_fin = theta+degree_sign
    print(theta_fin)

#5.3) Triangle quest 2

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((((10**i)-1)//9)**2)

#5.4) Mod Divmod
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ =="__main__":
    a = int(input())
    b = int(input())
    
    print(int(a/b))
    print(a%b)
    print(divmod(a,b))


#5.5) Power - Mod Power
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    
    print(pow(a,b))
    print(pow(a,b,m))

#5.6) Integers come in all sizes
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a = int(input())
    b = int(input()) 
    c = int(input())
    d = int(input())
    
    print(pow(a,b)+pow(c,d))

#5.7) Triangle quest
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    
    for i in range(1,int(input())):
        print(int(i*(10**i//9)))


'''6) Itertools'''

#6.1) itertools.product()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
if __name__ == '__main__':
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AxB = list(product(A,B))
    for i in AxB:
        print(i, end=" ")

#6.2) itertools.permutations()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
if __name__ == '__main__':
    S = input().split()
    string = S[0]
    permut = int(S[1])
    
    result = list(permutations(string, permut))
    
    for i in sorted(result):
        print(''.join(i))

#6.3) itertools.combinations()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    S = input().split()
    
    string = sorted(S[0])
    k = int(S[1])
    
    for i in range(1,k+1):
        result = list(combinations(string,i))
        for x in result:
            print(''.join(x))

#6.4) itertools.combinations_with_replacement()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cwr

if __name__ == '__main__':
    S = input().split()
    
    string = sorted(S[0])
    k = int(S[1])
    
    result = cwr(string, k)
    
    for i in result:
        print(''.join(i))

#6.5) Compress the String!
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

if __name__ == '__main__':
    s = input()
    
    for i,j in itertools.groupby(s):
        print("(%d, %d)" % (len(list(j)), int(i)), end=' ')

#6.6) Iterable and Iterators
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

if __name__ == '__main__':
    
    n, l, k = int(input()), input().split(), int(input())
    
    count = 0
    list_count = 0
    
    for i in combinations(l,k):
        list_count += 1
        
        if 'a' in i:
            count += 1
            
    print('%.3f' % (count/ list_count))

'''7) Collections'''

#7.1) collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__  == '__main__':
    
    #number of shoes
    X = int(input())

    #list of shoe sizes available in the store
    shoe_sizes = list(map(int, input().split()))
    
    #number of customers
    customers = int(input())
    
    availability = Counter(shoe_sizes)

    money = 0
    for customer in range(customers):
        size, price = map(int, input().split())
        
        if availability[size]:
            money += price
            availability[size] -= 1 #removing the availability of shoes
            
    print(money)

#7.2) DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == '__main__':
    n ,m = map(int, input().split())
    columns = list(input().split())
    
    d = defaultdict(list)
    
    for i in range(1, n+1):
        d[input()].append(i)

    for j in range(m):
        value = input()
        if value in d:
            print(value)

#7.3) Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == '__main__':
    students = int(input())
    cols_name = input().split()
    cols = namedtuple('col', cols_name)
    total_marks = 0

    for student in range(students):
        student_details = input().split()
        rows = cols(ID=student_details[cols_name.index('ID')], MARKS=student_details[cols_name.index('MARKS')],
                    NAME=student_details[cols_name.index('NAME')], CLASS=student_details[cols_name.index('CLASS')])
        total_marks += int(rows.MARKS)

    print("{:0.2f}".format(total_marks/students))

#7.4) Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    
    #number of items
    N = int(input())
    receipt = OrderedDict()
    
    for i in range(N):
        item = input().split()
        name = ' '.join(item[:-1])
        price = int(item[-1])
        if receipt.get(name):
            receipt[name] += price
        else:
            receipt[name] = price
    
    for i in receipt.keys():
        print (i,receipt[i])

#7.5) Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    
    n = int(input())
    
    ord_dict = OrderedDict()
    
    for i in range(n):
        a = input()
        ord_dict[a] = ord_dict.get(a,0)+1
    print(len(ord_dict))
    print(" ".join(str(v) for k,v in ord_dict.items()))

#7.6) Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    N = int(input())
    d = deque()
    
    for i in range(N):
        action = input().split()
        if action[0] == 'append':
            d.append(action[1])
        elif action[0] == 'appendleft':
            d.appendleft(action[1])
        elif action[0] == 'pop':
            d.pop()
        else:
            d.popleft()
    
    for i in range(len(d)):
        print(d[i], end=" ")

#7.7) Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    
    freq = Counter(list(s))
    
    for k,v in freq.most_common(3):
        print(k,v)

'''8) Date and Time'''

#8.1) Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
if __name__ == '__main__':
    
    date = input().split()
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())

#8.2) Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    #Sun 10 May 2015 13:54:36 -0700
    #%a  %d %B  %Y %H:%M:%S %z
    timestamp_1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    timestamp_2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    result = str(abs(int((timestamp_1-timestamp_2).total_seconds())))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input()) #test case

    for t_itr in range(t):
        t1 = input() #timestamp 1

        t2 = input() #timestamp 2

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

'''9) Errors and Exceptions'''

#9.1) Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    T = int(input())
    
    for i in range(1,T+1):
        a, b = input().split()
        
        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as v:
            print("Error Code:",v)

'''10) Classes'''

#10.1) Class 2 - Find the Torsional Angle
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        return Points((self.x-no.x), (self.y-no.y), (self.z-no.z))

    def dot(self, no):
        return Points((self.x*no.x), (self.y*no.y), (self.z*no.z))

    def cross(self, no):
        return Points( (self.y*no.z - self.z*no.y), (self.z*no.x - self.x*no.z), (self.x*no.y - self.y*no.x))
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))

#10.2) Classes: Dealing with Complex Numbers
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex((self.real+no.real), self.imaginary+no.imaginary)
        
    def __sub__(self, no):
        return Complex((self.real-no.real), (self.imaginary-no.imaginary))
        
    def __mul__(self, no):
        r = (self.real*no.real)-(self.imaginary*no.imaginary)
        i = (self.real*no.imaginary+no.real*self.imaginary)
        return Complex (r,i)

    def __truediv__(self, no):
        conj = Complex(no.real,  (-no.imaginary))
        num = self*conj
        denom = no*conj
        try:
            return Complex((num.real/denom.real), (num.imaginary/denom.real))
        except Exception as e:
            print(e)
    def mod(self):
        m = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(m,0)
        

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


'''11) Built-ins'''

#11.1) Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    number_of_students, number_of_subjects = map(int, input().split())
    grades = []
    
    # zipping all grades
    for i in range(number_of_subjects):
        grades.append(list(map(float, input().split())))
    
    #unzipping all grades per student
    grades_per_student = list(zip(*grades))
    
    for grade in grades_per_student:
        print(sum(grade)/number_of_subjects)



#11.2) ginorS
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    s = input()
    
    lower = []
    upper = []
    odd = []
    even = []
    
    for i in s:
        if i.islower():
            lower.append(i)
        elif i.isupper():
            upper.append(i)
        elif int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    print(''.join(sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)))
    
'''12) Python Functionals'''

#Map and Lambda function
cube = lambda x: pow(x,3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fibonacci(n-1))+fibonacci(n-2)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

'''13) Regex and Parsing Challenges'''

#13.1) Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    T = int(input())
    arr = [] 
    for i in range(T):
        i = input()
        arr.append(i)
    for j in arr:
        print(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$',j)))

#13.2) Re.split()
regex_pattern = r"[',' , '.']"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#13.3) Groups(), Groups() and Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
expression=r"([a-zA-Z0-9])\1+"
m=re.search(expression, input())
if m:
    print(m.group(1))
else:
    print('-1')

#13.4) Re.findall() and re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if m:
    for s in m:
        print(s)
else:
    print('-1')

#13.5) Re.start() and Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    S = input()
    k = input()
    
    pattern = re.compile(k)
    m = pattern.search(S)
    
    if not m: print('(-1, -1)')
    else:
        while m:
            print("({0}, {1})".format(m.start(), m.end()-1))
            m = pattern.search(S, m.start()+1)

#13.6) Validating Roman Numerals
regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#13.7) Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

[print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(int(input()))]

#13.8) Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')


#13.9) HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : %s" % tag)
        for attr, value in attrs:
            print("->", attr, ">", value)
    def handle_endtag(self, tag):
        print("End   : %s" % tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty : %s" % tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

string = ''
for _ in range(int(input())):
    string += input()

parser = MyHTMLParser()
parser.feed(string)

#13.10) HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        if (len(data.split('\n')) != 1):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.replace("\r", "\n"))
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#13.11) Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    N = input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')

'''14) XML'''

#14.1) XML 1 - Find the score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    score = 0
    for tag in node:
        score += get_attr_number(tag)
    return score + len(node.attrib)    

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#14.2) XML 2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)
        

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

'''15) Closures and Decorators'''

#15.1) Standardize Mobile Numbers Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


#15.2) Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

'''16) Numpy'''

#16.1) Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr)
    new_arr = a[::-1].astype(float)
    return new_arr
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#16.2) Shape and Reshape
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
if __name__ == "__main__":
    a = input().split()
    my_array = np.array(a, dtype=int)
    print(np.reshape(my_array,(3,3)))


#16.3) Transpose and Flatten
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    arr = []
    
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
  
    new_arr = np.array(arr)
    print(np.transpose(new_arr))
    print(new_arr.flatten())

#16.4) Concatenate
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N, M ,P = map(int, input().split())
    
    #first array of size NxP
    arr_1 = np.array([input().split() for _ in range(N)], dtype=int)
    #second array of size MxP
    arr_2 = np.array([input().split() for _ in range(M)], dtype=int)
    
    print(np.concatenate((arr_1, arr_2), axis = 0))


#16.5) Zeros and Ones
import numpy as np

if __name__ == '__main__':
    dimensions = list(map(int, input().split()))
    
    print(np.zeros(dimensions, dtype=int))
    print(np.ones(dimensions, dtype=int))


#16.6) Eye and Identity
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    print(np.eye(N,M))


#16.7) Floor, Ceil and Rint
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    A = list(map(float, input().split()))
    
    print(np.floor(A))
    print(np.ceil(A))
    print(np.rint(A))


#16.8) Sum and Prod
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    
    A = np.array([input().split() for _ in range(N)], dtype=int)
    
    print(np.prod(np.sum(A, axis=0)))

#16.9) Min and Max
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    
    matrix = np.array([input().split() for _ in range(N)], dtype=int)
    
    print(np.max(np.min(matrix, axis=1)))

#16.10) Mean, Var, and Std
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    arr_2D = np.array([input().split() for _ in range(N)], dtype=int)
    
    print(np.mean(arr_2D, axis=1))
    print(np.var(arr_2D, axis=0))
    print(round(np.std(arr_2D,axis=None),11))

#16.11) Dot and Cross
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N = int(input())
    result = 0

    A = np.array([input().split() for _ in range(N)], dtype=int)
    B = np.array([input().split() for _ in range(N)], dtype=int)
    result = np.dot(A,B)
    
    print(result)

#16.12) Inner and Outer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    A = np.array(input().split(), dtype=int)
    B = np.array(input().split(), dtype=int)
    
    print(np.inner(A,B))
    print(np.outer(A,B))


#16.13) Polynomials
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    coef = list(map(float, input().split()))
    point = int(input())
    
    print(np.polyval(coef, point))


#16.14) Linear Algebra
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N = int(input())
    A = np.array([input().split() for _ in range(N)], dtype = float)
    
    print(round(np.linalg.det(A),2))
    
#16.15) Array Mathematics
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    
    A = np.array([input().split() for _ in range(N)], dtype=int)
    B = np.array([input().split() for _ in range(N)], dtype=int)
    
    print(np.add(A,B))
    print(np.subtract(A,B))
    print(np.multiply(A,B))
    print(A // B)
    print(np.mod(A,B))
    print(np.power(A,B))


#############################################################################################################################
#### Problem 2

'''Birthday Cake Candles'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    heighest_candles = max(candles)
    counter = 0
    
    for candle in candles:
        if candle == heighest_candles:
            counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#############################################################################################################################
'''Kangaroo - Number Line Jumps'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here

    if x2 > x1 and v1 > v2:
        if (x2-x1)%(v1-v2) == 0:
            return 'YES'
        else: 
            return 'NO'
    if v1 < v2: return 'NO'
    if v1 == v2: return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#############################################################################################################################

'''Strange Advertising'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    people = 5
    likes = 0
    l = []
    
    for i in range(n):
        likes = people // 2
        people = likes*3
        l.append(likes)
    return sum(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#############################################################################################################################
'''Recursive Digit Sum'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    
    if len(n) == 1 and k == 1:
        return int(n)
    else:
        s = sum(list(map(int, n)))
        return superDigit(str(s*k),1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#############################################################################################################################
'''Insertionsort 1'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    tmp = arr[-1]
    
    for i in reversed(range(len(arr))):
        
        if arr[i] == tmp:
            continue
        elif arr[i] > tmp:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = tmp
            print(*arr)
            break
    
    if arr[0] > tmp:
        arr[0] = tmp
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#############################################################################################################################
'''Insertionsort 2'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,len(arr)):
        tmp = arr[i]
        
        j = i-1
        while j >= 0 and tmp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = tmp
        if i != 0:
            print(*arr)

        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)