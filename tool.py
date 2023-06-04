import os

def remove_lines_large_file(filename, num_lines):
    # Create a new temporary file.
    with open(filename + '.tmp', 'w') as new_file:
        with open(filename, 'r') as old_file:
            for _ in range(num_lines):
                old_file.readline()
            # Copy the rest of the lines.
            for line in old_file:
                new_file.write(line)
                new_file.write('\n')
    # Replace the old file with the new file.
    os.replace(filename + '.tmp', filename)

def count_lines(filename):
    i = -1
    with open(filename, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

fileName = '28.json'
storePath = os.path.join(os.getcwd(), fileName)
remove_lines_large_file(storePath, 290000)
print(count_lines(storePath))