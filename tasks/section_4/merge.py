nameOfFiles = ["cis_4.1.1.x.yml","cis_4.1.2.x.yml","cis_4.1.3.x.yml","cis_4.2.1.x.yml","cis_4.2.2.x.yml","cis_4.2.3.yml","cis_4.3.yml"]
with open("section_4.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
