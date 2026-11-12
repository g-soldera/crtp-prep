# III — Offensive .NET Tradecraft

> **Ementa CRTP (seção III)** — https://www.alteredsecurity.com/adlab
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

- Learn how to modify and use .NET tools to bypass Windows Defender and Microsoft Defender for Endpoint (MDE).
- Learn to use .NET Loaders that can run assemblies in-memory.

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

- **CVE-2026-108398** — *WDAC bypass via assembly .NET*: Assembly .NET registrado e carregado por processo protegido contorna o WDAC. Divulgado antes do patch — exatamente a fronteira entre "modificar tool" e "bypass de controle".
- **CVE-2026-96951** — *Mark of the Web bypass (zero-day)*: Zero-day ativo em out/2026, ligado a binários e scripts externos.

---

## Glossário

| Termo | Definição |
|---|---|
| | |
