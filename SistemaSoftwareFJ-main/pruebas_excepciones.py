"""
Pruebas de excepciones del Sistema Software FJ
Este archivo directamente es para ver el comportamiento
del manejo de excepciones ante casos válidos e inválidos.
"""

from modelos.cliente import Cliente
from modelos.asesoria import Asesoria
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.reserva_sala import ReservaSala
from modelos.reserva import Reserva
from excepciones.excepciones import SoftwareFJError


def prueba(descripcion, funcion):
    """Ejecuta una prueba individual mostrando el resultado de forma clara."""
    print(f"\n--- {descripcion} ---")
    try:
        resultado = funcion()
    except SoftwareFJError as error:
        print(f"Error controlado: {error}")
    else:
        print(f"Operación exitosa: {resultado}")
    finally:
        print("Prueba finalizada.")


# 1. Cliente válido
prueba(
    "Cliente válido",
    lambda: Cliente(1, "Veronica Valencia", "12345678", "veronica@unad.edu.co", "3101234567")
)

# 2. Cliente con nombre vacío (inválido)
prueba(
    "Cliente con nombre vacío",
    lambda: Cliente(2, "", "12345678", "correo@correo.com", "3001234567")
)

# 3. Cliente con documento no numérico (inválido)
prueba(
    "Cliente con documento inválido",
    lambda: Cliente(3, "Pedro Perez", "ABC123", "pedro@correo.com", "3001112233")
)

# 4. Cliente con correo mal formado (inválido)
prueba(
    "Cliente con correo inválido",
    lambda: Cliente(4, "Laura Gomez", "98765432", "correo-sin-arroba.com", "3009998877")
)

# 5. Servicio de Asesoría válido
prueba(
    "Asesoría válida",
    lambda: Asesoria(1, "Asesoría en Redes", 120000, "Redes")
)

# 6. Servicio de Asesoría con especialidad vacía (inválido)
prueba(
    "Asesoría con especialidad vacía",
    lambda: Asesoria(2, "Asesoría sin especialidad", 100000, "")
)

# 7. Alquiler de equipo con costo inválido (negativo)
prueba(
    "Alquiler de equipo con costo negativo",
    lambda: AlquilerEquipo(3, "Alquiler de Portátil", -50000, "Portátil")
)

# 8. Reserva de sala con capacidad inválida (cero)
prueba(
    "Reserva de sala con capacidad en cero",
    lambda: ReservaSala(4, "Sala de Juntas", 90000, 0)
)

# 9. Reserva válida
cliente_prueba = Cliente(5, "Carlos Ruiz", "11223344", "carlos@correo.com", "3005556677")
servicio_prueba = Asesoria(6, "Asesoría en Sistemas", 150000, "Sistemas")
prueba(
    "Reserva válida",
    lambda: Reserva(1, cliente_prueba, servicio_prueba, 3)
)

# 10. Reserva con duración inválida (negativa)
prueba(
    "Reserva con duración negativa",
    lambda: Reserva(2, cliente_prueba, servicio_prueba, -1)
)