# Menu:
print('''##########################################################################
Seja bem vindo ao testador de compatibilidade de tipagem sanguinea!
Vamos verificar se o tipo sanguineo do receptor e do doador são compatíveis?
Menu principal:
[1] A+
[2] A-
[3] B+
[4] B-
[5] O+
[6] O-
[7] AB+
[8] AB-
[9] Sair
#############################################################################
''')

# Digitar o tipo sanguíneo do receptor
while True:
    try:
        receptor = int(input("Digite o tipo sanguíneo do receptor: "))
        if 1 <= receptor <= 9:
            break
        else:
            print("Opção inválida. Por favor, digite um número entre 1 e 9.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Digitar o tipo sanguíneo do doador
while True:
    try:
        doador = int(input("Digite o tipo sanguíneo do doador: "))
        if 1 <= doador <= 9:
            break
        else:
            print("Opção inválida. Por favor, digite um número entre 1 e 9.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Verificar a compatibilidade entre o doador e o receptor:
def verificar_compatibilidade(doador, receptor):
    # Verifica a compatibilidade sanguínea entre doador e receptor.
    compatibilidade = {
        1: (1, 5, 6),  # A+
        2: (2, 6),  # A-
        3: (3, 5, 6),  # B+
        4: (4, 6),  # B-
        5: (5, 6),  # O+
        6: (6,),  # O-
        7: (1, 2, 3, 4, 5, 6, 7, 8),  # AB+
        8: (2, 4, 6, 8)  # AB-
    }

    if receptor == 9 or doador == 9:
        return 'Agradecemos sua consulta!\nVolte sempre!'
    elif doador in compatibilidade:
        if receptor in compatibilidade[doador]:
            return 'Doação compatível!'
        else:
            return 'Doação incompatível!'
    else:
        return 'Opção inválida de tipo sanguíneo.'

resultado = verificar_compatibilidade(doador, receptor)
print(resultado)
