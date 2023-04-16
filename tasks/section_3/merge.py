nameOfFiles = ["cis_3.1.x.yml","cis_3.2.x.yml","cis_3.3.x.yml","cis_3.4.1.x.yml","cis_3.4.2.x.yml","cis_3.4.3.1.x.yml","cis_3.4.3.2.x.yml","cis_3.4.3.3.x.yml"]
with open("section_3.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
