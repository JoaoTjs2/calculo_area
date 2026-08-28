from geometry.geo_structures_store import Retangle, Trapezy, Triangle

print("----- TIPOS DE ÁREAS COMPUTÁVEIS -----")
print("|      0       |       1       |       2      |")
print("|  Retângulo   |   Triângulo   |   Trapézio   |")

opcao = int(input("\nQual área deseja computar (0, 1, 2): "))
print("____________________________________________________")

geo_objeto = None

if opcao == 0:
    print("\nOpção escolhida: Cálculo da área do retângulo.\n")
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    geo_objeto = Retangle(comprimento, largura)

elif opcao == 1:
    print("\nOpção escolhida: Cálculo da área do triângulo.\n")
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    geo_objeto = Triangle(base, altura)

elif opcao == 2:
    print("\nOpção escolhida: Cálculo da área do trapézio.\n")
    b_maior = float(input("Digite a base maior do trapézio: "))
    b_menor = float(input("Digite a base menor do trapézio: "))
    altura = float(input("Digite a altura do trapézio: "))
    geo_objeto = Trapezy(b_maior, b_menor, altura)

else:
    print("\nOpção inválida!")

area = geo_objeto.calc_area()
print(f"A área calculada é: {area:.2f}")