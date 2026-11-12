# IV — Local Privilege Escalation

> **Ementa CRTP (seção IV)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Learn and practice different local privilege escalation techniques on a Windows machine.
- Hunt for local admin privileges on machines in the target domain using multiple methods.
- Abuse enterprise applications to execute complex attack paths that involve bypassing antivirus and pivoting to different machines.

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

- **CVE-2026-70229** — *AD DS RCE*: RCE sem autenticação — a partir de máquina membro, superfície adicional de Local PrivEsc.
- **CVE-2026-96913** — *Windows Kernel EoP*: Heap overflow no kernel — categoria clássica de Local PrivEsc.
- **CVE-2026-96934** — *Use-after-free*: CVSS 9.8 — EoP via UAF.
- **CVE-2026-69525** — *RDP RCE*: CVSS 9.8, set/2026 — RDP como vetor de escala lateral/local.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
