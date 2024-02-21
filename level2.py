


def calFactorial(n):
    if(n == 0):
        return 1
    return n* calFactorial(n-1)

def greet(s):
    if(s == "Hindi"):
        return "Namaskar"
    elif(s == "English"):
        return "Hello"
    else:
        return "Please select the correct language"

def cal(n1 , n2=0):
    return n1+n2 , n1-n2 , n1*n2 , n1/n2

if __name__ == '__main__':
    n = int(input("E nter a number : "))
    print("Factorial of ",n," : ",calFactorial(n))
    s = str(input("Enter the language : "))
    print(greet(s))
    in1 = int(input("Enter first no : "))
    in2 = int(input("Enter second no : "))
    print(cal(in1, in2))