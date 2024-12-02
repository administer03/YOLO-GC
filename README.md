# Globular Cluster Detection in M33 Using Multiple Views Representation Learning
## Abstract
Globular clusters (GC) are crucial for understanding galaxy formation and evolution. However, identifying them in large imagery datasets is a time-consuming task. This prompts the development of an automated GC detection algorithm. Although GC detection is fundamentally an object detection problem, the state-of-the-art object detection algorithms are unable to produce accurate results. Motivated by how GCs are identified by astronomers, we propose a deep neural network that fuses multiple views of raw imaging data and learns a better representation of the input image. The proposed network is then combined with YOLO object detection algorithm resulting in YOLO for Globular Cluster detection (YOLO-GC) model. Experimental results based on a real catalog of GCs in the M33 Galaxy showed that the proposed multi-view representation learning technique helps improve detection performance.

## Get starting
For details on data preprocessing, you can follow this link to execute: [Data preprocessing](https://github.com/administer03/Preprocessing-YOLO-GC)

## Installation
Clone the repository and install the required dependencies.
```bash
git clone https://github.com/administer03/YOLO-GC.git
cd YOLO-GC
pip install -r requirements.txt
```

Training script
```bash
python train.py \
    --img {image_size} \
    --epochs {num_epochs} \
    --batch-size {batch_size} \
    --data {dataset_config_path} \
    --weights {pretrained_weights} \
    --hyp {hyperparameter_file} \
    --cfg {model_config} \
    --device {device_id} \
    --exist-ok \
    --patience {early_stopping_patience} \
    --name {run_name} \
    --project {output_directory} \
    --fe_models {feature_extractor}
```
Training Parameters

| Parameter | Description | Example/Default |
|-----------|-------------|-----------------|
| `--img` | Input image size | 1024 |
| `--epochs` | Number of training epochs | 100 |
| `--batch-size` | Number of images per training batch | 16 |
| `--data` | Path to dataset configuration file | `data/data.yaml` |
| `--weights` | Pre-trained weights | Leave '' for training from scratch |
| `--hyp` | Hyperparameter configuration file | `data/hyp.with-mosaic.yaml` |
| `--cfg` | Model configuration | `models/yolov5n.yaml` |
| `--device` | GPU/CPU device ID | `0` for first GPU, `cpu` for CPU |
| `--exist-ok` | Allow overwriting existing training directories | Enabled by default |
| `--patience` | Early stopping patience | `0` to disable |
| `--name` | Name for the training run | `scratch` |
| `--project` | Output directory for training results | Specify your project path |
| `--fe_models` | Feature extractor module | Depends on your specific configuration, ie. 'FE_Add', 'FE_AddNS', 'FE_Conv', 'FE_ConvNS', 'FE_OneR' |

## Citation
```
@inproceedings{
  singlor2023globular,
  title={Globular Cluster Detection in M33 Using Multiple Views Representation Learning},
  author={Singlor, Taned and Thawatdamrongkit, Phonphrm and Techa-Angkoon,
          Prapaporn and Suwannajak, Chutipong and Bootkrajang, Jakramate},
  booktitle={International Conference on Intelligent Data Engineering and Automated Learning},
  pages={323--331},
  year={2023},
  organization={Springer}
}
```
