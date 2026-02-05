# By mais old. 
# Esse é meu primeiro script de muitos, o Gemini me auxiliou demais na criação disso. 
# Tá em Português porque, originalmente o script foi feito apenas para uso próprio, e talvez da equipe.  
# Resolvi colocá-lo no github para começar minha jornada, então se qualquer dev estiver lendo isso, bom, obrigado.
# Obs: Não copiei e colei, o prompt foi bem específico quanto a me AUXILIAR e me ENSINAR.

import subprocess
import os
import sys
import time
import winreg as reg

#Configuração do ambiente
if getattr(sys, 'frozen', False):
    pasta_atual = os.path.dirname(sys.executable)
    caminho_exe = sys.executable
else:
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_exe = os.path.abspath(__file__)

pasta_instaladores = os.path.join(pasta_atual, "Instaladores")
arquivo_status = os.path.join(os.environ.get('TEMP', 'C:\\Windows\\Temp'), "status_elder_deploy.txt")

#Barra de instalação
def exibit_progresso(percentual, largura=30):
    setas = int(percentual * largura // 100)
    espacos = largura - setas
    barra = '█' * setas + '░' * espacos
    sys.stdout.write(f'\r    [{barra}] {percentual}%')
    sys.stdout.flush()

#Autostart pós domínio
def configurar_autostart():
    try: 
        with open(arquivo_status, "w") as f:
            f.write("dominio_ok")

        chave_path = r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
        chave = reg.OpenKey(reg.HKEY_CURRENT_USER, chave_path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(chave, "ElderOnePrep", 0, reg.REG_SZ, caminho_exe)
        reg.CloseKey(chave)
        print("[*] Retorno automático configurado no Registro.")
        return True
    except Exception as e:
        print(f"\n[ ERRO CRÍTICO ] Falha ao preparar retorno: {e}")
        return False


def exibir_banner():
    os.system('') # 
    VERDE = '\033[92m'
    RESET = '\033[0m'
    
    art = [
        "  ###########################################################",
        "  #                                                         #",
        "  #  ███╗   ███╗ █████╗ ██╗███████╗ ██████╗ ██╗     ██████╗ #",
        "  #  ████╗ ████║██╔══██╗██║██╔════╝██╔═══██╗██║     ██╔══██╗#",
        "  #  ██╔████╔██║███████║██║███████╗██║   ██║██║     ██║  ██║#",
        "  #  ██║╚██╔╝██║██╔══██║██║╚════██║██║   ██║██║     ██║  ██║#",
        "  #  ██║ ╚═╝ ██║██║  ██║██║███████║╚██████╔╝███████╗██████╔╝#",
        "  #  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═════╝ #",
        "  #                                                         #",
        "  #                AUTOMATION BY: MAIS OLD                  #",
        "  #                     [ Elder One ]                       #",
        "  ###########################################################"
    ]
    
    print(VERDE)
    for linha in art:
        print(linha)
        time.sleep(0.05)
    print(RESET)

# Domínio
def ingressar_no_dominio():
    if os.path.exists(arquivo_status):
        print("\n[*] Domínio já configurado anteriormente. Pulando...")
        return True

    print("\n" + "="*42)
    print("      CONFIGURAÇÃO DE DOMÍNIO")
    print("="*42)
    
    confirmar = input("[?] Deseja ingressar no domínio e REINICIAR automaticamente? (S/N): ").upper()
    
    if confirmar == "S":
        dominio = "" # Coloque o domínio da sua empresa aqui
        usuario = "" # Coloque o usuário de administrador aqui
        senha = "" # E a senha vai aqui

        configurar_autostart()
        
        ps_comando = f'$password = "{senha}" | ConvertTo-SecureString -asPlainText -Force; $credential = New-Object System.Management.Automation.PSCredential("{usuario}", $password); Add-Computer -DomainName "{dominio}" -Credential $credential -Force -Restart'

        try:
            print("[*] Configurando Autostart e Reiniciando em 5 segundos...")
            time.sleep(5)
            subprocess.run(["powershell", "-Command", ps_comando], check=True)
        except Exception as e:
            print(f"[ ERRO ] Falha no domínio: {e}")
    else:
        print("[!] Domínio ignorado.")
        return True
    

# Instalação

def iniciar_automacao():
    exibir_banner()
    if not ingressar_no_dominio():
        return 

    if os.path.exists(arquivo_status):
        print("\n[!] BEM-VINDO DE VOLTA, JOVEM.")
        print("[*] O PC já está no domínio. Vamos às instalações.")
        try: os.remove(arquivo_status)
        except:
            pass

    programas_dict = {
        # Exemplo de configuração de instaladores
        # Certifique-se de colocar os arquivos na pasta "Instaladores"
         "1": ["exemplo_setup.exe", "/S", "Nome do Programa 1"],
         "2": ["exemplo_instalador.msi", "/quiet /norestart", "Nome do Programa 2"],
    }

    print("\n" + "="*42)
    print("       QUAIS PROGRAMAS VOCÊ QUER INSTALAR?")
    print("="*42)
    
    for num, dados in programas_dict.items():
        print(f" [{num}] {dados[2]}")

    escolha = input("\n[?] Digite os números (ex: 1,2,5) ou '0' para TODOS: ")
    if escolha.strip() == "0":
        selecionados = list(programas_dict.keys())
    else:
        selecionados = [x.strip() for x in escolha.split(",")]

        print(f"\n[*] Preparando motores...")

    for num in selecionados:
        if num in programas_dict:
            arquivo, parametro, nome = programas_dict[num]
            caminho = os.path.join(pasta_instaladores, arquivo)
            
            if os.path.exists(caminho):
                print(f"\n[>] Instalando: {nome}")
                for i in range(1, 41, 10):
                    exibit_progresso(i)
                    time.sleep(0.1)
                
                comando = f'msiexec /i "{caminho}" {parametro}' if arquivo.lower().endswith(".msi") else f'"{caminho}" {parametro}'
                subprocess.run(comando, shell=True)

                for i in range(50, 101, 10):
                    exibit_progresso(i)
                    time.sleep(0.1)
                print(f" [ CONCLUÍDO ]")
            else:
                print(f"\n[ X ] Erro: {arquivo} não encontrado.")


    print("\n" + "="*42)
    print("      OPERACAO CONCLUIDA - BY MAIS OLD")
    print("="*42)
    input("\nPressione ENTER para fechar...")

if __name__ == "__main__":
    iniciar_automacao()