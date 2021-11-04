p = '1 049,00'
p_1 = p.replace(',', '.')
price = float(p_1.replace(' ', ''))
print(price)