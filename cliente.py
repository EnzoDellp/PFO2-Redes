import requests

BASE_URL = 'http://127.0.0.1:5000'

def registrar_usuario():
    print("\n== Registro ==")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    payload = {'usuario': usuario, 'contraseña': contraseña}
    response = requests.post(f'{BASE_URL}/registro', json=payload)

    print(f"📡 Respuesta ({response.status_code}): {response.json()}")

def iniciar_sesion():
    print("\n== Login ==")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    payload = {'usuario': usuario, 'contraseña': contraseña}
    response = requests.post(f'{BASE_URL}/login', json=payload)

    print(f"📡 Respuesta ({response.status_code}): {response.json()}")
    if response.status_code == 200:
        return True
    return False

def ver_tareas():
    print("\n== Página de bienvenida ==")
    response = requests.get(f'{BASE_URL}/tareas')
    print(f"\n HTML recibido:\n{response.text}")

def menu():
    while True:
        print("\n=== Menú del Cliente ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver página de bienvenida (/tareas)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            if iniciar_sesion():
                print(" Acceso permitido")
            else:
                print(" Acceso denegado")
        elif opcion == '3':
            ver_tareas()
        elif opcion == '4':
            print(" Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == '__main__':
    menu()
