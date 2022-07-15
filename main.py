import PyPDF2
import re

#Passamos o caminho do arquivo
caminho_arquivo = open('fenabrave.pdf', 'rb')
#Aqui vai ser a lib vai fazer a leitura do pdf informado no caminho
leitura_pdf = PyPDF2.PdfFileReader(caminho_arquivo)
#Aqui escolhemos o numero da pagina de onde vamos capturar os dados
numero_da_pagina = leitura_pdf.getNumPages()
escolhe_pagina = leitura_pdf.getPage(8)
#Aqui o texto da pagina selecionada é extraido
conteudo = escolhe_pagina.extractText()
#Aqui é feita a junção
pega_texto = ''.join(conteudo)
#Isso remove a quebra de linhas
junta_texto = re.sub('n', '', pega_texto)
print("\nPegando o texto todo com quebra de linha")
print(junta_texto)
print("\n-----------")
#Isso pega as primeira 50 posições da pagina selecionada e imprimi
'''
print("Pegando apenas as 50 primeiras posições")
novaString = junta_texto[0:50]
print(novaString)
'''

import io
with io.open('fenabrave.txt', "w", encoding="utf-8") as file:
    file.write(str(junta_texto))
