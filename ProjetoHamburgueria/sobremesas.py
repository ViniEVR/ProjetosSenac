def cardapioSobremesas():
    print('Escolha a sobremesa que deseja!\n' +
          '\n\n\n1. Torta Gelada Negresco R$ 64,90\n ingredientes: Torta gelada com base de bolacha Negresco e mousse de maracujá. Manter refrigerado.' +
          '\n\n\n2. Torta Gelada Maracuja R$ 64,90\n ingredientes: Torta gelada com base de pão de ló ou casquinha de bolacha com recheio a base de maracujá, creme de leite e leite condensado. Manter refrigerado.' +
          '\n\n\n3. Mousse Sabores R$ 59,00\n ingredientes: Escolha entre os sabores chocolate, maracujá, morango ou napolitano (chocolate, morango e baunilha). Manter refrigerado.' +
          '\n\n\n4. Cheesecake Gelado R$ 69,00\n ingredientes: Sobremesa com base de bolacha e recheio composto de cream cheese e leite condensado, com cobertura de frutas vermelha.' +
          '\n\n\n5. Sobremesa de Amendoim R$ 52,00\n ingredientes: Sobremesa cremosa composta de amendoim, açúcar, manteiga e creme de leite. ')
    this.opcao = int(input())  # Coletar a digitação do usuário

def selecionarSobremesa():
    while this.opcao != 4:
        mostrarCardapio()
        if this.opcao == 1:
            print('1 né')

        if this.opcao == 2:
            print('2 né')

        if this.opcao == 3:
            print('3 né')

        if this.opcao == 4:
                print('4 né')
        else:
            print('____________________________________________')
            print('\nSelecione uma opção válida\n')
            print('____________________________________________')
            selecionarSobremesa()