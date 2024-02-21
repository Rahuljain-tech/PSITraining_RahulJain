import functools


# Q3 (a)
def FINDMAX(a, b):
    # if a>b:
    #   return a
    # else:
    #    return b
    return max(a, b)

# Q2
def mul(n):
    return lambda a: a * n

# Q1 (b)
def positive_list(l):
    l1 = [2 * x for x in l]
    l2 = [x for x in l1 if x > 0]
    return l2

# Q1 (a)
def print_list(l):
    l1 = [2 * x for x in l]
    return l1

# Q4 (a)
def isPositive(n):
    if(n>0):
        
        # return str(n) + (' is a positive number')
        return True
    else:
        # return str(n) +(" is not a positive number")
        return False


# Q5 (a)    
def multiply(a,b):
    return a*b    


if __name__ == '__main__':
    # print_hi('PyCharm')
    l = [10, 20, 30, 40, -1, 50, -2, -5]
    print(print_list(l))
    print("List containig only positive no are:-", positive_list(l))
    number = mul(3)
    print('Multiplication using lambda function is :- ', number(5))
    print('Max of two Numbers is : - ', FINDMAX(11, 32))
    # Q3 (b)
    max_value = max(map(FINDMAX, l,l[1:]))
    print(max_value)
    x = int(input("Enter a number :-"))
    print(isPositive(x))
    # Q4 (b)
    filtered = filter(isPositive,l)
    print("All positive numbers in the list are : ")
    for i in filtered:
        print(i)

    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print("Product of" "","" ,str(a) ,", " ,str(b), " is : ",multiply(a,b))   
    

    # Q5 (b)
    print("Product of elements of list is : ", functools.reduce(multiply,l)) 

