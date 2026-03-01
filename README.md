# Voz de Todos

Aplicação web para interação professor–aluno com **perguntas em tempo real** e **registro de respostas** para acompanhamento pedagógico.

> Projeto Integrador (PI) — UNIVESP  
> Comunidade externa: Instituto Federal de São Paulo (IFSP)

## Contexto e Problema

Em aulas presenciais, é comum que apenas 1–3 alunos respondam às perguntas feitas pelo professor, enquanto parte significativa da turma permanece silenciosa por timidez, receio de errar ou pela dinâmica do tempo. Métodos tradicionais para coletar respostas de todos (papel, chamada oral, discussões longas) são lentos e dificultam decisões imediatas do docente durante a aula.

**O projeto busca um meio simples e rápido de coletar respostas de toda a turma em tempo real**, com visualização imediata e histórico para análise posterior.

## Objetivo

Desenvolver e validar um **protótipo funcional** de aplicação web que permita ao professor:
- criar e publicar perguntas em tempo real para a turma;
- permitir que alunos respondam via celular;
- apresentar resultados consolidados imediatamente (inclusive para projeção);
- registrar respostas em banco de dados para consulta e análise posteriores.

## Escopo (MVP)

O MVP contempla:
1. Criação de turma/sessão
2. Publicação de pergunta (múltipla escolha e/ou resposta curta)
3. Resposta do aluno via interface mobile (web responsivo)
4. Painel do professor com resultados ao vivo (contagens/percentuais e/ou lista)
5. Persistência e consulta básica do histórico por turma/sessão/pergunta

## Stack (a definir)

- Frontend: _(ex.: React/Vite | HTML/CSS/JS)_
- Backend: _(ex.: Node/Express | Python/FastAPI)_
- Banco de dados: _(ex.: SQLite/PostgreSQL)_
- Tempo real: _(ex.: WebSocket/SSE)_

> Observação: a stack final será registrada em `docs/02-arquitetura.md`.

## Como rodar (placeholder)

> Esta seção será atualizada quando o MVP tiver a stack definida.

1. Clonar o repositório
2. Instalar dependências
3. Subir backend e frontend
4. Acessar:
   - Professor: `/teacher`
   - Aluno: `/student`

## Documentação

- Visão geral: `docs/00-visao-geral.md`
- Requisitos e user stories: `docs/01-requisitos.md`
- Arquitetura e decisões: `docs/02-arquitetura.md`
- Modelo de dados: `docs/03-banco-de-dados.md`
- Critérios de sucesso: `docs/04-criterios-sucesso.md`
- Plano de ação (quinzenas): `docs/05-plano-de-acao.md`

## Organização do Trabalho

- Branch principal: `main` (protegida)
- Features: `feat/<descricao-curta>`
- Correções: `fix/<descricao-curta>`
- Docs: `docs/<descricao-curta>`
- Pull requests obrigatórios para merge em `main`

Veja detalhes em `CONTRIBUTING.md`.

## Integrantes

- Helio Fernando Gomes Maziviero
- Jean Carlos Azevedo de Godoy
- Luis Fernando Macacari
- Rafael da Silva Nunes
- Raphael Guedes Frois
- Renato Bincoletto
- Richard Avante
- Rodrigo Cesar Pereira Martins

## Licença

Este projeto está sob a licença MIT. Veja `LICENSE`.
