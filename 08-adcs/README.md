# VIII — Abusing AD CS

> **Ementa CRTP (seção VIII)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Learn about Active Directory Certificate Services and execute some of the most popular attacks.
- Execute attacks across Domain trusts to escalate privileges to Enterprise Admins.

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

- **CVE-2026-62818** — *AD CS RCE (use-after-free)*: 🔴 Critical 8.8, ago/2026 — o mais relevante para este módulo.
- **CVE-2026-54121** — *AD CS EoP*: Critical — escalada de privilégio no serviço de certificados.
- **CVE-2026-105590** — *AD CS Security Feature Bypass*: Important — Server 2016 em diante.
- **CertiGhost** — *Certificado indevido de DC*: Usuário de baixo privilégio obtém certificado de Domain Controller. *(número CVE não confirmado — verificar na fonte)*

---

## Glossário

| Termo | Definição |
|---|---|
| | |
