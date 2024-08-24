import requests
from time import sleep
from os import system, name

class MonitoramentoCriptos():
    # Coletar dados de email e meta de valor
    def __init__(self) -> None:
        self.headers = {"accept": "application/json", "x-cg-demo-api-key": "<< SUA API KEY >>"}
        while True:
            print('')
            self.sublinhar('Monitoramento de Criptomoeda', cod_cor='\033[1;33m')
            print('''
Seja bem-vindo(a) ao sistema de Monitoramento de Bitcoin.

O sistema é responsável por monitorar a cada 10 minutos o valor dessa criptomoeda. 
Para isso, mantenha o sistema em funcionamento para o monitoramento ocorrer corretamente. 
Caso tenha interesse em manter esse sistema funcionando mesmo após o desligamento do dispositivo atual, entre em contato com o desenvolvedor através do seguinte link: "\033[1;36mhttps://ggalvesilva63.wixsite.com/gabriel-alves-silva\033[0;0m"''')
            self.email = str(input('\nInforme o email em que deseja receber uma notificação quando o valor da criptomoeda for abaixo ou igual ao desejado >> ')).strip().lower()
            ok = self.validar_email()
            if not ok:
                self.sublinhar('ERRO: Por favor, informe um email válido.', cod_cor='\033[1;34m')
                input('Pressione enter para inserir novamente.')
                self.limpar_terminal()
                continue
            while True:                
                self.meta_de_valor = str(input('\nInforme sua meta de valor para receber notificação ao ser atingida (somente valores inteiros)\n\n* R$ + Valor para meta em real (selecionado por padrão)\n* US$ + Valor para meta em dólar >> ')).strip().upper()
                tipo_de_moeda = self.validar_meta()
                if tipo_de_moeda == "":
                    self.sublinhar('ERRO: Informe um valor válido.', '\033[1;31m')
                    continue
                else:
                    self.moeda = tipo_de_moeda
                    break
            self.sublinhar("RESUMO DOS DADOS CADASTRADOS", '\033[1;33m')
            print(f'\nEmail cadastrado para receber a notificação: {self.email.lower()}')
            if tipo_de_moeda == "brl":
                formatacao = "R$"
            else:
                formatacao = "US$"
            print(f'Meta de valor para receber a notificação: {formatacao}{self.meta_de_valor}\n')
            break

    def validar_meta(self):
        tipo = 'brl'
        if "R$" in self.meta_de_valor:
            self.meta_de_valor = self.meta_de_valor.replace("R$", "")
        elif "US$" in self.meta_de_valor:
            self.meta_de_valor = self.meta_de_valor.replace("US$", "")
            tipo = "usd"
        if "." in self.meta_de_valor:
            self.meta_de_valor.replace(".", "")
        if "," in self.meta_de_valor:
            self.meta_de_valor.replace(",", "")
        try:
            self.meta_de_valor = int(self.meta_de_valor)
        except:
            return ""
        return tipo
    
    def validar_email(self):
        if self.email.count("@") == 1:
            return True
        else:
            return False
            
    @staticmethod
    def limpar_terminal():
        system('cls' if name == 'nt' else 'clear')
        
    @staticmethod
    def sublinhar(texto, cod_cor='\033[0;0m'):
        print(f'\n{cod_cor}' + '-'*(len(texto)+4) + f'\033[0;0m')
        print(f'{cod_cor}  {texto}  ' + f'\033[0;0m')
        print(f'{cod_cor}' + '-'*(len(texto)+4) + f'\033[0;0m')

    def requerir_cotacao(self):
        url = "https://api.coingecko.com/api/v3/coins/bitcoin"
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            response_json = response.json()
            input()
        else:
            pass
        
        

if __name__ == "__main__":
    teste = MonitoramentoCriptos()
# Solicitar valor do Bitcoin
    teste.requerir_cotacao()
# Agendar tarefa de 10 em 10 minutos









