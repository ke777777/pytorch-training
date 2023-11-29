from pathlib import Path
#問1
data_directory = "./data"
data_directory_path = Path(data_directory).resolve()
print("問1:\n---Displaying the abusolute path of data---")
print(data_directory_path)
#問2
file_list = list(data_directory_path.glob("*"))
print("問2:",file_list)
#問3
png_list = list(data_directory_path.glob("*/*.png"))
print("問3:",len(png_list))