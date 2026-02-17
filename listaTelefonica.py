contato = ('Lucio', '(21) 98484-7695', 'lucio@email.com')

telefone2 = []
telefone2.append(contato)
print(telefone2)

telefone3 = [("Lucio", "(21) 98484-7695", "lucio@email.com"), ("Maria", "(21) 98765-4321", "maria@email.com")]
print(telefone3)

print(telefone3[0][1])  # Acessa o telefone do primeiro contato

telefone3_dict = {contato[0]: {"phone": contato[1], "email": contato[2]} for contato in telefone3}
print(telefone3_dict)  # Imprime o dicionário criado a partir da lista de tuplas

telefone3_dict.pop("Lucio")  # Remove o contato "Lucio" do dicionário
print(telefone3_dict)  # Imprime o dicionário após a remoção do contato "Lucio" 