num=2
fact=1

while num > 0:
    fact= fact * num
    num-=1
print(f' recuretion is {fact}')


def recurtion(num):
    if num < 1:
        return 1
    else:
        output= num * recurtion(num-1)
        return output
    
print(recurtion(4))




def fiboonaci(num):
    a,b=0,1
    for i in range(num):
        a,b=b,a+b
    return a
print(fiboonaci(4))



def fibonaci2(num):
    if num <= 1:
        return num    
    else:
        return fibonaci2(num - 1) + fibonaci2(num - 2)

print(fibonaci2(4))


def is_pallindrome(s):
    if len(s)<=1 :
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_pallindrome(s[1:-1])
word='MADAMA'
print(is_pallindrome(word))



def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:])
    

piece=[1,2,3]
print(getSum(piece))
 

