import re
import sys
import os

# Check for command-line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + '_out.txt'

# Regular expression to match the timestamp and position_covariance
pattern = re.compile(r'\[(.*?)\] .*?position_covariance=array\(\[(.*?)\]\)', re.DOTALL)

# Read the entire file into a single string
with open(input_file, 'r') as infile:
    data = infile.read()

# Find all matches
matches = pattern.findall(data)

with open(output_file, 'w') as outfile:
    for timestamp, position_covariance in matches:
        # Remove unnecessary spaces and newline characters
        position_covariance = re.sub(r'\s+', '', position_covariance)
        outfile.write(f'{timestamp} {position_covariance}\n')

print(f'Parsed data written to {output_file}')

