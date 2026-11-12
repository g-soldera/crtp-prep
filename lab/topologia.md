# Lab Local - Topologia e Setup

## Topologia

```
Host: Windows 10 (Ghost Spectre) — 16GB RAM

Rede: VMware Host-Only (isolada do host, VMs se comunicam entre si)

Forest: lab.local
├── DC01.lab.local   — Domain Controller (Windows Server 2022 Eval)
└── WS01.lab.local   — Workstation / máquina de ataque (Windows Server 2022 Eval)
```

Expandir futuramente com `CHILDDC.child.lab.local` para ataques cross-trust.

## VMs

| VM | Papel | RAM | Disco | IP planejado |
|----|-------|-----|-------|--------------|
| DC01 | Domain Controller (`lab.local`) | 2GB | 60GB | 192.168.100.10 |
| WS01 | Workstation membro do domínio | 2GB | 50GB | 192.168.100.20 |

## Arquivos

```
D:/Studies/CRTP/
├── isos/
│   └── WinServer2022-eval.iso   (4.7GB — Windows Server 2022 Evaluation)
└── lab/
    ├── DC01/
    │   ├── DC01.vmx
    │   └── DC01.vmdk
    └── WS01/
        ├── WS01.vmx
        └── WS01.vmdk
```

## Hypervisor

VMware Workstation Pro — `vmrun.exe` v1.17.0

## Ordem de Setup

1. [ ] Instalar Windows Server 2022 no DC01
2. [ ] Instalar Windows Server 2022 no WS01
3. [ ] Configurar IPs estáticos (DC01: 192.168.100.10 / WS01: 192.168.100.20)
4. [ ] Instalar role AD DS no DC01
5. [ ] Promover DC01 a Domain Controller — criar domínio `lab.local`
6. [ ] Joinar WS01 ao domínio `lab.local`
7. [ ] Criar usuários e grupos de teste no AD
8. [ ] Tirar snapshot base de ambas as VMs

## Credenciais (uso local — lab isolado)

| Máquina | Usuário | Senha |
|---------|---------|-------|
| DC01 | Administrator | (definir na instalação) |
| WS01 | Administrator | (definir na instalação) |

## Notas

- Rede Host-Only: VMs isoladas do host e da internet, comunicam-se entre si
- Evaluation do Server 2022: válida por 180 dias, renovável via `slmgr /rearm`
- Tirar snapshot **antes de cada técnica nova** e após setup limpo
