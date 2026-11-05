






op = 0
productos = {123: {'nombre': 'Zapas', 'stock': 50, 'precio_venta': 60.0, 'precio_compra': 40.0}, 
             456: {'nombre': 'Camisetas', 'stock': 70, 'precio_venta': 80.0, 'precio_compra': 30.0}, 
             789: {'nombre': 'Pantalones', 'stock': 50, 'precio_venta': 60.0, 'precio_compra': 50.0}}

menu = """
- 1. Mostrar la info de todos los productos.
- 2. Solicitar un producto y mostrar su stock. 
- 3. Añadir un nuevo producto al diccionario
- 4. Vender un producto."""



while op != 9:
    print(menu)
    op = int(input("Introduce una op: "))
    
    if op == 1:
        # MUESTRO LA INFO DE LOS PRODUCTOS

        for id_producto in productos:
            valor = productos[id_producto]
            nombre_producto = valor["nombre"]
            stock = valor["stock"]
            precio_venta = valor["precio_venta"]
            
            print(f"ID : {id_producto} nombre: {nombre_producto}, stock {stock} precio: {precio_venta}")
            
            
                
                
    elif op == 2: 
        # MUESTRO EL STOCK DE UN SOLO PRODUCTO
        id_producto_pedido = int(input("Introduce el id del producto: "))
        while id_producto_pedido not in productos:
            print("Error no tenemos ese producto: ")
            id_producto_pedido = int(input("Introduce el id del producto: "))
            
        info_producto = productos[id_producto_pedido]

        stock = info_producto["stock"]
        print(f"El stock del producto con id producto: {id_producto_pedido} es {stock}")
    elif op == 3:
        # AÑADO UN NUEVO PRODUCTO
        
        id_producto = int(input("Introduce el id del producto: "))
        while id_producto in productos:
            print("Ya tenemos un producto con ese ID, prueba de nuevo")
            id_producto = int(input("Introduce el id del producto: "))
            
            
        nombres_productos = []

        for id_producto in productos:
            nombre_producto = productos[id_producto]["nombre"]
            nombres_productos.append(nombre_producto)
            
        nombre = input("Introduce el nombre: ").capitalize()


        while nombre in nombres_productos:
            print("Ya tenemos ese nombre: ")
            nombre = input("Introduce el nombre: ").capitalize()


        stock = int(input("Stock: "))
        pventa = float(input("Pventa: "))
        pcompra = float(input("Pcompra: "))

        productos[id_producto] = {"nombre":nombre, "stock": stock, "precio_venta":pventa, "precio_compra":pcompra}

    elif op == 4:
        id_producto = int(input("Introduce el ID del producto: "))
        while id_producto not in productos:
            id_producto = int(input("Introduce el ID del producto: "))
            

        productos[id_producto]["stock"] -= 1

        pventa = productos[id_producto]["precio_venta"] 
        pcompra = productos[id_producto]["precio_compra"]

        ganancia = pventa - pcompra
        print(f"Debes pagar: {pventa}")
        print(f"Estoy ganando: {ganancia}")

        print(productos)


        

