# Gerenciador de Eventos - Flask

Sistema completo para gerenciar eventos com autenticação de usuários.

## 🚀 Funcionalidades Implementadas

### ✅ Sistema de Usuários
- **Criar conta** - Registro com nome, email e senha
- **Login/Logout** - Autenticação segura
- **Proteção de rotas** - Páginas bloqueadas para usuários não logados

### ✅ Gerenciamento de Eventos
- **Criar eventos** - Formulário com nome, data e descrição
- **Listar eventos** - Dashboard mostra todos os eventos + eventos do usuário
- **Editar eventos** - Modificar nome, data e descrição
- **Deletar eventos** - Remover eventos com confirmação
- **Associação automática** - Eventos criados ficam ligados ao usuário logado

## 🛠️ Tecnologias Utilizadas
- Flask (framework web)
- SQLAlchemy (banco de dados)
- Flask-Login (autenticação)
- Flask-WTF (formulários)
- Bootstrap (interface)
- SQLite (banco de dados)

## 📦 Como executar

1. **Instalar dependências:**
```bash
pip install flask flask-wtf flask-sqlalchemy flask-login
```

2. **Criar banco de dados:**
```bash
python criar_banco.py
```

3. **Executar aplicação:**
```bash
python main.py
```

4. **Acessar:** http://localhost:5000

## 📁 Estrutura do Projeto
- `main.py` - Aplicação principal com todas as rotas
- `config.py` - Configurações do Flask
- `models.py` - Modelos do banco de dados (User, Evento)
- `formulario.py` - Formulários WTF
- `templates/` - Páginas HTML
- `criar_banco.py` - Script para criar banco

## 🎯 Rotas Disponíveis
- `/` - Página inicial
- `/register` - Criar conta
- `/login` - Fazer login
- `/logout` - Sair
- `/dashboard` - Painel principal (protegido)
- `/create_event` - Criar evento (protegido)
- `/edit_event/<id>` - Editar evento (protegido)
- `/delete_event/<id>` - Deletar evento (protegido)

---

## 👥 Alunos
- **Vitor Henrique Camillo** - RGM: 31382096
- **Hiro Alessandro Terato** - RGM: 29413711
