import glob
import os

import cv2
import moviepy.editor as mp

VIDEO_FPS = 20

def convert_to_gif(vid_path, gif_path):
    clip = mp.VideoFileClip(vid_path)
    clip.write_gif(gif_path)

def gen_video(directory, del_imgs=False):
    imgs = []

    file_paths = glob.glob(os.path.join(directory, '*.jpg'))
    root_file_path = sorted(file_paths, key=len)[0]
    file_paths.remove(root_file_path)

    for file_path in file_paths:
        img = cv2.imread(file_path)
        height, width, layers = img.shape
        size = (width, height)
        imgs.append(img)
    imgs.extend([img] * VIDEO_FPS * 2)

    root_file_name = os.path.basename(root_file_path)
    instance_name = root_file_name[:root_file_name.find('.jpg')]
    vid_path = instance_name + '.mp4'
    gif_path = instance_name + '.gif'

    out = cv2.VideoWriter(vid_path, cv2.VideoWriter_fourcc(*'mp4v'), VIDEO_FPS, size)
    
    for i in range(len(imgs)):
        out.write(imgs[i])
    out.release()

    convert_to_gif(vid_path, gif_path)

    if del_imgs:
        for file_path in file_paths:
            os.remove(file_path)

if __name__ == '__main__':
    gen_video('test_0', False)
