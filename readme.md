# QR Code Generator
A CLI tool to generate QR Code

## Installation
Make sure that you have make installed on your pc
```bash
make install
```

## Usage
```bash
py main.py <your-data> <output-file-name> --style <rounded|pixel|circle|v-bars|h-bars> --image <path/to/image>
```

Example:
| Command | Output |
| ------- | ------ |
|`py main.py "Lorem ipsum dolor sit amet" "sample-square" ` | <img src="./docs/sample-square.png" width="160"/> |
|`py main.py "Lorem ipsum dolor sit amet" "sample-rounded"  --style rounded` | <img src="./docs/sample-rounded.png" width="160"/> |
|`py main.py "Lorem ipsum dolor sit amet" "sample-pixel"  --style pixel` | <img src="./docs/sample-pixel.png" width="160"/> |
|`py main.py "Lorem ipsum dolor sit amet" "sample-circle"  --style circle` | <img src="./docs/sample-circle.png" width="160"/> |
|`py main.py "Lorem ipsum dolor sit amet" "sample-v-bars"  --style v-bars` | <img src="./docs/sample-v-bars.png" width="160"/> |
|`py main.py "Lorem ipsum dolor sit amet" "sample-h-bars"  --style h-bars` | <img src="./docs/sample-h-bars.png" width="160"/> |
|`py main.py "Lorem ipsum dolor sit amet" "sample-image"  --image "./logo.png"` | <img src="./docs/sample-image.png" width="160"/> |