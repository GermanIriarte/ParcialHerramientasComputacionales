def cafeteria():
    cedula=int(input("Digite su cédula: "))
    rol=int(input("Digite 1 si es profesor o 2 si es estudiante: "))
    deseo=1
    precioacumulado=0
    listaproductos=[]
    while deseo==1:
        codigoproducto=input("Digite el código del producto que desea comprar: ")
        cantidad=int(input("Digite la cantidad que desea comprar del producto: "))
        precio=float(input("Digite el precio por unidad del producto: "))
        precio=precio*cantidad
        precioacumulado=precioacumulado+precio
        listaproductos.append(codigoproducto)
        seguir=int(input("""¿Desea comprar más productos?
(1) Sí
(2) No
"""))
        if seguir==2:
            deseo=2
    if rol==1:
        precioacumulado=precioacumulado*(1-0.2)
        print ("El profesor con cédula", cedula, "debe pagar", precioacumulado, "por los productos:", listaproductos)
    elif rol==2:
        precioacumulado=precioacumulado*(1-0.5)
        print ("El estudiante con cédula", cedula, "debe pagar", precioacumulado, "por los productos:", listaproductos)
    else:
        print("No se pudo efectuar la compra, persona no vinculada a la universidad")
    
cafeteria()

        
    
