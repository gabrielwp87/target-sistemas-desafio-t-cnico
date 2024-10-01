# •	SP – R$67.836,43 
# •	RJ – R$36.678,66 
# •	MG – R$29.229,88 
# •	ES – R$27.165,48 
# •	Outros – R$19.849,53
values = {"SP": 67_836.43,
          "RJ": 36_678.66,
          "MG": 29_229.88,
          "ES": 27_165.48,
          "Outros": 19_849.53 }


def mensal_value(values):
    values_sum = 0
    
    for value in values.values():
        values_sum += value

    for key, value in values.items():
        if key != "Outros":
            print(f"O estado {key} dentro do valor total mensal da distribuidora teve o percentual de representação de {round((value/values_sum)*100, 2)}%.")
        else:
            print(f"Os {key} estados dentro do valor total mensal da distribuidora tiveram o percentual de representação de {round((value/values_sum)*100, 2)}%.")

mensal_value(values)