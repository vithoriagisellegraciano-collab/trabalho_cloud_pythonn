import json

# Lista de alunos (simulando dados que poderiam vir da nuvem)
alunos = [
    {"nome": "Guilherme", "curso": "ADS"},
    {"nome": "Luana", "curso": "ADS"},
    {"nome": "Vithoria", "curso": "ADS"}
]

# Salvando em arquivo local
with open("alunos.json", "w") as f:
    json.dump(alunos, f, indent=4)

print("Arquivo 'alunos.json' salvo com sucesso!")