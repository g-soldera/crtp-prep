import re
from pathlib import Path

ROOT = Path(r"D:\Studies\CRTP\crtp-prep")
EMENTA = ROOT / "refs" / "CRTP-ementa.md"
URL = "https://www.alteredsecurity.com/adlab"

# section heading (from ementa) -> target folder
MAP = {
    "I. Active Directory Enumeration": "01-enum",
    "II. Offensive PowerShell Tradecraft": "02-powershell",
    "III. Offensive .NET Tradecraft": "03-dotnet",
    "IV. Local Privilege Escalation": "04-local-privesc",
    "V. Domain Privilege Escalation": "05-domain-privesc",
    "VI. Domain Persistence and Dominance": "06-persistence",
    "VII. Cross Trust Attacks": "07-cross-trust",
    "VIII. Abusing AD CS": "08-adcs",
    "IX. Defenses and bypass – MDE EDR": "09-bypass-mde",
    "X. Defenses and bypass – MDI": "10-bypass-mdi",
    "XI. Defenses and bypass – Architecture and Work Culture Changes": "11-architecture",
    "XII. Defenses – Monitoring": "12-monitoring",
    "XIII. Defenses and Bypass – Deception": "13-deception",
}

text = EMENTA.read_text(encoding="utf-8")

# split into "#### heading" sections
sections = {}
cur = None
for line in text.splitlines():
    m = re.match(r"^####\s+(.+?)\s*$", line)
    if m:
        cur = m.group(1)
        sections[cur] = []
        continue
    if cur is None:
        continue
    li = re.match(r"^\*\s+(.+)$", line)
    if li:
        sections[cur].append(li.group(1))

missing = [k for k in MAP if k not in sections]
if missing:
    raise SystemExit(f"Secoes nao achadas na ementa: {missing}")

template = """# {num} — {title}

> **Ementa CRTP (seção {roman})** — {url}
> Objetivos de aprendizado oficiais. Ver `../refs/CRTP-ementa.md`.

## Objetivos desta seção

{bullets}

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

## Glossário

| Termo | Definição |
|---|---|
| | |
"""

for title, folder in MAP.items():
    roman = title.split(".", 1)[0]
    num = title.split(".", 1)[1].strip()
    objs = sections[title]
    bullets = "\n".join(f"- {o}" for o in objs)
    out = ROOT / folder / "README.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        template.format(num=roman, title=num, roman=roman, url=URL, bullets=bullets),
        encoding="utf-8",
        newline="\n",
    )
    print(f"{folder:18s} <- {title}  ({len(objs)} objetivos)")

print(f"\nTotal secoes mapeadas: {len(MAP)} / ementa: {len(sections)}")
