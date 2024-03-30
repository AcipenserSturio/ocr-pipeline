# ocr-pipeline
We strongly recommend using GPU while post-ocr inference to improve overall performance and prevent RAM overload

## Requirements
### Python
- `torch`
- `transformers`

### Debian-based

- `ocrmypdf`

- `tesseract-ocr-rus`

- `poppler-utils`

### Arch-based

- `ocrmypdf` (AUR)

- `tesseract-data-rus` (AUR)

- `tesseract-data-eng` (AUR)

- `poppler`

## Usage

```
./pipeline.sh "path/to/file.pdf"
```
