import itertools
import argparse
def leet_transforms(ch):
    leet_dict = {
        'a': ['a', '4', '@'],
        'b': ['b', '8'],
        'e': ['e', '3'],
        'g': ['g', '9'],
        'i': ['i', '1', '!'],
        'l': ['l', '1'],
        'o': ['o', '0'],
        's': ['s', '5', '$'],
        't': ['t', '7'],
        'z': ['z', '2'],
        '1': ['1', '!'],
        '0': ['0', 'o'],
        '3': ['3', 'e'],
        '4': ['4', 'a'],
        '5': ['5', 's', '$'],
        '6': ['6'],
        '7': ['7'],
        '8': ['8'],
        '9': ['9']
    }
    return leet_dict.get(ch, [ch])
def generate_leet_combinations(word):
    transformed_parts = [leet_transforms(ch) for ch in word]
    return set(''.join(combination) for combination in itertools.product(*transformed_parts))
def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    with open(output_file, 'w') as file:
        for line in lines:
            results = generate_leet_combinations(line.strip().lower())
            for result in results:
                file.write(result + '\n')
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate leet code transformations from an input file and write to an output file.")
    parser.add_argument('input_file', help='The path to the input file containing text.')
    parser.add_argument('output_file', help='The path to the output file to save transformations.')
    args = parser.parse_args()
    process_file(args.input_file, args.output_file)
