import os
from pathlib import Path
from PIL import Image

with_sig_path = "data/with_sig"
# image_paths = ['data/test','data/train']
image_paths = ['data/train']
save_path = "data/image_files"

for sig_xml in Path(with_sig_path).glob("**/*.xml"):
    for image_path in image_paths:
        image = Path(str(sig_xml).replace(with_sig_path,image_path).replace("xml","tif"))
        try:
            im = Image.open(image)
            print (f"Converting jpeg for {image.name}")
            im.thumbnail(im.size)
            image_save_path = str(image).replace(image_path,save_path).replace("tif","jpeg")
            im.save(image_save_path)
        except:
            "finished"