# Módulo 1 — Sniffing e Interceptação (Camada 2 e 3)

## Objetivo

Demonstração prática de captura de pacotes e funcionamento do **modo promíscuo** (promiscuous mode) em interfaces de rede, abordando o comportamento do controlador de interface de rede (NIC) nas camadas 2 e 3 do modelo OSI.

## Conceito Técnico

Em operação normal, uma NIC descarta quadros Ethernet cujo MAC de destino não corresponde ao seu próprio. No **modo promíscuo**, esse filtro é desativado: a interface repassa todos os quadros recebidos para a pilha de rede, permitindo capturar tráfego destinado a outros hosts — base do funcionamento de ferramentas como Wireshark e tcpdump.

## Ferramenta Utilizada

> _Preencher com a ferramenta escolhida pela equipe (ex: Scapy, Wireshark, tcpdump)_

## Estrutura da Demonstração

```
Ferramenta usada → Passo a Passo → Resultado → Explicação Técnica
```

Veja a implementação em [`poc.py`](./poc.py).

## Como Executar

```bash
# Requer privilégios de administrador/root
sudo python poc.py
```

## Resultado Esperado

> _Descrever/inserir print do resultado após implementação_
