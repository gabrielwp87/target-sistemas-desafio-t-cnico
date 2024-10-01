#  Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

# IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json


json_file = 'dados.json'

output_json = json.load(open(json_file))

def daily_billing(output_json):
    days_count = 0
    total_income = 0
    max_income = 0
    min_income = 1_000_000
    days_above_average = 0

    for value in output_json:
        income = float(value["valor"])

        if income > 0.0:
            days_count += 1
            total_income += income

            if income > max_income:
                max_income = income

            if income < min_income:
                min_income = income

    average = total_income / days_count

    for value in output_json:
        income = float(value["valor"])

        if income > average:
            days_above_average += 1

    min_income_str = str(round(min_income, 2)).replace('.', ',')
    max_income_str = str(round(max_income, 2)).replace('.', ',')
    average_str = str(round(average, 2)).replace('.', ',')

    print(f'O menor valor de faturamento ocorrido em um dia do mês foi: R$ {min_income_str}.')
    print(f'O maior valor de faturamento ocorrido em um dia do mês foi: R$ {max_income_str}.')
    print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal(R$ {average_str}) foi: {days_above_average} dias.')

daily_billing(output_json)