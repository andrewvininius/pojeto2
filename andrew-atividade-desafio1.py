lista = ("Pedra", "Papel", "Tesoura")

print("Digite seu nome jogador 1:")
nome1 = input() 
print("Bem-vindo, ", nome1)
print("Digite seu nome jogador2:")
nome2 = input()
print("Bem-vindo,",nome2)
 
 
count = 0
   while count <= 3:
     print(count)
      count += 1

     
       Jogador1 = int(input("Jogador1, digite 0 p/Pedra, 1 p/Papel ou 2/Tesoura: "))
       jogador2 = int(input("Jogador2, digite 0 p/Pedra, 1 p/Papel ou 2/Tesoura: "))
      
      pedra = 0
      papel = 1
      tesoura = 2


     print("JO\n")
     print("KEN\n")
     print("POOH!!!\n")

       if (jogador1 == jogador2):
         print("Empate! Ninguém ganhou.")
     elif (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
         print("Jogador 1 ganhou,", nome1)
     else:
        print("Jogador 2 ganhou,", nome2)
    
        
 
 