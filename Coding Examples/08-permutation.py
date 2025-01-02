#check permutation letter

def permutation(l1,l2):
    if len(l1)!=len(l2):
        return 0
    else:
        for i in range(0,len(l1)):
            if l1[i]!=l2[len(l1)-(1+i)]:
                return 0
        return 1

l1  =['l','i','a','r']
l2= ['r','a','i','l']

print(permutation(l1,l2))
