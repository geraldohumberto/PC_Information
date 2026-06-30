import tkinter as tk
import subprocess
import socket
import getpass
import platform
import winreg
import os
import sys
import ctypes


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def ocultar_console_windows():
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("PCInformation.App")
    except:
        pass


def powershell_unico():
    comando = r"""
$os = Get-CimInstance Win32_OperatingSystem
$cs = Get-CimInstance Win32_ComputerSystem
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
$bios = Get-CimInstance Win32_BIOS

Write-Output $os.Caption
Write-Output $os.Version
Write-Output $os.BuildNumber
Write-Output $cs.Manufacturer
Write-Output $cs.Model
Write-Output $cpu.Name
Write-Output $cs.TotalPhysicalMemory
Write-Output $bios.SerialNumber
"""

    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        resultado = subprocess.check_output(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", comando],
            text=True,
            encoding="utf-8",
            errors="ignore",
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        linhas = [linha.strip() for linha in resultado.splitlines() if linha.strip()]

        return {
            "sistema": linhas[0] if len(linhas) > 0 else "Não encontrado",
            "versao": linhas[1] if len(linhas) > 1 else "Não encontrado",
            "build": linhas[2] if len(linhas) > 2 else "Não encontrado",
            "fabricante": linhas[3] if len(linhas) > 3 else "Não encontrado",
            "modelo": linhas[4] if len(linhas) > 4 else "Não encontrado",
            "processador": linhas[5] if len(linhas) > 5 else "Não encontrado",
            "ram_bytes": linhas[6] if len(linhas) > 6 else "0",
            "serial": linhas[7] if len(linhas) > 7 else "Não encontrado",
        }

    except:
        return {
            "sistema": "Não encontrado",
            "versao": "Não encontrado",
            "build": "Não encontrado",
            "fabricante": "Não encontrado",
            "modelo": "Não encontrado",
            "processador": "Não encontrado",
            "ram_bytes": "0",
            "serial": "Não encontrado",
        }


def get_machine_guid():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Cryptography"
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")
        return value
    except:
        return "Não encontrado"


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Não encontrado"


def get_info():
    dados = powershell_unico()

    maquina = socket.gethostname()
    usuario = getpass.getuser()
    arquitetura = platform.architecture()[0]

    try:
        memoria = f"{round(int(dados['ram_bytes']) / (1024 ** 3), 1)} GB"
    except:
        memoria = "Não encontrado"

    return f"""Nome da Máquina: {maquina}
Usuário Logado: {usuario}
Sistema Operacional: {dados['sistema']}
Versão/Build: {dados['versao']} / {dados['build']}
Arquitetura: {arquitetura}
Fabricante: {dados['fabricante']}
Modelo: {dados['modelo']}
Processador: {dados['processador']}
Memória RAM: {memoria}
Número de Série: {dados['serial']}
Endereço IP: {get_ip()}
MachineGuid: {get_machine_guid()}
"""


ocultar_console_windows()

janela = tk.Tk()
janela.title("PC Information")
janela.geometry("500x235")
janela.resizable(False, False)

try:
    icone = resource_path("Windows.ico")
    janela.iconbitmap(icone)
except:
    pass

info = tk.Label(
    janela,
    text=get_info(),
    justify="left",
    anchor="nw",
    font=("Segoe UI", 10)
)

info.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

janela.mainloop()