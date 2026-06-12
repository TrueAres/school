pigments_file_name = input()
pigment_data = input()

with open(pigments_file_name, "w") as pigments_file:
    pigments_file.write(pigment_data)
    pigments_file.write("\n")