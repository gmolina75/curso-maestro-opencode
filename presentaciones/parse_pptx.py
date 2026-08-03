import re
import os

# Read the extracted content
with open('curso_contenido.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse each presentation
presentations = {}
current_pres = None
current_slide = None
slides = []
slide_lines = []

for line in content.split('\n'):
    line = line.rstrip()
    
    # Detect presentation header: === filename.pptx (with === prefix)
    m = re.match(r'=== (.+\.pptx)$', line)
    if m:
        if current_pres and slides:
            presentations[current_pres] = slides
        current_pres = m.group(1)
        slides = []
        current_slide = None
        slide_lines = []
        continue
    
    # Detect slide header
    m = re.match(r'--- Slide (\d+) ---', line)
    if m:
        if current_slide is not None and slide_lines:
            slides.append({'num': current_slide, 'lines': slide_lines})
        current_slide = int(m.group(1))
        slide_lines = []
        continue
    
    # Skip separator lines and empty lines at start
    if line.startswith('===') or line.startswith('---') or (not line.strip() and current_slide is None):
        continue
    
    if current_slide is not None:
        slide_lines.append(line)

# Save last presentation
if current_pres and slides:
    presentations[current_pres] = slides

# Print summary
for pres_name, slides in sorted(presentations.items()):
    print(f"{pres_name}: {len(slides)} slides")
    for s in slides:
        title = s['lines'][0] if s['lines'] else '(empty)'
        print(f"  Slide {s['num']}: {title[:60]}")
    print()
