import random 

usuarios = [
    {
        "nombre": "Juan Perez",
        "correo": "juan@bancolombia.com",
        "password": "123",
        "empresa": "Bancolombia",
        "rol": "Gestor"
    },
   
    {
        "nombre": "Maria Gomez",
        "correo": "maria@epm.com.co",
        "password": "abc",
        "empresa": "EPM",
        "rol": "Gestor"
    },
    
    {
        "nombre": "Carlos Ruiz",
        "correo": "carlos@nutresa.com",
        "password": "456",
        "empresa": "Grupo Nutresa",
        "rol": "Supervisor"
    },
   
    {
        "nombre": "Ana Lopez",
        "correo": "ana@postobon.com",
        "password": "789",
        "empresa": "Postobón",
        "rol": "Gestor"
    },
   
    {
        "nombre": "Pedro Diaz",
        "correo": "pedro@bancolombia.com",
        "password": "000",
        "empresa": "Bancolombia",
        "rol": "Auxiliar"
    }
]

def login():
    print("--- BIENVENIDO AL SISTEMA MEDELLÍN RECICLA 🌌 ---")
    intentos = 0
    max_intentos = 3
    while intentos < max_intentos:
        correo_ingresado = input("-👌Ingrese su correo: ")
        pass_ingresado = input("-👌Ingrese su contraseña: ")
        
        usuario_encontrado = False
        
        for usuario in usuarios:
            if usuario["correo"] == correo_ingresado and usuario["password"] == pass_ingresado:
                print(f"\n¡Bienvenido/a {usuario['nombre']} de la empresa {usuario['empresa']}! 🙌 ")
                return True
        
        if usuario_encontrado == False:
            intentos = intentos + 1
            print(f"Error: Datos incorrectos💥. Intentos restantes: {max_intentos - intentos}")
            print("-" * 30)

    print("Ha excedido el número máximo de intentos. El programa se cerrará. ❌ ")
    return False

def simular_recolecciones():
    print("\n--- 🟩 INICIANDO SIMULACIÓN DE RECOLECCIÓN ---")
    recolecciones = {} 
    tipos_materiales = ["PET", "CARTON", "VIDRIO", "METAL"]
    
    for material in tipos_materiales:
        lista_temporal = [] 
        
        for i in range(20):
            peso = random.randint(1, 25) 
        lista_temporal.append(peso)
            
        recolecciones[material] = lista_temporal
        print(f"-> 💯 Se generaron 20 datos para: {material}")

    return recolecciones

def generar_reporte(datos_recoleccion):
    print("\n" + "="*40)
    print(" 👉 REPORTE DE CLASIFICACIÓN POR MATERIAL")
    print("="*40)
    
    suma_total_global = 0
    cantidad_total_global = 0
    
    for material, lista_pesos in datos_recoleccion.items():
        
        suma_material = sum(lista_pesos)
        cantidad_datos = len(lista_pesos)
        promedio = suma_material / cantidad_datos
        
        suma_total_global += suma_material
        cantidad_total_global += cantidad_datos
        
        clasificacion = ""
        if promedio < 8:
            clasificacion = "Bajo :( (hay que mejorar cultura/flujo)"
        elif promedio >= 8 and promedio <= 15:
            clasificacion = "Estable ☝ "
        else:
            clasificacion = "Alto 🤑 (excelente… o están reciclando hasta la paciencia)"
            
        print(f"Material: {material}")
        print(f"- Promedio: {promedio:.2f} kg") 
        print(f"- Estado: {clasificacion}")
        print("-" * 20)
        
    return suma_total_global, cantidad_total_global

def reporte_global(suma_total, cantidad_total):
    print("="*40)
    print(" 👉 REPORTE DE DESEMPEÑO GLOBAL")
    print("="*40)
    
    if cantidad_total > 0:
        promedio_global = suma_total / cantidad_total
    else:
        promedio_global = 0
        
    print(f"-> 💥 Promedio Global Acumulado: {promedio_global:.2f} kg")
    
    if promedio_global < 10:
        print("ESTADO: ALERTA 💥 (No estan reciclando la paciencia!!)")
    elif promedio_global >= 10 and promedio_global < 15:
        print("ESTADO: OPERACIÓN NORMAL ✅ ")
    else:
        print("ESTADO: JORNADA SOBRESALIENTE (¡Excelente trabajo con la paciencia!)")
        
    print("="*40)
    print("FIN DEL REPORTE 💢 ")

acceso = login()

if acceso == True:
    datos_del_dia = simular_recolecciones()

    suma_acumulada, cantidad_acumulada = generar_reporte(datos_del_dia)
    
    reporte_global(suma_acumulada, cantidad_acumulada)
    
else:
    print("No se pudo iniciar el sistema❌. Verifique sus credenciales.")