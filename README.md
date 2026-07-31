# Agenda Django

Este projeto é uma aplicação simples de agenda de contatos desenvolvida com Django. A ideia principal é permitir o cadastro, visualização e organização de contatos de forma prática, com suporte a categorias, imagens e controle de exibição.

## Objetivo

O sistema oferece uma interface básica para:
- listar contatos cadastrados;
- visualizar detalhes de um contato específico;
- organizar contatos por categoria;
- exibir ou ocultar contatos com base em um campo de controle;
- enviar e armazenar fotos dos contatos.

## Principais funcionalidades

- Cadastro de contatos com nome, sobrenome, telefone, e-mail e descrição;
- Associação de contatos a categorias;
- Upload de imagem para cada contato;
- Controle de visibilidade com o campo `show`;
- Página inicial com uma lista dos contatos ativos;
- Página de detalhes para cada contato;
- Administração do Django para gerenciar os dados.

## Estrutura do projeto

```text
projeto-agenda-django/
├── base_static/          # arquivos estáticos globais
├── base_templates/       # templates base compartilhados
├── contact/              # app principal da aplicação
│   ├── migrations/       # migrações do banco de dados
│   ├── templates/        # templates da app contact
│   ├── views/            # views da aplicação
│   ├── models.py         # modelos de Categoria e Contato
│   ├── urls.py           # rotas do app
│   └── admin.py          # configuração do admin
├── media/                # arquivos enviados pelo usuário
├── project/              # configuração do projeto Django
│   ├── settings.py       # configurações gerais
│   ├── urls.py           # rotas principais do projeto
│   └── local_settings.py # configurações locais
├── static/               # arquivos estáticos coletados
├── manage.py             # comando principal do Django
└── db.sqlite3            # banco de dados local
```

## Arquitetura básica

- `contact` é o app principal responsável pelos modelos, templates e views.
- `project` contém a configuração do projeto e o roteamento principal.
- `base_templates` e `base_static` armazenam elementos reutilizáveis na interface.
- `media` armazena imagens enviadas para os contatos.

## Como executar

1. Entre na pasta do projeto.
2. Ative o ambiente virtual, se estiver usando um.
3. Execute:

```bash
python manage.py migrate
python manage.py runserver
```

4. Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Administração

A área administrativa do Django pode ser acessada em:

```text
http://127.0.0.1:8000/admin/
```

Para utilizar o admin, é necessário criar um superusuário:

```bash
python manage.py createsuperuser
```

## Observações

Este projeto é um exemplo inicial de aplicação Django e pode ser expandido com funcionalidades como:
- autenticação de usuários;
- cadastro e edição de contatos via formulário web;
- busca e filtros;
- API REST.
