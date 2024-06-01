from bs4 import BeautifulSoup
import requests
import sys
import re

class MercadoScraper:
    def __init__(self, url):
        self.url = url
        self.nome_mercado = ""
        self.dt_emissao = ""
        self.found = []

    def fetch_data(self):
        response = requests.get(url)
        if response.status_code == 200:
            html_text = response.text
            self.soup = BeautifulSoup(html_text, 'html.parser')
        else:
            print(f'A requisição falhou com o código de status {response.status_code}')

    def parse_data(self):
        self.nome_mercado = self.soup.find('div', class_='txtTopo').get_text()
        data_emissao = self.soup.find(string=re.compile('- Via Consumidor 2'))
        self.data_emissao = self.normalize_data_emissao(data_emissao)
        self.found = self.soup.find_all('span', class_=['txtTit', 'Rqtd', 'RUN', 'RvlUnit', 'valor'])

    @staticmethod
    def normalize_data_emissao(str_data_emissao):
        str_data_emissao = str_data_emissao.split(" ")
        return str_data_emissao[0]

    def clean_html(self):
        for strong_tag in self.soup.find_all('strong'):
            strong_tag.decompose()

    def save_to_csv(self, filename):
        with open(filename, 'a', encoding='utf-8') as csv:
            aux_concatena_texto = ''
            i = 0

            for link in self.found:
                if i == 0:
                    aux_concatena_texto += f'"{self.nome_mercado}",'

                aux_concatena_texto += f'"{link.get_text(separator=" ", strip=True)}",'
                i += 1
                if i == 5:
                    aux_concatena_texto += f'"{self.data_emissao}"\n'
                    i = 0

                if aux_concatena_texto.endswith(',\n'):
                    aux_concatena_texto = aux_concatena_texto[:-2]

            csv.write(aux_concatena_texto)

    def run(self):
        self.fetch_data()
        self.clean_html()
        self.parse_data()
        self.save_to_csv('assets/compras-mercado.csv')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <url>")
        exit(1)

url = sys.argv[1]
scraper = MercadoScraper(url)
scraper.run()