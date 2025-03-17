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
    directories_to_scan = ["/home/supandit/sandbox/valimar-ctf-ci/python2/features/L3_Protocols/ospf/", "/home/supandit/sandbox/valimar-ctf-ci/python3/features/L3_Protocols/ospf/MI_ISIS_OSPF_REDISTRIBUTE/", "/home/supandit/sandbox/valimar-ctf-ci/python3/features/L3_Protocols/ospf/OSPF_NSSA/", "/home/supandit/sandbox/valimar-ctf-ci/python3/features/L3_Protocols/ospf/OSPF_SR/", "/home/supandit/sandbox/valimar-ctf-ci/python3/features/L3_Protocols/ospf/OSPF_SR_LAG/", "/home/supandit/sandbox/valimar-ctf-ci/python3/features/L3_Protocols/ospf/OSPF_SR_TILFA/"] # Replace with your directory paths
    output_filename = "listfilesinDir.txt"

    list_files_to_file(directories_to_scan, output_filename)
    print(f"File list written to '{output_filename}'")