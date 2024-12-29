# Gerenciador de Senhas Criptografadas

## Descrição

Este projeto foi criado durante o evento **Pythonando 4day 4projects**, promovido pelo canal **Pythonando** ([link para o canal](https://www.youtube.com/@pythonando)). O evento tem como objetivo ajudar desenvolvedores a criarem projetos em Python de forma prática, aprendendo conceitos novos e melhorando habilidades de programação.

Este projeto é uma aplicação simples para gerenciar senhas de forma segura, utilizando criptografia. Ele permite criar e armazenar senhas criptografadas, visualizar senhas armazenadas, mostrar todas as senhas de uma vez, e até remover domínios específicos com suas senhas associadas.

A aplicação usa a biblioteca `cryptography` com o algoritmo de criptografia **Fernet** para garantir a segurança das senhas armazenadas. Além disso, os dados são armazenados localmente em arquivos de texto.

### Funcionalidades:
- **Criar chave de criptografia**: Geração de uma chave de criptografia para proteger as senhas.
- **Armazenar senhas**: Criptografa e armazena senhas de domínio.
- **Buscar senhas**: Permite buscar senhas armazenadas, fornecendo o domínio e a chave de criptografia.
- **Mostrar todas as senhas**: Exibe todas as senhas armazenadas, caso o usuário forneça a chave correta.
- **Remover senhas**: Permite remover senhas associadas a um domínio específico.

## Como Funciona

1. **Criação da chave de criptografia**:
   - Ao iniciar o programa, o usuário tem a opção de criar uma chave de criptografia. Essa chave será usada para criptografar as senhas antes de armazená-las.
   - A chave gerada pode ser armazenada em um arquivo de texto (opcional) para facilitar o backup ou transferências.
   
2. **Armazenamento de senhas**:
   - O programa permite que o usuário armazene senhas associadas a um domínio específico. Quando a senha é salva, ela é criptografada usando a chave fornecida.
   
3. **Busca e visualização das senhas**:
   - O usuário pode buscar por senhas criptografadas, fornecendo o domínio e a chave de criptografia. A senha correspondente é então descriptografada e exibida.
   - É possível também visualizar todas as senhas armazenadas ao mesmo tempo.
   
4. **Remoção de senhas**:
   - O programa permite que o usuário remova um domínio específico e sua senha associada do arquivo.

## Estrutura do Projeto

O projeto é dividido em diferentes módulos:

- **FernetHasher**: Responsável pela criação de chaves e pela criptografia/descriptografia de dados.
- **Password**: Representa o modelo de dados para armazenar senhas criptografadas, além de métodos para salvar, listar e remover senhas.
- **Template**: Interface de interação com o usuário, permitindo escolher as ações a serem realizadas (criar chave, buscar senha, mostrar senhas, remover senha).
  
## Como Rodar

1. **Instalar Dependências**:
   O projeto usa a biblioteca `cryptography` para criptografar as senhas. Para instalá-la, execute:

   ```
   pip install cryptography
   ```

2. **Rodar a aplicação**:
   Após instalar as dependências, execute o arquivo principal do programa, que provavelmente é o `template.py` ou similar:

   ```
   python template.py
   ```

3. **Interação com o usuário**:
   O programa interage com o usuário via terminal/console. Ao iniciar, o usuário verá um menu com as opções disponíveis, como:

   ```
   Digite o que deseja fazer:
   1 - Criar chave
   2 - Buscar senha
   3 - Mostrar todas as senhas
   4 - Remover senha
   5 - Sair
   ```

   O usuário pode escolher a ação desejada, fornecendo entradas conforme necessário.

## Alterações Recentes

Este projeto passou por algumas alterações, entre elas:

- **Função para remover domínios e senhas**: Agora é possível remover um domínio específico e sua senha associada do arquivo de senhas.
- **Mostrar todas as senhas**: Foi implementada a funcionalidade para exibir todas as senhas de uma vez, desde que o usuário forneça a chave correta.
- **Gerenciamento de arquivos de senhas**: As senhas são armazenadas localmente em um arquivo de texto. O programa agora permite a remoção de linhas desse arquivo com base no domínio.

## Contribuição

Sinta-se à vontade para contribuir com o projeto, sugerindo melhorias, corrigindo bugs ou adicionando novas funcionalidades.
