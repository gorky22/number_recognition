import numpy as np

# uloha cislo 4 zadanie cislo 6
# newton

x = [1,2,4,8,16]
y = [0,1,2,3,4]


# vypocet rozielu
def compute_frac(x1,x0,y1,y0):
    return (y1-y0)/(x1-x0)

# vypocet vyslednej funkcie pre bod
def aproximate_point(x, arr, coef):
    count = coef[0]
    
    for i in range(1, len(coef)):
        tmp_count = 1
        
        for j in range(len(coef[: i])):
            tmp_count *= x - arr[j]
        count += coef[i] * tmp_count

    return count

# 
def print_ftion(x, arr, coef):
    tmp_arr = [f'{coef[0]}']
    for i in range(1, len(coef)):
       
        tmp_arr.append(f"{coef[i]}*")
        
        for j in range(len(coef[: i])):
            tmp_arr[i ] += f'(x - {arr[j]})'
        
    print( " + ".join(tmp_arr))

    

def newton(x,y):
    tmp_y = []

    N = len(x) 
    coef = [y[0]]

    for i in range(0,N-1):
    
        for j in range(0, len(y) -1):
            tmp_y.append(compute_frac(x[i + 1 + j],x[j],y[j + 1], y[j]))
     
        y = tmp_y.copy()
        coef.append(y[0])
        tmp_y = []
    return coef

coef = newton(x,y)

print(f'A) koeficienty su: {coef}')
print(f"A) vysledna rovnica pomocou newtonovej interpolacie je teda: ")
print_ftion(12, x, coef)
print(f'B) Aproximacia funkcie v bode 12 je: {aproximate_point(12, x, coef)}')
print(f'C) Relativna chyba aproximacie voci presnemu vysledku je: {(abs(aproximate_point(12, x, coef) - 3.58496)/3.58496) *100}%')
