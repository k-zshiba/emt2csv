import os

emt_file_folder = "./emtFile"
csv_file_folder = "./csvFile/"

emt_files =  os.listdir(emt_file_folder)
for emt_file in emt_files:
    emt_file_path = emt_file_folder + "/" + emt_file
    if emt_file_path.endswith('.emt'):
        file_name = os.path.splitext(os.path.basename(emt_file))[0]
        with open(emt_file_path, 'r') as f:
            file_text = f.read()
            replaced_text = file_text.replace('\t',',')
            csv_file_path = csv_file_folder + file_name + ".csv"
        with open(csv_file_path, 'w') as csv_file:
            csv_file.write(replaced_text)

