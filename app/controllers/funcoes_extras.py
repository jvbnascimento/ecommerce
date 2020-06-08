def formatar_mostragem_cpf(cpf):
    cpf = cpf
    cpf_formatado = ""

    for c in cpf[3:]:
        if (c != '.' and c != '-'):
            cpf_formatado += "X"
        else:
            cpf_formatado += c

    return (cpf[:3] + cpf_formatado)


def formatar_mostragem_telefone(telefone):
    telefone = telefone

    telefone_formatado = ""

    for t in range(len(telefone[2:])):
        if (t != 5):
            telefone_formatado += telefone[t+2]
        else:
            telefone_formatado += "-" + telefone[t+2]

    telefone_formatado = "(" + telefone[:2] + ") " + telefone_formatado

    return telefone_formatado


def formatar_mostragem_endereco(endereco):
	endereco = endereco.split("Nº: ")
	
	endereco_completo = []
	endereco_formatado = ""

	endereco_sem_espaco = endereco[0].replace(",", "").split(" ")
	endereco_sem_espaco.pop()

	for e in range(len(endereco_sem_espaco)):
		if (e != len(endereco_sem_espaco)-1):
			endereco_formatado += endereco_sem_espaco[e] + " "
		else:
			endereco_formatado += endereco_sem_espaco[e]


	endereco_completo.append(endereco_formatado)
	endereco_completo.append(endereco[1])

	return endereco_completo
