# Gerador de Senhas Fortes
**Este script Python é um gerador de senhas fortes que cria exatamente 5 senhas com critérios específicos e as exibe em uma única linha**

## Qualidade das senhas geradas
[Kaspersky Password Check](https://prnt.sc/rN9_Ik8eRym2)

**Requisitos**\n
Python 3.x

## Funcionamento
**Importação de Bibliotecas**\n
secrets: Utilizado para gerar senhas criptograficamente seguras.\n
string: Fornece constantes para letras e caracteres especiais.

**Configuração dos Caracteres**\n
caracteres_especiais: Filtra caracteres especiais comuns da constante string.punctuation para incluir apenas @, #, !, e ?.\n
letras: Combina letras (maiúsculas e minúsculas), dígitos e os caracteres especiais filtrados em uma única string.

**Geração de Senhas**\n
Um loop while é utilizado para gerar senhas até que 5 senhas válidas sejam criadas.\n
Cada senha é gerada com 10 caracteres aleatórios, escolhidos da string letras.\n
As senhas são validadas para garantir que contenham pelo menos 2 letras maiúsculas e 2 caracteres especiais.

**Armazenamento e Exibição**\n
Senhas válidas são armazenadas em uma lista senhas_geradas.\n
Após gerar 5 senhas válidas, todas as senhas são combinadas em uma única string, separadas por "/".\n
A string resultante é então exibida em uma única linha para a facilitar a cópia.

**Como Usar**\n
Clone o repositório.\n
Execute o script com Python.
