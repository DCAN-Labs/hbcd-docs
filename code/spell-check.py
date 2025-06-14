import os

def replace_respondant_with_respondent(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                if "Respondant" in content:
                    new_content = content.replace("Respondant", "Respondent")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed typo in: {file_path}")

if __name__ == "__main__":
    # Replace with the path to your Markdown directory (e.g., "./docs")
    root_directory = "./docs"
    replace_respondant_with_respondent(root_directory)
