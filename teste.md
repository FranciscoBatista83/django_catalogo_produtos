# 📦 Catálogo de Produtos Online - Django

![Django](https://img.shields.io/badge/Django-3.2-green) ![Python](https://img.shields.io/badge/Python-3.12-blue) ![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

---

## 📖 Sobre o Projeto

Este projeto é um sistema web desenvolvido com Django para cadastro, gerenciamento e exibição de produtos em um catálogo online. Ideal para quem deseja aprender ou implementar funcionalidades básicas de um CRUD (Create, Read, Update, Delete) em Django, com boa organização de código e boas práticas.

---

## 🚀 Funcionalidades

- Cadastro de produtos com nome, descrição, preço e data de cadastro automática.
- Listagem de produtos para visualização dos dados.
- Administração completa via Django Admin.
- Formulário web para adicionar novos produtos.
- Estrutura modular com separação clara entre models, views, templates e URLs.
- Controle de versão com Git integrado.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Django 5.x
- SQLite (banco de dados)
- HTML/CSS para templates
- Git para versionamento

---

## 🎯 Objetivo do Projeto

Fornecer uma aplicação prática para aprender Django, focando em:

- Estruturação do projeto e apps.
- Modelagem de banco de dados com models.
- Criação e aplicação de migrações.
- Construção de views e templates.
- Gerenciamento de rotas.
- Utilização do Django Admin para controle administrativo.

---

## 📁 Estrutura do Projeto

```plaintext
projeto-catalogo-de-produtos-online/
│
├── django_catalogo_produtos/       # Configurações do projeto Django
├── produtos/                      # App para gerenciamento dos produtos
│   ├── migrations/                # Migrações do banco
│   ├── templates/                 # Templates HTML
│   │   └── produtos/
│   │       ├── lista_produtos.html
│   │       └── criar_produto.html
│   ├── admin.py                   # Registro do model no admin
│   ├── forms.py                   # Formulários Django
│   ├── models.py                  # Models do banco de dados
│   ├── urls.py                   # URLs do app
│   └── views.py                  # Lógica das views
├── db.sqlite3                    # Banco SQLite
├── manage.py                    # Gerenciador de comandos Django
└── README.md                    # Documentação do projeto
🚀 Como Executar
Pré-requisitos
Python 3.12 instalado

Git instalado (opcional para clonar o projeto)

Passos para rodar localmente
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/projeto-catalogo-de-produtos-online.git
cd projeto-catalogo-de-produtos-online
Crie e ative um ambiente virtual (recomendado):

bash
Copiar
Editar
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
Instale as dependências (Django):

bash
Copiar
Editar
pip install django
Aplique as migrações para criar o banco:

bash
Copiar
Editar
python manage.py migrate
Crie um superusuário para acessar o Django Admin:

bash
Copiar
Editar
python manage.py createsuperuser
Inicie o servidor de desenvolvimento:

bash
Copiar
Editar
python manage.py runserver
Acesse no navegador:

Lista de produtos: http://127.0.0.1:8000/produtos/

Django Admin: http://127.0.0.1:8000/admin/

📝 Uso
Na página /produtos/ é possível visualizar todos os produtos cadastrados.

Em /produtos/novo/ é possível adicionar novos produtos via formulário web.

No Django Admin, gerencie produtos de forma avançada (edição, exclusão, listagem).

🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:

Fork este repositório.

Crie uma branch com sua feature (git checkout -b feature/nova-funcionalidade).

Commit suas alterações (git commit -m 'Adiciona nova funcionalidade').

Push para a branch (git push origin feature/nova-funcionalidade).

Abra um Pull Request.