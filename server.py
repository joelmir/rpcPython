# Server
import SimpleXMLRPCServer

class minha_agenda:
    contatos = {}
    
    def __init__(self):
        #realiza a carga inicial dos dados
        self.carrega_dados()
    
    def cadastra(self, nome,cidade,telefone):
        mensagem = 'cadastrado'
        #Verifica se o contato ja existe
        if self.contatos.has_key(nome):
            mensagem = 'atualizado'
            
        #Atualiza dos dados
        self.contatos[nome] = (cidade,telefone)
        
        #salva as alteracoes no arquivo
        self.persiste()
        
        return 'contato '+mensagem+'!'
    
    #Retorna todos usuarios cadastrados em ordem alfabetica
    def consulta(self):
        resultado = []
        for key in sorted(self.contatos.iterkeys()):
            resultado.append((key,self.contatos[key][0],self.contatos[key][1]))
        if len(resultado) == 0:
            return 'A base nao possui contatos cadastrado'
        retorno = ''
        for r in resultado:
            retorno +='\nO contato %s mora da cidade %s e possui o telefone %s'%r
        return retorno
    
    #Retorna os usuarios conforme o filtro por nome, em ordem alfabetica
    def consulta_nome(self,nome):
        resultado = []
        for key in sorted(self.contatos.iterkeys()):
            if nome.upper() in key.upper():
                resultado.append((key,self.contatos[key][0],self.contatos[key][1]))
        if len(resultado) == 0:
            return 'Nenhum usuario encontrado com o filtro informado ('+nome+')'
        retorno = ''
        for r in resultado:
            retorno +='\nO contato %s mora da cidade %s e possui o telefone %s'%r
        return retorno
    
    #Retorna os usuarios conforme o filtro por cidade, em ordem alfabetica
    def consulta_cidade(self,cidade):
        resultado = []
        for key in sorted(self.contatos.iterkeys()):
            if cidade.upper() in self.contatos[key][0].upper():
                resultado.append((key,self.contatos[key][0],self.contatos[key][1]))
        if len(resultado)==0:
            return 'Sua pesquisa nao retornou nenhum dado'
        retorno = ''
        for r in resultado:
            retorno +='\nO contato %s mora da cidade %s e possui o telefone %s'%r
        return retorno
    
    #Retorna os usuarios conforme o filtro por telefone, em ordem alfabetica    
    def consulta_telefone(self,telefone):
        resultado = []
        for key in sorted(self.contatos.iterkeys()):
            if telefone.upper() in self.contatos[key][1].upper():
                resultado.append((key,self.contatos[key][0],self.contatos[key][1]))
        if len(resultado)==0:
            return 'Sua pesquisa nao retornou nenhum dado'
        retorno = ''
        for r in resultado:
            retorno +='\nO contato %s mora da cidade %s e possui o telefone %s'%r
        return retorno
        
    #remove o usuario por nome
    def remove(self,nome):
        if self.contatos.has_key(nome):
            del self.contatos[nome]
            #salva as alteracoes no arquivo
            self.persiste()
            return 'O contato foi excluido com sucesso!!!'
        else:
            return 'Contato nao encontrato, verifique o nome e letras "maiusculas" e "minusculas"'
    
    #salva a lista de contatos no arquivo
    def persiste(self):
        try:
            with open('agenda.data','w') as agenda:
                agenda.write(str(self.contatos))
        except IOError:
            print 'Nao foi possivel gravar o arquivo em disco\nVerifique as permicoes'
            print 'O servidor continuara funcionando, porem nao vai salvar as alteracoes para futuras consultas'
    #recupera a lista de contatos do arquivo
    def carrega_dados(self):
        try:
            with open('agenda.data','r') as agenda:
                retorno = agenda.read()
                if retorno:
                    try:
                        self.contatos = eval(retorno)
                        if type(self.contatos) == dict:
                            print 'Contatos carregados com sucesso!!\n'
                        else:
                            raise SyntaxError
                    except SyntaxError:
                        print 'O arquivo esta corrompido, nao foi possivel acessar!!\n'
        except IOError:
            #Se o arquivo nao foi encontrado, nao faz nada
            pass
        print 'Servidor no Ar!!!'
#Define o IP e a porta do servidor            
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("127.0.0.1", 50000))
#Define a instacia que tera as funcoes que o servidor suporta
server.register_instance(minha_agenda())
#Main loop (fica rodando e executando as requisicoes dos clientes)
server.serve_forever()