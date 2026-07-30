# Exercício 01 — Deduplicar IPs Suspeitos de um Log de Acesso

## 📖 Contexto

Em ambientes corporativos, logs de autenticação podem conter milhares de registros repetidos provenientes de tentativas de acesso ao servidor. Antes de gerar relatórios ou alimentar ferramentas de monitoramento, é importante remover duplicatas para facilitar a análise.

Neste exercício, o objetivo é criar uma lista contendo apenas os IPs únicos, preservando a ordem da primeira ocorrência.

---

## 🎯 Objetivo

Receber uma lista de endereços IP contendo valores repetidos e retornar uma nova lista apenas com os IPs únicos, mantendo a ordem original em que apareceram.

---

## 📝 Exemplo

### Entrada

```text
[
  "192.168.1.10",
  "10.0.0.5",
  "192.168.1.10",
  "172.16.0.2",
  "10.0.0.5"
]
```

### Saída

```text
[
  "192.168.1.10",
  "10.0.0.5",
  "172.16.0.2"
]
```

---

## 🧠 Conceitos praticados

- Estrutura de Dados: **Set**
- Listas
- Busca eficiente
- Remoção de duplicatas
- Preservação da ordem dos elementos

---

## 💡 Estratégia

Durante o percurso da lista:

1. Verificar se o IP já foi encontrado.
2. Caso ainda não exista, adicioná-lo ao conjunto (`Set`) e à lista de resposta.
3. Caso já exista, ignorá-lo.

Como a busca em um `Set` possui complexidade média **O(1)**, a solução percorre a lista apenas uma vez.

---

## 📊 Complexidade

| Métrica | Complexidade |
|----------|--------------|
| Tempo | **O(n)** |
| Espaço | **O(n)** |

Onde **n** representa a quantidade de IPs na lista.

---

## 🛠 Estruturas utilizadas

- `Set` para controlar quais IPs já foram processados.
- `List` para armazenar o resultado preservando a ordem de inserção.

> Em Python, também seria possível utilizar `dict.fromkeys()` para obter o mesmo comportamento de forma concisa.

---

## 📂 Arquivos

```text
01-deduplicar-ips/
│
├── README.md
└── resolucao.py
```

---

## 🎓 Aprendizados

Este exercício demonstra como combinar duas estruturas de dados para obter eficiência e preservar a ordem dos elementos, um padrão muito utilizado em:

- análise de logs;
- processamento de eventos;
- SIEMs;
- ETL de dados;
- pipelines de segurança;
- eliminação de registros duplicados.

---

## 🚀 Próximos passos

Algumas evoluções possíveis para este exercício:

- considerar endereços IPv4 e IPv6;
- ordenar os IPs após a deduplicação;
- contar quantas vezes cada IP apareceu;
- identificar os IPs com maior número de tentativas de autenticação.