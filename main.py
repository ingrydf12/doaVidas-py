#MARK: - Menu
def menu():
    while True:
        print("""
--------

DOA VIDAS

Programa direcionado ao espaço do doador para entender e incentivar a doação de sangue em Fortaleza.
                                                                                                          
   MENU INTERATIVO: PARA ONDE VOCÊ QUER IR?
   [1] Quem pode doar?
   [2] Saiba os benefícios e procedimentos
   [3] Elegibilidade: você pode doar com base nessas perguntas?
   [4] Locais de doação em Fortaleza
   [5] Dicas para doadores
   [0] Sair
""")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            doacaoInfo()
        elif opcao == 2:
            beneficiosProcedimentos()
        elif opcao == 3:
            elegibilidade()
        elif opcao == 4:
            locaisDoacao()
        elif opcao == 5:
            dicasDoadores()
        elif opcao == 0:
            exit()
            break
        else:
            print("Essa opção é inválida, tente novamente.")


#MARK: - Quem pode doar
def doacaoInfo():
    print("""
________________________________________________________________________________________
𝗤𝗨𝗘𝗠 𝗣𝗢𝗗𝗘 𝗗𝗢𝗔𝗥?

Se você estiver saudável, bem alimentado antes da doação, pesar acima de 50kg, tiver entre 16 a 69 anos
e apresentar documento oficial com foto, você pode doar. Caso você tenha idade entre 16 e 17 anos, você precisa
ter um termo de consentimento formal por escrito do seu responsável legal para cada doação que fizer.
          
O HEMOCE disponibiliza em seu site o TERMO DE CONSENTIMENTO PARA MENORES DE 18 ANOS que deverá ser apresentado para autorização desses jovens nessa faixa etária.

O limite máximo para PRIMEIRA DOAÇÃO é de 60 (Sessenta) ANOS, 11 (Onze) MESES e 29 (vinte e nove) DIAS.
          
Caso queira mais informações acerca da doação, acesse o site do HEMOCE: https://www.hemoce.ce.gov.br/servicos/espaco-do-doador/doacao-de-sangue/duvidas-frequentes/
________________________________________________________________________________________
""")


#MARK: - Benefícios e procedimentos
def beneficiosProcedimentos():
    print("""
________________________________________________________________________________________
𝗕𝗘𝗡𝗘𝗙Í𝗖𝗜𝗢𝗦 𝗘 𝗣𝗥𝗢𝗖𝗘𝗗𝗜𝗠𝗘𝗡𝗧𝗢𝗦

- Benefícios:
  Doar sangue ajuda a salvar vidas e proporciona ao doador a oportunidade de realizar exames laboratoriais gratuitos, como verificação de tipos sanguíneos, doenças infecciosas e o bem-estar geral.

- Procedimentos:
  A doação é simples e segura. Antes de doar, você passará por uma triagem para verificar se está apto. Após a doação, será orientado a descansar por alguns minutos e ingerir líquidos.
________________________________________________________________________________________
""")


#MARK: - Elegível (Usuário)
def elegibilidade():
    print("""
________________________________________________________________________________________
𝗘𝗟𝗘𝗚𝗜𝗕𝗜𝗟𝗜𝗗𝗔𝗗𝗘

Responda a algumas das perguntas básicas para saber se você pode doar ou não.

1: Qual sua idade?
""")
    idade = input()

    print("2: Você pesa mais de 50 kg? (s/n)")
    peso = input().strip().lower()
    
    print("4: Você já doou sangue nos últimos 3 meses? (s/n)")
    doacao_recente = input().strip().lower()

    print("5: Você tem alguma condição de saúde que possa impedir a doação? (s/n)")
    condicao_saude = input().strip().lower()
    
    elegivel = True
    
    if int(idade) < 18 or int(idade) > 69:
        print("\nVocê deve ter entre 18 e 69 anos para doar.")
        elegivel = False

    if peso != 's':
        print("\nVocê deve pesar mais de 50 kg para doar.")
        elegivel = False

    if condicao_saude == 's':
        print("\nVocê deve estar se sentindo bem para doar.")
        elegivel = False

    if doacao_recente == 's':
        print("\nVocê deve esperar no mínimo 2 a 3 meses antes da próxima doação. Saiba mais sobre quem pode doar.")
        elegivel = False

    if condicao_saude == 's':
        print("\nCertas condições de saúde podem impedir a doação.")
        elegivel = False

    if elegivel:
        print("\nParabéns! Você é elegível para doar sangue.")
    else:
        print("\nInfelizmente, você não é elegível para doar sangue no momento.")


#MARK: - Locais
def locaisDoacao():
    print("""
________________________________________________________________________________________
𝗟𝗢𝗖𝗔𝗜𝗦 𝗗𝗘 𝗗𝗢𝗔𝗖̧𝗔̃𝗢 𝗘𝗠 𝗙𝗢𝗥𝗧𝗔𝗟𝗘𝗶𝗥𝗔

Você pode doar sangue em diferentes unidades do HEMOCE espalhadas por Fortaleza. Acesse o site do HEMOCE para verificar o local mais próximo de você:
https://www.hemoce.ce.gov.br/
________________________________________________________________________________________
""")


def dicasDoadores():
    print("""
________________________________________________________________________________________
𝗗𝗜𝗖𝗔𝗦 𝗣𝗔𝗥𝗔 𝗗𝗢𝗔𝗗𝗢𝗥𝗘𝗦

- Beba bastante líquido antes e depois da doação.
- Alimente-se bem antes de doar, priorizando alimentos leves e nutritivos.
- Evite esforço físico intenso após a doação e mantenha-se em repouso se sentir tontura.
________________________________________________________________________________________
""")


#MARK: - Inicio
menu()
