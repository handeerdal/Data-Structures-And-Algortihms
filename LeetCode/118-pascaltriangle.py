def generate(numRows):
        array = [[] for _ in range(numRows)]
        array[0]=[1]
        array[1]=[1,1]
        if numRows!=2:
            for j in range(2,numRows):
                if j==(numRows-1):
                     array[j].append(1)
                else:
                    print(array[j-1])
                    print(array[j])
                    value=int(array[j-1]+array[j])
                    array[j].append(value)

        print(array)


    
    




numRows = 5
generate(numRows)