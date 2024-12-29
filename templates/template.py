import sys, os
sys.path.append(os.path.abspath(os.curdir))
from models.password import Password
from views.fernet_hasher import FernetHasher

def read_key_from_file(path):
    with open(path, 'rb') as f:
        key = f.read().strip()
    return key

action = input("Digite o que deseja fazer:\n 1 - Criar chave\n 2 - Buscar senha\n 3 - Mostrar todas as senhas\n 4 - Remover senha\n 5 - Sair\n ")

os.system('cls' if os.name == 'nt' else 'clear')
# Criar chave
if action == "1":
    if len(Password.get()) == 0:
        key, path = FernetHasher.create_key(archive=True)
        print("Chave criada com sucesso Key: " + key.decode('utf-8'))
        if path:
            print('Chave salva no arquivo, lembre-se de remover o arquivo após o transferir de local')
            print(f'Caminho do arquivo: {path}')
    else:
        key = input("Digite sua chave usada para criptografia: ")
    domain = input("domain: ")
    password = input("password: ")
    fernet_user = FernetHasher(key)
    encrypted_password = fernet_user.encrypt(password)
    p1 = Password(domain, encrypted_password)
    p1.save()
    os.system('cls' if os.name == 'nt' else 'clear')
# Buscar senha
elif action == "2":
    domain = input("Digite o domínio: ")
    key = input("Digite a chave: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    fernet_user = FernetHasher(key)
    data = Password.get()
    senha_encontrada = False
    for i in data:
        if domain == i['domain']:
            encrypted_password = i['password'].encode('utf-8')
            password = fernet_user.decrypt(encrypted_password)
            senha_encontrada = True
            break
    if senha_encontrada:
        print(f'Senha: {password}')
    else:
        print('Senha não encontrada')
# Mostrar todas as senhas
elif action == "3":
    data = Password.get()
    key = input("Digite a chave:\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    fernet_user = FernetHasher(key)
    for i in data:
        encrypted_password = i['password'].encode('utf-8')
        password = fernet_user.decrypt(encrypted_password)
        print(f"Domínio: {i['domain']}")
        print(f"Senha: {password}")
        print("-" * 40)
# Remover senha
elif action == "4":
    # Remover um domínio
    domain_to_remove = input("Digite o domínio que deseja remover: ")
    key = input("Digite a chave: ")
    fernet_user = FernetHasher(key)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Chama o método remove da classe Password
    data = Password.get()  # Para garantir que os dados existam no arquivo antes de tentar remover
    senha_encontrada = False
    for i in data:
        if domain_to_remove == i['domain']:
            p = Password(domain=i['domain'], password=i['password'])
            p.remove(domain_to_remove)  # Chama a função remove da classe Password
            break

elif action == "5":
    print("Saindo...")