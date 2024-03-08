import os

imgsize = 1024
epochs = 1000
batch_size = 8
data_475 = "/home/taned/nas/multiview/export_dataset/for_learning/version2/475/data.yaml"
data_814 = "/home/taned/nas/multiview/export_dataset/for_learning/version2/814/data.yaml"
hpy_aug = "./data/hyps/hyp.with-mosaic.yaml"
patience = 200
device = 0


'''
With Augmentations
'''

project_name = "./runs/train/datav2_475/augment"

# # 3x3 and 1x1
os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--weights '' --hyp {} --cfg yolov5n.yaml \
--device {} --exist-ok --patience {} \
--name scratch_5n --project {}".format(imgsize, epochs, batch_size, data_475, hpy_aug, device, patience, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--weights '' --hyp {} --cfg yolov5m.yaml \
--device {} --exist-ok --patience {} \
--name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_475, hpy_aug, device, patience, project_name))

project_name = "./runs/train/datav2_814/augment"

# # 3x3 and 1x1
os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--weights '' --hyp {} --cfg yolov5n.yaml \
--device {} --exist-ok --patience {} \
--name scratch_5n --project {}".format(imgsize, epochs, batch_size, data_814, hpy_aug, device, patience, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--weights '' --hyp {} --cfg yolov5m.yaml \
--device {} --exist-ok --patience {} \
--name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_814, hpy_aug, device, patience, project_name))