tabela_botao = {
    "A": {"G": 9, "P": 7},
    "B": {"G": 7, "P": 5},
    "C": {"G": 4, "P": 3},
}

tabela_camisa = {
    "A": {"Maio": 100, "Junho": 120},
    "B": {"Maio": 80, "Junho": 90},
    "C": {"Maio": 60, "Junho": 70},
}

total_maio = 0
total_junho = 0

for modelo, qtd_botao in tabela_botao.items():
    qtd_maio = tabela_camisa[modelo]["Maio"]
    qtd_junho = tabela_camisa[modelo]["Junho"]
    total_maio += qtd_botao["G"] * qtd_maio + qtd_botao["P"] * qtd_maio
    total_junho += qtd_botao["G"] * qtd_junho + qtd_botao["P"] * qtd_junho

print("Total de botões em maio: ", total_maio)
print("Total de botões em junho: ", total_junho)
