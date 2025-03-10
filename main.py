import random

def get_random_lines_from_file(file_path, num_lines=1):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip()]

    if len(lines) < num_lines:
        print("Not enough lines in the file.")
        return None, lines

    random_lines = random.sample(lines, num_lines)

    remaining_lines = [line for line in lines if line not in random_lines]

    return random_lines, remaining_lines
if __name__ == "__main__":
    file_path = 'database.txt'
    random_lines, remaining_lines = get_random_lines_from_file(file_path, num_lines=1)

    if random_lines:
    
    
        for line in random_lines:
            print(line)
    else:
        print("missing")
