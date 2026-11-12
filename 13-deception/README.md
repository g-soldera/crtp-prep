# XIII — Defenses and Bypass – Deception

> **Ementa CRTP (seção XIII)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Understand how Deception can be effective deployed as a defense mechanism in AD.
- Deploy decoy user objects, which have interesting properties set, which have ACL rights over other users and have high privilege access in the domain along with available protections.
- Deploy computer objects and Group objects to deceive an adversary.
- Learn how adversaries can identify decoy objects and how defenders can avoid the detection.

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

- **CVE-2026-27912** — *ResetNightmare*: Objetos *decoy* com UPN/SamAccountName confusos podem **ser a isca** — e também podem ser acidentalmente vítimas da colisão.
- **CVE-2026-25177** — *KerberLoss*: SPNs invisíveis são tanto arma quanto possível armadilha/ruído num ambiente com decoys.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
