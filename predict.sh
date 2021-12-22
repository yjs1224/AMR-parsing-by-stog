data_dir=$1

python -u -m stog.commands.predict \
    --archive-file ckpt-amr-2.0 \
    --weights-file ckpt-amr-2.0/best.th \
    --input-file ${data_dir}/test.txt.features.preproc \
    --batch-size 32 \
    --use-dataset-reader \
    --cuda-device 0 \
    --output-file test.pred.txt \
    --silent \
    --beam-size 5 \
    --predictor STOG