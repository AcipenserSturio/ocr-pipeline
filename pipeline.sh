#!/usr/bin/sh

if [ -f "$1" ]; then
    file=$1;
fi

# echo $file;
filename=${file%.*};
filename_pdf="${filename}_out.pdf";
filename_txt="${filename}_out.txt";
# echo "$filename_pdf";
# echo "$filename_txt";
ocrmypdf "$file" "$filename_pdf" -l rus+eng --force-ocr;
pdftotext -layout "$filename_pdf" "$filename_txt";
python model.py;
