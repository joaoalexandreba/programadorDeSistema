import sqlite3
con = sqlite3.connect('base_deDados.db') #criando base
cur = con.cursor() #conectando cursor
#sintaxe do sql
sql = """
CREATE TABLE TabelaFuncionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                          nome TEXT NOT NULL,
                          sobrenome TEXT NOT NULL,
                          cpf INTEGER NOT NULL,
                          tempoDeServico INTEGER NOT NULL,
                          remuneracao INTEGER NOT NULL)
"""
cur.execute(sql)
con.commit() #executar os comandos na base
con.close()
