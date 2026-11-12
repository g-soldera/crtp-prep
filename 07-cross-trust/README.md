# VII — Cross Trust Attacks

> **Ementa CRTP (seção VII)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Learn to elevate privileges from Domain Admin of a child domain to Enterprise Admin on the forest root by abusing Trust keys and krbtgt account.
- Execute intra-forest trust attacks to access resources across forest.
- Abuse SQL Server database links to achieve code execution across forest by just using the databases.

---

## Fluxo de estudo

```
Criar defesa → Entender defesa → Atacar → Entender ataque → Documentar
```

O aluno explica com as próprias palavras **antes** de o conteúdo ser gravado aqui.

---

## Prática no lab

| Item | Estado |
|---|---|
| Guardrail criado | ⏳ pendente |
| Ataque executado | ⏳ pendente |
| Explicado pelo aluno | ⏳ pendente |

## Comandos e saídas reais

*(preencher durante a prática — colar comando + output real, não exemplo inventado)*

## O que aprendi

*(o aluno escreve aqui, com as próprias palavras)*

---

## Vulnerabilidades relacionadas (2026)

> Detalhes e fontes em [`../refs/vulnerabilidades-2026.md`](../refs/vulnerabilidades-2026.md)

- **CVE-2026-65674** — *SQL Server deserialization RCE*: 🔴 ZDI apontou como **o mais explorável do mês** (out/2026). Interliga direto com o objetivo "SQL database links" da ementa.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
