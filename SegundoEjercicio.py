cuentas = []

for i in range(0, 3):
    cuenta = {}
    cuenta["numeroCuenta"] = int(input("Digite el numero de cuenta: "))
    cuenta["saldo"] = float(input("Digite el saldo de la cuenta: "))
    cuentas.append(cuenta)
    
cuentasOrdenadas = sorted(cuentas, key=lambda cuenta:cuenta["saldo"], reverse=True)

for mostrarCuenta in cuentasOrdenadas:
    print(f'Cuenta: {mostrarCuenta["numeroCuenta"]}')
    print(f'Saldo: {mostrarCuenta["saldo"]}')