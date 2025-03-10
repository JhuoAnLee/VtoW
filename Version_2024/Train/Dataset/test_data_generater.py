import os

from tqdm import tqdm

# generate test data from news data

if __name__ == "__main__":
    SRC_DATASET_PATH = ".\Test_Datasets\\"
    TARGET_DATASET_PATH = ".\Test_Datasets\\"

    target_languages = ["bopomofo", "cangjie", "pinyin", "english"]
    prefixes = ["0", "r0-1"]


    for file in os.listdir(TARGET_DATASET_PATH):
        if not file.endswith("_test.txt"):
            os.remove(TARGET_DATASET_PATH + file)
        elif file.find("labeled_") >= 0:
            os.remove(TARGET_DATASET_PATH + file)
    
    for target_language in target_languages:
        for prefix in prefixes:
                files = os.listdir(SRC_DATASET_PATH)
                src_file_names = [file for file in files if file.startswith(f"{prefix}_")]
                assert len(src_file_names) == 4
                target_file_name = f"labeled_{target_language}_{prefix}_test.txt"
                if os.path.exists(TARGET_DATASET_PATH + target_file_name):
                    if "y" == input("File already exists. Do you want to overwrite it? (y/n)"):
                        print("Removing old file: " + target_file_name)
                        os.remove(TARGET_DATASET_PATH + target_file_name)
                    else:
                        print("File not overwritten. Exiting...")
                        exit()

                for file_name in tqdm(src_file_names, desc="Processing files"):
                    with open(SRC_DATASET_PATH + file_name, "r", encoding="utf-8") as file:
                        lines = file.readlines()
                        lines = [line.replace("\n", "") for line in lines] # remove the \n in the line
                        new_lines = [line + "\t1" if target_language in file_name else line + "\t0" for line in lines]
                    
                    with open(os.path.join(TARGET_DATASET_PATH, target_file_name), "a", encoding="utf-8") as file:
                        for line in new_lines:
                            file.write(line + "\n")
