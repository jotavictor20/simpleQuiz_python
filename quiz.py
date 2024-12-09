#colocar informação para o usuario
print("Seja muito bem vindo ao quiz do joão")
#cria uma variavel e armazena a informação enviada pelo usuario
answer_user=input("Quer começar? (S/N)")
#print da variavel
print(answer_user)
#se o answer_user for diferende de s o programa será encerrado
if answer_user!="S":
    quit()
score = 0
print("començando...")
print("Quem desenvolveu o jogo grand theft auto?\n A)Rockstar\n B)Ubsifot\n C)Activision\n D)EA")
answer1 = input("Resposta:")
if answer1 == "A" :
    print("A resposta está correta")
    score = score+ 1
else:
    print("a resposta está incorreta")
print("Quem desenvolveu o jogo minecraft?\n (A) Rockstar\n (B) Ubisoft\n (C) Mojang\n (D) EA")
answer2 = input("Resposta:")
if answer2 == "C" :
    print("A resposta está correta")
    score = score+ 1

else:
    print("a resposta está incorreta")
print("Quem desenvolveu o jogo Fifa?\n (A) Rockstar\n (B) Ubisoft\n (C) Mojang\n (D) EA")
answer3 = input("Resposta:")
if answer3 == "D" :
    print("A resposta está correta")
    score = score+ 1

else:
    print("a resposta está incorreta")
print("Quem é o protagonista de minecraft?\n (A) Carl johnson\n (B) Steve\n (C) Kratos\n (D) John")
answer4 = input("Resposta:")
if answer4 == "B" :
    print("A resposta está correta")
    score = score+ 1

else:
    print("a resposta está incorreta")

print(f"quiz acabou {score}/4")