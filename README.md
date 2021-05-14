# AI Art Generator
######*by Edan Meyer*

This project provides a wraper over [DeepDaze](https://github.com/lucidrains/deep-daze) for generating artwork. It focuses on simplifying the process even further and adding more automation. It adds 3 things in addition to the base ability to generate images from text:
- Predefined preset for varying levels of quality
- Generation of videos and gifs from the images
- Automatic generation of text prompts for end-to-end image generation

## Install
    $ pip install -r requirements.txt

## Examples
**Generate a random piece of art**

    $ python gen_cli.py

**Generate many, low-quality random pieces of art**

    $ python gen_cli.py -p low -n 10

**Generate a specific piece of art**

    $ python gen_cli.py -t 'A doge in a coin going to the moon'

## Usage
    DESCRIPTION
        Generates art varying based on provided parameters.

    FLAGS
        --text / -t
            Default: None
            Prompt used to generate the image.
        --text_file / -f
            Default: None
            Path to file with a list of prompts delimited by new lines,
            and image for each prompt will be generated sequentially.
        --preset / -p
            Default: 'med'
            Preset for the level of quality of the image generated, valid
            presets are: ['test', 'vlow', 'low', 'med', 'high'].
        --genre / -g
            Default: None
            A string giving the genre of art you want to be generated.
            Leaving it as None will result in no specific genre.
        --count / -n
            Default: 1
            The number of pieces to produce. If --text is passed in, n
            variations of the same piece are produced, if --text_file is
            passed in, n variations of each prompt are produced.
            If neither is specified, n random pieces are produced.