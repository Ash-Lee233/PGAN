#!/bin/bash


if [ $# != 2 ]
then
    echo "Usage: sh run_eval_ascend.sh [checkpoint_path] [device_id]"
exit 1
fi

export CKPT=$1
export DEVICE_ID=$2
cd ..
python -u eval.py --checkpoint_g=$CKPT --device_id=$DEVICE_ID > log_eval 2>&1 &
