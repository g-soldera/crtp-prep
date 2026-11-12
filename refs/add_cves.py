from pathlib import Path

ROOT = Path(r"D:\Studies\CRTP\crtp-prep")
REF = "../refs/vulnerabilidades-2026.md"

# folder -> list of (cve, title, one-liner)
BLOCKS = {
    "01-enum": [
        ("CVE-2026-25177", "KerberLoss",
         "Unicode invisível em `servicePrincipalName` bypassa a checagem de unicidade de SPN. Enumeração de SPNs passa a ser também caça a colisões."),
        ("CVE-2026-70229", "AD DS RCE (sem autenticação)",
         "Pacote crafted sobre a rede, sem credenciais — a enumeração já é superfície de ataque. *Exploitation More Likely*."),
        ("CVE-2026-49179", "AD DS command injection",
         "Injection via rede (SMB) contra serviços do AD DS."),
        ("CVE-2026-69546", "AD DS use-after-free RCE", "Outra RCE de AD DS, patchada em 09/2026."),
        ("CVE-2026-33826", "Windows AD RCE",
         "*Improper input validation* em rede adjacente — relevante para quem enumera a partir de dentro."),
        ("CVE-2026-57976", "AD DS DoS", "Null pointer dereference — lembrete de que enumeração agressiva pode derrubar serviços."),
    ],
    "02-powershell": [
        ("CVE-2026-96951", "Mark of the Web bypass (zero-day)",
         "Ativo em exploração desde out/2026. Afeta como scripts baixados são tratados — interliga com o uso de PowerShell ofensivo."),
    ],
    "03-dotnet": [
        ("CVE-2026-108398", "WDAC bypass via assembly .NET",
         "Assembly .NET registrado e carregado por processo protegido contorna o WDAC. Divulgado antes do patch — exatamente a fronteira entre \"modificar tool\" e \"bypass de controle\"."),
        ("CVE-2026-96951", "Mark of the Web bypass (zero-day)",
         "Zero-day ativo em out/2026, ligado a binários e scripts externos."),
    ],
    "04-local-privesc": [
        ("CVE-2026-70229", "AD DS RCE", "RCE sem autenticação — a partir de máquina membro, superfície adicional de Local PrivEsc."),
        ("CVE-2026-96913", "Windows Kernel EoP", "Heap overflow no kernel — categoria clássica de Local PrivEsc."),
        ("CVE-2026-96934", "Use-after-free", "CVSS 9.8 — EoP via UAF."),
        ("CVE-2026-69525", "RDP RCE", "CVSS 9.8, set/2026 — RDP como vetor de escala lateral/local."),
    ],
    "05-domain-privesc": [
        ("CVE-2026-27912", "ResetNightmare",
         "🔴 **O mais importante.** UPN igual ao `SamAccountName` de outra conta → usuário de baixo privilégio vira **Domain Admin instantâneo**. Black Hat USA 2026."),
        ("CVE-2026-25177", "KerberLoss",
         "🔴 SPN invisível por Unicode → bypass de unicidade, downgrade Kerberos→NTLM, impersonation. Sem permissão no alvo."),
        ("CVE-2026-122164", "Kerberos EoP (weak authentication)",
         "🔴 Novembro 2026 — o CVE de Kerberos mais recente."),
        ("CVE-2026-62766 / 62752 / 62754 / 62773", "Lote Kerberos EoP",
         "Double free no Kerberos, 4 CVEs de ago/2026."),
        ("CVE-2026-20833", "KDC RC4 downgrade",
         "Rebaixamento criptográfico no KDC — relevant para contas de serviço, o alvo do Kerberoast."),
    ],
    "06-persistence": [
        ("CVE-2026-122164", "Kerberos EoP (weak authentication)",
         "Persistência via autenticação Kerberos fraca — complementa Golden/Silver ticket."),
        ("CVE-2026-65777", "AD Security Feature Bypass",
         "Bypass de controle de segurança do AD — o adversário que persiste quer exatamente isso."),
    ],
    "07-cross-trust": [
        ("CVE-2026-65674", "SQL Server deserialization RCE",
         "🔴 ZDI apontou como **o mais explorável do mês** (out/2026). Interliga direto com o objetivo \"SQL database links\" da ementa."),
    ],
    "08-adcs": [
        ("CVE-2026-62818", "AD CS RCE (use-after-free)",
         "🔴 Critical 8.8, ago/2026 — o mais relevante para este módulo."),
        ("CVE-2026-54121", "AD CS EoP", "Critical — escalada de privilégio no serviço de certificados."),
        ("CVE-2026-105590", "AD CS Security Feature Bypass", "Important — Server 2016 em diante."),
        ("CertiGhost", "Certificado indevido de DC",
         "Usuário de baixo privilégio obtém certificado de Domain Controller. *(número CVE não confirmado — verificar na fonte)*"),
    ],
    "09-bypass-mde": [
        ("CVE-2026-96951", "Mark of the Web bypass (zero-day)",
         "Zero-day ativo — lógica de \"o que o EDR confia\" em binários externos."),
        ("CVE-2026-108398", "WDAC bypass", "Bypass de controle de aplicativos — mesma fronteira de confiança do MDE."),
    ],
    "10-bypass-mdi": [
        ("CVE-2026-96222", "AD FS spoofing (certificate validation)", "CVSS 7.4 — identidade federada."),
        ("CVE-2026-108131", "AD FS spoofing", "CVSS 7.5."),
        ("CVE-2026-25177 / 27912", "KerberLoss / ResetNightmare",
         "Os dois geram identidade falsa — é exatamente o que o MDI tenta detectar por anomalia."),
    ],
    "11-architecture": [
        ("CVE-2026-108398", "WDAC bypass", "Por que o WDAC sozinho não basta."),
        ("CVE-2026-96222 / 108131", "AD FS spoofing", "Falhas de validação de certificado."),
        ("CVE-2026-65777", "AD Security Feature Bypass", "Controles de segurança do AD podem ser contornados — daí a defesa em profundidade."),
        ("CVE-2026-27912", "ResetNightmare",
         "Justifica *Tiered Administration* e *Protected Users*: um único objeto mal escrito derruba o domínio."),
    ],
    "12-monitoring": [
        ("CVE-2026-27912", "ResetNightmare",
         "Detecção: Security Event **4738/4742** (conta alterada) e **5136** (objeto modificado) com UPN/SPN não-ASCII."),
        ("CVE-2026-25177", "KerberLoss", "Detecção: SACL auditando modificação de `servicePrincipalName` com caracteres invisíveis."),
        ("CVE-2026-70229", "AD DS RCE", "Detecção: tráfego anômalo de pacotes crafted para os serviços do AD DS."),
    ],
    "13-deception": [
        ("CVE-2026-27912", "ResetNightmare",
         "Objetos *decoy* com UPN/SamAccountName confusos podem **ser a isca** — e também podem ser acidentalmente vítimas da colisão."),
        ("CVE-2026-25177", "KerberLoss", "SPNs invisíveis são tanto arma quanto possível armadilha/ruído num ambiente com decoys."),
    ],
}

SECTION = """
## Vulnerabilidades relacionadas (2026)

> Detalhes e fontes em [`{ref}`]({ref})

{rows}
"""

ROW = "- **{cve}** — *{title}*: {desc}"

inserted = 0
for folder, items in BLOCKS.items():
    readme = ROOT / folder / "README.md"
    if not readme.exists():
        print(f"SKIP (sem README): {folder}")
        continue
    text = readme.read_text(encoding="utf-8")
    if "## Vulnerabilidades relacionadas" in text:
        print(f"SKIP (já tem): {folder}")
        continue
    rows = "\n".join(ROW.format(cve=c, title=t, desc=d) for c, t, d in items)
    block = SECTION.format(ref=REF, rows=rows)
    anchor = "## Glossário"
    if anchor not in text:
        print(f"SKIP (sem âncora Glossário): {folder}")
        continue
    text = text.replace(anchor, block.strip() + "\n\n---\n\n" + anchor, 1)
    readme.write_text(text, encoding="utf-8", newline="\n")
    inserted += 1
    print(f"OK {folder:18s} ({len(items)} CVEs)")

print(f"\nTotal: {inserted} READMEs atualizados")
