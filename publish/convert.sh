declare -A resolutions
resolutions=( ["3k"]="3000x3000" ["2k"]="2000x2000" ["1k"]="1000x1000")

num_images=$(ls original | wc -l)
echo "Converting [$num_images] images to:"

for res in "${!resolutions[@]}"
do
    echo "$res"
    
    if [ ! -d "$res" ]
    then
        mkdir "$res"
    fi

    for file in $(ls original/*.png)
    do
        fname=$(basename $file)
        convert $file -resize "${resolutions[$res]}" "$res/$fname"
    done
done
