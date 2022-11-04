## CADASTRO ADM BANKING ##
print("- BEM VINDO AO ADM BANKING - \n")

def cadastro():
    print(" Área de cadastro.")
    print("- OLÁ, COMO POSSO TE CHAMAR? ")
    nome = input("NOME:")
    log = input("EMAIL:")
    pwd = input("SENHA:")

def alterar_dados():
	escolha = input("\n[1] Alterar nome.\n"
					"[2] Alterar email.\n"
					"[3] Alterar senha.\n"
					"[0] Sair.\n"
					"\nDigite sua escolha:")
	if escolha == "1":
		nome = input("Digite o seu novo nome: ")
		print("Seu nome foi alterado com sucesso!")
		return alterar_dados()
	
	elif escolha == "2":
		email = input("Digite o seu novo email: ")
		print("Email alterado com sucesso!")
		return alterar_dados()
		
	elif escolha == "3":
		print("Alterar senha.")
		pwd = input("Nova Senha: ")
		pwd2 = input ("Confirme a senha: ")
	
		if pwd == pwd2:
			print("Senha alterada com sucesso!")
		else:
			print("As senhas não coicidem. Tente novamente!")
			return alterar_dados()

	elif escolha == "0":
		exit()
	else:
		print("Comando inválido. Tente novamente! ")
		return alterar_dados()

cadastro()
alterar_dados()
