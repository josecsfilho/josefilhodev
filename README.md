

# `Portfólio - José Filho`

Este é o meu portfólio pessoal, onde apresento meu trabalho e projetos relacionados à minha carreira como desenvolvedor de software. Aqui estão os detalhes do meu projeto e como configurá-lo localmente.

## Propósito

Este portfólio tem como objetivo:

- Apresentar meus projetos de desenvolvimento de software.
- Compartilhar informações sobre minha educação e experiência profissional.
- Fornecer uma visão geral das minhas habilidades e certificações.

## Ferramentas e Bibliotecas

Este projeto utiliza as seguintes ferramentas e bibliotecas:

- **Django**: Um framework web em Python para o desenvolvimento rápido de aplicativos web.

- **django-admin-logs**: Uma extensão que melhora o registro de atividades no painel de administração do Django.

- **django-jazzmin**: Um painel administrativo personalizado para o Django, que oferece uma experiência de administração mais avançada.

- **django-redis**: Uma biblioteca para integração com o Redis, um armazenamento em cache de alto desempenho.

- **psycopg2-binary**: Um adaptador de banco de dados PostgreSQL para Django.

- **sqlparse**: Uma biblioteca para análise de SQL em Python.

- **tzdata**: Dados de fuso horário para gerenciamento de datas e horas.

## Instalação

Siga as etapas abaixo para configurar o projeto em sua máquina local:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/josecsfilho/josefilhodev.git

Instale as dependências:

    
    pip install -r requirements.txt
Execute as migrações do banco de dados:


    python manage.py migrate
Crie um superusuário para acessar o painel de administração (opcional):


    python manage.py createsuperuser
Inicie o servidor de desenvolvimento:


    python manage.py runserver
Acesse o portfólio no seu navegador:

http://localhost:8000/

Uso
Neste portfólio, você encontrará informações sobre meus projetos, habilidades, experiência educacional e profissional. Fique à vontade para explorar e entrar em contato comigo caso tenha alguma pergunta ou oportunidade de colaboração.

Administração do Django
Para gerenciar os dados do portfólio, você pode usar o painel de administração do Django. Para acessá-lo, siga estas etapas:

Inicie o servidor de desenvolvimento (se ainda não estiver em execução):


    python manage.py runserver
Abra o navegador e acesse:

    http://localhost:8000/admin/

Faça login com as credenciais do superusuário criado anteriormente.

Agora você pode adicionar, editar e excluir projetos, habilidades, certificados, educação, experiências, etc., diretamente por meio do painel de administração.

Hospedagem e Domínio
Este portfólio está hospedado no Vercel, e o domínio "josefilho.tech" foi adquirido no Hostinger.

Hospedagem Vercel: `https://vercel.com/`
Domínio Hostinger: `https://www.hostinger.com.br/`
Configuração de Deploy
Para implantar este projeto no Vercel, você pode seguir o arquivo vercel.json fornecido no repositório. Certifique-se de adicionar os hosts corretos na configuração do Vercel para garantir que seu domínio personalizado funcione corretamente.

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.josefilho.tech/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josecsfilho/)
 
**Licença - Este projeto está licenciado.**