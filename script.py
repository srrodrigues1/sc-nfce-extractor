from bs4 import BeautifulSoup
import requests
import sys
import re

if len(sys.argv) != 2:
    print("Uso: python main.py <url>")
    exit(1)

def normalize_data_emissao(str_data_emissao):
    str_data_emissao = str_data_emissao.split(" ")
    return str_data_emissao[0]

url = sys.argv[1]

response = requests.get(url)

if response.status_code == 200:
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')

    classes = ['txtTit', 'Rqtd', 'RUN', 'RvlUnit', 'valor']
    found = soup.find_all('span', class_=classes)

    nome_mercado = soup.find('div', class_='txtTopo').get_text()
    data_emissao = soup.find(string=re.compile('- Via Consumidor 2'))
    data_emissao = normalize_data_emissao(data_emissao)

    for strong_tag in soup.find_all('strong'):
        strong_tag.decompose()

    with open('compras-mercado.csv', 'a', encoding='utf-8') as csv:
        aux_concatena_texto = ''
        i = 0

        for link in found:
            if i == 0:
                aux_concatena_texto += f'"{nome_mercado}",'

            aux_concatena_texto += f'"{link.get_text(separator=" ", strip=True)}",'
            i += 1
            if i == 5:
                aux_concatena_texto += f'"{data_emissao}"\n'
                i = 0

            if aux_concatena_texto.endswith(',\n'):
                aux_concatena_texto = aux_concatena_texto[:-2]

        csv.write(aux_concatena_texto)

else:
    print(f'A requisição falhou com o código de status {response.status_code}')
