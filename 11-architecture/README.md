# XI — Defenses and bypass – Architecture and Work Culture Changes

> **Ementa CRTP (seção XI)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Learn briefly about architecture and work culture changes required in an organization to avoid the discussed attacks. We discuss Temporal group membership, ACL Auditing, LAPS, SID Filtering, Selective Authentication, credential guard, device guard, Protected Users Group, PAW, Tiered Administration and ESAE or Red Forest

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

- **CVE-2026-108398** — *WDAC bypass*: Por que o WDAC sozinho não basta.
- **CVE-2026-96222 / 108131** — *AD FS spoofing*: Falhas de validação de certificado.
- **CVE-2026-65777** — *AD Security Feature Bypass*: Controles de segurança do AD podem ser contornados — daí a defesa em profundidade.
- **CVE-2026-27912** — *ResetNightmare*: Justifica *Tiered Administration* e *Protected Users*: um único objeto mal escrito derruba o domínio.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
