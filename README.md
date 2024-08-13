# Gerador de Senhas Fortes
**Este script Python é um gerador de senhas fortes que cria exatamente 5 senhas com critérios específicos e as exibe em uma única linha**

## Qualidade das senhas geradas
[Kaspersky Password Check](https://prnt.sc/rN9_Ik8eRym2)

**Requisitos**\**
Python 3.x

## Funcionamento
**Importação de Bibliotecas**\**
secrets: Utilizado para gerar senhas criptograficamente seguras.\**
string: Fornece constantes para letras e caracteres especiais.

**Configuração dos Caracteres**\**
caracteres_especiais: Filtra caracteres especiais comuns da constante string.punctuation para incluir apenas @, #, !, e ?.\**
letras: Combina letras (maiúsculas e minúsculas), dígitos e os caracteres especiais filtrados em uma única string.

**Geração de Senhas**\**
Um loop while é utilizado para gerar senhas até que 5 senhas válidas sejam criadas.\**
Cada senha é gerada com 10 caracteres aleatórios, escolhidos da string letras.\**
As senhas são validadas para garantir que contenham pelo menos 2 letras maiúsculas e 2 caracteres especiais.

**Armazenamento e Exibição**\**
Senhas válidas são armazenadas em uma lista senhas_geradas.\**
Após gerar 5 senhas válidas, todas as senhas são combinadas em uma única string, separadas por "/".\**
A string resultante é então exibida em uma única linha para a facilitar a cópia.

**Como Usar**\**
Clone o repositório.\**
Execute o script com Python.
