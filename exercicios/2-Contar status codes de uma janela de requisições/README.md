# Exercício #02 — Contar status codes de uma janela de requisições

**Nível:** Fácil

## Cenário
O time de observabilidade quer saber, a cada janela de tempo, quantas requisições retornaram cada código de status HTTP (200, 404, 500...), para alimentar um dashboard de monitoramento.

## Entrada
```python
status_codes = [200, 200, 404, 500, 200, 404, 200, 500, 500, 500]
```

## Tarefa
Implementar `contar_status(status_codes)`, que recebe uma lista de status codes e retorna um dicionário `{status: quantidade}`.

## Saída esperada
```python
{200: 4, 404: 2, 500: 4}
```

## Estrutura utilizada
Dicionário como contador — para cada status, verifica se a chave já existe (inicializa com `0` se não) e incrementa em `1`.

## Aprendizados
- Reaplicação do padrão "dicionário-contador" (mesmo usado no exercício bônus de tentativas de login)
- Diferença entre percorrer a lista de entrada vs. o dicionário que está sendo construído