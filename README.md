# Desafio QA

Este projeto implementa uma automação usando Selenium para acessar o site [4Devs](https://www.4devs.com.br/gerador_de_cpf) e gerar CPF até encontrar um número que comece com 7. Cada CPF gerado é exibido no console indicando se começa ou não com 7.


## Pré-Condições

Antes de executar o script, confira os requisitos:

- Python 3.x instalado.
- Edge WebDriver correspondente à versão do Microsoft Edge instalada.  
  - [Download do Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
- Selenium instalado (confira abaixo).


## Instalação

1. Clone este repositório ou copie o arquivo `main.py` para o seu ambiente local.
2. Instale o Selenium:
   ```bash
   pip install selenium
   ```
3. Certifique-se de que o Edge WebDriver está configurado no PATH do sistema ou na mesma pasta do script.


## Execução

1. Abra um terminal na pasta onde o script está salvo.
2. Execute o script com o comando:
   ```bash
   python main.py
   ```
3. O script abrirá o navegador Edge, acessará o site [4Devs](https://www.4devs.com.br/gerador_de_cpf), e começará a gerar CPFs até encontrar um que comece com o número 7 e feche o navegador.


## Possíveis Erros

1. **Edge WebDriver não configurado corretamente**:
2. **Timeout ao carregar elementos da página**:
   - O site pode estar lento. Verifique sua conexão.
