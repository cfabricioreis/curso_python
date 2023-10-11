"""
Faça um jogo para o usuário adivinhar qual 
a palavra secreta.
- Você vai propor uma palavra secreta 
qualquer e vai dar a possibilidade para 
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está 
na palavra secreta. 
    - se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import re 

PALAVRA_SECRETA = 'PerFumE'
resposta =        re.sub('.', '*', PALAVRA_SECRETA)
tentativas=0

while resposta!=PALAVRA_SECRETA:
    letra= input('Digite uma letra: ')
    if letra in PALAVRA_SECRETA:
        i=0
        while i<len(PALAVRA_SECRETA):
            if letra==PALAVRA_SECRETA[i]:
                resposta= resposta[:i]+letra+resposta[i+1:] 
            i+=1
    print(resposta) 
    tentativas+=1

print("Finalizado!")
print(f"Palavra secreta era {resposta}")
print(f'Você precisou de {tentativas} tentativas')
