nameOfFiles = ["section_1_main.yml","section_2_main.yml","section_3_main.yml","section_4_main.yml","section_5_main.yml","section_6_main.yml"]
with open("RHEL7_main.yml", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")
