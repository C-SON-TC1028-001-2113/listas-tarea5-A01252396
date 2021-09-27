def main():
    #escribe tu código abajo de esta línea
    n=int(input())
    Lista1=[]
    Lista2=[]
    if n>0: 
        for c in range (n):
            Elemento=input()
            Lista1.append(Elemento)
            if (Elemento in Lista2)==False:
                Lista2.append(Elemento) 
        print(Lista1)   
        print(Lista2)       
    else:
        print('Error')  
if __name__=='__main__':
    main()
