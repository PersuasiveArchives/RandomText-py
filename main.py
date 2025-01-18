import random

def get_random_lines_from_file(file_path, num_lines=5):
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    
    lines = [line.strip() for line in lines if line.strip()]

    # Select random lines from the file
    random_lines = random.sample(lines, min(num_lines, len(lines)))

    return random_lines


if __name__ == "__main__":
    file_path = 'database.txt'  
    random_lines = get_random_lines_from_file(file_path, num_lines=5)
    
