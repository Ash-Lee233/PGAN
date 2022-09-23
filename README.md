# PGAN

PGAN refers to Progressive Growing of GANs for Improved Quality, Stability, and Variation, this network is
characterized by the progressive generation of face images

[Paper](https://arxiv.org/abs/1710.10196): Progressive Growing of GANs for Improved Quality, Stability,
and Variation//2018 ICLR

# Dataset

Dataset web-page: [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

> Note: For this task we use the "Align&Cropped Images" dataset (from the "Downloads" section on the official web-page.).

Dataset link (1.34 GB): [Celeba Aligned and Cropped Images](https://drive.google.com/file/d/0B7EVK8r0v71pZjFTYXZWM3FlRnM/view?usp=sharing&resourcekey=0-dYn9z10tMJOBAkviAcfdyQ)

After unpacking the dataset, it should look as follows:

```text
.
└── Celeba
    └── img_align_celeba
        ├── 000001.jpg
        ├── 000002.jpg
        └── ...
```

CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset with over 200K celebrity images,
each with 40 attribute annotations. CelebA is diverse, numerous, and annotated, including

- 10,177 number of identities,
- 202,599 number of face images, and 5 landmark locations, 40 binary attributes annotations per image.

This dataset can be used as a training and test set for the following computer vision tasks: face attribute recognition,
face detection, and face editing and synthesis.

# Train

```bash
# run the training example
export DEVICE_ID=0
export RANK_SIZE=1
python train_data_path.py --train_data_path /path/data/image --config_path ./910_config.yaml
OR
bash run_standalone_train.sh /path/data/image device_id ./910_config.yaml
```

# Eval

- Generate images in the Ascend environment
  User-generated 64 face pictures

  When evaluating, select the generated checkpoint file and pass it into the test script as a parameter.
  The corresponding parameter is `checkpoint_g` (the checkpoint of the generator is saved)

- Use a checkpoint which name starts with `AvG` (for example, AvG_12000.ckpt)

```bash
# run the distributed training example
bash run_distributed_train.sh /path/data/image /path/hccl_config_file ./910_config.yaml
# run the evaluation example
export DEVICE_ID=0
export RANK_SIZE=1
python eval.py --checkpoint_g=/path/checkpoint --device_id=0
OR
bash run_eval.sh /path/checkpoint 0
```