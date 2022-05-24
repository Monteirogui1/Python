import json


cadastros = [
    {
        "Nome": "João",
        "Idade": 25,
        "Profissão": ["Analista de Sistemas", "Full Stack Python", "Engenheiro de Software"]
    }, {
        "Nome": "Ana",
        "Idade": 19,
        "Profissão": ["Designer", "Back-End", "Auxiliar de TI"]
    }
]

print(json.dumps(cadastros, ensure_ascii=False, indent=True))