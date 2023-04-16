nameOfFiles = ["cis_2.1.x.yml","cis_2.2.x.yml","cis_2.3.x.yml","cis_2.4.yml"]
with open("section_2.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
