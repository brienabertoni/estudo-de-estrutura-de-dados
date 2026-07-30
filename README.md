# 🧩 Estrutura de Dados em Python — Exercícios Aplicados

Resoluções dos **30 exercícios de estrutura de dados** com foco no dia a dia de um(a) engenheiro(a) de software: logs, filas de mensagens, caches, dependências de deploy, rate limiting, arquitetura de microsserviços e mais.

Cada exercício simula um cenário real (não é um "LeetCode genérico") e é resolvido em **Python puro**, com a estrutura de dados apropriada justificada no processo.

---

## 🎯 Objetivo

Consolidar fundamentos de estrutura de dados — não só "decorando algoritmo", mas entendendo **por que** cada estrutura resolve melhor cada tipo de problema, com o raciocínio documentado exercício a exercício.

---

## 📁 Estrutura do repositório

```
.
├── facil/              # Exercícios 01–10 · listas, dicts, sets, pilhas e filas
│   ├── 01_ips_unicos.py
│   ├── 02_contar_status_http.py
│   └── ...
├── intermediario/       # Exercícios 11–20 · listas encadeadas, árvores, heaps, hashing
│   ├── 11_ciclo_tarefas.py
│   └── ...
├── dificil/             # Exercícios 21–30 · grafos, tries, Union-Find, Bloom Filter
│   ├── 21_ordem_migrations.py
│   └── ...
├── tests/                # Testes (assert / pytest) de cada solução
└── README.md
```

> 💡 Cada arquivo de exercício contém: o enunciado resumido em comentário, a solução, e a complexidade de tempo/espaço anotada ao final.

---

## ✅ Progresso

### Nível Fácil (1–10)
- [x] 01 — Deduplicar IPs suspeitos de um log de acesso
- [ ] 02 — Contar status codes de uma janela de requisições
- [ ] 03 — Validar chaves balanceadas em um arquivo de configuração
- [ ] 04 — Fila de processamento de tickets de suporte
- [ ] 05 — Segunda maior latência em uma lista de métricas
- [ ] 06 — Inverter o histórico de commits
- [ ] 07 — Comparar chaves entre dois arquivos de configuração
- [ ] 08 — Agrupar usuários por papel (role)
- [ ] 09 — Remover e-mails duplicados de uma lista de notificação
- [ ] 10 — Pilha de "undo" para um editor de configuração

### Nível Intermediário (11–20)
- [ ] 11 — Detectar ciclo em uma cadeia de tarefas dependentes
- [ ] 12 — Cache LRU para respostas de uma API externa
- [ ] 13 — Tabela hash própria para índice de sessões
- [ ] 14 — Ordenar deploys por timestamp com merge sort
- [ ] 15 — Busca binária em versões de API (semver)
- [ ] 16 — Fila de prioridade para triagem de alertas
- [ ] 17 — Achatar uma estrutura de permissões aninhada
- [ ] 18 — Árvore binária de busca para índice de usuários
- [ ] 19 — Detectar tickets duplicados por similaridade
- [ ] 20 — Rate limiter de janela fixa por usuário

### Nível Difícil — viável para jr (21–30)
- [ ] 21 — Ordem de execução de migrations com dependências
- [ ] 22 — Detectar dependência circular entre microsserviços
- [ ] 23 — Cache LFU para um serviço de recomendação
- [ ] 24 — Autocomplete de comandos para uma CLI interna
- [ ] 25 — Caminho mais curto entre serviços em uma arquitetura
- [ ] 26 — Rate limiter de janela deslizante
- [ ] 27 — Balanceador de carga round-robin ponderado
- [ ] 28 — Deduplicação aproximada de eventos em stream (Bloom Filter)
- [ ] 29 — Agrupar servidores em clusters de rede (Union-Find)
- [ ] 30 — Fila de mensagens com prioridade, retry e backoff

**Progresso geral:** 1 / 30 ✅

---

## 🧠 Estruturas de dados cobertas

`list` · `set` · `dict` · `deque` · pilha · fila · lista encadeada · árvore binária de busca · heap (`heapq`) · tabela hash própria · trie · grafo (BFS/DFS/topológica) · Union-Find · Bloom Filter

---

## ▶️ Como rodar

```bash
# Rodar um exercício específico
python3 facil/01_ips_unicos.py

# Rodar os testes (se estiver usando pytest)
pytest tests/
```

---

## 🛠️ Tecnologias

- Python 3
- `collections` (deque, defaultdict, Counter, OrderedDict)
- `heapq`
- `pytest` (testes)

---

## 👩‍💻 Sobre

Repositório de estudo mantido como parte da preparação para vagas júnior de **backend/segurança**, com foco em fundamentos sólidos de estrutura de dados aplicados a problemas reais de engenharia.
