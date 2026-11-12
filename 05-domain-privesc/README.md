# V — Domain Privilege Escalation

> **Ementa CRTP (seção V)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Learn to find credentials and sessions of high privileges domain accounts like Domain Administrators, extracting their credentials and then using credential replay attacks to escalate privileges, all of this with just using built-in protocols for pivoting.
- Learn to extract credentials from a restricted environment where application whitelisting is enforced. Abuse derivative local admin privileges and pivot to other machines to escalate privileges to domain level.
- Understand the classic Kerberoast and its variants to escalate privileges.
- Enumerate the domain for objects with unconstrained delegation and abuse it to escalate privileges.
- Find domain objects with constrained delegation enabled. Understand and execute the attacks against such objects to escalate privileges to a single service on a machine and to the domain administrator using alternate tickets.
- Learn how to abuse privileges of Protected Groups to escalate privileges

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

- **CVE-2026-27912** — *ResetNightmare*: 🔴 **O mais importante.** UPN igual ao `SamAccountName` de outra conta → usuário de baixo privilégio vira **Domain Admin instantâneo**. Black Hat USA 2026.
- **CVE-2026-25177** — *KerberLoss*: 🔴 SPN invisível por Unicode → bypass de unicidade, downgrade Kerberos→NTLM, impersonation. Sem permissão no alvo.
- **CVE-2026-122164** — *Kerberos EoP (weak authentication)*: 🔴 Novembro 2026 — o CVE de Kerberos mais recente.
- **CVE-2026-62766 / 62752 / 62754 / 62773** — *Lote Kerberos EoP*: Double free no Kerberos, 4 CVEs de ago/2026.
- **CVE-2026-20833** — *KDC RC4 downgrade*: Rebaixamento criptográfico no KDC — relevant para contas de serviço, o alvo do Kerberoast.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
