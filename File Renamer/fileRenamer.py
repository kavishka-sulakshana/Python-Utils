import os

directory = input("Enter the path of the directory: ")
if directory == "":
    directory = "."
output_file = 'output.txt' 

file_names = os.listdir(directory)

# Write the file names to a text file
with open(output_file, 'w') as file:
    for file_name in file_names:
        barcode = file_name.split('_')[0][:8]
        file.write(barcode + '\n')
        if file_name[-3:] == "pdf" or file_name[-3:] == "PDF":
            try :
                os.rename(file_name, barcode+".pdf")
            except:
                os.remove(file_name)
        print(barcode + " done!")
    i = input("Press any key to exit")
