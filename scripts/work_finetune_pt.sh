#! /usr/bin/env bash

set -ex

PRE_SEQ_LEN=128
LR=5e-3
NUM_GPUS=1
MAX_SEQ_LEN=2048
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=16
MAX_STEP=300
SAVE_INTERVAL=100

AUTORESUME_FROM_CHECKPOINT=True
DATESTR=`date +%Y%m%d-%H%M%S`
RUN_NAME=tool_alpaca_pt

BASE_MODEL_PATH=ZhipuAI/chatglm3-6b
DATASET_PATH=formatted_data/glm.jsonl
OUTPUT_DIR=output/${RUN_NAME}-${DATESTR}-${PRE_SEQ_LEN}-${LR}

mkdir -p $OUTPUT_DIR

torchrun --standalone --nnodes=1 --nproc_per_node=$NUM_GPUS finetune.py \
    --train_format multi-turn \
    --train_file $DATASET_PATH \
    --max_seq_length $MAX_SEQ_LEN \
    --preprocessing_num_workers 1 \
    --model_name_or_path $BASE_MODEL_PATH \
    --output_dir $OUTPUT_DIR \
    --per_device_train_batch_size $DEV_BATCH_SIZE \
    --gradient_accumulation_steps $GRAD_ACCUMULARION_STEPS \
    --max_steps $MAX_STEP \
    --logging_steps 1 \
    --save_steps $SAVE_INTERVAL \
    --learning_rate $LR \
    --pre_seq_len $PRE_SEQ_LEN \
    --resume_from_checkpoint $AUTORESUME_FROM_CHECKPOINT 2>&1 | tee ${OUTPUT_DIR}/train.log
