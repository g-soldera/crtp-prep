# CRTP Prep

Estudo pessoal para a certificação **Certified Red Team Professional** —
[Altered Security](https://www.alteredsecurity.com/adlab).

Aprendizado guiado do zero, com lab local reproduzindo o adlab real.

## Começar por aqui

1. **`AGENTS.md`** — memória do workspace: fluxo de estudo, papéis das VMs, convenções
2. **`EMENTA.md`** — a ementa oficial mapeada para as pastas deste repo
3. **`PLANO.md`** — cada objetivo da ementa ligado a uma prática no lab
4. **`lab/topologia.md`** — topologia e setup das VMs

## Fluxo de estudo

```
Criar defesa → Entender defesa → Atacar → Entender ataque → Documentar
```

O aluno explica com as próprias palavras **antes** de o material ser gravado no repo.
Só assim o registro serve como teste de entendimento.

## Estrutura — espelha as 13 seções da ementa

```
crtp-prep/
├── AGENTS.md               # memória do workspace (ler primeiro)
├── EMENTA.md               # ementa oficial → pastas
├── PLANO.md                # ementa → prática no lab
├── 00-fundamentos/         # pré-requisito (não é seção da prova)
├── 01-enum/                # I.  Active Directory Enumeration
├── 02-powershell/          # II. Offensive PowerShell Tradecraft
├── 03-dotnet/              # III. Offensive .NET Tradecraft
├── 04-local-privesc/       # IV. Local Privilege Escalation
├── 05-domain-privesc/      # V.  Domain Privilege Escalation
├── 06-persistence/         # VI. Domain Persistence and Dominance
├── 07-cross-trust/         # VII. Cross Trust Attacks
├── 08-adcs/                # VIII. Abusing AD CS
├── 09-bypass-mde/          # IX.   Defenses and bypass – MDE EDR
├── 10-bypass-mdi/          # X.    Defenses and bypass – MDI
├── 11-architecture/        # XI.   Architecture and Work Culture Changes
├── 12-monitoring/          # XII.  Defenses – Monitoring
├── 13-deception/           # XIII. Defenses and Bypass – Deception
├── lab/                    # topologia, VMs, configs
├── notes/                  # anotações manuscritas
└── tools/                  # notas sobre ferramentas
```

Duas camadas de guardrail, montadas incrementalmente:

- **Vulnerável** (I–VIII) — criada para ser explorada
- **Defesa** (IX–XIII) — criada para ser contornada

## Progresso

| # | Seção da ementa | Status |
|---|---|---|
| — | 00 Fundamentos | 🔄 Em andamento |
| I | Active Directory Enumeration | ⏳ Pendente |
| II | Offensive PowerShell Tradecraft | ⏳ Pendente |
| III | Offensive .NET Tradecraft | ⏳ Pendente |
| IV | Local Privilege Escalation | ⏳ Pendente |
| V | Domain Privilege Escalation | ⏳ Pendente |
| VI | Domain Persistence and Dominance | ⏳ Pendente |
| VII | Cross Trust Attacks | ⏳ Pendente *(exige child domain)* |
| VIII | Abusing AD CS | ⏳ Pendente *(exige role AD CS)* |
| IX | MDE EDR bypass | ⏳ Pendente |
| X | MDI bypass | ⏳ Pendente |
| XI | Architecture / Work Culture | ⏳ Pendente |
| XII | Monitoring | ⏳ Pendente |
| XIII | Deception | ⏳ Pendente |

## Lab Local

Topologia e setup em `lab/`.

| VM | Papel | IP |
|---|---|---|
| DC01 | Forest root domain `lab.local` | 192.168.32.10 |
| WS01 | Servidor membro — origem dos ataques | 192.168.32.20 |
