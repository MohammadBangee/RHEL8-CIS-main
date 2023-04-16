nameOfFiles = ["cis_1.1.1.x.yml","cis_1.1.2.x.yml","cis_1.1.3.x.yml","cis_1.1.4.x.yml","cis_1.1.5.x.yml","cis_1.1.6.x.yml","cis_1.1.7.x.yml","cis_1.1.8.x.yml","cis_1.1.x.yml","cis_1.2.x.yml","cis_1.3.x.yml","cis_1.4.x.yml","cis_1.5.x.yml","cis_1.6.1.x.yml","cis_1.7.x.yml","cis_1.8.x.yml","cis_1.9.yml","cis_1.10.yml"]
with open("section_1.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
