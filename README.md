# Gerador de Senhas Fortes
**Este script Python é um gerador de senhas fortes que cria exatamente 5 senhas com critérios específicos e as exibe em uma única linha**

## Qualidade das senhas geradas
[Kaspersky Password Check](https://prnt.sc/rN9_Ik8eRym2)

## Funcionamento
**Importação de Bibliotecas**
- _secrets_: Utilizado para gerar senhas criptograficamente seguras.
- _string_: Fornece constantes para letras e caracteres especiais.

**Configuração dos Caracteres**
- caracteres_especiais: Filtra caracteres especiais comuns da constante string.punctuation para incluir apenas "_@, #, !, e ?_".
- letras: Combina letras (maiúsculas e minúsculas), números e os caracteres especiais aleatórios filtrados em uma única string.

**Geração de Senhas**
- Um loop _while_ é utilizado para gerar senhas até que **5 senhas válidas** sejam criadas.
- Cada senha é gerada com **13 caracteres aleatórios**, escolhidos da string _letras_.
- As senhas são validadas para garantir que contenham pelo menos **2 letras maiúsculas e 2 caracteres especiais**.

**Armazenamento e Exibição**
- Senhas válidas são armazenadas em uma lista _senhas_geradas_.
- Após gerar 5 senhas válidas, todas as senhas são combinadas em uma única string, separadas por "/".
- A string resultante é então exibida em uma única linha para a facilitar a cópia.

**Como Usar**
- Clone o repositório.
- Execute o script com **Python**.

**Requisitos**
- Python 3.x
