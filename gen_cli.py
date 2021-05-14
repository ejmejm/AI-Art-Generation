import argparse

from image_gen import *
from text_gen import gen_titles

parser = argparse.ArgumentParser(description='Generate art.')
parser.add_argument('--text', '-t', type=str,
                    help='text to generate an image')
parser.add_argument('--text_file', '-f', type=str,
                    help='path to images to generate, one per line')
parser.add_argument('--preset', '-p', default='med',
                    help='preset for image quality/gen speed')
parser.add_argument('--genre', '-g', type=str,
                    help='genre of the title to be generated')
parser.add_argument('--count', '-n', type=int, default=1, 
                    help='number of images to generate')

PRESET_MAP = {
    '0': TEST_PRESET,
    '1': VERY_LOW_QUALITY_PRESET,
    '2': LOW_QUALITY_PRESET,
    '3': MED_QUALITY_PRESET,
    '4': HIGH_QUALITY_PRESET,
    'test': TEST_PRESET,
    'vlow': VERY_LOW_QUALITY_PRESET,
    'low': LOW_QUALITY_PRESET,
    'med': MED_QUALITY_PRESET,
    'high': HIGH_QUALITY_PRESET
}

if __name__ == '__main__':
    args = parser.parse_args()
    preset = PRESET_MAP[args.preset.lower()]

    if args.text is not None:
        texts = [args.text] * args.count
    elif args.text_file is not None:
        with open(args.text_file, 'r') as f:
            lines = f.readlines()
        texts = []
        for line in lines:
            for _ in range(args.count):
                texts.append(line)
    else:
        print('No titles given, so generating a random title...')
        texts = gen_titles(n=args.count, genre=args.genre)
        print('Generated titles:')
        for text in texts:
            print(text)
    
    for text in texts:
        generate_image(text.strip(), preset, True)