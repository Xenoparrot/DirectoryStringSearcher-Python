### Directory String Searcher Tool
I wrote this code when I first wanted to contribute to the Godot repository. It allowed me to search the entire codebase for any array of characters I chose, and find where they were. Using this I made my first contribution fixing grammatical errors.

The main function of the code comes with instructions on how to use it, but I'll sumarrize the steps here. Keep in mind the tool was just built for me, so it's only built to function, not be polished. But it can check 6000 files in 2 seconds.

- Open the script in Vscode and use the terminal to `cd` into the project folder. 
- Then edit the core values that are in `main()`
  - `directory` must be set to the directory you want to search. Example: os.fsencode('C:/0-Godot Games/0-Engine/Godot Source/godot').
  - `desired_text_array` must be an array of characters or strings, these are what the tool will look for in the directory in every file, scanning each line to find any matching text. All strings will be searched for independently, not together.
  - `valid_filetype_array` determines which filetypes will be checked, all other types will be ignored even if they do include the strings.
- Assuming your computer can run python code, you'll then run `py stringsearcher.py`.


This was also my first real attempt at python. I originally tried in C++ but learned that there was no easy way to search directories in C++. I would later contribute an editor feature to the Godot repo to learn C++.
This tool is still good for easily searching for entire arrays, but otherwise it is outdated because now Visual Studio has an arbitrary text search feature.
