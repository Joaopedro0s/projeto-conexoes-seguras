# =============================================================================
# Módulo 1 — Sniffing e Interceptação (Camada 2 e 3)
# PoC: Captura de pacotes com modo promíscuo
# =============================================================================
from scapy.all import sniff, Ether, IP

def processar_pacote(packet):
    # Verifica se o pacote possui a Camada 3 (IP) e Camada 2 (Ethernet)
    if packet.haslayer(IP) and packet.haslayer(Ether):
        mac_origem = packet[Ether].src
        mac_destino = packet[Ether].dst
        ip_origem = packet[IP].src
        ip_destino = packet[IP].dst
        protocolo = packet[IP].proto
        
        print(f"[+] Capturado: MAC {mac_origem} -> {mac_destino} | IP {ip_origem} -> {ip_destino} (Proto: {protocolo})")

def main():
    print("="*70)
    print("[*] Iniciando a PoC do Módulo 1 - Sniffing em Modo Promíscuo")
    print("[*] Certifique-se de executar como Administrador/sudo.")
    print("[*] Capturando os primeiros 10 pacotes trafegados na rede...")
    print("="*70)
    
    # O parâmetro 'sniff' do Scapy força o modo promíscuo por padrão (promisc=True)
    sniff(prn=processar_pacote, count=10, store=0)
    
    print("\n[*] Captura finalizada com sucesso!")

if __name__ == "__main__":
    main()