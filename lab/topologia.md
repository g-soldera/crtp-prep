# Lab Local — Topologia e Setup

> **Ementa:** https://www.alteredsecurity.com/adlab
> Fluxo de estudo e papéis das VMs: `../AGENTS.md` · Mapa ementa→pastas: `../EMENTA.md`

## Topologia

```
Host: Windows 10 (Ghost Spectre) — 16GB RAM
Hypervisor: VMware Workstation Pro
Rede: VMware VMnet1 host-only — 192.168.32.0/24 (isolada)

Forest: lab.local  (forest root domain)
├── DC01  192.168.32.10   Domain Controller
└── WS01  192.168.32.20   Servidor membro — origem dos ataques

Planejado (criar no módulo 07 — Cross Trust):
└── CHILDDC  child.lab.local
```

## Estado atual

| VM | Hostname AD | Papel | IP | DNS | Status |
|---|---|---|---|---|---|
| DC01 | `WIN-K7NHQG47OQ6` ⚠️ | Primary DC (role 5) | 192.168.32.10 | `192.168.32.10`, `127.0.0.1` | ✅ promovido |
| WS01 | `WS01` | Member Server (role 3) | 192.168.32.20 | `192.168.32.10` | ✅ join OK |

- Domínio: `lab.local` / NetBIOS `LAB` / Forest+Domain Mode: `WinThreshold`
- Roles instaladas no DC: **AD-Domain-Services**, **DNS**, **GPMC**, **RSAT**
- Secure channel do WS01: `True` · `whoami` → `lab\administrator`

> ⚠️ **Pendente:** renomear o DC de `WIN-K7NHQG47OQ6` para `DC01`.

## Setup — checklist

### Concluído

- [x] Instalar Windows Server 2022 no DC01
- [x] Instalar Windows Server 2022 no WS01
- [x] Instalar VMware Tools nas duas VMs
- [x] IP estático (DC01 `.10` / WS01 `.20`), DNS corretos
- [x] Instalar role AD DS + DNS no DC01
- [x] Promover DC01 → criar domínio `lab.local`
- [x] Join do WS01 em `lab.local` + rename para `WS01`
- [ ] Renomear DC → `DC01`
- [ ] Snapshot `BASE` (lab limpo) ⬅️ **próximo passo**
- [ ] Criar usuários/grupos vulneráveis (a cada módulo, conforme o fluxo)

### Por módulo (criar quando chegar)

| Módulo | Pré-requisito |
|---|---|
| 04 `local-privesc` | usuário `LOWPRIV` sem privilégios |
| 05 `domain-privesc` | serviço `svc_sql` com SPN + senha fraca, ACLs fracas |
| 07 `cross-trust` | VM `CHILDDC` com `child.lab.local` |
| 08 `adcs` | role **AD CS** no DC01 + template vulnerável |
| 09/10 | trials MDE + MDI |

## Acesso via host (WinRM)

```powershell
$pw = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('LAB\Administrator', $pw)
$opt = New-PSSessionOption -OpenTimeout 25000 -OperationTimeout 60000

Invoke-Command -ComputerName 192.168.32.10 -Credential $cred -SessionOption $opt -ScriptBlock { hostname }
Invoke-Command -ComputerName 192.168.32.20  -Credential $cred -SessionOption $opt -ScriptBlock { hostname }
```

### Aprendizados do setup (não repetir os erros)

- **`vmrun` trava** em `runProgramInGuest`/`runScriptInGuest` → usar **WinRM 5985**
- **Ping falha** — firewall do Server bloqueia ICMP. É **normal**, não é "sem rede"
- **Trocar o IP derruba a sessão WinRM** para o IP antigo → o comando já rodou,
  o erro "connection interrupted" é esperado
- **`Invoke-Command -TimeoutSeconds` não existe no PowerShell 5.1** → `-SessionOption`
- VMware Tools precisa estar instalado para qualquer automação no guest

## Credenciais (lab isolado)

| Escopo | Usuário | Senha |
|---|---|---|
| Domain Admin (ambas as VMs após join) | `LAB\Administrator` | `Password123!` |
| DSRM (Directory Services Restore Mode) | `Administrator` | `Password123!` |

## Notas

- Rede host-only: VMs isoladas do host e da internet, comunicam-se entre si
- Evaluation do Server 2022: 180 dias, renovável com `slmgr /rearm`
- **Snapshot `BASE` antes de cada técnica nova**, restaurar ao final
- ICMP bloqueado no Server por padrão — `Test-NetConnection -Port` é o teste útil

## Portas úteis (para diagnóstico)

| Porta | Serviço | Esperado |
|---|---|---|
| 389 | LDAP | aberta **só após** promoção a DC |
| 445 | SMB | bloqueada pelo firewall por padrão |
| 5985 | WinRM | ✅ aberta — nosso canal de automação |
| 3389 | RDP | bloqueada por padrão |
