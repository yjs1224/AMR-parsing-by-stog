my_data=$1
data_dir=$2
python convert.py --in_file ${my_data} --out_dir ${data_dir}
./scripts/annotate_features.sh ${data_dir}
./scripts/preprocess_2.0.sh ${data_dir}
./predict.sh ${data_dir}