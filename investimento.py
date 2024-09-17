import matplotlib.pyplot as plt

# Função para calcular o montante final de um investimento
def calcular_investimento(valor_inicial, aporte_mensal, taxa_anual, anos):
    meses = anos * 12
    valor_total = valor_inicial
    historico = [valor_inicial]
    
    for mes in range(1, meses + 1):
        valor_total += aporte_mensal
        valor_total *= (1 + (taxa_anual / 12))  # Taxa mensal aplicada ao saldo total
        historico.append(valor_total)
        
    return valor_total, historico

# Dados de entrada fornecidos pelo usuário
valor_inicial = float(input("Digite o valor inicial a ser investido: "))
aporte_mensal = float(input("Digite o valor a ser investido mensalmente: "))
anos = int(input("Por quantos anos deseja investir? "))

# Rentabilidades anuais (%)
tesouro_prefixado = 0.1184  # 11,84% ao ano (Tesouro Prefixado 2027)
tesouro_ipca = 0.0639  # IPCA + 6,39% ao ano (Tesouro IPCA+ 2029)
tesouro_selic = 0.13631  # SELIC + 0,0631% ao ano (Tesouro Selic 2027)
poupanca = 0.006  # 0,6% ao ano (Poupança)

# Cálculo para cada investimento
valor_final_prefixado, historico_prefixado = calcular_investimento(valor_inicial, aporte_mensal, tesouro_prefixado, anos)
valor_final_ipca, historico_ipca = calcular_investimento(valor_inicial, aporte_mensal, tesouro_ipca, anos)
valor_final_selic, historico_selic = calcular_investimento(valor_inicial, aporte_mensal, tesouro_selic, anos)
valor_final_poupanca, historico_poupanca = calcular_investimento(valor_inicial, aporte_mensal, poupanca, anos)

# Exibição dos resultados
print(f"Valor total investido no Tesouro Prefixado: R${valor_final_prefixado:.2f}")
print(f"Valor total investido no Tesouro IPCA: R${valor_final_ipca:.2f}")
print(f"Valor total investido no Tesouro Selic: R${valor_final_selic:.2f}")
print(f"Valor total investido na Poupança: R${valor_final_poupanca:.2f}")

# Gráfico de linhas mostrando a evolução de cada investimento
plt.plot(historico_prefixado, label=f"Tesouro Prefixado (11,84% a.a.)")
plt.plot(historico_ipca, label=f"Tesouro IPCA (IPCA + 6,39% a.a.)")
plt.plot(historico_selic, label=f"Tesouro Selic (SELIC + 0,0631% a.a.)")
plt.plot(historico_poupanca, label="Poupança (0,6% a.a.)")
plt.xlabel("Meses")
plt.ylabel("Valor do Investimento (R$)")
plt.title("Evolução dos Investimentos")
plt.legend()

# Exibir apenas o valor final ao lado de cada linha
plt.text(len(historico_prefixado)-1, historico_prefixado[-1], f'{historico_prefixado[-1]:.2f}', fontsize=10, ha='left')
plt.text(len(historico_ipca)-1, historico_ipca[-1], f'{historico_ipca[-1]:.2f}', fontsize=10, ha='left')
plt.text(len(historico_selic)-1, historico_selic[-1], f'{historico_selic[-1]:.2f}', fontsize=10, ha='left')
plt.text(len(historico_poupanca)-1, historico_poupanca[-1], f'{historico_poupanca[-1]:.2f}', fontsize=10, ha='left')

plt.show()
