# Ementa CRTP → Pastas do repo

> **Fonte:** https://www.alteredsecurity.com/adlab → "What will you learn?"
> Ementa espelhada em `refs/CRTP-ementa.md` — 13 seções, 45 objetivos de aprendizado.
> Cada seção da ementa tem exatamente uma pasta aqui.

## Pré-requisito

| Pasta | Seção da ementa | Conteúdo |
|---|---|---|
| `00-fundamentos/` | *(não é seção da prova)* | Domain, forest, trust, Kerberos vs NTLM, ACL/ACE, SID, GPO |

## Seções da ementa (I–XIII)

| # | Seção (ementa) | Pasta | Camada do lab |
|---|---|---|---|
| I | Active Directory Enumeration | `01-enum/` | vulnerável |
| II | Offensive PowerShell Tradecraft | `02-powershell/` | defesa (AMSI/CLM/Transcription) |
| III | Offensive .NET Tradecraft | `03-dotnet/` | defesa (Defender/MDE) |
| IV | Local Privilege Escalation | `04-local-privesc/` | vulnerável |
| V | Domain Privilege Escalation | `05-domain-privesc/` | vulnerável |
| VI | Domain Persistence and Dominance | `06-persistence/` | vulnerável |
| VII | Cross Trust Attacks | `07-cross-trust/` | vulnerável *(exige child domain)* |
| VIII | Abusing AD CS | `08-adcs/` | vulnerável *(exige role AD CS)* |
| IX | Defenses and bypass – MDE EDR | `09-bypass-mde/` | defesa |
| X | Defenses and bypass – MDI | `10-bypass-mdi/` | defesa |
| XI | Architecture and Work Culture Changes | `11-architecture/` | defesa |
| XII | Defenses – Monitoring | `12-monitoring/` | defesa |
| XIII | Defenses and Bypass – Deception | `13-deception/` | defesa |

> **Nota sobre Lateral Movement:** a ementa **não tem seção própria** —
> movimentação lateral vive dentro da **seção V** ("using built-in protocols for
> pivoting", credential replay, abuso de local admin derivado). Estudamos isso
> em `05-domain-privesc/`.

## Onde cada seção exige infraestrutura extra

| Seção | Pré-requisito no lab |
|---|---|
| VII — Cross Trust | VM `CHILDDC` com domínio `child.lab.local` — **criar ao entrar no módulo 07** |
| VIII — AD CS | Role **AD CS** instalada no DC01 + template vulnerável |
| IX — MDE | Trial Microsoft Defender for Endpoint |
| X — MDI | Trial Microsoft Defender for Identity |
| II/III — Bypass | Defender ativo no WS01 |

## Fluxo por tópico

`Criar defesa → Entender defesa → Atacar → Entender ataque → Documentar`

Ver `AGENTS.md` para a regra completa: **o aluno explica, o assistente registra.**
