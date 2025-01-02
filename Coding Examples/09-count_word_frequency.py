'''
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}

'''

def count_word_frequency(w):
    newdict={}
    for i in w:
        if i not in newdict:
            newdict[i]=1
        else:
            newdict[i]+=1
    print(newdict)

                

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
