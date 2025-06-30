import os

# Define folder paths
processed_data_path = r"G:/My Drive/Info_Project/Processed_Data"
defect_folders = [os.path.join(processed_data_path, "Defect_Class0"), 
                  os.path.join(processed_data_path, "Defect_Class1")]

# Rename files in Defect0 and Defect1 folders
for defect_folder in defect_folders:
    for file_name in os.listdir(defect_folder):
        if file_name.endswith(".png") or file_name.endswith(".jpg"):
            old_path = os.path.join(defect_folder, file_name)
            new_name = file_name.replace("defect0", "powder").replace("defect1", "printed")
            new_path = os.path.join(defect_folder, new_name)
            os.rename(old_path, new_path)

print("✅ Renaming complete for Defect0 and Defect1 folders!")
