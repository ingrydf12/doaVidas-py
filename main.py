#MARK: - Menu
def menu():
    while True:
        print(r"""
--------
  ____            __     ___     _           
 |  _ \  ___   __ \ \   / (_) __| | __ _ ___ 
 | | | |/ _ \ / _` \ \ / /| |/ _` |/ _` / __|
 | |_| | (_) | (_| |\ V / | | (_| | (_| \__ |
 |____/ \___/ \__,_| \_/  |_|\__,_|\__,_|___/
                                             
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

Etapas da doação:
1. AGENDAMENTO -> Você deve agendar online a sua doação no portal do doador, escolhendo dia, horário e local.

2. CADASTRO -> Você precisa apresentar um documento de identificação oficial com foto ou cópia autenticada (RG, carteira nacional de habilitação, carteira de trabalho, carteira profissional emitida por classe, certificado de reservista ou passaporte)
Além disso, é necessário deixar um meio de contato com o doador. 
OBS: TAMBÉM SÃO ACEITOS OUTROS TIPOS DE DOCUMENTOS DIGITAIS COMO ETITULO, CARTEIRA DIGITAL...

3. LANCHE ->  Você como doador é convidado a realizar o pré-lanche, para manter o nível de hidratação e também os níveis de açúcar adequados para a coleta.

4. PRÉ-TRIAGEM -> Verificação básica por meio de exames de verificação de pressão arterial, pulso, temperatura, dosagem de hemoglobina e verificação de peso.

5. TRIAGEM CLÍNICA -> Perguntas individuais e sigilosas feitas ao possível doador para verificar se é apto a realizar a doação de sangue naquele momento ou não. Necessário ser respondidas com sinceridade e honestidade.

6. VOTO DE AUTO-EXCLUSÃO -> Totalmente sigiloso, permite ao candidato confirmar ou negar as informações prestadas sem expor diretamente suas respostas ao profissional da triagem.

7. COLETA DE SANGUE -> O doador é orientado a lavar os braços (local da punção) com água e sabão, caso o posto de coleta ou coleta externa não tenha lavatório, é feita assepsia do local da punção, o que traz segurança à coleta.
O volume máximo de sangue colhido é de 460 ml em um tempo médio de 7 a 10 minutos.

8. LANCHE -> Após a coleta de sangue, o doador é novamente convidado a fazer um lanche e aguardar, no mínimo, 15 minutos sentado no posto de coleta.

9. ENTREGA DE CARTEIRINHA ->  Em caso de primeira doação, o doador recebe a carteirinha de doador de primeira vez.

10. EXAMES REALIZADOS NO SANGUE COLETADO -> Os exames realizados no sangue coletado são: tipagem sanguínea, eletroforese de hemoglobina e testes para hepatite B e C, sífilis, doença de Chagas, HIV e HTLV I e II.

11. RESULTADO DE EXAMES -> Cerca de 45 dias após a doação, o voluntário pode acessar o resultado dos exames sorológicos pelo portal do doador, através do site: doador.hemoce.ce.gov.br.
. Caso seja necessário esclarecimento sobre os resultados, o voluntário será convidado a comparecer novamente ao Hemocentro para coletar uma nova amostra de sangue e receber orientações.

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
𝗟𝗢𝗖𝗔𝗜𝗦 𝗗𝗘 𝗗𝗢𝗔𝗖̧𝗔̃𝗢 𝗘𝗠 𝗙𝗢𝗥𝗧𝗔𝗟𝗘𝗭𝗔


----
SEDE HEMOCE
Av. José Bastos, 3390 – Rodolfo Teófilo – CEP: 60.431-086 – Fortaleza-CE


Horário de Funcionamento:
-> 7h às 17h30min, de segunda a sexta-feira
-> 7h às 16h, aos sábados
-> 7h às 13h, aos domingos

------ 
HEMOCE PRAÇA DAS FLORES
Av. Desembargador Moreira, sn – Aldeota

Horário de Funcionamento:
-> 7h às 12h30 e 14h às 16h, de terça a sábado

-----

Contatos para agendamento
(85) 99681-7597 (WhatsApp) / (85) 32080805


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
