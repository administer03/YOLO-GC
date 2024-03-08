import os

imgsize = 1024
source = "../running_data/sample_fits/"
project_name = "./runs/detect"
conf_thres = 0.25
iou_thres = 0.45

# Full image output filter
out_filter = 'Linear'

# weight_ = "./pretrain_weight/later_train_weight/vanila_yolo_n.pt"
weight_ = "./pretrain_weight/later_train_weight/full_n.pt"
yologc_weight = './pretrain_weight/later_train_weight/YOLOGC_n.pt'

# weight_ = "./pretrain_weight/ignore_weights/yolo_best_s.pt"
# yologc_weight = './pretrain_weight/ignore_weights/FE_stacked_convns_s_3.pt'

os.system("python detect_modify.py --imgsz {} \
--source {} --conf-thres {} --iou-thres {}  \
--weights {} --save-conf --save-txt \
--device 0 --exist-ok --raw-type 0 \
--name testing --project {} --yologc_weight {} --out_filter {}".format(imgsize, source,
                                                                       conf_thres, iou_thres,
                                                                       weight_, project_name,
                                                                       yologc_weight,
                                                                       out_filter))