#!/bin/bash
# extract_mermaid.sh
# Usage: ./extract_mermaid.sh fichier.md fichier.mmd

if [ $# -ne 2 ]; then
  echo "Usage: $0 input.md output.mmd"
  exit 1
fi

input_file="$1"
output_file="$2"

sed -n '/^```mermaid$/,/^```$/p' "$input_file" | sed '1d;$d' > "$output_file"

echo "Extraction complete: $output_file created."