# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

soma = n1 + n2
media = (n1 + n2) / 2

print('A soma entre {} e {} é {}. E a média {}'.format(n1, n2, soma, media))
