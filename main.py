# This is a sample Python script.
from _ctypes import sizeof


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def findmax(a,b):
    #if a>b:
     #   return a
    #else:
    #    return b
    return max(a, b)
def mul(n):
    return lambda a : a*n
def positive_list(l):
    l1 = [2*x for x in l]
    l2 = [x for x in l1 if x>0]
    return l2
def print_list(l):
    l1 = [2*x for x in l]
    return l1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    l = [10, 20 , 30 , 40 , -1, 50 , -2 , -5]
    print(print_list(l))
    print("List containig only positive no are:-",positive_list(l))
    number = mul(3)
    print('Multiplication using lambda function is :- ',number(5))
    print('Max of two Numbers is : - ', findmax(11, 32))
    # print(max(map(findmax,l)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
