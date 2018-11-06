# Python script to resize your images, vacation photos, what not
from glob import glob
from PIL import Image
from pathlib import Path

input_path = r'/Users/atma6951/Documents/temp/pics'
image_list = glob(input_path + "/*.png", recursive=False)
# print(image_list)

for image in image_list:
    img_obj = Image.open(image)
    current_size = img_obj.size

    # make images 50% smaller
    new_size = (round(current_size[0]/1), round(current_size[1]/1))
    # Use high quality downsampling filter to reduce size without noise
    img_obj_smaller = img_obj.resize(new_size, Image.LANCZOS)

    # Save to disk with same name and a suffix "_sm"
    pth = Path(image)
    # new_name = pth.name.rsplit('.', 1)[0] + "_sm." + pth.name.split('.')[-1]
    new_name = pth.name.rsplit('.', 1)[0] + "_sm.jpg"
    img_obj_smaller.save(str(pth.parent) + "/same_dims/" + new_name)
    print(str(pth.parent) + "/same_dims/" + new_name)
