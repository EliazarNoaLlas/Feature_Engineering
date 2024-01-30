def calcular_importes(metros_cubicos):
    cargo_fijo = 4.27

    if 0 <= metros_cubicos <= 8:
        tarifa_agua = 0.8673
        factor_ajuste = 0.0089
        tarifa_alcantarillado = 0.7615
    elif 9 <= metros_cubicos <= 22:
        tarifa_agua = 1.4907
        factor_ajuste = 0
        tarifa_alcantarillado = 1.3123
    else:  # Mayor a 22
        tarifa_agua = 3.6776
        factor_ajuste = 0
        tarifa_alcantarillado = 3.2357

    tarifa_final_agua = tarifa_agua * (1 + factor_ajuste)
    tarifa_final_alcantarillado = tarifa_alcantarillado * (1 + factor_ajuste)

    importe_agua = metros_cubicos * tarifa_final_agua + cargo_fijo
    importe_desague = metros_cubicos * tarifa_final_alcantarillado + cargo_fijo
    subtotal = importe_agua + importe_desague
    total_pagar = subtotal * 1.18

    return importe_agua, importe_desague, cargo_fijo, subtotal, total_pagar

def main():
    metros_cubicos = float(input("Ingrese el consumo de agua en m^3: "))

    importe_agua, importe_desague, cargo_fijo, subtotal, total_pagar = calcular_importes(metros_cubicos)

    print("\nDescripción de conceptos \tImporte")
    print(f"Servicio de agua potable \tS/ {importe_agua:.2f}")
    print(f"Servicio de desagüe \t\tS/ {importe_desague:.2f}")
    print(f"Cargo fijo \t\t\tS/ {cargo_fijo:.2f}")
    print(f"Subtotal \t\t\tS/ {subtotal:.2f}")
    print(f"IGV (18%) \t\t\tS/ {(subtotal * 0.18):.2f}")
    print(f"Total a Pagar \t\t\tS/ {total_pagar:.2f}")

if __name__ == "__main__":
    main()
