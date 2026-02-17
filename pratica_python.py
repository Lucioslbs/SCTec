# Aula 02 - Prática #

nome = input("Digite seu nome: ");
sobrenome = input("Digite seu sobrenome: ");
print("Olá, " + nome + " " + sobrenome + "! Bem-vindo à aula de Python!");
idade = input("Digite sua idade: ");
print("Você tem " + idade + " anos.");
nascimento = 2026 - int(idade);
print("Você nasceu em " + str(nascimento) + ".");
anos = 2030 - int(nascimento);
print("Em 2030, você terá " + str(anos) + " anos.");
