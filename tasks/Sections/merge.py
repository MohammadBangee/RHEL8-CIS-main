nameOfFiles = ["section_1.yml","section_2.yml","section_3.yml","section_4.yml","section_5.yml","section_6.yml"]
with open("RHEL7.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
