# input

C=int(input("Favor digite el valor inicial: "))
print("su valor de capital inicial fue: " + str(C))
# processing

N=0
D=2*C

while (C<=D):
    C=C + 0.05 * C
    N=N+1
# OUTPUT
    
print("Capital final: " + str (C))
print("En " + str(N), "meses se te duplicara tu dinero")