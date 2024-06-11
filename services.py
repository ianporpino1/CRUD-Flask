import repositories as repo
from datetime import datetime, timedelta
from models import User, Sale


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def register_user(email, password):
    if repo.get_user_by_email(email):
        return {"msg": "User already exists"}, 400
    new_user = User(email=email)
    new_user.set_password(password)
    repo.add_user(new_user)
    return {"msg": "User registered successfully"}, 201

def authenticate_user(email, password):
    user = repo.get_user_by_email(email)
    if user and user.check_password(password):
        return user
    return None

def create_sale(nome_cliente, produto, valor, data_venda_str,user_id):

    data_venda = datetime.strptime(data_venda_str, '%d-%m-%Y')

    new_sale = Sale(nome_cliente=nome_cliente, produto=produto, valor=valor, data_venda=data_venda, user_id=user_id)
    repo.add_sale(new_sale)
    return {"msg": "Sale created successfully"}, 201

def fetch_all_sales():
    sales = repo.get_all_sales()
    
    sales_dicts = [sale.to_dict() for sale in sales]
    
    return sales_dicts, 200


def update_sale(sale_id, data):
    sale = repo.get_sale_by_id(sale_id)

    data_venda_str = data.get('data_venda')

    if not sale:
        return {"msg": "Sale not found"}, 404

    if 'nome_cliente' in data:
        sale.nome_cliente = data.get('nome_cliente')
    if 'produto' in data:
        sale.produto = data.get('produto')
    if 'valor' in data:
        sale.valor = data.get('valor')
    if 'data_venda' in data:
        sale.data_venda = datetime.strptime(data_venda_str, '%d-%m-%Y')
    
    repo.update_sale()
    return {"msg": "Sale updated successfully"}, 200

def remove_sale(sale_id):
    sale = repo.get_sale_by_id(sale_id)
    if not sale:
        return {"msg": "Sale not found"}, 404
    
    repo.delete_sale(sale)
    return {"msg": "Sale deleted successfully"}, 200


def generate_sales_pdf(start_date_str, end_date_str, user_id):

    #por algum motivo, se start_date == data_venda, a venda nao é exibida no pdf
    um_dia = timedelta(days=1)
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y') - um_dia
    end_date = datetime.strptime(end_date_str, '%d-%m-%Y')

    sales = repo.get_sales_by_period(start_date, end_date, user_id)

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    title_text = f"Relatório de Vendas Entre os dias {start_date.strftime('%d-%m-%Y')} e {end_date.strftime('%d-%m-%Y')}"
    title = Paragraph(title_text, title_style)
    elements.append(title)

    
    elements.append(Paragraph("<br/><br/>", title_style))

    
    data = [["ID", "Nome do Cliente", "Produto", "Data da Venda", "Valor (R$)"]]

   
    for sale in sales:
        print(sale)
        data.append([str(sale.id), str(sale.nome_cliente), str(sale.produto), str(sale.data_venda.strftime('%d-%m-%Y')),  str(sale.valor)])


    table = Table(data)
    table.setStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )

    
    elements.append(table)

    
    doc.build(elements)

    buffer.seek(0)
    return buffer

