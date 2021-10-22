import xml.etree.ElementTree as et
import os
import os.path as op


def YOLOboundingBox():
    xml_namesapce = "{http://lamp.cfar.umd.edu/GEDI}"
    annotation_save_path = "/data/labels"
    for root, folders, files in os.walk("./data/with_sig"):
        for file in files:
            xml_root = et.parse(op.join(root, file)).getroot()
            for page in xml_root.findall(f'{xml_namesapce}DL_DOCUMENT/{xml_namesapce}DL_PAGE'):
                page_width = int(page.attrib['width'])
                page_height = int(page.attrib['height'])

                for zone in page.findall(f'{xml_namesapce}DL_ZONE'):
                    if zone.attrib["gedi_type"] != "DLSignature":
                        continue
                    else:
                        class_id = 1
                        x = int(zone.attrib["col"])
                        y = int(zone.attrib["row"])
                        w = int(zone.attrib["width"]) / page_width
                        h = int(zone.attrib["height"]) / page_height

                        center_x = (x + (w/2))/ page_width
                        center_y = (y + (h/2))/ page_height

                        entry = f'{class_id} {center_x} {center_y} {w} {h}'
                        file_path = os.path.join(annotation_save_path, file[:-4] + '.txt')
                        with open(file_path, "w") as f:
                            f.write(f"{entry}\n")

YOLOboundingBox()