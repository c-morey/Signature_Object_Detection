import xml.etree.ElementTree as et
import os, shutil
import os.path as op

count_sig = 0
count_no_sig = 0
xml_namesapce = "{http://lamp.cfar.umd.edu/GEDI}"
with_sign_path = "/Users/cerenmorey/PycharmProjects/Signature_Object_Detection/data/with_sig"
without_sign_path = "/Users/cerenmorey/PycharmProjects/Signature_Object_Detection/data/without_sig"

for root, folders, files in os.walk("data/train_xml"):
    for file in files:
        src_sig_path = os.path.join("data/train_xml", file)
        xml_root = et.parse(op.join(root, file)).getroot()
        for DL in xml_root.findall(f'{xml_namesapce}DL_DOCUMENT/{xml_namesapce}DL_PAGE'):
            value = DL.find(f'{xml_namesapce}DL_ZONE')
            if value is None:
                continue
            elif value.attrib["gedi_type"] == "DLSignature":
                # new_path = os.path.join(with_sign_path, file)
                shutil.copy2(src_sig_path, with_sign_path)
                count_sig += 1
            elif value.attrib["gedi_type"] != "DLSignature":
                # new_path = os.path.join(without_sign_path, file)
                shutil.copy2(src_sig_path, without_sign_path)
                count_no_sig += 1

            continue

print(f"Found {count_sig} XML files with a signature")
print(f"Found {count_no_sig} XML files without a signature")
