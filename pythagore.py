

def pytha(a,b):
    while type(X)==str or type(X)== complex :
        print("veillez saisir une valeur correct de a")
        if type(X)==str:
            while type(X)==str:    
                try : 
                    X=int(input())
                except ValueError : 
                    print( "le type de a  n'est pas correct")
                    X=int(input())
        elif type(X)== complex:
            while type(X)==complex:
                try:
                    X=int(input())
                except ValueError :
                    X=int(input())    
        
        else :
            X=input()       
    while type(b)==str or type(b)== complex :
        print("veillez saisir une valeur correct de b ")
        if type(b)==str:
            while type(b)==str:    
                try : 
                    b=int(input())
                except ValueError : 
                    print( "le type de b n'est pas correct")
                    b=int(input())
        elif type(b)== complex:
            while type(b)==complex:
                try:
                    b=int(input())
                except ValueError :
                    b=int(input())    
        
        else :
            b=input() 
    c =(a**2+b**2)**(1/2)
    return(c)


print("la valeur de c est : ", pytha('A',3))


