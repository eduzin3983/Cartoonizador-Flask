# 🖼️ Cartoonizador de Imagens com Flask + OpenCV

Este projeto é uma aplicação web que permite aos usuários:  
- Fazer upload de uma imagem 📤  
- Gerar uma versão cartoonizada em preto e branco 🖌️  
- Visualizar uma galeria de imagens enviadas 🖼️  
- Acessar detalhes de cada imagem (data, URLs, etc.)

---

## 📚 Projeto Prático — *Introdução à Nuvem*  
**AiotLab — PUC-Campinas**

Este projeto foi desenvolvido como parte prática do curso **"Introdução à Nuvem"**, oferecido pela **AiotLab / PUC-Campinas** 🎓.

Além disso, este projeto serviu como uma oportunidade prática para **desenvolver e implementar APIs REST com Flask**, bem como para **hospedar a aplicação na nuvem**. As principais práticas abordadas incluem:

- Upload de arquivos via requisições POST  
- Redirecionamento com mensagens flash para feedback ao usuário  
- Configuração de rotas com parâmetros dinâmicos para maior flexibilidade  
- Retorno de arquivos estáticos e páginas HTML renderizadas dinamicamente  
- Integração e execução em ambientes de nuvem para escalabilidade e acessibilidade  

---

## 🚀 Funcionalidades

✅ Upload de imagens (.jpg, .png, .jpeg...)  
✅ Detecção automática de nomes duplicados  
✅ Aplicação de filtro estilo cartoon em preto e branco  
✅ Visualização em galeria  
✅ Detalhes individuais para cada imagem  
✅ Registro de dados
✅ Layout responsivo com fundo animado (vídeo)

---

## 🌐 Rotas da Aplicação

| Rota                    | Método | Função                                                               |
|-------------------------|--------|----------------------------------------------------------------------|
| `/`                     | GET    | Página inicial com formulário de upload                             |
| `/upload`               | POST   | Recebe a imagem, processa, salva e redireciona com mensagem flash   |
| `/imagens`              | GET    | Exibe uma galeria de imagens enviadas                               |
| `/image/<filename>`     | GET    | Página de detalhes da imagem original e cartoonizada                |
| `/uploads/<filename>`   | GET    | Serve a imagem original diretamente                                 |
| `/cartooned/<filename>` | GET    | Serve a imagem cartoonizada diretamente                             |

---

## 🛠️ Como Executar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/your-username/cartoonizer-flask.git
cd cartoonizer-flask
```
```bash
# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
```

```bash
# 3. Instale as dependências
pip install -r requirements.txt
```
```bash
# 4. Inicie o servidor
python app.py
```

```bash
# 5. Acesse no navegador:
http://localhost:5000
```

---

## 🧪 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- HTML5, CSS3, JavaScript
- Banco de dados SQLite local

---

## 📂 Estrutura do Projeto

```
.  
├── app.py                  # Arquivo principal da aplicação  
├── database.db             # Banco de dados SQLite  
├── uploads/                # Imagens originais  
├── cartooned/              # Imagens cartoonizadas  
├── static/                 # Arquivos estáticos  
│   ├── style.css           # Estilos CSS  
│   └── fundo/              # Recursos de fundo  
├── templates/              # Templates HTML  
│   ├── index.html          # Página inicial  
│   ├── galeria.html        # Página da galeria  
│   └── detalhe_imagem.html # Página de detalhes da imagem  
└── README.md               # Documentação do projeto
```

---

## 📸 Interface

- Página inicial com botão de upload
- Galeria de imagens com botão "Ver imagem processada"
- Página de detalhes com imagem original, imagem cartoonizada e metadados

---

## 📬 Contato

Para dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato.  
Se quiser contribuir, será muito bem-vindo! 🤝