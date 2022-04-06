#Tuple
''' 
my_tuple = 1,2,3,4
print(my_tuple)
'''
#Set
'''
def test():
    return {1,2,3}

my_set = test()
my_set.add(1)

print(my_set)
'''
#list comprehension

#1
'''
my_list = [1,2,3,4,-6,54,9,4,-7]

result = [number for number in my_list if number>6]

print(result)
'''
#2

class Human:
    def __init__(self,name,age):
        self.name =name
        self.age = age

my_list = [Human("John",22),Human("Jack",25), Human("Jill",30),Human("Bill",19)]

result = [human.name for human in my_list if human.age>=25]

print(result)
