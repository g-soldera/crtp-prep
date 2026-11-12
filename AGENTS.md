# AGENTS.md — Memória do Workspace CRTP

> Instruções persistentes para qualquer sessão de estudo neste repositório.
> Se você é um assistente trabalhando aqui, leia isto antes de qualquer coisa.

## Objetivo

Estudo guiado do zero para a certificação **CRTP — Certified Red Team Professional**
(Altered Security). Lab local reproduz o que será feito no adlab real.

- **Ementa oficial:** https://www.alteredsecurity.com/adlab → seção "What will you learn?"
- **Ementa espelhada neste repo:** `refs/CRTP-ementa.md` (13 seções, 45 objetivos)
- **Não inventar conteúdo da prova** — tudo sai da ementa.

## Fluxo de estudo (obrigatório — não pular etapas)

Cada tópico percorre este ciclo, **nesse ordem**:

```
1. CRIAR a defesa        → configurar no lab o controle/vulnerabilidade
2. ENTENDER a defesa     → explicar o que ela faz e por quê existe
3. ATACAR                → executar a técnica a partir do WS01
4. ENTENDER o ataque     → explicar por que funcionou, o que permitiu
5. DOCUMENTAR            → o aluno EXPICA DE VOLTA ao assistente o que entendeu;
                           só então o assistente grava o markdown no repo
```

O passo 5 é o critério de "entendi": **o aluno fala, o assistente registra.**
Nunca gravar material que o aluno ainda não explicou com as próprias palavras.

## Camadas do guardrail

O lab tem **duas camadas**, montadas incrementalmente conforme o avanço:

| Camada | Conteúdo | Seções da ementa |
|---|---|---|
| **Vulnerável** | ACLs fracas, delegation, SPNs, contas de serviço — criadas para serem exploradas | I–VIII |
| **Defesa** | LAPS, Protected Users, SID Filtering, MDE, MDI, monitoring, deception — criadas para serem contornadas | IX–XIII |

Regra: **criar a defesa daquilo que precisamos contornar**, e a vulnerabilidade
daquilo que precisamos explorar. Igual ao adlab.

## Papéis das VMs

| VM | Papel | IP |
|---|---|---|
| **DC01** | Domain Controller, **forest root domain** de `lab.local` | 192.168.32.10 |
| **WS01** | **Servidor membro** de `lab.local` — origem de todos os ataques | 192.168.32.20 |
| **CHILDDC** | Domínio filho `child.lab.local` — **criar só no módulo 07** | planejado |

> ⚠️ WS01 **não é um domain**. É membro. `Add-Computer -DomainName lab.local`
> é join ao nível do **domínio**. A forest só importa nos ataques cross-trust.

## Convenções

- **Snapshot antes de cada técnica**, restaurar ao final. Snapshot `BASE` = lab limpo.
- **Commits** ao fim de cada tópico documentado.
- Cada markdown de estudo termina com **Glossário** (termo → definição).
- Senha do lab: `Password123!`
- Explicar conceitos fundamentais **antes** de qualquer técnica.
- Respostas concisas e diretas.

## Acesso ao lab (via host)

```powershell
$pw = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('LAB\Administrator', $pw)
Invoke-Command -ComputerName 192.168.32.10 -Credential $cred -ScriptBlock { hostname }
```

- **WinRM (5985)** é o canal — `vmrun` trava, não usar.
- ICMP é bloqueado pelo firewall do Server: ping falhar é **normal**.
- PowerShell 5.1 **não tem** `Invoke-Command -TimeoutSeconds` — usar `-SessionOption`.
- `LAB\Administrator` funciona nas duas VMs (credencial local, pré-join).

## Ordem dos módulos

`00-fundamentos` é pré-requisito, não é seção da prova. Depois, I→XIII na ordem:

`01-enum` → `02-powershell` → `03-dotnet` → `04-local-privesc` → `05-domain-privesc`
→ `06-persistence` → `07-cross-trust` → `08-adcs` → `09-bypass-mde` → `10-bypass-mdi`
→ `11-architecture` → `12-monitoring` → `13-deception`

## Status

Ver `PLANO.md` para o mapa ementa → prática e o checklist de setup.
