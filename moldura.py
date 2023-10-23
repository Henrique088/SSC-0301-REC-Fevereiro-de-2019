
def retangulo(linha, coluna):

    for i in range(linha+1):

        for j in range(coluna+1):
            if(i ==0 ):
                if (j ==0):
                    print("+",end="")

                elif( j == coluna):
                    print("+")


            elif(i == linha and coluna == 1):

                if(j==0):

                    print("+", end="")
                    # print(" "*coluna, end="")

                elif(j==coluna):

                    print("+")

            elif(i == linha):
                if(j==1):
                    print("+", end="")
                elif (j == coluna):

                    print("+")

            if(i ==0 and j == coluna-1):
                print("-"*coluna, end="")



            if(i == 1 and j ==0):
                count = 0
                while(count !=linha):
                    print("|", end="")
                    print(" "*coluna, end="")
                    print("|")
                    count+= 1

            if(i ==linha and j == coluna-1):
                print("-" * coluna, end="")


linha= int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

retangulo(linha,coluna)



