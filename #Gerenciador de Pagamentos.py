#Gerenciador de Pagamentos

import qrcode
import matplotlib.pyplot as plt

print('{:=^50}'.format('Fernanda Locações e Eventos'))
v = float(input('Preço das compras: R$ '))
opcao = 0
print('FORMAS DE PAGAMENTO')
while opcao != 5:
    print('''
    [1] Pix
    [2] á vista cartão
    [3] 2x ou mais no cartão
    [4] á vista dinheiro
    [5] Sair
    ''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        pix_key = "fermichelinedecor@gmail.com"  # Insira sua chave PIX
        beneficiario = "Fernanda Micheline"
        cidade = "Uberlândia"
        valor = v  # Valor em reais (se quiser deixar em aberto, não defina um valor)

        # Estrutura do código PIX conforme o padrão BR Code (sem espaços e quebras de linha)
        pix_code = f"""
        000201
        010212
        26{len(pix_key):02d}{pix_key}
        52040000
        5303986
        5802BR
        59{len(beneficiario):02d}{beneficiario[:25]}
        60{len(cidade):02d}{cidade[:15]}
        62070503***
        6304
        """

        # Gerar o QR Code a partir do código PIX
        qr = qrcode.make(pix_code)

        # Mostrar o QR Code na tela usando matplotlib
        plt.imshow(qr, cmap='gray')  # Exibir a imagem em escala de cinza
        plt.axis('off')  # Ocultar os eixos
        plt.show()
    if opcao == 2:
        d = (v*0.05)
        n = v-d
        print('Sua compra de R${} vai custar R${}'.format(v,n))
    if opcao == 3:
        p = int(input('Quantas parcelas? '))
        if p == 2:
            n=v/p
            print('Sua compra de R${} vai custar {} vezes de R${}'.format(v,p,n))
        elif p > 2:
            j = (v*0.2)+v
            n = j/p
            print('Sua compra de R${}  vai custar com o aumento de 20% de juros R${}, dividido em {} vezes de R${}'.format(v,j,p,n))
    if opcao == 4:
        d = v-(v*0.1)
        print('Sua compra de R${} com desconto de 10% vai custar R${}'.format(v,d))
    elif opcao ==5:
        print('Encerrando...')
        break