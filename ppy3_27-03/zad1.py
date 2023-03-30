def calculate_panels(fl, fw, pl, pw, no):
    farea = 1.1 * (fl * fw)
    parea = pl * pw

    res_float = (farea / parea) / no
    res_int = int(res_float)

    if res_float > res_int:
        res_int += 1

    return res_int

if __name__ == '__main__':
    floor_length = float(input("Podaj długość podłogi [m]: "))
    floor_width = float(input("Podaj szerokość podłogi [m]: "))
    panel_length = float(input("Podaj długość panelu [m]: "))
    panel_width = float(input("Podaj szerokość panelu [m]: "))
    no_of_panels = float(input("Podaj ilość paneli w opakowaniu: "))

    print(f"Potrzebna ilość opakowań to {calculate_panels(floor_length, floor_width, panel_length, panel_width, no_of_panels)}")