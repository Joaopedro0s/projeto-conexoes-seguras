# Projeto: Conexões Seguras

Projeto semestral da Faculdade de Tecnologia SENAI Felix Guisard — Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas.

## Descrição

Documentação técnica e implementação prática dos principais mecanismos de segurança em redes corporativas, dividida em 4 módulos:

| Módulo | Tema |
|--------|------|
| [Módulo 1 — Sniffing e Interceptação](./modulo1-sniffing/README.md) | Modo promíscuo e captura de pacotes (Camadas 2 e 3) |
| [Módulo 2 — Criptografia e Handshake TLS](./modulo2-tls/README.md) | Criptografia híbrida, base do TLS/HTTPS |
| [Módulo 3 — Segurança na Camada de Aplicação](./modulo3-sessao/README.md) | Gestão de sessão, cookies e proteção via HTTPS |
| [Módulo 4 — VPN](./modulo4-vpn/README.md) | Túneis seguros e redes privadas virtuais |

## Documentação

A documentação completa está disponível via **GitHub Pages**:
> `https://joaopedro0s.github.io/projeto-conexoes-seguras/`

## Estrutura do Repositório

```
projeto-conexoes-seguras/
├── modulo1-sniffing/   # PoC de sniffing e modo promíscuo
├── modulo2-tls/        # PoC de handshake TLS e criptografia híbrida
├── modulo3-sessao/     # PoC de gestão de sessão e cookies
├── modulo4-vpn/        # PoC de VPN + pasta de evidências
├── relatorio.pdf       # Relatório técnico final (máx. 5 páginas)
└── README.md
```

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Joaopedro0s/projeto-conexoes-seguras.git
   ```
2. Acesse a pasta do módulo desejado e leia o `README.md` do módulo.
3. Execute a PoC correspondente:
   ```bash
   cd modulo1-sniffing
   python poc.py
   ```

## Equipe

|  | Nome |
|------|----|
| Integrante 1 | Ana Carolina Gonçalves |
| Integrante 2 | João Pedro Fonseca Alves de Carvalho |
| Integrante 3 | Pedro de Lima Cavalcanti |

## Licença

Projeto acadêmico — SENAI Felix Guisard.
