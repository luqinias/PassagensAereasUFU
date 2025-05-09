# PassagensAereasUFU

# 📚 API REST (API RESTful) - Sistema Gerenciador de Passagens Aéreas
Essa API, com uso do framework FastAPI, foi desenvolvida para tratar o backend de um sistema/site de reservas de passagens aéreas, estão implementadas tecnologias para:
CRUD em tabelas de Aeroportos, Passagens, Voos; Sessões de login com chave de sessão temporária (duração de 1h), permitindo validar, criar e encerrar. 
Além de reservas de passagens, com geração de e-tickets e localizador de acordo com a quantidade de passagens compradas.

Foram utilizados conceitos avançados de: Padrão APIs REST, Kubernetes(Minikube), Dockerfile, Containers, Rede, Deployments, Bancos de Dados(PostgreSQL), Linux.

# Requisitos
É necessário ter um sistema Linux instalado na máquina, ou terminal WSL, Ambiente de desenvolvimento de sua preferência, foi utilizado Visual Studio Code, instalações de tecnologias: Kubernetes (Minikube), Docker.
Conferir requirements.txt.

## Objetivos:
- Projeto final para a disciplina Arquitetura de Software Aplicada da Universidade Federal de Uberlândia;
- Estudar tecnologias citadas e aprofundá-las em sistemas diversos.

  
## Entregáveis:
   1. **Repositório GitHub:**
      - Repositório público contendo o código fonte e documentação.
   2. **Apresentação:**
      - Apresentação do Projeto, realizada no laboratório da instituição.
   3. **Documentação:**
      - README.md com instruções básicas sobre o projeto.



---

# Como subir a aplicação:
1. Inicializar o minikube, minikube start, no terminal Linux;
2. Verifique se o minikube foi inicialiado corretamente através do Docker ou o próprio terminal;
3. Abrir projeto com o ambiente de desenvolvimento;
4. Digitar o comando eval $(minikube docker-env) para alternar o local de construção das imagens;
5. Construir a imagem da aplicação a partir do Dockerfile dentro do ambiente Minikube;
6. Aplicar deployments e services .yaml:

   *sugiro seguir essa sequência*
- kubectl apply -f postgres-pv.yaml
- kubectl apply -f postgres-deployment.yaml
- kubectl apply -f postgres-service.yaml
  
importante citar que o banco de dados postgres:13 será usado dentro do ambiente VM criado, assim, completamente isolado, apesar de não ser a forma mais indicada, para estudos acadêmicos
é de importante experiência; lembre-se de verificar informações como: nome do banco de dados, usuário, senha e port a ser usada, para erros de conflitos.

- kubectl apply -f deployment.yaml
- kubectl apply -f service.yaml
  
    *Verifique se está tudo bem,* 
- kubectl get pods

7. Expor a porta;
- kubectl port-forward deployment/projeto-asa 5000:5000
  
8. Acesse com o seu navegador padrão.


---



🔗 **Conecte-se comigo:**
- [LinkedIn](https://www.linkedin.com/in/luc-aslira/)
  
🌐 **Contato:**
- Email institucional: luc.aslira@ufu.br
- Email pessoal: lucasbizil@gmail.com

---

### Lucas Lira
Estudante em Engenharia de Computação pela Universidade Federal de Uberlândia; 
Técnico de Informática.
Atualmente no meu tempo livre estudo e dedico para Vaga em Estágio Backend: Java, Python, RPA, SQL, FastAPI. 

