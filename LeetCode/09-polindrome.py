def isPalindrome(x):
    if x<0:
        return 0
    x=str(x)
    a=len(x)
    for i in range(0,len(x)//2):
        if x[i]!=x[a-(i+1)]:
            return 0
        
    return 1









print(isPalindrome(44))