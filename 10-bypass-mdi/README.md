# X — Defenses and bypass – MDI

> **Ementa CRTP (seção X)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Learn about Microsoft Identity Protection (MDI).
- Understand how MDI relies on anomaly to spot an attack.
- Bypass various MDI detections throughout the course.

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

- **CVE-2026-96222** — *AD FS spoofing (certificate validation)*: CVSS 7.4 — identidade federada.
- **CVE-2026-108131** — *AD FS spoofing*: CVSS 7.5.
- **CVE-2026-25177 / 27912** — *KerberLoss / ResetNightmare*: Os dois geram identidade falsa — é exatamente o que o MDI tenta detectar por anomalia.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
