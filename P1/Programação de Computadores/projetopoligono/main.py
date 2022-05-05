forma = str(input('''Escolha uma das figuras que deseja calcular a área:
Triângulo, Quadrado, Retângulo, Paralelogramo, Trapézio, Losango, Pentágono, Hexágono\n''' )).upper()

if forma in 'TRIANGULO':
    baset = float(input('Quanto vale a base do triângulo? \n'))
    alturat = float(input('Quanto vale a altura do triângulo? \n'))
    areat = (baset * alturat) / 2
    print('Fórmula = (Base * Altura) / 2')
    print(f'({baset} * {alturat}) / 2 ')
    print(f'A área do triângulo vale {areat}.')

elif forma in 'QUADRADO':
    baseq = float(input('Quanto vale a base do quadrado? \n'))
    alturaq = float(input('Quanto vale a altura do quadrado? \n'))
    areaq = baseq * alturaq
    print('Fórmula = Base * Altura')
    print(f'({baseq} * {alturaq}) ')
    print(f'A área do quadrado vale {areaq}.')

elif forma in 'RETANGULO':
    baser = float(input('Quanto vale a base do retângulo? \n'))
    alturar = float(input('Quanto vale a altura do retângulo? \n'))
    arear = baser * alturar
    print('Fórmula = Base * Altura')
    print(f'({baser} * {alturar}) ')
    print(f'A área do retângulo vale {arear}.')

elif forma in 'PARALELOGRAMO':
    basep = float(input('Quanto vale a base do paralelogramo? \n'))
    alturap = float(input('Quanto vale a altura do paralelogramo? \n'))
    areap = basep * alturap
    print('Fórmula = Base * Altura')
    print(f'({basep} * {alturap}) ')
    print(f'A área do paralelogramo vale {areap}.')

elif forma in 'TRAPEZIO':
    basetp1 = float(input('Quanto vale a base maior do trapézio? \n'))
    basetp2 = float(input('Quanto vale a base menor do trapézio? \n'))
    alturatp = float(input('Quanto vale a altura do trapézio? \n'))
    areatp = ((basetp1 + basetp2) * alturatp) / 2
    print('Fórmula = [(Base maior + Base menor) * Altura] / 2')
    print(f'[({basetp1} + {basetp2}) * {alturatp}] / 2')
    print(f'A área do trapézio vale {areatp}.')

elif forma in 'LOSANGO':
    diagonal1 = float(input('Quanto vale a diagonal maior do losango? \n'))
    diagonal2 = float(input('Quanto vale a diagonal menor do losango? \n'))
    areal = (diagonal1 * diagonal2) / 2
    print('Fórmula = (Diagonal maior * Diagonal menor) / 2')
    print(f'({diagonal1} * {diagonal2}) / 2')
    print(f'A área do losango vale {areal}.')

elif forma in 'PENTAGONO':
    ladopen = float(input('Quanto vale o lado do pentágono? \n'))
    apotemapen = float(input('Quanto vale o apotema do pentágono? \n'))
    areapen = ladopen * 5 * apotemapen
    print('Fórmula = 5 * Lado * apotema')
    print(f'(5 * {ladopen} * {apotemapen})')
    print(f'A área do pentágono vale {areapen}.')

elif forma in 'HEXAGONO':
    ladohex = float(input('Quanto vale o lado do hexágono? \n'))
    areahex = (3 * pow(ladohex, 2) * 1.732) / 2
    #Raiz quadrada de 3 = 1,732
    print('Fórmula = (3 * Lado^2 * 1,732) / 2')
    print(f'(3 * {ladohex}^2 * 1,732) / 2')
    print(f'A área do hexágono vale {areahex}.')
