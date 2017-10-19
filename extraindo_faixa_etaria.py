# Descrição do Script
#Extraindo de uma Base de dados Mysql a quantidade de visitantes por faixa etária 

import pymysql
import datetime

data = datetime.datetime.now()

# Cria uma Conexão com o banco Mysql
conn = pymysql.connect(host = "teste.wifiaqui.com.br", user = "root", password = "mysql.xlogic", db = "radius-teste")
connect = conn.cursor()


# Seleciona a Idade de todos os Visitantes da tabela Visitantes
def select_visitantes():
	connect.execute("""SELECT DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(ano_nascimento, '%Y') AS idade FROM visitante WHERE ano_nascimento != '000-00-00'""")
	
	lista_idades = []

	for idade in connect.fetchall():
		lista_idades.append(idade[0])

	return lista_idades


# Classifica a quantidade por faixa etaria
def faixa_etaria(idades):

	faixa_etaria = {'criancas': 0, 'adolescentes': 0, 'jovens': 0,  'adultos': 0, 'idosos': 0}
	
	for idade in idades:

		if idade > 0 and idade <= 11:
			faixa_etaria['criancas'] += 1 

		if idade >= 12 and idade <= 17:
			faixa_etaria['adolescentes'] += 1

		if idade >= 18 and idade <= 19:
			faixa_etaria['jovens'] += 1

		if idade >= 30 and idade <= 60:
			faixa_etaria['adultos'] += 1

		if idade > 60:
			faixa_etaria['idosos'] += 1

	return faixa_etaria
			

print(faixa_etaria(select_visitantes())) 

# Exemplo de resultados obtidos: {'criancas': 1, 'adolescentes': 7, 'jovens': 10, 'idosos': 2, 'adultos': 82}