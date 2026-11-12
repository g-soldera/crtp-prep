# VI — Domain Persistence and Dominance

> **Ementa CRTP (seção VI)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Abuse Kerberos functionality to persist with DA privileges. Forge tickets to execute attacks like Golden ticket, Silver ticket and Diamond ticket to persist.
- Subvert the authentication on the domain level with Skeleton key and custom SSP.
- Abuse the DC safe mode Administrator for persistence.
- Abuse the protection mechanism like AdminSDHolder for persistence.
- Abuse minimal rights required for attacks like DCSync by modifying ACLs of domain objects.
- Learn to modify the host security descriptors of the domain controller to persist and execute commands without needing DA privileges.

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

- **CVE-2026-122164** — *Kerberos EoP (weak authentication)*: Persistência via autenticação Kerberos fraca — complementa Golden/Silver ticket.
- **CVE-2026-65777** — *AD Security Feature Bypass*: Bypass de controle de segurança do AD — o adversário que persiste quer exatamente isso.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
