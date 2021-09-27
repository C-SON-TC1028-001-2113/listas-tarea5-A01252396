def main():
    r=int(input())
    c=int(input())
    m=r*c
    Lista=[]
    for n in range (m):
        e=int(input())
        if e<10:
            Lista.append(e)
    print(Lista)     
if __name__=='__main__':
    main()
