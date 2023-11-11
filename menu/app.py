"""from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Carrega os dados dos arquivos Excel
dados_excel1 = pd.read_excel('menu/tabelas/Contratos-2023.xlsx')
dados_excel2 = pd.read_excel('menu/tabelas/Obras-2023.xlsx')
dados_excel3 = pd.read_excel('menu/tabelas/DespesasPagas-2023.xlsx')

# Rota para a primeira página
@app.route('/contratos', methods=['GET', 'POST'])
def pagina1():
    dados_filtrados = dados_excel1.copy()

    if request.method == 'POST':
        # Aplica filtros aos dados do primeiro arquivo Excel
        # Suponha que os filtros estejam em um formulário HTML com campos de filtro chamados 'campo1' e 'campo2'
        filtro1 = int(request.form['campo1'])
        filtro2 = int(request.form['campo2'])
        
        # Aplica os filtros aos dados
        dados_filtrados = dados_filtrados[dados_filtrados['NumeroContrato'] == filtro1]
        dados_filtrados = dados_filtrados[dados_filtrados['AnoContrato'] == filtro2]

    tabela_html = dados_filtrados.to_html(index=False, classes='table table-striped table-sm')
    return render_template('contratos.html', tabela_html=tabela_html)

# Rota para a segunda página
@app.route('/obras', methods=['GET', 'POST'])
def pagina2():
    dados_filtrados = dados_excel2.copy()

    if request.method == 'POST':
        # Aplica filtros aos dados do segundo arquivo Excel
        # Suponha que os filtros estejam em um formulário HTML com campos de filtro chamados 'campo3' e 'campo4'
        filtro3 = request.form['campo3']
        filtro4 = request.form['campo4']
        
        # Aplica os filtros aos dados
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna3'] == filtro3]
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna4'] == filtro4]

    tabela_html = dados_filtrados.to_html(index=False, classes='table table-striped table-sm')
    return render_template('obras.html', tabela_html=tabela_html)

# Rota para a terceira página
@app.route('/despesas', methods=['GET', 'POST'])
def pagina3():
    dados_filtrados = dados_excel3.copy()

    if request.method == 'POST':
        # Aplica filtros aos dados do terceiro arquivo Excel
        # Suponha que os filtros estejam em um formulário HTML com campos de filtro chamados 'campo5' e 'campo6'
        filtro5 = request.form['campo5']
        filtro6 = request.form['campo6']
        
        # Aplica os filtros aos dados
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna5'] == filtro5]
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna6'] == filtro6]

    tabela_html = dados_filtrados.to_html(index=False, classes='table table-striped table-sm')
    return render_template('despesas.html', tabela_html=tabela_html)

if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Carregar dados do Excel
dados_excel1 = pd.read_excel('menu/tabelas/Contratos-2023.xlsx')
dados_excel2 = pd.read_excel('menu/tabelas/Obras-2023.xlsx')
dados_excel3 = pd.read_excel('menu/tabelas/DespesasPagas-2023.xlsx')

# Rota para a primeira página com o formulário de filtro
@app.route('/contratos', methods=['GET', 'POST'])
def contratos():
    if request.method == 'POST':
        filtro_numero_contrato = request.form.get('campo1')
        filtro_ano_contrato = request.form.get('campo2')
        filtro_tipo_contrato = request.form.get('campo3')
        filtro_processo = request.form.get('campo4')
        filtro_ano_processo = request.form.get('campo5')
        filtro_valor_contratado = request.form.get('campo6')
        filtro_cpf_cnpj = request.form.get('campo7')
        filtro_fornecedor = request.form.get('campo8')
        filtro_coronavirus = request.form.get('campo9')

        # Aplicando filtros aos dados
        dados_filtrados = dados_excel1

        if filtro_numero_contrato:
            dados_filtrados = dados_filtrados[dados_filtrados['NumeroContrato'] == int(filtro_numero_contrato)]

        if filtro_ano_contrato:
            dados_filtrados = dados_filtrados[dados_filtrados['AnoContrato'] == int(filtro_ano_contrato)]

        if filtro_processo:
            dados_filtrados = dados_filtrados[dados_filtrados['Processo'] == int(filtro_processo)]

        if filtro_ano_processo:
            dados_filtrados = dados_filtrados[dados_filtrados['AnoProcesso'] == int(filtro_ano_processo)]

        if filtro_valor_contratado:
            dados_filtrados = dados_filtrados[dados_filtrados['ValorContratado'] == float(filtro_valor_contratado)]

        if filtro_cpf_cnpj:
            dados_filtrados = dados_filtrados[dados_filtrados['CPFCNPJ'] == int(filtro_cpf_cnpj)]

        if filtro_fornecedor:
            dados_filtrados = dados_filtrados[dados_filtrados['Fornecedor'] == filtro_fornecedor]

        if filtro_tipo_contrato and filtro_tipo_contrato != 'Todos':
            dados_filtrados = dados_filtrados[dados_filtrados['TipoContrato'] == filtro_tipo_contrato]

        if filtro_coronavirus == 'true':
            dados_filtrados = dados_filtrados[dados_filtrados['Coronavirus'] == True]
        elif filtro_coronavirus == 'false':
            dados_filtrados = dados_filtrados[dados_filtrados['Coronavirus'] == False]

    else:
        dados_filtrados = dados_excel1
        # Não aplique o filtro se a opção "Todos" for selecionada    
    tabela_html = dados_filtrados.to_html(index=False, classes='table table-striped table-sm')
    return render_template('contratos.html', tabela_html=tabela_html)

# Rota para a segunda página
@app.route('/obras', methods=['GET', 'POST'])
def pagina2():
    dados_filtrados = dados_excel2.copy()

    if request.method == 'POST':
        # Aplica filtros aos dados do segundo arquivo Excel
        # Suponha que os filtros estejam em um formulário HTML com campos de filtro chamados 'campo3' e 'campo4'
        filtro3 = request.form['campo3']
        filtro4 = request.form['campo4']
        
        # Aplica os filtros aos dados
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna3'] == filtro3]
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna4'] == filtro4]

    tabela_html = dados_filtrados.to_html(index=False, classes='table table-striped table-sm')
    return render_template('obras.html', tabela_html=tabela_html)

# Rota para a terceira página
@app.route('/despesas', methods=['GET', 'POST'])
def pagina3():
    dados_filtrados = dados_excel3.copy()

    if request.method == 'POST':
        # Aplica filtros aos dados do terceiro arquivo Excel
        # Suponha que os filtros estejam em um formulário HTML com campos de filtro chamados 'campo5' e 'campo6'
        filtro5 = request.form['campo5']
        filtro6 = request.form['campo6']
        
        # Aplica os filtros aos dados
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna5'] == filtro5]
        dados_filtrados = dados_filtrados[dados_filtrados['Nome da Coluna6'] == filtro6]

    tabela_html = dados_filtrados.to_html(index=False, classes='table table-striped table-sm')
    return render_template('despesas.html', tabela_html=tabela_html)

if __name__ == '__main__':
    app.run(debug=True)
