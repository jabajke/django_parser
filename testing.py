q = "('Холодильники',)"
q_1 = q.replace('(', '')
q_2 = q_1.replace(')', '')
q_3 = q_2.replace("'", "")
q_4 = q_3.replace(",", '')
print(q_4)

