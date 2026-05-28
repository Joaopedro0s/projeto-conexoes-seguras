# Módulo 2 — Criptografia e Handshake TLS

## Objetivo

Demonstração prática da **criptografia híbrida** que fundamenta o HTTPS: uso de RSA/ECC para troca segura de chaves e AES para a transferência de dados.

## Conceito Técnico

A criptografia assimétrica é computacionalmente cara para volumes grandes de dados. Por isso, o TLS usa RSA/ECC apenas para trocar com segurança uma **chave de sessão** temporária; toda a comunicação subsequente é cifrada com AES, que é ordens de grandeza mais eficiente.

**Fluxo simplificado do handshake TLS:**
1. Cliente solicita chave pública do servidor.
2. Servidor envia certificado com a chave pública.
3. Cliente gera chave de sessão (AES) e a envia cifrada com a chave pública do servidor.
4. Servidor decifra com sua chave privada — ambos agora compartilham a chave AES.
5. Toda a comunicação passa a ser cifrada simetricamente com AES.

## Ferramenta Utilizada

> _Preencher com a ferramenta escolhida (ex: biblioteca `cryptography`, OpenSSL)_

## Estrutura da Demonstração

```
Ferramenta usada → Passo a Passo → Resultado → Explicação Técnica
```

Veja a implementação em [`poc.py`](./poc.py).

## Como Executar

```bash
pip install cryptography
python poc.py
```

## Resultado Esperado

> _Descrever/inserir print do resultado após implementação_
