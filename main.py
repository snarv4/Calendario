import calendar
from datetime import datetime


def mostrar_calendario(anio: int, mes: int) -> None:
    """Muestra el calendario de un mes en la consola."""
    print()
    print(calendar.TextCalendar(firstweekday=calendar.MONDAY).formatmonth(anio, mes))


def pedir_numero(mensaje: str, minimo: int, maximo: int) -> int:
    """Solicita al usuario un numero dentro de un rango."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo <= valor <= maximo:
                return valor
            print(f"Introduce un numero entre {minimo} y {maximo}.")
        except ValueError:
            print("Introduce un numero valido.")


def main() -> None:
    hoy = datetime.now()
    print("Calendario basico")

    while True:
        anio = pedir_numero(
            f"Anio ({hoy.year} para el actual): ",
            1,
            9999,
        )
        mes = pedir_numero(
            "Mes (1-12): ",
            1,
            12,
        )

        mostrar_calendario(anio, mes)

        continuar = input("¿Mostrar otro mes? (s/n): ").strip().lower()
        if continuar not in ("s", "si", "sí"):
            print("Hasta luego.")
            break


if __name__ == "__main__":
    main()