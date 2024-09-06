import sys
import re

# Check for command-line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Regular expression to parse timestamp and position_covariance array
pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+\[([^\]]+)\]')

def check_values(covariance_str):
    # Convert covariance array string to a list of floats
    try:
        values = list(map(float, re.findall(r'[-\d.]+', covariance_str)))
        if len(values) >= 9:
            return values[1], values[5], values[9]
    except ValueError:
        pass
    return None, None, None

with open(input_file, 'r') as infile:
    for line in infile:
        match = pattern.search(line)
        if match:
            timestamp, covariance_str = match.groups()
            pos1, pos5, pos9 = check_values(covariance_str)
            if pos1 is not None and (pos1 > 0.01 or pos5 > 0.01 or pos9 > 0.01):
                print(f"WARNING: At {timestamp}, values exceed threshold: pos1={pos1}, pos5={pos5}, pos9={pos9}")

