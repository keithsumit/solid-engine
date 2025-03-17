import os

def list_files_to_file(directories, output_file):
    """
    Lists all files from specified directories and writes them to an output file.

    Args:
    directories: A list of directory paths.
    output_file: The path to the output file.
    """
    with open(output_file, 'w') as outfile:
       for directory in directories:
         if os.path.isdir(directory):
             for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    outfile.write(file_path + '\n')
         else:
             print(f"Warning: '{directory}' is not a valid directory.")

if __name__ == "__main__":
    directories_to_scan = ["path_to_dir1", "path_to_dir2", "path_to_dir3", "path_to_dir4", "path_to_dir5"] # Replace with your directory paths
    output_filename = "listallfilesinDir.txt"

    list_files_to_file(directories_to_scan, output_filename)
    print(f"File list written to '{output_filename}'")
