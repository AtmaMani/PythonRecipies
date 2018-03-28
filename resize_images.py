# Python script to resize your images, vacation photos, what not
from glob import glob
from PIL import Image
from pathlib import Path

input_path = r'/Users/atma6951/Documents/temp/pics'
image_list = glob(input_path + "/*.jpg", recursive=False)
# print(image_list)

for image in image_list:
    img_obj = Image.open(image)
    current_size = img_obj.size

    # make images 70% smaller
    new_size = (round(current_size[0]/7), round(current_size[1]/7))
    # Use high quality downsampling filter to reduce size without noise
    img_obj_smaller = img_obj.resize(new_size, Image.LANCZOS)

    # Save to disk with same name and a suffix "_sm"
    pth = Path(image)
    new_name = pth.name.rsplit('.', 1)[0] + "_sm." + pth.name.split('.')[-1]
    img_obj_smaller.save(str(pth.parent) + "/smaller/" + new_name)
    print(str(pth.parent) + "/smaller/" + new_name)
