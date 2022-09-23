#!/bin/bash
echo "=============================================================================================================="
echo "Please run the script as: "
echo "sh run_standalone_train.sh DATASET_PATH DEVICE_ID CONFIG_PATH"
echo "for example: sh run_standalone_train.sh /path/data/image 1 /home/PGAN/910_config.yaml"
echo "It is better to use absolute path."
echo "=============================================================================================================="

get_real_path(){
  if [ "${1:0:1}" == "/" ]; then
    echo "$1"
  else
    echo "$(realpath -m $PWD/$1)"
  fi
}
DATASET=$(get_real_path $1)
DEVICEID=$2

config_path=$3
echo "config path is : ${config_path}"

export DEVICE_NUM=1
export DEVICE_ID=$DEVICEID
export RANK_ID=0
export RANK_SIZE=1


if [ -d "train" ];
then
    rm -rf ./train
fi
mkdir ./train
cp ../*.py ./train
cp ../*.yaml ./train
cp -r ../src ./train
cp -r ../model_utils ./train
cp -r ../script/*.sh ./train
cd ./train || exit
echo "start training for device $DEVICE_ID"
env > env.log
python train.py --config_path $config_path --train_data_path $DATASET > log_train.log 2>&1 &
cd ..