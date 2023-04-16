nameOfFiles = ["cis_5.1.x.yml","cis_5.2.x.yml","cis_5.3.x.yml","cis_5.4.x.yml","cis_5.5.x.yml","cis_5.6.1.x.yml","cis_5.6.x.yml"]
with open("section_5.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
