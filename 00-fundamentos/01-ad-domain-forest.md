# Active Directory - Estrutura Hierárquica

> Fonte: anotações pessoais — 2026-08-31

Active Directory é uma estrutura hierárquica para gerenciar usuários, computadores e permissões em escala organizacional e corporativa.

## Domain

Unidade básica de administração. Um domínio é um conjunto de objetos (usuários, computadores, grupos) que compartilham:

- Um banco de dados central, gerenciado pelo **Domain Controller**
- Uma política de segurança comum
- Uma relação de confiança interna

**Exemplo:**

`empresa.local` é um domínio.
- Todos os funcionários têm conta nesse domínio
- O Domain Controller sabe quem pode logar onde

## Forest

Container de mais alto nível. Uma forest pode ter um ou mais domínios.

- O primeiro domínio criado em uma forest é o **forest root domain**
- Todos os domínios dentro de uma forest confiam uns nos outros automaticamente (**two-way transitive trust**)

Isso é essencial para entender ataques cross-trust: um domínio filho pode ser o caminho para comprometer o forest root.

## Attack Path Clássico do CRTP

```
Atacante entra por WS01 (membro de child.lab.local)
        ↓
Escala privilégio no child domain
        ↓
Abusa da trust entre child e root
        ↓
Compromete lab.local inteiro (Enterprise Admin)
```

> **Alvo** = qualquer entidade (objeto) no AD: usuário, computador, grupo, GPO, etc.

## Glossário

| Termo | Definição |
|-------|-----------|
| **Active Directory (AD)** | Serviço da Microsoft para gerenciar identidades e recursos em redes Windows. |
| **Domain** | Unidade administrativa do AD. Agrupa objetos sob um DC com política comum. |
| **Forest** | Container máximo do AD. Agrupa um ou mais domínios com schema compartilhado. |
| **Domain Controller (DC)** | Servidor que hospeda o banco de dados do AD e autentica usuários/computadores. |
| **Forest Root Domain** | Primeiro domínio da forest. Enterprise Admins vivem aqui. |
| **Child Domain** | Subdomínio dentro da mesma forest. Ex: `rh.empresa.local` é filho de `empresa.local`. |
| **Trust** | Relação que permite usuários de um domínio acessarem recursos de outro. Dentro da forest é automática e bidirecional. |
| **Two-way Transitive Trust** | Trust bidirecional e transitiva: se A confia em B e B confia em C, A confia em C. |
| **Enterprise Admin** | Grupo com privilégios sobre toda a forest. O "troféu final" do CRTP. |
| **Object** | Qualquer entidade no AD: usuário, computador, grupo, GPO, etc. |
