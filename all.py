def product(a, b):
    return a * b
print(product(2,3))#6

def weekday_name(l):
    L=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if l< 1 or l> 7: return None
    return L[l- 1]
print(weekday_name(2))#Monday

def last_element(L):
    if L: return L[-1]
print(last_element([1, 2, 3]))#3
print(last_element([]))#None(functions return None by default)

def number_compare(a, b):
    if a > b:return "First is greater"
    elif b > a:return "Second is greater"
    else:return "Numbers are equal"
print(number_compare(1,1))#Numbers are equal

def reverse_string(s):
    return s[::-1]
print(reverse_string('abc'))#'cba'

def single_letter_count(s, c):
    return s.lower().count(c.lower())
print(single_letter_count('abA','A'))#2

def multiple_letter_count(s):
    D = {} #dict
    for c in s:
        D[c] = D.get(c, 0) + 1
    return D
print(multiple_letter_count('aba'))#{'a':2,'b':1}

def list_manipulation(L, command, location, value=None):
    if command == "add":
        if location == "beginning":
            L.insert(0, value)
            return L
        elif location == "end":
            L.append(value)
            return L
    elif command == "remove":
        if location == "beginning":return L.pop(0)
        elif location == "end":return L.pop()
print(list_manipulation([1,2],'add','beginning',3))#[3,1,2]
print(list_manipulation([1,2],'add','end',3))#[1,2,3]
print(list_manipulation([1,2],'remove','beginning'))#1
print(list_manipulation([1,2],'remove','end'))#2
print(list_manipulation([1,2],'abc','end'))#None

def is_palindrome(s):
    normalized = s.lower().replace(' ', '')
    return normalized == normalized[::-1]
print(is_palindrome('ab A'))#True
print(is_palindrome('abc'))#False

def frequency(L,x):
    return L.count(x)
print(frequency([1,1,2,1],1))#3

def flip_case(s, flippedChar):
    flippedChar = flippedChar.lower()
    ans = ''
    for c in s:
        if c.lower() == flippedChar:c = c.swapcase()
        ans += c
    return ans
print(flip_case('abA','a'))#'Aba'

def flip_case2(s, flippedChar):#a bit clever,but harder to read,same runtime
    flippedChar = flippedChar.lower()
    fixed=[(char.swapcase() if char.lower()==flippedChar else char) for char in s
    ]
    return "".join(fixed)
print(flip_case2('Aba','a'))#'abA'

def multiply_even_numbers(L):
    ans = 1
    for l in L:
        if l % 2 == 0:ans = ans * l
    return ans
print(multiply_even_numbers([1,2,3,4]))#8
print(multiply_even_numbers([5,3]))#1

def capitalize(s):
    return s.capitalize()
print(capitalize('capitalize first letter of first word'))#'Capitalize first letter of first word'
def capitalize2(s):
    return s[:1].upper() + s[1:]
print(capitalize2('capitalize first letter of first word'))#'Capitalize first letter of first word'

def compact(L):
    return [l for l in L if l]
print(compact([0,1,'',[],(),{},False,True,None,'all falsy elements removed']))#[1,True,'ok'l]

def intersection(L1, L2):
    return list(set(L1) & set(L2))#or return [l for l in L1 if l in set(L2)]
print(intersection([1,2,2,3],[2,2,3,4]))#[2,3]
    
def is_even(n):return n % 2 == 0
def is_string(ele):return isinstance(ele, str)
def partition(L, F):# Best solution
    """F returns True or False
     Returns new list of 2 sublists [L1,L2], where L1 contains items that passed F test,
     and L2 contain items that failed F test
    """
    L1 = []
    L2 = []
    for l in L:
        if F(l):L1.append(l)
        else:L2.append(l)
    return [L1,L2]
print(partition([1,2,3,4],is_even))#[[2,4],[1,3]]
print(partition(["hi",1,True,None,[],(),{}], is_string))#[['hi'],[1,True,None,[],(),{}]]
    
def partition2(L,F):# Clever,but less optimal solution,F() run twice
    return [[l for l in L if F(l)],[l for l in L if not F(l)]]
print(partition([1,2,3,4],is_even))#[[2,4],[1,3]]
print(partition(["hi",1,True,None,[],(),{}], is_string))#[['hi'],[1,True,None,[],(),{}]]
    
def mode(L):
    D = {}#dict to count
    for l in L:
        D[l] = D.get(l, 0) + 1
    max_v = max(D.values())
    for (k,v) in D.items():
        if v == max_v:return k #most-freq number.Given,always only one answer
print(mode([1,2,1]))#1

def calculate(operation, a, b, make_int=False, message='Result is:'):
    """make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) if not provided, use default'Result is:'
    Performs operation (truncating if make_int), then returns as
    "[message] [result]"
    """
    if operation == "add":res = a + b
    elif operation == "subtract":res = a - b
    elif operation == "multiply":res = a * b
    elif operation == "divide":res = a / b
    else:return #return None

    if make_int:res = int(res)

    return f"{message} {res}"
print(calculate('add',1.5,2,make_int=True,message='Result='))#Result=3
print(calculate('ABC',1,2))#None

def friend_date(T1,T2):
    """Given 2 friends(tuples(name,age,hobbies list),return True if they have common hobby"""
    if set(T1[2]) & set(T2[2]):return True
    else:return False
    # return bool(set(a[2] & set(b[2])
print(friend_date(('Li',30,['swim','gym']),('Emy',20,['gym','walk'])))#True
print(friend_date(('Li',30,['swim','gym']),('Emy',20,['walk'])))#False

def filter_and_double(L):
    return [l*2 for l in L if l%4==0]
print(filter_and_double([1,8,2,12]))#[16,24]

def extract_full_names(L):
    return [f"{D['k1']} {D['k2']}" for D in L]
print(extract_full_names([{'k1':'A','k2':'B'},{'k1':'C','k2':'D'}]))#['A B','C D']

def sum_floats(L):
    return sum([l for l in L if isinstance(l, float)])
print(sum_floats([1.0,2.2,10]))#3.2

def list_check(L):
    for l in L:
        if not isinstance(l, list):return False
    return True#if all items in L are lists
    # return all(isinstance(l, list) for l in L)
print(list_check([[1,2],[3,4]]))#True
print(list_check([[1,2],3]))#False

def remove_every_other(L):
    return L[::2]#new list of other item
    # return [val for i, val in enumerate(L) if i % 2 == 0]
print(remove_every_other([1,2,3,4,5]))#[1,3,5]

def sum_pairs(L,sum):
    """Return tuple of first 2 elements that add up to sum"""
    seen = set()
    for l in L:
        difference = sum - l
        if difference in seen:return (difference, l)
        seen.add(l)
    return ()#if no pair found
print(sum_pairs([1,2,3,4],5))#(2,3):finish before (1,4)

def vowel_count(s):
    VOWELS = set("aeiou")
    s = s.lower()
    ans = {}
    for c in s:
        if c in VOWELS:ans[c] = ans.get(c, 0) + 1
    return ans
print(vowel_count('abAe'))#{'a':2,'e':1}

def titleize(s):
    return s.title()
print(titleize('first letter of each word capitalized'))#First Letter Of Each Word Capitalized

def find_factors(x):
    ans = [n for n in range(1,x//2 + 1) if x%n==0]
    ans.append(x)
    return ans
print(find_factors(10))#[1,2,5,10]
print(find_factors(11))#[1,11]

def find_factors2(x):
    n=1
    ans = []
    while(n <= x):
        if x % n == 0: ans.append(n)
        n += 1
    return ans
print(find_factors2(10))#[1,2,5,10]
print(find_factors2(11))#[1,11]

def includes(collection, sought, startIdx=None):
    """True if sought is in collection(string,list,set,tuple),starting at startIdx
    for dict:sought is key
    startIdx is ignored for sets/dictionaries(they aren't ordered)"""
    if startIdx is None or isinstance(collection, set):
        return sought in collection
    if isinstance(collection, dict):
        return sought in collection.values()
    return sought in collection[startIdx:]
print(includes("hi", "i"))#True
print(includes("hi", "i",5))#False
print(includes([1,2],2))#True
print(includes((1,2),2))#True
print(includes({1,2},1))#True
print(includes({"a":1, "b":2},'b'))#True
print(includes({"a":1, "b":2},'c'))#False

def repeat(s, n):
    if not isinstance(n, int) or n < 0: return None
    return s * n
print(repeat('ab',2))#'abab'
print(repeat('a',-1))#None
print(repeat('a','XYZ'))#None

def truncate(phrase, n):
    if n < 3: return "Truncation must be at least 3 characters"
    if n > len(phrase) + 2: return phrase
    return phrase[:n - 3] + "..."
print(truncate("Hello World",2))#"Truncation must be at least 3 characters"
print(truncate("Hello World",18))#'Hello World'
print(truncate("Hello World",8))#'Hello...'

def two_list_dictionary(L1, L2):
    ans = {}
    for i,val in enumerate(L1):
        ans[val] = L2[i] if i < len(L2) else None
    return ans
print(two_list_dictionary(['a','b'],[1,2]))#{'a':1,'b':2}
print(two_list_dictionary(['a','b','c'],[1,2]))#{'a':1,'b':2,'c':None}
print(two_list_dictionary(['a','b'],[1,2,3]))#{'a':1,'b':2}

from itertools import zip_longest
def two_list_dictionary2(L1,L2):
    return dict(zip_longest(L1, L2))
print(two_list_dictionary2(['a','b'],[1,2]))#{'a':1,'b':2}
print(two_list_dictionary2(['a','b','c'],[1,2]))#{'a':1,'b':2,'c':None}
print(two_list_dictionary2(['a','b'],[1,2,3]))#{'a':1,'b':2}

def sum_range(L, start=0, end=None):
    if end is None: end = len(L)
    return sum(L[start:end+1])
print(sum_range([1,2,3,4,5]))#15
print(sum_range([1,2,3,4,5],1,2))#5
print(sum_range([1,2,3,4,5],1,20))#14

def same_freq(x, y):
    D1,D2={},{}
    for c in str(x):
        D1[c]=D1.get(c,0)+1
    for c in str(y):
        D2[c]=D2.get(c,0)+1
    return D1==D2
print(same_freq(1122,1221))#True
print(same_freq(1122,12213))#False

def two_largest(L):#O(nlogn)
    return tuple(sorted(set(L))[-2:])
print(two_largest([1,8,2,9]))#(8,9)
print(two_largest([1,8,9,9,9]))#(8,9)

def two_largest2(L):  # O(n)
    largest, second = None, None
    for x in set(L):
        if largest is None or x > largest:
            second = largest
            largest = x
        elif second is None or x > second:
            second = x
    return (second, largest)

print(two_largest2([1,8,2,9]))#(8,9)
print(two_largest2([1,8,9,9,9]))#(8,9)

def find_first_duplicate(L):
    seen = set()

    for l in L:
        if l in seen: return l#return first duplicate 
        seen.add(l)
print(find_first_duplicate([1,2,1,2,2]))#1
print(find_first_duplicate([1,2]))#None

def sum_diagonals(M):#square matrix using list of lists
    ans = 0
    for i in range(len(M)):
        ans += M[i][i]
        ans += M[i][-1-i]#i=0,-1-i=-1:last element in row
    return ans
    # return sum([M[i][i]+M[i][-1-i]M for i in range(len(M))])
print(sum_diagonals([[1,2],[3,4]]))#10
print(sum_diagonals([[1,2,3],[4,5,6],[7,8,9]]))#30

def min_max_keys(D):#dict
    return (min(D.keys()),max(D.keys()))#any kind of keys that can be compared
print(min_max_keys({2:'a',7:'b',1:'c',10:'d'}))#(1,10)
print(min_max_keys({"pen":"a","cat":"b","dog":"c"}))#('cat','pen')

def find_greater_numbers(L):
    ans = 0
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[j] > L[i]: ans += 1
    return ans
print(find_greater_numbers([4,1,2,5]))#4
print(find_greater_numbers([4,3,2]))#0
print(find_greater_numbers([]))#0

def is_odd_string(s):
    total = sum((ord(char) - 96) for char in s.lower())
    return total % 2 == 1
print(is_odd_string('b'))#False (ord('b')=98;98-96=2:even)
print(is_odd_string('ab'))#True (ord('a')=97;97-96=1;1+2:odd)

def valid_parentheses(s):
    count = 0
    for c in s:
        if c == '(': count += 1
        elif c == ')': count -= 1
        if count < 0: return False#at any point,if more closing paren than opening paren,immediately returns False
    return count == 0
print(valid_parentheses(')('))#False

def three_odd_numbers(L):
    for i in range(len(L) - 2):
        if (L[i]+L[i+1]+L[i+2]) % 2 != 0: return True#sum of any 3 sequential numbers odd
    return False
print(three_odd_numbers([1,2,3,4]))#True

def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    L = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if L[i] not in vowels: i += 1
        elif L[j] not in vowels: j -= 1
        else:
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1
    return "".join(L)
print(reverse_vowels('abEbibObu'))#'ubObibEba'

def read_file_list(filename):
    with open(filename) as f:
        for l in f:#go through each line l in file
            l = l.strip()#emoves leading/trailing whitespaces,newline from string
            print(f"- {l}")
print(read_file_list('cats'))
