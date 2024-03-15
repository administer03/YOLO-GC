import os

imgsize = 1024
project_name = "./runs/detect"
conf_thres = 0.25
iou_thres = 0.45

# Full image output filter
out_filter = 'Linear'

# """ old exp """
# weight_ = "/home/taned/nas/detection/stacked_conv_noskip_main_for_training/pretrain_weight/ignore_weights/yolo_best_s.pt"
# yologc_weight = '/home/taned/nas/detection/stacked_conv_noskip_main_for_training/pretrain_weight/ignore_weights/FE_stacked_convns_s_3.pt'
# source = "../running_data/sample_fits/"


""" new dataset """
weight_ = "./pretrain_weight/later_train_weight/full_n.pt"
yologc_weight = './pretrain_weight/later_train_weight/YOLOGC_n.pt'
source = "../running_data/sample_fits/lastest_full_fits/"



# weight_ = "./pretrain_weight/later_train_weight/full_m.pt"
# yologc_weight = './pretrain_weight/later_train_weight/YOLOGC_m.pt'

# weight_ = "./pretrain_weight/ignore_weights/yolo_best_s.pt"
# yologc_weight = './pretrain_weight/ignore_weights/FE_stacked_convns_s_3.pt'

os.system("python detect_modify.py --imgsz {} \
--source {} --conf-thres {} --iou-thres {}  \
--weights {} --save-conf --save-txt \
--device 0 --raw-type 0 --large-img True --debug False \
--name 814_infer_fully --project {} --yologc_weight {} --out_filter {}".format(imgsize, source,
                                                                       conf_thres, iou_thres,
                                                                       weight_, project_name,
                                                                       yologc_weight,
                                                                       out_filter))

# --exist-ok