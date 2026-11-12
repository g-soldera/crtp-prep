# Vulnerabilidades recentes — 2026

> Pesquisa de ameaças para incluir nos estudos do CRTP.
> Ementa: https://www.alteredsecurity.com/adlab
> Mantido por sessão de estudo — revisar antes de cada módulo.

## Antes de tudo: CVE ≠ técnica CRTP

| | O que é | Precisa de lab desatualizado? | Peso na prova |
|---|---|---|---|
| **Técnicas CRTP** | **misconfigurations** — ACLs fraca, unconstrained delegation, Kerberoast, DCSync | ❌ Não — funcionam em domínio atualizado | **Alto** — é o corpo da prova |
| **CVEs** | falha de código — precisa de versão vulnerável | ✅ Sim | **Médio** — prova conhecimento, mas a prova não pede 0-day |

**Conclusão prática:** as CVEs abaixo são *contexto de ameaça* e *material de
estudo complementar*. O núcleo do CRTP continua sendo abuso de configuração.
Não trocar um pelo outro.

---

## Contexto — "Dark October" (Patch Tuesday 13/10/2026)

- **~1410–1415 CVEs** — primeiro release de 4 dígitos na história da Microsoft
- **~70 Critical**, sendo ~67 deles RCE
- **1 zero-day ativo:** `CVE-2026-96951` — Windows Shell **bypass de Mark of the Web**
  (CISA exigiu correção até 16/10/2026). Classificado *Important*, não Critical.
- **2 divulgados publicamente antes do patch:** `CVE-2026-108398` (.NET Framework,
  bypass de WDAC) e `CVE-2026-92707` (MessagePack-CSharp)
- Novembro 2026 seguiu o ritmo: **1252 CVEs, 68 Critical, 1 zero-day**
  (`CVE-2026-116928` — Windows Search RCE)

---

## Prioridade 1 — AD / Kerberos (mais relevante pro CRTP)

| CVE | Nome | Severidade | Data | Resumo | Módulo |
|---|---|---|---|---|---|
| **CVE-2026-27912** | **ResetNightmare** | 8.0 High | 14/04/2026 | UPN igual ao `SamAccountName` de outra conta → **low-priv vira Domain Admin instantâneo**. Descoberto pela Semperis. O mais grave. | `05-domain-privesc` |
| **CVE-2026-25177** | **KerberLoss** | 8.8 High | 10/03/2026 | Unicode **invisível** em `servicePrincipalName` bypassa checagem de unicidade (CWE-641) → DoS, Kerberos→NTLM downgrade, impersonation. Sem permissão no alvo. | `01-enum`, `05-domain-privesc` |
| **CVE-2026-122164** | — | 8.0 High | 10/11/2026 | Windows Kerberos EoP por *weak authentication* (CWE-1390). **O mais novo.** | `05-domain-privesc` |
| **CVE-2026-70229** | — | 8.1 **Critical** | 13/10/2026 | **AD DS RCE sem autenticação** — pacote crafted (CWE-863). *"Exploitation More Likely"*. Complexidade de ataque alta. | `01-enum`, `04-local-privesc` |
| **CVE-2026-49179** | — | 8.8 | 11/08/2026 | AD DS **command injection** sobre rede (SMB). | `01-enum` |
| **CVE-2026-69546** | — | 8.1 High | 08/09/2026 | AD DS RCE via **use-after-free** (CWE-416). | `01-enum` |
| **CVE-2026-33826** | — | 8.0 High | 14/04/2026 | Windows AD RCE, *improper input validation*, rede adjacente. | `01-enum` |
| **CVE-2026-119948 / 105559** | — | Important | 10/11/2026 | AD RCE + DoS, baixo privilégio, sem interação. | `01-enum` |
| **CVE-2026-62766 / 62752 / 62754 / 62773** | — | 7.0–7.8 | 11/08/2026 | Lote de **Kerberos EoP** (double free). | `05-domain-privesc` |
| **CVE-2026-20833** | — | — | 2026 | KDC usa RC4 para ticket de conta de serviço — rebaixamento criptográfico. | `05-domain-privesc` |
| **CVE-2026-57976** | — | 6.5 Med | 14/07/2026 | AD DS **DoS** via null pointer. | `01-enum` |
| **CVE-2026-65777** | — | 5.3 Imp | ago/2026 | AD **Security Feature Bypass**. | `11-architecture` |

> **ResetNightmare + KerberLoss** têm slides do **Black Hat USA 2026**
> ("Identity Crisis") — material obrigatório de leitura.

---

## Prioridade 2 — AD CS (módulo `08-adcs`)

| CVE | Severidade | Data | Resumo |
|---|---|---|---|
| **CVE-2026-62818** | 8.8 Critical | 11/08/2026 | **AD CS RCE** via use-after-free. |
| **CVE-2026-54121** | Critical | 14/07/2026 | **AD CS Elevation of Privilege.** |
| **CVE-2026-105590** | Important | 2026 | AD CS **Security Feature Bypass** (Server 2016+). |
| **CertiGhost** | *(sem CVE confirmada)* | 2026 | Usuário de baixo privilégio obtém **certificado do DC**. Verificar número na fonte. |

---

## Prioridade 3 — Defesas e bypass (módulos `09` a `13`)

| CVE | Produto | Severidade | Resumo | Módulo |
|---|---|---|---|---|
| **CVE-2026-96951** | Windows Shell | Important 8.8 | **Zero-day ativo** — bypass de **Mark of the Web**. | `02-powershell`, `03-dotnet` |
| **CVE-2026-108398** | .NET Framework | 8.8 | Bypass de **WDAC** via assembly .NET malicioso carregado por processo protegido. Divulgado antes do patch. | `03-dotnet`, `11-architecture` |
| **CVE-2026-70571** | Exchange Server | 8.1 **Critical** | RCE via e-mail malicioso, *stack buffer overflow*, sem interação. *"Exploitation More Likely"*. | *(fora do escopo AD)* |
| **CVE-2026-70242** | Outlook | — | RCE pela **reading pane**, sem interação. | *(fora do escopo AD)* |
| **CVE-2026-96222** | **AD FS** | 7.4 | Spoofing por *improper certificate validation*. | `10-bypass-mdi`, `11-architecture` |
| **CVE-2026-108131** | **AD FS** | 7.5 | Spoofing. | `10-bypass-mdi` |
| **CVE-2026-65674** | SQL Server | — | Deserialization RCE — ZDI apontou como **o mais explorável do mês** (out/2026). | `07-cross-trust` |
| **CVE-2026-96913** | Windows Kernel | 8.8 | EoP, heap overflow. | `04-local-privesc` |
| **CVE-2026-96934** | Windows | 9.8 | Use-after-free. | `04-local-privesc` |
| **CVE-2026-69525** | RDP | 9.8 | RCE — set/2026. | `04-local-privesc` |
| **CVE-2026-69435** | Azure SRE Agent | Critical | EoP via **SSRF**. | *(cloud)* |
| **CVE-2026-50481** | Azure AD | 9.9 Critical | EoP. | *(cloud)* |
| **CVE-2026-62869** | Azure Entra ID | 8.8 Critical | Spoofing. | *(cloud)* |

---

## Como usar isto no lab

### 1. Verificar o nível de patch das VMs

```powershell
# No DC01 e WS01
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 15 HotFixID, InstalledOn
[System.Environment]::OSVersion.Version
```

Se o ISO de avaliação já veio com patches recentes, as CVEs acima **não vão
reproduzir** — e é isso que esperamos num lab de *misconfiguration*.

### 2. Decisão por CVE

- **Quer estudar o conceito** → ler advisory + slides Black Hat, sem precisar
  de VM vulnerável
- **Quer reproduzir** → usar snapshot `BASE` + VM **sem** o hotfix correspondiente,
  nunca no lab principal
- **Quer entender a defesa** → ler os eventos de segurança gerados

### 3. Para a prova CRTP

Priorizar as **técnicas de misconfiguration** listadas em `../PLANO.md`.
As CVEs entram como: *entender o que é e por que foi relevante*, não como
*executar 0-day*.

---

## Fontes

- https://www.alteredsecurity.com/adlab
- MSRC Security Update Guide — https://msrc.microsoft.com/update-guide/
- Zero Day Initiative — reviews mensais
- Semperis — pesquisa KerberLoss / ResetNightmare
- SANS ISC / Tenable / Lansweeper — Patch Tuesday reports

---

## Glossário

| Termo | Definição |
|---|---|
| **CVE** | Common Vulnerabilities and Exposures — identificador único de uma falha pública. |
| **CVSS** | Common Vulnerability Scoring System — nota 0–10 da gravidade. |
| **CWE** | Common Weakness Enumeration — *tipo* de falha (ex.: CWE-863 = autorização incorreta). |
| **RCE** | Remote Code Execution — executar código de longe. |
| **EoP** | Elevation of Privilege — escalar de usuário comum para administrador. |
| **Zero-day** | Falha explorada antes de existir patch. |
| **Patch Tuesday** | 2ª terça do mês — dia de patches da Microsoft. |
| **Mark of the Web (MotW)** | Marca de arquivo baixado da internet; bloqueia execução. |
| **WDAC** | Windows Defender Application Control — controla quais binários rodam. |
| **SPN** | Service Principal Name — identifica serviço Kerberos. |
| **UPN** | User Principal Name — email-format do usuário no AD. |
| **SamAccountName** | Nome de logon legado (até 20 caracteres) de um objeto AD. |
| **KDC** | Key Distribution Center — componente do Kerberos que emite tickets. |
| **DCS** | Domain Controller Security — (uso informal para o DC). |
| **AD FS** | Active Directory Federation Services — autenticação federada. |
| **Avaliação "Exploitation More Likely"** | Índice de explorabilidade da Microsoft — priorizar. |
