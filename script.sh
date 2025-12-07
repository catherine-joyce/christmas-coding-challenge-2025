# Rename all test_code.py files to include their parent directory name
find . -name "test_code.py" -type f | while read file; do
    dir=$(dirname "$file")
    dirname_base=$(basename "$dir")
    mv "$file" "$dir/test_${dirname_base}.py"
done