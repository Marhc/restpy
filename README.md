# restpy

Exemplo de uma Api Rest escrita em Python seguindo o padrão MRC (Model-Resource-Controller) e usando [SQLite](https://www.sqlite.org), [Flask](https://github.com/pallets/flask), [Flask-RESTful](https://github.com/flask-restful/flask-restful) e [Flask-SQLAlchemy-Session](https://github.com/dtheodor/flask-sqlalchemy-session).

## Pré-Requisitos

Antes de começar, você precisa instalar em seu sistema:

- [Git](https://git-scm.com/downloads)
- [Python 3.6](https://www.python.org/downloads)
- [pip](https://pip.pypa.io/en/stable/installing) (geralmente, já incluído na instalação do Python)
- [pipenv](https://packaging.python.org/tutorials/managing-dependencies)
- [Visual Studio Code](https://code.visualstudio.com/download) (**VSCode**), mas somente no ambiente de desenvolvimento.

No ambiente de desenvolvimento, também recomendamos instalar, no **VSCode**, a extensão [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

Use o **_REST Client_** para testar os endereços relacionados no arquivo **_urls.rest_**.

Mas se preferir, você pode utilizar qualquer cliente como [Postman](https://www.getpostman.com), [Insomnia](https://insomnia.rest/download), [httpie](https://httpie.org/doc#installation) ou simplesmente o comando **_curl_** para testar a Api.

## Instalação

O primeiro passo é clonar o projeto para o seu sistema:

```git
git clone https://github.com/Marhc/restpy.git
```

Depois, mude para a pasta que foi criada:

```bash
cd restpy
```

A partir daí o procedimento varia conforme o ambiente de instalação.

### No ambiente de produção

Instale somente as dependências de produção:

```
pipenv install
```

E inicie a aplicação digitando:

```
pipenv run start
```

### No ambiente de desenvolvimento

Instale todos os componentes, tanto de produção como de desenvolvimento:

```
pipenv install --dev
```

Crie o arquivo **_.env_** na raiz do projeto e inclua apenas duas variáveis:

```bash
echo FLASK_ENV=development > .env
echo FLASK_APP=app.py >> .env
```

Com o arquivo **_.env_** podemos gerenciar as variáveis de ambiente utilizadas pela aplicação.

Agora, inicie a Api em modo de desenvolvimento com o comando:

```
pipenv run dev
```

## Advertência

Esse é apenas um projeto de exemplo e muitos recursos necessários para o funcionamento em produção **_NÃO_** foram incluídos, tais como:

- Validação
- Autenticação
- _Query String parsing_
- Registro de Migrações da base de dados

Portanto, **_NÃO USE ESSA API EM PRODUÇÃO_**.

O objetivo inicial do projeto foi apenas exercitar os conceitos básicos envolvidos na criação de uma Api simples, porém escalável.

## Lançamentos futuros

Algumas funcionalidades são previstas para versões futuras:

- [ ] Criar modelo base com os atributos comuns a todos os modelos e habilitar **_timestamp_**

- [ ] Reconstruir a classe **_Controller_** para facilitar a criação de novos **_controllers_** a partir de um modelo qualquer

- [ ] Criar a classe **_ResourceSet_** para facilitar a criação de novos **_resources_**

Sinta-se a vontade para contribuir com esses recursos ou alguma outra funcionalidade que considerar importante. Você só precisa fazer um **_fork_** do projeto e enviar um **_Pool Request_** da sua contribuição.

## Licença

Esse projeto está licenciado sob a licença [MIT](https://choosealicense.com/licenses/mit), isso significa que você é livre para:

- **Compartilhar**: copiar, distribuir e usar o código.
- **Criar**: produzir trabalhos a partir do projeto.
- **Adaptar**: modificar, transformar e desenvolver o código incluído no projeto.

Desde que:

- **Atribua a fonte**: você deve fazer a atribuição em qualquer uso público do projeto ou trabalhos produzidos a partir do projeto, usando um link de retorno semelhante a este:

  "Restpy: https://github.com/Marhc/restpy".

Para qualquer uso ou redistribuição do projeto, ou trabalhos produzidos a partir dele, você deve deixar bem claro qual foi a licença utilizada e manter intactos os avisos originais.

Este texto não é uma licença em si e seu conteúdo não faz parte da licença real.

Leia atentamente a licença completa [MIT](https://choosealicense.com/licenses/mit) para saber os termos exatos que se aplicam.

## Direitos Autorais

Por favor, preserve o aviso de direitos autorais ao usar ou redistribuir esse projeto:

"Copyright (c) 2019 Marcio Coutinho. Alguns direitos reservados."
