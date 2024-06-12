from flask import request, jsonify, send_file
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from exceptions import *
from services import *

def register_routes(app):
    #Registra usuarios a partir de email e senha
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        return jsonify(*register_user(email, password))

    #Loga os usuarios a partir de email e senha    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        #tenta autenticar usuario, se for invalido, lancara uma excecao
        user = authenticate_user(email, password) 
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
        

    #Permite usuarios logados cadastrar vendas
    @app.route('/sales', methods=['POST'])
    @jwt_required()
    def create():
        data = request.get_json()
        user_id =  get_jwt_identity()
        nome_cliente = data.get('nome_cliente')
        produto = data.get('produto')
        valor = data.get('valor')
        data_venda = data.get('data_venda')
        return jsonify(*create_sale(nome_cliente, produto, valor, data_venda,user_id))

    #Permite usuarios logados ver todas as vendas
    @app.route('/sales', methods=['GET'])
    @jwt_required()
    def get_all():
        return jsonify(*fetch_all_sales())

    #Permite usuarios logados alterar vendas
    @app.route('/sales/<int:sale_id>', methods=['PUT'])
    @jwt_required()
    def update(sale_id):
        data = request.get_json()
        user_id =  get_jwt_identity()
        return jsonify(*update_sale(sale_id, data,user_id))

    #Permite usuarios logados deletar vendas
    @app.route('/sales/<int:sale_id>', methods=['DELETE'])
    @jwt_required()
    def delete(sale_id):
        return jsonify(*remove_sale(sale_id))
    
    #Permite usuarios logados gerar o relatorio de vendas de um periodo
    @app.route('/sales/pdf', methods=['GET'])
    @jwt_required()
    def generate_pdf():
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        

        pdf_file =  generate_sales_pdf(start_date,end_date)
        return send_file(pdf_file, as_attachment=True, download_name='sales.pdf')


