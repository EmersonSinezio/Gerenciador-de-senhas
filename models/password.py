from datetime import datetime
from pathlib import Path

#TODO Fazer uma função para remover algum dominio
#TODO Fazer uma função para ver todos dominios
#TODO Fazer uma função para modificar algum dominio

class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DB_DIR = BASE_DIR / 'db'

    def save(self):
        self.DB_DIR.mkdir(parents=True, exist_ok=True)
        table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')
        if not table_path.exists():
            table_path.touch()
        with open(table_path, 'a') as f:
            f.write("|".join(list(map(str, self.__dict__.values()))))
            f.write('\n')
    def view_all(self):
        table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')
        if not table_path.exists():
            return []
        with open(table_path, 'r') as f:
            lines = f.readlines()
        return lines
    def remove(self, domain_to_remove):
    # Caminho para o arquivo de senhas
        table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')
        
        # Verifica se o arquivo existe
        if not table_path.exists():
            print("Arquivo de senhas não encontrado.")
            return
        
        # Lê todas as linhas do arquivo
        with open(table_path, 'r') as f:
            lines = f.readlines()
        
        # Reabre o arquivo em modo de escrita (para sobrescrever)
        with open(table_path, 'w') as f:
            removed = False
            for line in lines:
                # Se o domínio na linha não for o que queremos remover, mantemos a linha
                domain = line.strip().split('|')[0]  # Considerando que o domínio é o primeiro campo
                if domain != domain_to_remove:
                    f.write(line)
                else:
                    removed = True
            
            # Se o domínio foi removido, avisa o usuário
            if removed:
                print(f"Domínio '{domain_to_remove}' removido com sucesso!")
            else:
                print(f"Domínio '{domain_to_remove}' não encontrado.")

    @classmethod
    def get(cls):
        table_path = Path(cls.DB_DIR / f'{cls.__name__}.txt')
        if not table_path.exists():
            return []
        with open(table_path, 'r') as f:
            lines = f.readlines()
        results = []
        atributos = vars(cls())
        for i in lines:
            split_v = i.strip().split('|')
            tmp_dict = dict(zip(atributos, split_v))
            results.append(tmp_dict)
        return results

class Password(BaseModel):
    def __init__(self, domain=None, password=None):
        self.domain = domain
        self.password = password
        self.create_at = datetime.now().isoformat()
