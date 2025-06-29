# ✅ Checklist Diário – Projeto Django: Catálogo de Produtos Online

Ambiente: VS Code, Git, GitHub, Google Chrome

---

## 📍 Semana 1 – Estrutura Inicial + Listagem de Produtos

- [x] Criei o projeto Django no VS Code
- [x] Inicializei o repositório Git local com `git init`
- [x] Fiz o primeiro commit (`git add .` / `git commit`)
- [x] Criei o app `produtos`
- [x] Configurei o banco SQLite

- [x] Modelei a tabela `Produto` com os campos: Nome, Descrição, Preço, Data
- [x] Fiz as migrações iniciais (`makemigrations` e `migrate`)
- [x] Fiz um commit com essa etapa

- [x] Cadastrei pelo menos 3 produtos no Django Admin
- [x] Testei o Django Admin no Chrome (`http://127.0.0.1:8000/admin`)
- [x] Fiz commit

- [x] Criei a view para listar os produtos
- [x] Configurei a URL para a listagem
- [x] Fiz commit

- [ ] Criei o template HTML para exibir a lista de produtos
- [ ] Testei no navegador Chrome
- [ ] Fiz commit
- [ ] Subi o projeto para o GitHub (`git remote add` + `git push`)

---

## 📍 Semana 2 – CRUD Completo + Categorias

- [ ] Criei o formulário para adicionar novos produtos (Create)
- [ ] Testei o cadastro no Chrome
- [ ] Fiz commit e push

- [ ] Criei a página de detalhes para cada produto
- [ ] Testei a navegação entre listagem e detalhe
- [ ] Fiz commit

- [ ] Implementei a edição (Update) de produtos
- [ ] Implementei a exclusão (Delete) de produtos
- [ ] Testei no navegador
- [ ] Fiz commit e push

- [ ] Criei o modelo `Categoria`
- [ ] Relacionei produtos a categorias (ForeignKey)
- [ ] Fiz migração e commit

- [ ] Implementei o filtro por categoria na listagem
- [ ] Testei os filtros no Chrome
- [ ] Dei um tapa no layout com Bootstrap ou Tailwind
- [ ] Fiz commit e push

---

## 📍 Semana 3 – Sistema de Usuários + Área Restrita

- [ ] Criei o sistema de cadastro de usuários (UserCreationForm)
- [ ] Testei o cadastro no Chrome
- [ ] Fiz commit

- [ ] Implementei login e logout
- [ ] Testei o fluxo de autenticação no Chrome
- [ ] Fiz commit

- [ ] Protegi as views de criar, editar e excluir produtos usando `@login_required`
- [ ] Testei com usuário logado e deslogado
- [ ] Fiz commit e push

- [ ] Relacionei cada produto ao usuário criador (campo `ForeignKey` para `User`)
- [ ] Testei se cada usuário só vê os próprios produtos
- [ ] Fiz commit

- [ ] Criei um dashboard simples com o resumo de produtos do usuário
- [ ] Melhorei o layout do dashboard
- [ ] Testei no Chrome
- [ ] Fiz commit e push

---

## 📍 Semana 4 – Upload de Imagens + Deploy

- [ ] Adicionei um campo de imagem ao modelo `Produto`
- [ ] Configurei o `MEDIA_ROOT` e `MEDIA_URL`
- [ ] Fiz commit

- [ ] Ajustei os templates para exibir as imagens nas listagens e nos detalhes
- [ ] Testei upload e exibição no Chrome
- [ ] Fiz commit e push

- [ ] Testei todo o sistema de upload (criar, editar e visualizar com imagem)
- [ ] Fiz commit

- [ ] Ajustei `settings.py`, banco de dados, static e media files para produção
- [ ] Fiz o commit final antes do deploy

- [ ] Fiz o deploy no PythonAnywhere, Railway ou Render
- [ ] Testei o site online no Chrome
- [ ] Fiz o commit final (caso tenha ajustes pós-deploy)

---

✅ **Dicas extras:**

- Crie um `README.md` no GitHub explicando o projeto
- Adicione um `.gitignore` específico para Django
- Se quiser: trabalhe em branch `dev` e depois faça `merge` pra `main`
