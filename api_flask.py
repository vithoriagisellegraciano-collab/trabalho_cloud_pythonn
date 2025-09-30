from flask import Flask, jsonify

app = Flask(__name__)

# DADOS DA API: Lista de Alunos
# Esta lista será retornada pela rota /alunos
alunos = [
    {"nome": "Guilherme", "curso": "ADS"},
    {"nome": "Luana", "curso": "ADS"},
    {"nome": "Vithoria", "curso": "ADS"}
]

# Rota raiz (página inicial da API)
@app.route("/")
def home():
    # Mensagem de boas-vindas para guiar o usuário
    # As quatro rotas solicitadas estão listadas aqui: /, /alunos, /saudacao/<nome>, /curso/<nome_do_curso>
    return "✅ API rodando! Rotas disponíveis: /alunos, /saudacao/<nome>, /curso/<nome_do_curso>"


# Rota que retorna lista de alunos em formato JSON
@app.route("/alunos")
def get_alunos():
    # Retorna a lista de alunos definida globalmente
    return jsonify(alunos)


# Rota que retorna saudação personalizada, pegando o nome da URL
@app.route("/saudacao/<nome>")
def saudacao(nome):
    # Retorna um objeto JSON com a mensagem formatada
    return jsonify({"mensagem": f"Olá, {nome}! Seja bem-vindo à API."})


# ROTA: Retorna informações básicas sobre um curso
@app.route("/curso/<nome_do_curso>")
def info_curso(nome_do_curso):
    # Dicionário de cursos para busca
    cursos = {
        "ADS": "Análise e Desenvolvimento de Sistemas. Foco em aplicações web e mobile.",
        "CC": "Ciência da Computação. Foco em teoria, algoritmos e fundamentos de software.",
        "ENGENHARIA": "Engenharia de Software. Foco em processos e qualidade de desenvolvimento em larga escala."
    }

    # 1. Busca a informação do curso (convertendo para maiúsculas para evitar erros de digitação)
    # 2. Se o curso não for encontrado, retorna a mensagem de 'não encontrado'
    info = cursos.get(nome_do_curso.upper(), f"Informação sobre o curso '{nome_do_curso}' não encontrada.")

    # 3. Retorna o resultado da busca em formato JSON
    return jsonify({"curso": nome_do_curso, "descricao": info})


if __name__ == "__main__":
    # Inicia a aplicação em modo de depuração (debug=True)
    app.run(debug=True)