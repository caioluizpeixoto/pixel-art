content = open('index.html', 'r', encoding='utf-8').read()
lines = content.split('\n')

for idx, line in enumerate(lines):
    if '#pixel-guarantee-section' in line:
        print(f"Line {idx+1}: {line.strip()}")
