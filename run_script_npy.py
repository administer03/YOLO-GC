import os

imgsize = 1024
epochs = 1000
batch_size = 2
data_ = "../running_data/npy_dataset/data.yaml"
# data_ = './data/data_npy.yaml'
hpy_aug = "./data/hyps/hyp.with-mosaic.yaml"
hpy_no_aug = "./data/hyps/hyp.no-mosaic.yaml"
device = 0


'''
No Augmentations
'''

project_name = "./runs/train/npy_version/no_augment"

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --weights '' --hyp {} --cfg yolov5n.yaml \
# --device {} --exist-ok --patience 0 \
# --name test_n --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, device, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--weights '' --hyp {} --cfg yolov5s.yaml \
--device {} --exist-ok --patience 0 \
--name test_s --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, device, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --weights '' --hyp {} --cfg yolov5m.yaml \
# --device {} --exist-ok --patience 0 \
# --name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, device, project_name))



# '''
# With Augmentations
# '''

# project_name = "./runs/train/npy_version/augment"

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --weights '' --hyp {} --cfg yolov5n.yaml \
# --device {} --exist-ok --patience 0 \
# --name scratch_5n --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, device, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --weights '' --hyp {} --cfg yolov5s.yaml \
# --device {} --exist-ok --patience 0 \
# --name scratch_5s --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, device, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --weights '' --hyp {} --cfg yolov5m.yaml \
# --device {} --exist-ok --patience 0 \
# --name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, device, project_name))
