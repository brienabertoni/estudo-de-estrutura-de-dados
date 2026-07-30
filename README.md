# 40 Problemas de Engenharia de Software

Resoluções pessoais dos 40 desafios práticos de engenharia de software, baseados em situações reais do dia a dia (bugs, arquitetura, banco de dados, testes, APIs, DevOps, segurança e boas práticas).

Estudando 1 exercício por dia, com foco em entender o problema antes de sair codando.

## Como está organizado

Cada problema tem sua própria pasta, numerada, com:

```
01-deteccao-ciclos-grafo/
├── README.md        # contexto, desafio e anotações do meu processo
└── solucao.*         # código da solução
```

O `README.md` de cada pasta traz: o problema original, minhas anotações de raciocínio, decisões tomadas e o que eu pesquisei/aprendi no caminho — o objetivo é documentar o processo, não só entregar a resposta final.

## Progresso

### Lógica & Algoritmos
- [ ] 01 (Pleno) — Detecção de ciclos em grafo
- [ ] 02 (Pleno) — Rate limiter com janela deslizante
- [ ] 03 (Júnior) — Retry com backoff exponencial
- [ ] 04 (Júnior) — Compressão de logs (RLE)

### Debug & Troubleshooting
- [ ] 05 (Pleno) — Memory leak em aplicação Node.js
- [ ] 06 (Pleno) — Condição de corrida em endpoint de pagamento
- [ ] 07 (Júnior) — N+1 Query Problem
- [ ] 08 (Pleno) — Deadlock entre duas transações
- [ ] 09 (Júnior) — Erro silencioso em pipeline assíncrono
- [ ] 10 (Júnior) — Vazamento de credenciais via variável de ambiente

### Arquitetura de Software
- [ ] 11 (Pleno) — Refatoração: monolito para módulos
- [ ] 12 (Pleno) — Circuit Breaker
- [ ] 13 (Pleno) — Design de API RESTful versionada
- [ ] 14 (Pleno) — Event Sourcing simples
- [ ] 15 (Pleno) — Cache com invalidação inteligente
- [ ] 16 (Pleno) — Padrão Saga para transações distribuídas

### Banco de Dados
- [ ] 17 (Pleno) — Modelagem de hierarquia de categorias
- [ ] 18 (Pleno) — Migração de banco sem downtime
- [ ] 19 (Pleno) — Índices compostos e cobertura de queries
- [ ] 20 (Júnior) — Soft delete com auditoria

### Testes & Qualidade
- [ ] 21 (Pleno) — Testes de integração com banco real
- [ ] 22 (Pleno) — Contract testing (produtor/consumidor)
- [ ] 23 (Pleno) — Teste de carga com identificação de gargalo
- [ ] 24 (Júnior) — TDD em cálculo de frete

### APIs & Integrações
- [ ] 25 (Pleno) — Webhook com garantia de entrega
- [ ] 26 (Pleno) — OAuth2 com refresh token
- [ ] 27 (Pleno) — Integração com API de terceiros instável
- [ ] 28 (Pleno) — GraphQL com N+1 resolvido via DataLoader

### DevOps & Infraestrutura
- [ ] 29 (Júnior) — Dockerização com multi-stage build
- [ ] 30 (Pleno) — Pipeline CI/CD com deploy blue-green
- [ ] 31 (Pleno) — Observabilidade: logs, métricas e traces
- [ ] 32 (Pleno) — Health checks e graceful shutdown

### Segurança
- [ ] 33 (Júnior) — Prevenção de SQL Injection
- [ ] 34 (Pleno) — RBAC (autorização baseada em papéis)
- [ ] 35 (Júnior) — Proteção contra ataques de enumeração

### Boas Práticas & Código Limpo
- [ ] 36 (Júnior) — Refatoração de code smells
- [ ] 37 (Pleno) — DDD tático
- [ ] 38 (Pleno) — Feature flags com controle granular
- [ ] 39 (Júnior) — Documentação viva com OpenAPI
- [ ] 40 (Júnior/Pleno) — Revisão de Pull Request

## Método de estudo

1. Ler o contexto e o desafio, sem consultar solução pronta
2. Tentar resolver sozinha (~30-40min), pesquisando o que for necessário
3. Comparar com abordagens da comunidade / discutir alternativas
4. Documentar decisões e aprendizados no README da pasta

## Stack

Linguagem livre por exercício — priorizando a ferramenta mais adequada ao problema (ex: SQL puro para os de banco, Docker para os de DevOps).

---

Lista original: *40 Problemas de Engenharia de Software para Programadores Júnior e Pleno*
