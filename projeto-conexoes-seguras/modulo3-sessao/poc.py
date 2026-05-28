# =============================================================================
# Módulo 3 — Segurança na Camada de Aplicação
# PoC: Gestão de sessão e cookies (SessionID)
# =============================================================================
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "mensagem": "Bem-vindo a PoC do Modulo 3!",
        "rotas_disponiveis": ["/login-vulneravel", "/login-seguro", "/verificar-cookies"]
    })

@app.route('/login-vulneravel')
def login_vulneravel():
    response = make_response(jsonify({"status": "Autenticado via rota VULNERAVEL!"}))
    # Cookie sem NENHUMA flag de segurança (Acessível via scripts e HTTP comum)
    response.set_cookie('SessionID_Inseguro', 'aF83jK9_VULNERAVEL_123')
    return response

@app.route('/login-seguro')
def login_seguro():
    response = make_response(jsonify({"status": "Autenticado via rota SEGURA!"}))
    # Cookie robusto com as diretivas recomendadas de segurança
    response.set_cookie(
        'SessionID_Protegido', 
        's9X2mL1_PROTEGIDO_789',
        httponly=True,   # Impede roubo via JavaScript (Ataques XSS)
        secure=True,     # Exige tráfego exclusivo via HTTPS (Criptografado)
        samesite='Strict' # Bloqueia envio em requisições de sites terceiros (CSRF)
    )
    return response

@app.route('/verificar-cookies')
def verificar():
    cookies_recebidos = request.cookies
    return jsonify({"cookies_ativos_no_navegador": cookies_recebidos})

if __name__ == '__main__':
    print("[*] Iniciando o servidor web da PoC...")
    app.run(debug=True, port=5000)