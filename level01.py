import os

def process_paces(file_path):

    if not file_path.endswith('.in'):
        raise ValueError("Input file must have a '.in' extension")
    output_file_path = file_path[:-3] + '.out'
    
    try:
        with open(file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            for line in infile:
                
                paces = list(map(int, line.strip().split()))
                
                total_time = sum(paces)
                
                
                outfile.write(f"{total_time}\n")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError as e:
        print(f"Error processing file: {e}")


process_paces('level1_0_example.in')
process_paces('level1_1_small.in')
process_paces('level1_2_large.in')