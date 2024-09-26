opcao = input("")

def menu(opcao):
    print("""
 ________  ________  ___       ___      ___ ________  ___      ___ ___  ________  ________  ________      
|\   ____\|\   __  \|\  \     |\  \    /  /|\   __  \|\  \    /  /|\  \|\   ___ \|\   __  \|\   ____\     
\ \  \___|\ \  \|\  \ \  \    \ \  \  /  / | \  \|\  \ \  \  /  / | \  \ \  \_|\ \ \  \|\  \ \  \___|_    
 \ \_____  \ \   __  \ \  \    \ \  \/  / / \ \   __  \ \  \/  / / \ \  \ \  \ \\ \ \   __  \ \_____  \   
  \|____|\  \ \  \ \  \ \  \____\ \    / /   \ \  \ \  \ \    / /   \ \  \ \  \_\\ \ \  \ \  \|____|\  \  
    ____\_\  \ \__\ \__\ \_______\ \__/ /     \ \__\ \__\ \__/ /     \ \__\ \_______\ \__\ \__\____\_\  \ 
   |\_________\|__|\|__|\|_______|\|__|/       \|__|\|__|\|__|/       \|__|\|_______|\|__|\|__|\_________/
                                                                        
    Programa direcionado ao espaço do doador para entender e incentivar a doação de sangue em Fortaleza.
                                                                                                          
   MENU INTERATIVO: PARA ONDE VOCÊ QUER IR?
   [1] Quem pode doar?
   [2] Saiba os benefícios e procedimentos
   [3] Elegilibidade: você pode doar com base nessas perguntas?
   [4] Locais de doação em Fortaleza
   [5] Dicas para doadores
   [0] Sair                                                                                
""")
    
    if opcao == 1: 
         return doacaoInfo
    elif opcao == 2: 
     return "Caso 2" 

    elif opcao == 3: 
     return "Caso 3" 

    elif opcao == 4: 
     return "Caso 4" 
    
    elif opcao == 5: 
     return "Caso 5" 
    
    elif opcao == 0: 
     return exit()
    
    else: 
     return "Essa opção é inválida, tente novamente." 
    
#Separar uma funcao para cada opcao
def doacaoInfo():
    print(""" 
________________________________________________________________________________________
𝗤𝗨𝗘𝗠 𝗣𝗢𝗗𝗘 𝗗𝗢𝗔𝗥?

Se você estiver saudável, bem alimentado antes da doação, pesar acima de 50kg, tiver entre 16 a 69 anos
e apresentar documento oficial com foto, você pode doar. Caso você tenha idade entre 16 e 17 anos, você precisa
ter um termo de consentimento formal por escrito do seu responsável legal para cada doação que fizer.
          
O HEMOCE disponbiliza em seu site o TERMO DE CONSENTIMENTO PARA MENORES DE 18 ANOS que deverá ser apresentado para autorização desses jovens nessa faixa etária.

O limite máximo para PRIMEIRA DOAÇÃO é de 60 (Sessenta) ANOS, 11 (Onze) MESES e 29 (vinte e nove) DIAS.
          
Caso queira mais informações acerca da doação, acesse o site do HEMOCE: https://www.hemoce.ce.gov.br/servicos/espaco-do-doador/doacao-de-sangue/duvidas-frequentes/
________________________________________________________________________________________
""")