import os
def finding():
    rol =[]
    num =[]
    n = 0
    print(type(rol))
    for roat, dirs, files in os.walk('.'):
        for dr in dirs:
            rol.append(dr)
            for fl in files:
                n = n+1
            num.append(n)
    return rol, num

def counting(x,y):
    maxy = 0
    for indx, letter in enumerate(y):
        if y[indx] > maxy:
            maxy = y[indx]
            maxn = indx
    print(x[maxn])
    return x[maxn]

def main():
    a, b = finding()
    c = counting(a, b)
if __name__ == '__main__':
    main()

        
        
        
    
