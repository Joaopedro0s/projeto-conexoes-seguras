# =============================================================================
# Módulo 4 — VPN (Virtual Private Network)
# PoC: Demonstração de encapsulamento e proteção de tráfego
# =============================================================================
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def simular_tunel_vpn(ip_origem, ip_destino, carga_util_dados, chave_vpn, iv):
    # 1. Monta o pacote de dados original (Texto Claro)
    pacote_original = f"SRC:{ip_origem}|DST:{ip_destino}|DATA:{carga_util_dados}".encode()
    
    # 2. Cifra o pacote inteiro (Criptografia de Túnel)
    cipher = Cipher(algorithms.AES(chave_vpn), modes.CFB(iv))
    encryptor = cipher.encryptor()
    payload_criptografado = encryptor.update(pacote_original) + encryptor.finalize()
    
    # 3. Encapsula o conteúdo cifrado dentro de um novo cabeçalho IP (IP da VPN)
    pacote_vpn = {
        "CABECALHO_IP_EXTERNO": {
            "IP_Origem_Virtual": "10.8.0.2 (Interface VPN)",
            "IP_Destino_Virtual": "10.8.0.1 (Gateway VPN)"
        },
        "PAYLOAD_PROTEGIDO_HEX": payload_criptografado.hex()
    }
    return pacote_original, pacote_vpn

def main():
    print("="*70)
    print("[*] Iniciando PoC do Módulo 4 - Simulação de Encapsulamento VPN")
    print("="*70)
    
    # Dados reais do usuário na rede local
    ip_local = "192.168.1.5"
    ip_destino_final = "192.168.1.100"
    dados_usuario = "SenhaPrivadaDoAdmin_E_DadosBancarios"
    
    # Chaves do Túnel VPN
    chave_vpn = os.urandom(32)
    iv = os.urandom(16)
    
    # Executando a simulação
    dados_expostos, pacote_tunelado = simular_tunel_vpn(ip_local, ip_destino_final, dados_usuario, chave_vpn, iv)
    
    print(f"[-] TRÁFEGO SEM VPN (Capturado por Sniffer na LAN):\n    {dados_expostos.decode()}")
    print("\n" + "-"*50)
    print("[+] TRÁFEGO DENTRO DO TÚNEL VPN (Capturado por Sniffer na LAN):")
    print(f"    IP Externo Visível: {pacote_tunelado['CABECALHO_IP_EXTERNO']['IP_Origem_Virtual']} -> {pacote_tunelado['CABECALHO_IP_EXTERNO']['IP_Destino_Virtual']}")
    print(f"    Conteúdo do Payload: {pacote_tunelado['PAYLOAD_PROTEGIDO_HEX']}")
    print("-"*50)
    print("\n[+] CONCLUSÃO: Mesmo que um atacante use a PoC do Módulo 1, ele só verá os IPs virtuais da VPN e um amontoado de caracteres Hexadecimais ilegíveis!")

if __name__ == "__main__":
    main()