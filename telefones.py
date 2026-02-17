telefone = ['(11) 1234-5678', '(11) 99999-2345', '(11) 99999-3456', '(11) 99999-4567', '(11) 99999-5678', '(11) 99999-6789', '(11) 99999-7890'];
print(telefone[0]);

telefone.append('(11) 99999-8765'); # Adiciona um novo número de telefone no final da lista 
print(telefone);

telefone.insert(0, '(11) 99999-7654'); # Insere um novo número de telefone na posição 0 (início da lista)
print(telefone);

telefone.remove('(11) 1234-5678'); # Remove o número de telefone específico da lista
print(telefone);    

telefone.pop(5); # Remove o número de telefone na posição 5 (índice 5)
print(telefone);