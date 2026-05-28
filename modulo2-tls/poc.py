# =============================================================================
# Módulo 2 — Criptografia e Handshake TLS
# PoC: Demonstração de criptografia híbrida (RSA + AES)
# =============================================================================
import time
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def main():
    print("="*70)
    print("[*] Iniciando PoC do Módulo 2 - Criptografia Híbrida (Base do HTTPS)")
    print("="*70)

    # 1. GERAR PAR DE CHAVES RSA (Simulando o Servidor)
    print("[+] 1. Servidor gerando par de chaves RSA (2048 bits)...")
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chave_publica = chave_privada.public_key()

    # 2. GERAR CHAVE DE SESSÃO AES (Simulando o Cliente)
    print("[+] 2. Cliente gerando chave de sessão simétrica AES-256 e IV...")
    chave_aes = os.urandom(32)
    iv = os.urandom(16)

    # 3. CIFRAR A CHAVE AES COM A PÚBLICA RSA (Handshake TLS)
    print("[+] 3. Simulando Handshake: Cliente cifra a chave AES usando a Chave Pública do Servidor...")
    inicio_rsa = time.time()
    chave_aes_cifrada = chave_publica.encrypt(
        chave_aes,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    tempo_rsa = time.time() - inicio_rsa

    # 4. SERVIDOR DECIFRA A CHAVE AES COM A PRIVADA RSA
    chave_aes_decifrada = chave_privada.decrypt(
        chave_aes_cifrada,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

    # 5. CIFRAR E DECIFRAR MENSAGEM COM AES (Tráfego de Dados Veloz)
    mensagem_original = b"Dados Confidenciais da Web do SENAI: TokenDeAutenticacao123"
    print(f"\n[+] Texto original para envio: {mensagem_original.decode()}")
    
    print("[+] 4. Transferência de Dados: Cifrando o payload real com AES...")
    inicio_aes = time.time()
    cipher = Cipher(algorithms.AES(chave_aes_decifrada), modes.CFB(iv))
    encryptor = cipher.encryptor()
    texto_cifrado = encryptor.update(mensagem_original) + encryptor.finalize()
    tempo_aes = time.time() - inicio_aes

    print(f"[!] Payload Cifrado na Rede (Hex): {texto_cifrado.hex()[:50]}...")

    # Decifrando os dados
    decryptor = cipher.decryptor()
    texto_decifrado = decryptor.update(texto_cifrado) + decryptor.finalize()
    print(f"[+] Destino decifrou com AES: {texto_decifrado.decode()}")

    # 6. EXIBIR RESULTADO DE DESEMPENHO
    print("\n" + "="*40)
    print("   MÉTRICAS DE DESEMPENHO COMPATIVEL")
    print("="*40)
    print(f"Tempo Cifra RSA (Assimétrica): {tempo_rsa:.6f} segundos")
    print(f"Tempo Cifra AES (Simétrica):  {tempo_aes:.6f} segundos")
    razao = tempo_rsa / max(tempo_aes, 1e-9)
    print(f"👉 O AES foi aproximadamente {razao:.2f}x mais rápido que o RSA!")
    print("="*70)

if __name__ == "__main__":
    main()