nameOfFiles = ["cis_6.1.x.yml","cis_6.2.x.yml"]
with open("section_6.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
