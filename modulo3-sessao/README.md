# Módulo 3 — Segurança na Camada de Aplicação

## Objetivo

Demonstração prática de **gestão de sessão e cookies**, abordando riscos de Session Hijacking e o papel do HTTPS na proteção de cookies durante a transmissão.

## Conceito Técnico

### O que é Cookie SessionID?
Um `SessionID` é um identificador único gerado pelo servidor após autenticação. É armazenado no navegador via cookie e enviado a cada requisição para manter o estado da sessão do usuário.

**Preocupações para desenvolvedores:**
- Gerar IDs com alta entropia (evitar valores previsíveis)
- Usar flags obrigatórias: `HttpOnly`, `Secure`, `SameSite`
- Definir tempo de expiração adequado
- Invalidar o cookie corretamente no logout
- Regenerar o SessionID após login (evitar session fixation)

### HTTPS vs HTTP para Cookies
Com **HTTPS**, os cookies trafegam dentro do túnel TLS — mesmo interceptados, são ilegíveis. Com **HTTP puro**, qualquer atacante na mesma rede pode capturar o `SessionID` em texto claro e assumir a sessão da vítima (Session Hijacking).

## Ferramenta Utilizada

> _Preencher com a ferramenta escolhida (ex: Flask, Django, Node.js/Express)_

## Estrutura da Demonstração

```
Ferramenta usada → Passo a Passo → Resultado → Explicação Técnica
```

Veja a implementação em [`poc.py`](./poc.py).

## Como Executar

```bash
pip install flask
python poc.py
```

## Resultado Esperado

> _Descrever/inserir print do resultado após implementação_
