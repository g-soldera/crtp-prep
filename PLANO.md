# Plano de Estudo — CRTP (ementa → prática no lab)

> **Ementa:** https://www.alteredsecurity.com/adlab → "What will you learn?"
> Espelhada em `refs/CRTP-ementa.md` (13 seções, 45 objetivos).
> Estrutura de pastas em `EMENTA.md` · fluxo de estudo em `AGENTS.md`.

## Fluxo por tópico

```
Criar defesa → Entender defesa → Atacar → Entender ataque → Documentar
```

Duas camadas de guardrail, montadas **incrementalmente** conforme cada módulo:

- **Vulnerável** (I–VIII) — criada para ser explorada
- **Defesa** (IX–XIII) — criada para ser contornada

---

## Módulos

### `00-fundamentos/` — pré-requisito (não é seção da prova)

Conceitos sem os quais nada do resto faz sentido: domain, forest, DC, trust,
Kerberos vs NTLM, security principal, ACL/ACE, SID, GPO.

- **Lab:** `Get-ADDomain`, `Get-ADForest`, `nltest /dsgetdc:`, `whoami /all` no WS01.
- **Entender:** por que `lab.local` tem `krbtgt` e `Enterprise Admins`, e por que a
  trust padrão é two-way transitive.

---

### `01-enum/` — I. Active Directory Enumeration

| Objetivo (ementa) | Prática no lab |
|---|---|
| Scripts, built-in tools e AD module | `Get-ADUser/Group/Computer`, `net group "Domain Users" /domain`, `dsquery` |
| Info disponível a qualquer usuário | Logar como usuário comum e enumerar: usuários, grupos, máquinas, SPNs, descrições |
| Trusts intra/inter-forest | `Get-ADTrust`, `nltest /trusted_domains` |
| Group Policies | `Get-GPO -All`, `gpresult /h gpo.html`, ler `SYSVOL` |
| ACLs e rights interessantes | `Get-DomainObjectAcl`, caçar `GenericAll`/`WriteDacl`/`ForceChangePassword` |
| BloodHound | `SharpHound` → `bloodhound-python` → paths `krbtgt`→`DA` |

**Guardrail a criar:** usuários/grupos com descrições interessantes, ACLs permissivas.

---

### `02-powershell/` — II. Offensive PowerShell Tradecraft

| Objetivo | Prática no lab |
|---|---|
| PowerShell ainda serve para enum | rodar PowerView num host com logs |
| Modificar tools p/ bypassar Defender | alterar assinaturas/strings |
| Bypass AMSI, CLM, Script Block Logging, Transcription | AMSI bypass, `CLM` bypass |

**Guardrail a criar:** Transcription, Script Block Logging, CLM, AMSI.

---

### `03-dotnet/` — III. Offensive .NET Tradecraft

| Objetivo | Prática no lab |
|---|---|
| Modificar .NET tools p/ bypassar Defender e MDE | renomear/refletir assembly |
| .NET Loaders in-memory | loaders (ex.: `Fare`, spoofed assembly) |

---

### `04-local-privesc/` — IV. Local Privilege Escalation

| Objetivo | Prática no lab |
|---|---|
| Técnicas de Local PrivEsc | token impersonation, unquoted service path, writable service DLL, AlwaysInstallElevated, autorun em `ProgramData`, `SeBackupPrivilege` |
| Caçar local admin no domínio | `Get-LocalGroupMember`, BloodHound `AdminTo`, psexec/WMI/WinRM |
| Abusar enterprise apps / AV bypass + pivot | scheduled tasks, DCOM (`mmc20`/`ShellWindows`), COM |

**Guardrail a criar:** usuário `LOWPRIV` sem privilégios + serviços mal configurados.

---

### `05-domain-privesc/` — V. Domain Privilege Escalation

> Inclui **Lateral Movement** — a ementa não tem seção própria; pivoting,
> credential replay e abuso de local admin derivado vivem aqui.

| Objetivo | Prática no lab |
|---|---|
| Credenciais/sessões de DA + credential replay | `Get-NetSession`, `Get-NetLoggedon`, LSASS dump, CredMan, PtH/PtT/Overpass-the-Hash, `runas /netonly` |
| Ambiente com AppLocker | habilitar AppLocker no WS01, extrair via `comsvcs.dll` MiniDump |
| Kerberoast e variantes | `Get-ADUser -Filter {ServicePrincipalName -like "*"}` → Rubeus → hashcat |
| Unconstrained delegation | `TrustedForDelegation -eq $true` → coerce (SpoolSample/PrinterBug) → TGT de DA |
| Constrained delegation | `Rubeus s4u2self/s4u2proxy` |
| Protected Groups | `adminCount=1`, DCSync |
| ACL abuse → DCSync | `Replicating Directory Changes All` → `lsadump::dcsync` |

**Guardrail a criar:** `svc_sql` com SPN + senha fraca, unconstrained delegation, ACL fraca.

---

### `06-persistence/` — VI. Domain Persistence and Dominance

| Objetivo | Prática no lab |
|---|---|
| Golden / Silver / Diamond ticket | DCSync do `krbtgt` → `goldenPac`/Rubeus `golden` |
| Skeleton key e custom SSP | `misc::skeleton`, SSP custom |
| DC safe mode admin | `dsrm` → trocar senha do DA |
| AdminSDHolder | ACE no `CN=AdminSDHolder,CN=System` |
| DCSync via ACL | formalizar como persistência |
| Host security descriptor do DC | DACL do DC p/ executar sem DA |

---

### `07-cross-trust/` — VII. Cross Trust Attacks

**Exige:** VM `CHILDDC` com `child.lab.local` — **criar ao entrar neste módulo.**

| Objetivo | Prática no lab |
|---|---|
| Child DA → Enterprise Admin | trust key → `kerberos::golden` com SID de Enterprise Admin |
| Intra-forest trust attacks | SID history injection, SID Filtering |
| SQL Server database links | SQL no WS01, `db_link` cross-domain, `xp_cmdshell` |

---

### `08-adcs/` — VIII. Abusing AD CS

**Exige:** role **AD CS** no DC01 + template vulnerável.

| Objetivo | Prática no lab |
|---|---|
| Ataques populares de ADCS | ESC1, ESC2, ESC3, ESC6, ESC8 (Certipy/Certify) |
| Cross-trust até Enterprise Admin | cert-based auth entre domínios |

---

### `09-bypass-mde/` → `13-deception/` — IX–XIII (defesas e bypass)

| Seção | Guardrail a criar | Prática |
|---|---|---|
| **IX** MDE EDR | instalar trial MDE no WS01 | chain de ataques sem alerta, verificar no portal 365 |
| **X** MDI | trial MDI | entender anomaly detection, contornar |
| **XI** Architecture | LAPS, Protected Users, PAW, Tiered Admin, SID Filtering, Credential Guard | configurar e tentar atacar |
| **XII** Monitoring | Security log 4624/4625/4688/4768 | correlacionar evento com cada ataque |
| **XIII** Deception | decoy user com `adminCount`, ACL falsa | identificar/decepcionar o atacante |

---

## Ordem proposta

```
Semana 1  →  00 Fundamentos + 01 Enum        ✅ setup do lab concluído
Semana 2  →  02 PowerShell + 03 .NET + 04 LocalPrivEsc
Semana 3  →  05 DomainPrivEsc (incl. Lateral Movement)
Semana 4  →  06 Persistence
Semana 5  →  07 Cross Trust   (cria child domain)
Semana 6  →  08 ADCS          (instala role AD CS)
Semana 7  →  09–13 Defesas e bypass (trials MDE/MDI)
```

## Bloqueadores por módulo

- [x] VMs criadas e ligadas
- [x] VMware Tools instalado
- [x] IP estático DC01/WS01
- [x] AD DS + promoção DC → `lab.local`
- [x] Join do WS01
- [ ] Renomear DC → `DC01`
- [ ] Snapshot `BASE`
- [ ] *(04)* usuário `LOWPRIV`
- [ ] *(05)* `svc_sql` com SPN, delegation, ACLs fracas
- [ ] *(07)* child domain `child.lab.local`
- [ ] *(08)* role AD CS + template vulnerável
- [ ] *(09/10)* trials MDE + MDI

---

## Glossário

| Termo | Definição |
|---|---|
| **Enum** | Enumeration — coleta passiva de informações do alvo antes do ataque. |
| **ACL** | Access Control List — lista de ACEs aplicada a um objeto AD. |
| **ACE** | Access Control Entry — permissão individual (ex.: `GenericAll`). |
| **GPO** | Group Policy Object — política aplicada a OU/domínio/computador. |
| **SPN** | Service Principal Name — identifica serviço Kerberos, alvo do Kerberoast. |
| **TGT** | Ticket Granting Ticket — ticket do Kerberos para obter outros tickets. |
| **TGS** | Ticket Granting Service — ticket para acessar um serviço específico. |
| **Delegation** | Permissão de um serviço usar credenciais do usuário em outro recurso. |
| **DCSync** | Replicar credenciais do DC pedindo como se fosse outro DC. |
| **Golden Ticket** | TGT forjado com hash do `krbtgt` — domínio comprometido. |
| **Silver Ticket** | TGS forjado com hash de um serviço — acesso a um recurso. |
| **Trust** | Relação entre domínios permitindo autenticação cruzada. |
| **Cross Trust** | Ataque explorando trust entre domínios/forests. |
| **AD CS** | Active Directory Certificate Services — infra de PKI do AD. |
| **AMSI** | Antimalware Scan Interface — hook de inspeção de scripts do Windows. |
| **CLM** | Constrained Language Mode — restrição de PowerShell a APIs seguras. |
| **MDE** | Microsoft Defender for Endpoint — EDR da Microsoft. |
| **MDI** | Microsoft Defender for Identity — monitora comportamento no AD. |
| **EDR** | Endpoint Detection and Response. |
| **AppLocker** | Allowlisting de aplicativos do Windows. |
| **PAW** | Privileged Access Workstation — máquina dedicada para admin. |
| **Secure Channel** | Canal autenticado entre máquina membro e DC. |
| **NTDS.dit** | Arquivo que armazena o banco de dados do AD. |
