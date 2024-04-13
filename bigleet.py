import itertools
import argparse

def leet_transforms(ch):
    leet_dict = {
        'a': ['a', '4', '@', '^', '/\\'],
        'b': ['b', '8', '13', '|3'],
        'c': ['c', '(', '{', '[', '<', '¢'],
        'd': ['d', '|)', '|}', '|]'],
        'e': ['e', '3', '&', '€', '£'],
        'f': ['f', '|=', 'ph'],
        'g': ['g', '9', '6', '&', '(_+'],
        'h': ['h', '#', '|-|', ']-[', '}{', '(-)'],
        'i': ['i', '1', '!', '|', '][', ':'],
        'j': ['j', ';', '_|', ']', 'ʝ'],
        'k': ['k', '|<', '1<', '|{', ']{'],
        'l': ['l', '1', '|', '|_', '£'],
        'm': ['m', '|v|', '[V]', '{V}', '/\\/\\', '^^'],
        'n': ['n', '|\\|', '/\\/', '[\\]', '<\\>', '{\\}', '₪'],
        'o': ['o', '0', '()', '[]', '{}', '<>', 'Ø'],
        'p': ['p', '|o', '|O', '|>', '|*', '9', '[]D', '|D'],
        'q': ['q', '0_', '()_', '(_,)', '0,'],
        'r': ['r', '|2', '12', '.-', '|^', 'l2', 'Я'],
        's': ['s', '5', '$', '§', 'z'],
        't': ['t', '7', '+', '†', '|-'],
        'u': ['u', '|_|', '\\_\\', '/_/', '(_)', 'µ'],
        'v': ['v', '\\/', '|/', '\\|'],
        'w': ['w', '\\/\\/', 'vv', '\\N', "'//", '\\\\', '//'],
        'x': ['x', '%', '*', '><', '}{', ')('],
        'y': ['y', '`/', '¥', '\\|/', 'Ч'],
        'z': ['z', '2', '7_', '>_', 's', '`/_'],
        '0': ['0', 'o', '()', '[]', '{}', '<>', 'Ø'],
        '1': ['1', '!', '|', 'i', 'l', ']['],
        '2': ['2', 'z', '7_', '>_', '`/_'],
        '3': ['3', 'e', '€', '&', '£'],
        '4': ['4', 'a', '@', '^', '/\\'],
        '5': ['5', 's', '$', '§'],
        '6': ['6', 'g', '9', 'b'],
        '7': ['7', 't', '+'],
        '8': ['8', 'b', '|3', '13', '&'],
        '9': ['9', 'g', '6', 'q']
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
    parser = argparse.ArgumentParser(description="Generate comprehensive leet code transformations from an input file and write to an output file.")
    parser.add_argument('input_file', help='The path to the input file containing text.')
    parser.add_argument('output_file', help='The path to the output file to save transformations.')

    args = parser.parse_args()

    process_file(args.input_file, args.output_file)
