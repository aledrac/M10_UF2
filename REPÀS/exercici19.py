areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print(areas_pis[1])
print(areas_pis[-1])
print(areas_pis[areas_pis.index("Terrassa") + 1])
print(areas_pis[:3])
print(areas_pis[2:])
print(areas_pis[areas_pis.index("Habitació1") + 1] + areas_pis[areas_pis.index("Habitació2") + 1])

areas_pis[areas_pis.index("Lavabo") + 1] = 8.5
print(areas_pis)

areas_pis.extend(["pati interior", 2.78])
print(areas_pis)

total_area_piso = sum(areas_pis[1::2])
print(f"Total de área del piso: {total_area_piso}")
