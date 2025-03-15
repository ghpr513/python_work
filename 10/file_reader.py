from pathlib import Path

# 使用相对路径
path = Path('10\pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
