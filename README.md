## Instalação do flake8 e do mypy:
- <code> pip install flake8 mypy <code>
  
## Configuração do flake8-hook para git
*Essa configuração impede que o código fora do estilo seja commitado*
<code>$ git config --bool flake8.strict true <code>

## Verificando se o projeto contem erros:
<code>$ mypy main.py<code>
<code>$ flake8 main.py<code>