# GO TO BOTTOM OF FILE TO FIND MAIN FUNCTION, THAT IS WHERE THE IMPORTANT STUFF IS
# GO TO BOTTOM OF FILE TO FIND MAIN FUNCTION, THAT IS WHERE THE IMPORTANT STUFF IS
import os
import time

total_files_checked = 0
total_lines_matched = 0
total_folders_found = 0

def search_multiple_strings_in_file(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r', encoding='Latin1') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line.lower():
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, ' '.join(line.split()))) # strip white space
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results

def path_is_valid_file(path, valid_filetype_array) -> bool:
    for filetype in valid_filetype_array:
        if path.endswith(filetype):
            return True
    
    return False

def search_for_strings_in_directory(directory, strings_array, valid_filetype_array):
    global total_files_checked
    global total_lines_matched
    global total_folders_found

    # iterate over files in
    # the directory
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        _file = os.path.join(os.fsdecode(directory), filename)

        if path_is_valid_file(filename, valid_filetype_array):
            total_files_checked += 1
            matched_lines = search_multiple_strings_in_file(_file, strings_array)
            found_matches = len(matched_lines) > 0
            if(found_matches):
                total_lines_matched += len(matched_lines)
                # if there are matches tell me about them
                print("Path = ", _file)
                for elem in matched_lines:
                    print('String = ', elem[0])
                    print('Line Number = ', elem[1])
                    print('Line = ', elem[2], '\n')
        elif os.path.isdir(_file):
            # this is a subfolder (hopefully), because there is no period (which would be a file)
            total_folders_found += 1
            # search recursively further down directory
            search_for_strings_in_directory(os.fsencode(_file), strings_array, valid_filetype_array)
    
    
    


def main():
    # run this script in any terminal (or cmd) --as long as you have python--
    # definitely works on Windows, on a budget gaming laptop it runs quite fast
    # the below (default) settings checked 6035 files, with 962 sub folders, in about 5 seconds
    # it can look for an array of strings, but I only searched for 1 here

    # HOW-TO (in case you forgot)
    # open vscode, open the folder containing this script
    # edit the code as needed, edit the directory, the strings searched for, and the accepted filetypes
    # open terminal in terminal tab of vscode
    # finally type in the below:
    # py stringsearcher.py
    # you should then have your results (if strings were found, they will be printed along with location)
    # you know it's done when it prints FINISHED
    # to run the script a second time, in the terminal press the up arrow key and press enter

    start_time = time.time()
    os.system('cls') # clear console
    global total_files_checked
    global total_lines_matched
    global total_folders_found

    directory = os.fsencode('C:/0-Godot Games/Engine/Godot 4.0 Source/Godot_v4.0.2')
    desired_text_array = ['local position or translation of this node relative to the parent']
    valid_filetype_array = [".txt",".py",".cpp",".h",".xml"]

    search_for_strings_in_directory(directory, desired_text_array, valid_filetype_array)

    print("Files Checked: ", str(total_files_checked))
    print("Lines Matched: ", str(total_lines_matched))
    print("Sub Folders Found: ", str(total_folders_found))
    print("FINISHED in ", "%.2f seconds" % (time.time() - start_time))



if __name__ == '__main__':
    main()