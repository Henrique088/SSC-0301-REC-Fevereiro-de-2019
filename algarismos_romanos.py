def equivalente(num_romano,vetor):

    for item in vetor:
        if item[0] == num_romano:
            return item[1]

    return None
def romanos(romano, vetor):
    romano = romano.strip()
    vet = []
    vet_resul = []
    d = 0
    p = 0
    for i in romano:
        vet.append(i)
        if(len(romano)== 1):
            print()

    for k in range(len(vet)):

        try:
            a = str(equivalente(vet[d], vetor))

        except:
            return vet_resul

        if(k != len(vet)-1):
            try:
                b = str(equivalente(vet[d+1], vetor))

            except:
                b = 0

        elif(p ==0):
            vet_resul.append(int(a))
            return vet_resul
        else:
            return vet_resul

        if(int(a) < int(b)):

            vet_resul.append(int(b)-int(a))
            d +=2
            p = 1

        else:
            vet_resul.append(int(a))
            p = 0
            d+=1


print("Escreva o algorismo romano: ")
rom = input().upper()

vetor = [('I', 1),('V', 5),('X', '10'),('L', 50),('C', 100),('D', 500),('M', 1000)]


print("O valor de cimal de {} é: {}".format(rom, sum(romanos(rom,vetor))))



