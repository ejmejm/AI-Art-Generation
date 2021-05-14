import gc
import os

import deep_daze
from deep_daze import Imagine
import torch
from tqdm import trange

from utils import sanitize_file_name, sanitize_folder_name
from video_gen import gen_video

HIGH_QUALITY_PRESET = {
    'num_layers': 24,
    'image_width': 512,
    'epochs': 4,
    'iterations': 1050,
    'lr': 1e-5,
    'batch_size': 4,
    'gradient_accumulate_every': 6,
    'save_every': 10
}

MED_QUALITY_PRESET = {
    'num_layers': 16,
    'image_width': 512,
    'epochs': 3,
    'iterations': 900,
    'lr': 1e-5,
    'batch_size': 4,
    'gradient_accumulate_every': 4,
    'save_every': 10
}

LOW_QUALITY_PRESET = {
    'num_layers': 16,
    'image_width': 256,
    'epochs': 3,
    'iterations': 512,
    'lr': 2e-5,
    'batch_size': 4,
    'gradient_accumulate_every': 4,
    'save_every': 10
}

VERY_LOW_QUALITY_PRESET = {
    'num_layers': 16,
    'image_width': 128,
    'epochs': 1,
    'iterations': 128,
    'lr': 2e-5,
    'batch_size': 4,
    'gradient_accumulate_every': 2,
    'save_every': 10
}

TEST_PRESET = {
    'num_layers': 16,
    'image_width': 64,
    'epochs': 2,
    'iterations': 10,
    'lr': 2e-5,
    'batch_size': 4,
    'gradient_accumulate_every': 1,
    'save_every': 2
}

def generate_image(text, preset, save_video=False):
    i = 0
    output_dir = sanitize_folder_name(
        '{}_{}'.format(text.replace(' ', '_'), i))

    while os.path.exists(output_dir) and os.path.isdir(output_dir):
        i += 1
        output_dir = sanitize_folder_name(
            '{}_{}'.format(text.replace(' ', '_'), i))

    os.mkdir(output_dir)
    os.chdir(output_dir)

    model = Imagine(
        text = text,
        num_layers = preset['num_layers'],
        save_every = preset['save_every'],
        image_width = preset['image_width'],
        lr = preset['lr'],
        iterations = preset['iterations'],
        save_progress = True,
        save_video = save_video,
        save_gif = False
    )

    # Write text used to generate the piece
    with open('name.txt', 'w+') as f:
        f.write(text)
    # Overwrite the output path of images
    model.textpath = sanitize_file_name(text)

    for epoch in trange(preset['epochs'], desc='epoch'):
        for i in trange(preset['iterations'], desc='iteration'):
            model.train_step(epoch, i)

    del model
    gc.collect()
    torch.cuda.empty_cache()

    if save_video:
        gen_video('./', del_imgs=True)
    
    os.chdir('../')

if __name__ == '__main__':
    generate_image('red_roses', TEST_PRESET, True)