# Vendas Interativo (Django)

O **Vendas Interativo** é um sistema web desenvolvido em Django (Python) que permite gerenciar vendas e produtos, com uma interface simples e um gráfico interativo feito com Chart.js.

Ele pode ser usado por pequenas empresas, lojas ou qualquer pessoa que queira registrar suas vendas e visualizar resultados em tempo real.

---

## O que o site faz

### 1. Cadastra produtos

O usuário (via painel admin ou formulário) pode criar produtos que serão vendidos.

Exemplos:
- Notebook Dell
- Mouse sem fio
- Teclado mecânico

Esses produtos ficam salvos no banco de dados.

### 2. Registra vendas

O site permite registrar novas vendas informando:

- Data da venda
- Produto vendido
- Quantidade
- Preço unitário

Cada venda é salva no banco (db.sqlite3) e vinculada a um produto.

### 3. Lista todas as vendas em uma tabela

Na página principal (`/`), o sistema mostra uma tabela interativa com:

| Data       | Produto  | Quantidade | Preço  | Total da venda  |
|------------|----------|------------|--------|-----------------|
| 2025-10-10 | Mouse    | 3          | 80.00  | 240.00          |
| 2025-10-15 | Teclado  | 2          | 120.00 | 240.00          |

### 4. Filtros de pesquisa

Na parte superior da página, o usuário pode filtrar as vendas por:

- Data inicial e final
- Nome do produto

Exemplo:  
Mostrar apenas as vendas de “Notebook” entre 01/10/2025 e 20/10/2025.

O site atualiza automaticamente os resultados conforme o filtro.

### 5. Gráfico interativo (Chart.js)

Abaixo da tabela, o sistema exibe um gráfico de barras mostrando:

- Cada produto
- Total de unidades vendidas

Exemplo:

| Produto   | Unidades Vendidas |
|-----------|-------------------|
| Mouse     | 30                |
| Teclado   | 20                |
| Notebook  | 10                |

O gráfico é gerado em tempo real a partir dos dados do banco de dados e renderizado pelo Chart.js.

### 6. Painel administrativo (Admin Django)

O site também possui uma área administrativa em:


Lá o administrador pode:

- Gerenciar Produtos
- Gerenciar Vendas
- Criar, editar ou excluir registros
- Cadastrar novos usuários com permissões

---

## Como funciona por dentro

### Backend (Python/Django)

O Django faz toda a parte lógica e de banco de dados.

As tabelas principais são:

- `Product` (produtos)
- `Sale` (vendas)

Quando o usuário acessa o site, o Django busca os dados do banco, processa os filtros e envia tudo para o template.

### Frontend (HTML + Chart.js)

Os templates HTML (em `/templates/sales/`) são renderizados pelo Django.

O Chart.js (incluso via CDN) cria os gráficos dinâmicos direto no navegador.

### Banco de dados

O projeto usa SQLite, que já vem embutido no Python.

O banco se chama `db.sqlite3`.

Armazena todas as informações de:

- Produtos
- Vendas
- Usuários (admin e comuns)

### Usuários e autenticação

Para acessar o painel admin, é preciso um usuário superuser, criado via comando:

```bash
python manage.py createsuperuser
