#Shirong Zheng    CSC11300
#Project5-GCD Module

def gcd(a,b):
    while b !=0:
	    a,b=b,a%b
    return a

def xgcd(a,b):
    prevx, x=1,0 
    prevy,y=0,1
    while b:
	    q,r=divmod(a,b)
	    x,prevx=prevx-q*x,x
	    y,prevy=prevy-q*y,y
	    a,b=b,r
    return a,prevx,prevy

def egcd(a,b):
    if a==0:
        return (b,0,1)
    else:
	    g,y,x=egcd(b%a,a)
	    return(g,x-(b//a)*y,y)
    	
def modinv(a,m):   
    gcd,x,y=egcd(a,m)
    if gcd!=1:
	    return None
    else:
	    return x%m
	
def main():
    print gcd(42,6)
	
    print xgcd(56,8)
    print xgcd(2,12)
	
    print modinv(17,23)
    print modinv(2,4)
	
if __name__ == '__main__':
    main()
