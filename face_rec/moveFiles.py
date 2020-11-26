import shutil
import os

source_dir = 'C:/Users/pwhee/Documents/archive/img_align_celeba/img_align_celeba'
target_dir = 'C:/Users/pwhee/Documents/archive/img_align_celeba'

file_names = os.listdir(source_dir)

for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
