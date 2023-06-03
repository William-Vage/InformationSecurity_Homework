import os

def remove_lines_large_file(filename, num_lines):
    # Create a new temporary file.
    with open(filename + '.tmp', 'w+') as new_file:
        with open(filename, 'r') as old_file:
            for _ in range(num_lines):
                old_file.readline()
            # Copy the rest of the lines.
            for line in old_file:
                new_file.write(line)
    # Replace the old file with the new file.
    os.replace(filename + '.tmp', filename)

curPath = os.getcwd()
storePath = os.path.join(curPath, '28.json')
remove_lines_large_file(storePath, 100000)
