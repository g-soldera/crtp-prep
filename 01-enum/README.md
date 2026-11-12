# I — Active Directory Enumeration

> **Ementa CRTP (seção I)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Use scripts, built-in tools and Active Directory module to enumerate the target domain.
- Understand and practice how useful information like users, groups, group memberships, computers, user properties etc. from the domain controller is available to even a normal user.
- Understand and enumerate intra-forest and inter-forest trusts. Practice how to extract information from the trusts.
- Enumerate Group policies.
- Enumerate ACLs and learn to find out interesting rights on ACLs in the target domain to carry out attacks.
- Learn to use BloodHound and understand its applications in a red team operation.

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

- **CVE-2026-25177** — *KerberLoss*: Unicode invisível em `servicePrincipalName` bypassa a checagem de unicidade de SPN. Enumeração de SPNs passa a ser também caça a colisões.
- **CVE-2026-70229** — *AD DS RCE (sem autenticação)*: Pacote crafted sobre a rede, sem credenciais — a enumeração já é superfície de ataque. *Exploitation More Likely*.
- **CVE-2026-49179** — *AD DS command injection*: Injection via rede (SMB) contra serviços do AD DS.
- **CVE-2026-69546** — *AD DS use-after-free RCE*: Outra RCE de AD DS, patchada em 09/2026.
- **CVE-2026-33826** — *Windows AD RCE*: *Improper input validation* em rede adjacente — relevante para quem enumera a partir de dentro.
- **CVE-2026-57976** — *AD DS DoS*: Null pointer dereference — lembrete de que enumeração agressiva pode derrubar serviços.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
