import secrets
import string

caracteres_especiais = ''.join(x for x in string.punctuation if x in '@#!?')
letras = string.ascii_letters + string.digits + caracteres_especiais
senhas_geradas = []

while len(senhas_geradas)< 5:
    senha_forte = ''.join(secrets.choice(letras) for x in range(13))

    upper_count = sum(1 for x in senha_forte if x.isupper())
    special_count = sum(1 for x in senha_forte if x in caracteres_especiais)
    numbers_count = sum(1 for x in senha_forte if x.isdigit())

    if upper_count >= 2 and special_count >= 2 and numbers_count >= 2:
        senhas_geradas.append(senha_forte)
senhas = ' / '.join(senhas_geradas)
print("/",senhas,"/")
