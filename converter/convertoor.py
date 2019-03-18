import unicodedata 
import csv
import re

diretorio = "Auditiva.csv"
arq = open("t.xml", "w")
idt = 0

with open(diretorio) as arquivocsv: #abre o arquivo do diretorio
	ler = csv.DictReader(arquivocsv, delimiter=",") #ler como csv
	for linha in ler: #varre as linhas do arquivo
		nome = linha["nome"]
		ano = linha["ano"]
		objetivo = linha["objetivo"]
		solucao = linha["solucao"]
		plataforma = linha["plataforma"]
		faixa = linha["faixa"]
		licenca = linha["licenca"]
		deficiencia = linha["deficiencia"]
		arq.write("\n<ta>\n\t<id>"+str(idt)+"</id>\n\t<nome>"+nome+"</nome>\n\t<ano>"+ano+"</ano>\n\t<objetivo>"+objetivo+"</objetivo>\n\t<solucao>"+solucao+"</solucao>\n\t<plataforma>"+plataforma+"</plataforma>\n\t<faixa>"+faixa+"</faixa>\n\t<licenca>"+licenca+"</licenca>\n\t<deficiencia>"+deficiencia+"</deficiencia>\n</ta>\n")
		idt = idt + 1 			




# "<ta>\n\t<id>"+id+"</id>\n\t<nome>"+nome+"</nome>\n\t<ano>"+ano+"</ano>\n\t<objetivo>"+objetivo+"</objetivo>\n\t<solucao>"+solucao+"</solucao>\n\t<plataforma>"+plataforma+"</plataforma>\n\t<faixa>"+faixa+"</faixa>\n\t<licenca>"+licenca+"</licenca>\n\t<deficiencia>"+deficiencia+"</deficiencia>\n</ta>"