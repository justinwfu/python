# Python Notes
# 2020-06-11

# strings - immutable data type
# new value reassigned if modified
s = 'justin'
s[::-1] 'nitsuj'
s[3::-1] 'tsuj'

# data structures
# lists -- mutable so assigning a variable that is assinged a list to anew variable means both change
l = ['apple', 'banana', 'cherry']
l2 = l
l2
l.append('date')
l # ['apple', 'banana', 'cherry', 'date']
l2 # ['apple', 'banana', 'cherry', 'date']

l = ['apple', 'banana', 'cherry', 'apricot']
sorted(l)
['apple', 'apricot', 'banana', 'cherry']
l
['apple', 'banana', 'cherry', 'apricot']
l.sort()
l
['apple', 'apricot', 'banana', 'cherry']


# sets - contains
a = [123, 'asdf', 4]
b = [456, 'asdf', 9]
# a_set = set(a)

# for item in set(a):
#     if item in b:
#             print(item)

[item for item in set(a) if item in b]

# for loops
# printing and formatting strings
for i in range(10):
        if i % 2 != 0:
            print(i)
        else:
            # print('{i} is even'.format(i=i))
            print('{0} is even'.format(i))

# printing lists and reversing
a = ['atlanta', 'boston', 'cincinatti', 'detroit', 'edinburgh']
for city in a:
    if len(city) % 2 == 0:
        print('{0} had an even number of letters'.format(city[::-1]))
    elif len(city) % 3 == 0:
        print('{0} is divisible by 3'.format(city[::-1]))
    else:
        print(city.capitalize())

#inplace object sort - method on object
a.sort()

#instntiate new object sorted - function returns object
b = sorted(a)

#inplace object reverse sort
a.reverse() 



# list comprehension
# making a list of ints
l = [x for x in range(10)]
# list of even ints only
l = [x for x in range(10) if x % 2 == 0]
# list of squares
l = [x**2 for x in range(10)]
# add tax to a price
def price_with_sales_tax(txn, tax_rate):
    return txn * (1 + tax_rate)
l = [price_with_sales_tax(x, 0.08) for x in range(10)]
l

# enumerate
# get indices from a list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
l = enumerate(colors)
for i, color in l:
    print('color {0} is \t\t{1}'.format(i, color))

# zip
# iterate through two lists simultaneously
states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california']
capitals = ['montgomery', 'juneau', 'phoenix', 'little rock', 'sacramento']
for state, capital in zip(states, capitals):
    print('The capital of\t{0}\t\tis {1}'.format(state, capital))


# dictionary
person = {'name': 'Eric', 'age': 74}
"Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])
# 'Hello, Eric. You are 74.'

for k, v in person.items():
    print(k,v)

for k in person.keys():
    print(k)

for v in person.values():
    print(v)


# first_names = ['alan', 'bill', 'cody', 'dave']
# last_names = ['ackerman', 'bolton', 'carter', 'douglas']

states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california']
capitals = ['montgomery', 'juneau', 'phoenix', 'little rock', 'sacramento']

d = dict()
for state, capital in zip(states, capitals):
    d[state] = capital


# check key exists
'tennessee' in d

# sort dictionary by values
[x for x in sorted(d, key=lambda x: d[x])]
for x in sorted(d, key=lambda k: d[k]):
    print(f'{x}\n\t{d[x]}')

d2 = {'a' : 1, 'b' : 2, 'c' : 3}
d2


# functions
def dummy():
    pass

def square(int):
    return int**2

l = [square(x) for x in range(10)]

# lambda (takes in an interable)
# lambda, argument, body
lambda x: x
lambda x: x + 1
(lambda x: x + 1)(10)
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')


# list of lists, rotation question 

a = [list(range(4)) for _ in range(4)]
b = [[] for _ in range(4)]
# clockwise
for i in range(len(a)):
    for j in range(len(a[i])):
        b[j].append(a[i][j])

b = [[] for _ in range(4)]
# ctrclockwise
for i in range(len(a)):
    for j in range(len(a[i])):
        b[abs(j - (len(a)-1))].append(a[i][j])

b = [[] for _ in range(4)]
# mirror y same, flip x
for i in range(len(a)):
    for j in range(len(a[i])):
        b[i].append(a[i][abs(j-(len(a)-1))])



# objects are mutable instantations of classes, which can have attributes and methods that alter objects