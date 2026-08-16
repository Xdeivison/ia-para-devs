---
name: dockerize
description: Containerize uma aplicação de forma mínima, reproduzível e não privilegiada.
---

# Dockerize Application

1. Detecte runtime, porta, comando e dependências.
2. Crie `.dockerignore`.
3. Prefira imagem base mínima e versão explícita.
4. Execute como usuário não root sempre que possível.
5. Separe build e runtime quando isso reduzir superfície e tamanho.
6. Nunca copie `.env`, chaves ou credenciais para a imagem.
7. Adicione healthcheck quando fizer sentido.
8. Valide build e inicialização local.
