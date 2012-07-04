#Client
import xmlrpclib,socket,xml

try:
    #Define o servidor que vai acessar
    server = xmlrpclib.Server('http://127.0.0.1:50000')
    while 1:
        try:
            opcao = raw_input('''
1 - Cadastrar
2 - Consultar
3 - Exluir
4 - Sair
''')
            #Cadastrar
            if opcao == '1':
                print '\nCadastro de contatos'
                nome = raw_input('Digite o nome do contato: ')
                cidade = raw_input('Digite a cidade do contato: ')
                telefone = raw_input('Digite o telefone do contato: ')
                print server.cadastra(nome,cidade,telefone)
            #Consultar
            elif opcao == '2':
                print '\nCConsulta de contatos\nConsultar por:'
                opcao2 = raw_input('''
0 - Todos
1 - Nome
2 - Cidade
3 - Telefone
4 - Cancelar consulta
''')
                if opcao2 == '0':
                    print server.consulta()
                elif opcao2 == '1':
                    nome = raw_input('Consultando pelo nome...\nDigite o nome do contato: ')
                    print server.consulta_nome(nome)
                elif opcao2 == '2':
                    cidade = raw_input('Consultando pela cidade...\nDigite a cidade do contato: ')
                    print server.consulta_cidade(cidade)
                elif opcao2 == '3':    
                    telefone = raw_input('Consultando pelo telefone...\nDigite o telefone do contato: ')
                    print server.consulta_telefone(telefone)
                elif opcao2 == '4':
                    print 'Consulta cancelada pelo usuario'
                else:
                    print 'Consulta cancelada, opcao invalida!'
            #Remover
            elif opcao == '3':
               nome = raw_input('Digite o nome do contato a ser removido: ')
               print server.remove(nome)
            #Sair
            elif opcao == '4':
                break
            else:
                print 'Opcao invalida!'
                
        #trata os erros de acentuacao, pois o sistema ainda esta na versao beta
        except xmlrpclib.Fault:
            print '\nOpsss, esse sistema nao permite caracteres acentuados!!!\nTente novamente sem acentos.\n'
        except xml.parsers.expat.ExpatError:
            print '\nOpsss, esse sistema nao permite caracteres acentuados!!!\nO servidor esta tentando lhe enviar arquivos com acentos'
            print 'Entre em contato com o Administrador do sistema\n:D\n'
            
#Caso ocorrer algum erro de conexao com o servidor
except socket.error:
    print 'O servidor recusou a conexao, verifique se o servidor esta acessivel e se os parametros de conexao estao corretos.'
    print 'O programa sera encerrado em 3 segundos...'
    import time
    time.sleep(3)