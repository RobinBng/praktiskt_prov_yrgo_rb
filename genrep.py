#Author: Robin Bengtsson
# Date: 2025-10-07

serie = 0
parallell = 0

print("Ei24 - genrep praktiskt prov ht25")
resistors = input(f"Ange resistorer: ")
if(resistors):
    resistor_list = resistors.split()

    for i in resistor_list:
        serie += int(i)
        parallell += (1 / int(i))
    parallell = 1 / parallell

    print(f"Serieresistans: {serie}")
    print(f"Parallellresistans: {parallell}")
else:
    print("Du har inte angett något värde")