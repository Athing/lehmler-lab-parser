path=$1

for file in $1/*
do
    python parse.py "$file"
done
