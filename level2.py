


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

if __name__ == '__main__':
    n = int(input("E nter a number : "))
    print("Factorial of ",n," : ",calFactorial(n))
    s = str(input("Enter the language : "))
    print(greet(s))