umidadeI = int(input("insira a umidade interna: "))
temperaturaI = int(input("insira a Temperatura interna do ar: "))
temperaturaE = int(input("insira a Temperatura externa do ar: "))
Estacao = int(input("Escolha a estação do ano [1] para Inverno [2] para o verão"))


if Estacao == 1 :

    while temperaturaI > 15 and umidadeI >= 40 :
        print ("acionando exaustores")
        umidadeI = int(input("insira a umidade interna: "))
        temperaturaI = int(input("insira a Temperatura interna do ar: "))
    while  temperaturaI < 15 and umidadeI >= 40 :
        print ("acionando exaustores e aquecedores")
        umidadeI = int(input("insira a umidade interna: "))
        temperaturaI = int(input("insira a Temperatura interna do ar: "))
    
    while temperaturaI > 100 :
        print ("temperatura supoerior a 100 graus, desligando aquecedores")
        temperaturaI = int(input("insira a Temperatura interna do ar: "))

    if umidadeI <= 5 :
        print ("desumidificação concluiida")
    
        print ("iniciando processo de cocção")

        umidadeI = int(input("insira a umidade interna: "))

        while umidadeI > 15 :
            print ("acionando exaustores")
            umidadeI = int(input("insira a umidade interna: "))
        else :
            print ("exaustores desligados")

        temperaturaI = int(input("insira a Temperatura interna do ar: "))

        while temperaturaI < 200 :
            print ("acionando aquecimento ate 380 graus")
            temperaturaI = int(input("insira a Temperatura interna do ar: "))

        while umidadeI < 5 and temperaturaI >= 380 :
            print ("inserir conteudo para cocção, quando concluir pressione o botão (PRONTO)")
            break
        print ("cocção concluida")
    
elif Estacao == 2 :
##cocção
    
    print ("iniciando processo de cocção")

    umidadeI = int(input("insira a umidade interna: "))

    while umidadeI > 15 :
        print ("acionando exaustores")
        umidadeI = int(input("insira a umidade interna: "))
    else :
        print ("exaustores desligados")

    temperaturaI = int(input("insira a Temperatura interna do ar: "))

    while temperaturaI < 200 :
        print ("acionando aquecimento ate 380 graus")
        temperaturaI = int(input("insira a Temperatura interna do ar: "))

    while umidadeI < 5 and temperaturaI >= 380 :
        print ("inserir conteudo para cocção, quando concluir pressione o botão (PRONTO)")
        break
    print ("cocção concluida")