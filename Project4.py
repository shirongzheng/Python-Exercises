#Shirong Zheng    CSC11300
#Porject4-List_exercise

import random

def list_sum(t):
    if t==[]:
	    return 0
    elif type(t[0]) == type([]):
	    return list_sum(t[0]) +\
		       list_sum(t[1:])
    else:
	    return t[0] +\
		        list_sum(t[1:])

def cumulative(t):
    amount=0
    result=[]
    for number in t:
	    result.append(amount+number)
    return result
	    	
def remove(t):
    del t[0],t[-1]
	
def middle(t):
    m=t[1:-1]
    return m

def is_sorted(t):
    return t==sorted(t)

def anagram(xWord,yWord):
    anagram=(sorted(xWord)==sorted(yWord))
    return anagram

def duplicates(s):
    t=list(s)
    t.sort()
    length=len(t)-1
    for i in range(length):
	    if t[i] ==t[i+1]:
		    return True
	    else:
		    return False
	
def main():
    t=[[1,2],[3],[4,5,6]]
    print(list_sum(t))
	
    t=[1,2,3]
    print(cumulative(t))
	
    t=[1,2,3,4]
    print(middle(t))
    remove(t)
    print(t)

    print(is_sorted([1,2,3]))
    print(is_sorted(['z','f']))   
    print(anagram('student','tneduts'))
    print(anagram('same','some'))
    print(anagram([1,2,2],[2,1,2]))
    print(duplicates('zdg'))
    print(duplicates('fhhf'))

if __name__ == '__main__':
    main()
