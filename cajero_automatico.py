# Menú de cajero automático
def cajero():
    print("Bienvenido al Cajero Automático de Codo a Codo.")
    print("Ingresa tu clave para acceder a la cuenta \n (La clave es 1234) ")
    clave = int(input("Ingrese su clave: "))
    nombre = str(input("Ingrese su nombre: "))
    saldo = float(85200)
    saldoDolar = float(0)
    exit = False
    while exit == False:
        if clave == 1234:
            print("#########################################")
            print("Bienvenido a su cuenta", nombre)
            print("#########################################")
            print("Lea las opciones y seleccione la deseada: ")
            print("#########################################")
            print("     #1  Consultar saldo;")
            print("     #2  Depositar dinero;")
            print("     #3  Extraer dinero;")
            print("     #4  Transferir dinero;")
            print("     #5  Comprar dólares;")
            print("     #6  Vender dólares;")
            print("     #7  Crear plazo fijo;")
            print("     #8  Ver últimos movimientos;")
            print("     #9  Salir de la cuenta.")
            print("#########################################")
            opcion = int(input("Ingrese su opción: "))
            print("#####################################################")
            #1consultar saldo
            if opcion == 1:
                print("Su saldo actual en pesos es de: $" ,saldo)
                salir = int(input("Si desea salir presione 1, si desea volver al menú presione 2: "))
                if salir == 1:
                    exit = True
                else:
                    exit = False
            #2depositar dinero
            elif opcion == 2:
                ingreso = int(input("Digite el monto que va a depositar y luego inserte su dinero: "))
                print("#########################################")
                saldo = saldo + ingreso
                print("Gracias por confiar en nuestros servicios, su saldo actual es de: $",saldo)
                print("#####################################################")
                salir = int(input("Si desea salir presione 1, si desea volver al menú presione 2: "))
                if salir == 1:
                    exit = True
                else:
                    exit = False
            #3extraer dinero
            elif opcion == 3:
                extraccion = int(input("Ingrese el monto a extraer: "))
                saldo = saldo - extraccion
                print("Gracias por utilizar nuestros servicios, su saldo restante es de: $" , saldo)
                print("#####################################################")
                salir = int(input("Si desea salir presione 1, si desea volver al menú presione 2: "))
                if salir == 1:
                    exit = True
                else:
                    exit = False
            #4transferir dinero
            elif opcion == 4:
                transferir = str(input("Ingrese el CBU de la cuenta a la cual desea tranferir: "))
                while len(transferir) != 8:
                    print("#####################################################")
                    print("ERROR! El CBU ingresado es inválido, inténtalo nuevamente.")
                    tranferir = str(input("Ingrese el CBU de la cuenta a la cual desea tranferir: "))
                monto = int(input("Ingresa el monto a tranferir: "))
                print("#########################################################")
                print("Se está por efectuar una transferencia de $", monto," al número de cuenta: ",transferir,"¿Desea seguir con la operación?")
                confirmar = str(input("Ingrese: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
                if confirmar == "si":
                    saldo = saldo - monto
                    print("Gracias por utilizar nuestros servicios, su tranferencia ha sido realizada con éxito. Su saldo actual es de: $" , saldo)
                    print("#####################################################")
                elif confirmar == "no":
                    print("Se ha cancelado la operación")
                    print("#####################################################")
                else:
                    print("Has ingresado un valor inválido")
                    print("#####################################################")
                salir = int(input("Si desea salir presione 1, si desea volver al menú presione 2: "))
                if salir == 1:
                    exit = True
                else:
                    exit = False
            #5comprar dolares
            elif opcion == 5:
                print("    El precio del dólar actualmente es de: $160")
                print("    Su saldo actual es de: $" , saldo)
                print("#####################################")
                compraDolar = float(input("Ingrese la cantidad de dólares que desea comprar: "))
                print("#####################################")
                totalPesos = compraDolar * 160
                if totalPesos < saldo:
                    print("¿Confirma la operación de la compra de: u$s" , compraDolar, " dólares por AR$", totalPesos, "?")
                    confirma  = str(input("Ingrese \n     #si para confirmar. \n     #no para cancelar: \n "))
                    if confirma == "si":
                        conversion = compraDolar * 160
                        saldo = saldo - conversion
                        saldoDolar = saldoDolar + compraDolar
                        print("#####################################################")
                        print("Su saldo actual en pesos es de: AR$" , saldo)
                        print("Su saldo actual en dólares es de: u$s" , saldoDolar )
                        print("#####################################################")
                    elif confirma == "no":
                        print("Se ha cancelado la operación.")
                        print("#####################################################")
                else:
                    print("Fondos insuficientes.")
                salir = int(input("Si desea salir presione 1, si desea volver al menú presione 2: "))
                if salir == 1:
                    exit = True
                else:
                    exit = False
            #6vender dolares
            elif opcion == 6:
                if saldoDolar > 1:
                    print("El valor actual del dólar es de: AR$160")
                    print("Su saldo actual en pesos es de: AR$", saldo)
                    print("Su saldo actual en dólares es de: usd$", saldoDolar)
                    print("#####################################################")
                    monto = int(input("Ingrese la cantidad de dólares que desea vender: "))
                    if monto > saldoDolar:
                        print("#####################################################")
                        print("La operación no puede continuar ya que usted no posee el monto que ingresó.")
                        print("#####################################################")
                    else:
                        total = monto * 160
                        op = int(input("El total de la venta en pesos es de AR$", total, ". ¿Desea seguir con la operación? \n    #si para confirmar \n     #no para cancelar: "))
                        if op == "si":
                            saldo = saldo + total
                            saldoDolar = saldoDolar - monto
                            print("¡Venta exitosa!")
                            print("Su saldo actual en pesos es de: AR$", saldo)
                            print("Su saldo actual en dólares es de: usd$", saldoDolar)
                            print("#####################################################")
                        else:
                            print("Se cancelo la operación.")
                            print("#####################################################")
                else:
                    print("No posee dólares en su cuenta de ahorro.")
                    print("#####################################################")
                salir = int(input("Si desea salir presione 1, si desea volver al menú presione 2: "))
                if salir == 1:
                    exit = True
                else:
                    exit = False
            #7crear plazo fijo
            #8ver ultimos movimientos
            #9salir de la cuenta
            elif opcion == 9:
                print("Gracias por utilizar nuestros servicios.")
                print("######## SE CERRÓ LA SESIÓN ########")
                exit = True
        else:
            print("clave incorrecta")
cajero()