import requests

# URL da API pública do GitHub
url = "https://api.github.com/repos/torvalds/linux"

# Fazendo a requisição HTTP
resp = requests.get(url)

# Convertendo resposta para JSON (dicionário Python)
data = resp.json()

# Exibindo alguns campos
print("Repositório:", data["name"])
print("Descrição:", data["description"])
print("Número de estrelas:", data["stargazers_count"])