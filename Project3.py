#Shirong Zheng  CSC11300
#Project 3-Analyze Book

import string

def compareItems((w1,c1),(w2,c2)):
    if c1>c2:
	    return -1
    elif c1==c2:
	    return cmp(w1,w2)
    else:
	    return 1


def main():
    print "This program is work to analyzes words frequency in a text"
    print "and that will prints the n most frequent words.\n"
	
	#input my text book name and lead the location
    fname=raw_input("Name of the text to analyze:")
    text=open('C:\Users\Shirong\My Documents\emma.txt','r').read()
    text=string.lower(text)
	
	#replace non-words
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
	    text =string.replace (text,ch,'')
		
	#count the words
    words =string.split(text)
    counts={}
    for w in words:
	    counts[w]=counts.get(w,0)+1
    n=input("Output analysis of how many words?")
    items =counts.items()
    items.sort(compareItems)
    for i in range(n):
	    print "%-10s%5d" % items[i]
		
if __name__ == '__main__':
    main()
	
#Find the stop words and replace	
STOPWORDS=['able','about','above','according','across','after','again','all','allow','almost',
'afraid','believe','indeed']

def remove_stop_words(wordlist,stopwords=STOPWORDS):
    if not wordlist:
	    sentence=raw_input("Please Find a sentence in emma.txt:")
	    wordlist=sentence.split()
    marked=[]
    for t in wordlist:
	    if t.lower() in stopwords:
		    marked.append('&')
	    else:
		    marked.append(t)
    return marked

wordlist=[]
marked_list=remove_stop_words(wordlist)
print(marked_list)

wordlist= "You should find other stop words".split()
marked_list=remove_stop_words(wordlist)
print(marked_list)
