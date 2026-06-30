# 🖥️ PC Information

Ferramenta simples para inventário e identificação de computadores Windows.

O aplicativo coleta informações do sistema operacional, hardware e identificação da máquina, exibindo tudo em uma interface gráfica leve e amigável.

---

## 📸 Preview

Exibe informações como:

- Nome da Máquina
- Usuário Logado
- Sistema Operacional
- Versão e Build do Windows
- Arquitetura
- Fabricante
- Modelo
- Processador
- Memória RAM
- Número de Série
- Endereço IP
- MachineGuid

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Tkinter
- PowerShell
- PyInstaller

---

## 📋 Requisitos

- Windows 10
- Windows 11
- Windows Server 2016+
- Python 3.10 ou superior

---

## 🔧 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/pc-information.git
```

Entre na pasta:

```bash
cd pc-information
```

Execute:

```bash
python pc_information.py
```

---

## 📦 Gerando Executável

Instale o PyInstaller:

```bash
pip install pyinstaller
```

Compile:

```bash
python -m PyInstaller --onefile --noconsole --clean --icon=Windows.ico --add-data "Windows.ico;." pc_information.py
```

O executável será criado em:

```text
dist\pc_information.exe
```

---

## 📁 Estrutura do Projeto

```text
PC-Information/
│
├── pc_information.py
├── Windows.ico
├── README.md
└── dist/
```

---

## 🎯 Objetivo

Este projeto foi criado para facilitar a coleta rápida de informações de inventário em computadores Windows, sem necessidade de acessar diversas telas do sistema operacional.

Ideal para:

- Suporte Técnico
- Help Desk
- Infraestrutura
- Inventário de Ativos
- Auditoria de Equipamentos

---

## 📄 Licença

Este projeto é distribuído sob a licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por Geraldo Humberto.

GitHub:
https://github.com/geraldohumberto