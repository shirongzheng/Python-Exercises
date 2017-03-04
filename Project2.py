#Shirong Zheng     csc11300
#Project2

MAX_N_SIZE =26

def Mode():
    while True:
	    print('Would you like to encrypt or decrypt your message?')
	    mode=raw_input().lower()
	    if mode in 'encrypt decrypt '.split():
		    return mode
	    else:
		    print('Only enter either "encrypt"or "decrypt".')

def Message():
    print('Please enter your message:')
    return raw_input()

def N():
    n=0
    while True:
	    print('Enter the n number(-1-%s)' % (MAX_N_SIZE))
	    n=int(input())
	    if (n>=-1 and n<=MAX_N_SIZE):
		    return n
		
def TranslatedMessage(mode,message,n):
    if mode[0]=='d':
	    n=-n
    translated = ''
    for symbol in message:
	    if symbol.isalpha():
		    num = ord(symbol)
		    num += n
		    if symbol.islower():
			    if num>ord('z'):
				    num -= 26
			    elif num<ord('a'):
				    num += 26
					
		    elif symbol.isupper():
			    if num>ord('z'):
				    num -=26
		    elif num<ord('a'):
				    num +=26
		    translated += chr(num)
			
	    else:
		    translated +=symbol
    return translated
	
mode = Mode()
message = Message()
n = N()

print('Your translated text is:')
print(TranslatedMessage(mode,message,n))	