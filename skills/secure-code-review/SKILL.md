---
name: secure-code-review
description: Revise alterações de código procurando bugs, regressões, riscos de segurança e testes ausentes.
---

# Secure Code Review

## Quando usar
Use quando houver um diff, PR ou conjunto delimitado de arquivos para revisão.

## Processo
1. Entenda a intenção da mudança.
2. Examine o diff antes de sugerir reescritas amplas.
3. Classifique achados por severidade e evidência.
4. Procure autenticação quebrada, autorização ausente, injeção, exposição de segredo, path traversal e validação insuficiente.
5. Procure regressões funcionais e testes ausentes.
6. Cite arquivo e trecho afetado.

## Saída
- Achados bloqueantes.
- Achados importantes.
- Sugestões não bloqueantes.
- Testes recomendados.
