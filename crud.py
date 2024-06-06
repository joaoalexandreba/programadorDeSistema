import senac.servidor as cd
from pprint import pprint


def main():

    while True:
        print("""\n
            Escolha uma opção abaixo:
        ("+====================================+")
        ("|    ***GESTÃO DE FUNCIONÁRIOS***    |")
        ("|          MENU DE OPÇÕES            |")
        ("|        1 - Cadastro de usuários    |")
        ("|        2 - Buscar                  |")
        ("|        3 - Atualizar Dados         |")
        ("|        4 - Deletar                 |")
        ("|        0 - Sair                    |")      
        ("+====================================+")    
                
        """
        )
        option=int(input())

        if (option ==1):
            # MENU CADASTRAR

            print("""
            +----------------------------------------+
                    **** INSERIR NO CADASTRO *****
            **** Tem certeza que inserir novo cadastro? ****
                        1 - sim
                        0 - não
            +----------------------------------------+
            """)

            op = int(input())

            if(op ==1):
                nome = input("nome: ")
                sobrenome = input("sobrenome: ")
                cpf = input("cpf: ")
                tempoDeServico = int(input("Tempo de Serviço: "))
                remuneracao = float(input("Remuneração: "))
                cd.db_insert(nome, sobrenome, cpf, tempoDeServico, remuneracao)
                print("usuário incluído com sucesso!")

            cd.db_insert('Felipe','silva',526845765,5,5000)
            cd.db_insert('Alice','Mendes',6256845,3,4500)
            cd.db_insert('Geraldo','Menezes',8546785,2,2530)
            cd.db_insert('Lia','Contente',478547,8,12500)

        elif(option ==2):
            # MENU SELECIONAR
            print("""
            Buscar usuário:
                1 - id
                2 - nome
                3 - sobrenome
                4 - cpf
                5 - tempoDeServico
                6 - remuneracao
            """)

            field = int(input())

            if (field ==1):
                valorDoCampo = int(input("Id: "))
                pprint(cd.db_select(valorDoCampo, 'id'))
            elif(field ==2):
                valorDoCampo = input("Nome: ")
                pprint(cd.db_select(valorDoCampo, 'nome'))
            elif(field ==3):
                valorDoCampo = input("Sobrenome: ")
                pprint(cd.db_select(valorDoCampo, 'sobrenome'))
            elif(field ==4):
                valorDoCampo = int(input("CPF: "))
                pprint(cd.db_select(valorDoCampo, 'cpf'))
            elif(field ==5):
                valorDoCampo = int(input("Tempo de Serviço: "))
                pprint(cd.db_select(valorDoCampo, 'tempoDeServico'))
            elif(field ==6):
                valorDoCampo = int(input("Remuneração"))
                pprint(cd.db_select(valorDoCampo, 'remuneracao'))


        elif(option ==3):
            # MENU ATUALIZAR
            print("   *** ALTERAR CADASTRO DO USUÁRIO ***   ")
            cpfE = input("Digite o CPF: ")

            print("""
            O que deseja alterar no cadastro?\n
                1 - nome
                2 - sobrenome
                3 - cpf
                4 - tempoDeServico
                5 - remuneracao
            """)

            field = int(input())
            if (field ==1):
                nome = input("Novo nome: ")
                cd.db_updateNome(nome, cpfE)

            elif(field ==2):
                sobrenome = input("Novo sobrenome: ")
                cd.db_updateSobrenome(sobrenome, cpfE)

            elif(field ==3):
                cpfnovo = input("Novo cpf: ")
                id = int(input("Qual é o id do usuário? "))
                cd.db_updateCpfNovo(cpfnovo, id)

            elif(field ==4):
                tempoDeServico = input("Novo tempo de serviço: ")
                cd.db_updatetempoDeServico(tempoDeServico, cpfE)

            elif(field ==5):
                valorDoCampo = input("Tempo de Serviço: ")
                cd.db_updatetempoDeServico(valorDoCampo, cpfE)

            elif(field ==6):
                remuneracao = input("nova remuneração: ")
                cd.db_updateremuneracao(remuneracao, cpfE)

            print("Atualização executada com sucesso!")

        elif(option ==4):
            # MENU DELETAR
            cpf = int(input("informe o CPF:\n"))

            print("""
            +----------------------------------------+
                    **** DELETAR CADASTRO *****
            **** Tem certeza que deseja deletar? ****
                        1 - sim
                        0 - não
            +----------------------------------------+
            """)

            op = int(input())

            if(op ==1):
                cd.db_delete(cpf)
                print("usuário excluído com sucesso!")
        elif(option ==0):
            print("Operação encerrada pelo usuário!")
            break
        else:
            print("Escolha uma opção válida!")

if __name__ == "__main__":
    main()


