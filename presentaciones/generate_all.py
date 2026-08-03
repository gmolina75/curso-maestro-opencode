import re
import os
import json

# Read the extracted content
with open('curso_contenido.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Theme definition
THEME = """theme:
  colors:
    primary: "#2563EB"
    secondary: "#1E293B"
    accent: "#10B981"
    background: "#FFFFFF"
    text: "#1F2937"
    lightGray: "#F3F4F6"
    border: "#E5E7EB"
  textStyles:
    title:
      fontSize: 36
      color: "$secondary"
      fontFamily: "MiSans"
    subtitle:
      fontSize: 20
      color: "$text"
      fontFamily: "MiSans"
    body:
      fontSize: 18
      color: "$text"
      fontFamily: "MiSans"
      lineHeight: 1.6
    code:
      fontSize: 16
      color: "#374151"
      fontFamily: "MiSans"
      lineHeight: 1.4
      backgroundColor: "$lightGray"
    bullet:
      fontSize: 18
      color: "$text"
      fontFamily: "MiSans"
      lineHeight: 1.6
    check:
      fontSize: 18
      color: "$accent"
      fontFamily: "MiSans"
      lineHeight: 1.6
"""

def slugify(name):
    """Convert filename to base slug"""
    return name.replace('.pptx', '')

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_cover_page(slide_lines, out_path):
    # Parse cover: "Clase X: Título" and "Módulo X | Duración: X"
    title = slide_lines[0] if slide_lines else "Clase"
    subtitle = slide_lines[1] if len(slide_lines) > 1 else ""
    
    content = f"""pageType: cover
background:
  type: solid
  color: "$background"
elements:
  - elementId: title
    elementType: text
    bounds: [140, 240, 1000, 80]
    content:
      style: "$title"
      align: [center, middle]
      text: |
        <p><strong>{title}</strong></p>
  - elementId: subtitle
    elementType: text
    bounds: [140, 340, 1000, 40]
    content:
      style: "$subtitle"
      align: [center, middle]
      text: |
        <p>{subtitle}</p>
  - elementId: deco-line
    elementType: shape
    bounds: [540, 400, 200, 4]
    shapeName: rect
    fill:
      type: solid
      color: "$primary"
"""
    write_file(out_path, content)

def generate_content_page(slide_lines, out_path, is_code_heavy=False):
    title = slide_lines[0] if slide_lines else ""
    body_lines = slide_lines[1:] if len(slide_lines) > 1 else []
    
    # Detect if content is mostly code/config
    code_lines = [l for l in body_lines if l.startswith('#') or l.startswith('{') or l.startswith('}') or l.startswith('"') or 'export ' in l or l.startswith('git ') or l.startswith('opencode ') or l.startswith('npm ') or l.startswith('AWS_')]
    has_code = len(code_lines) >= 2
    
    # Detect table-like content (short lines with colons or dashes)
    has_table = False
    
    # Build body content
    if not body_lines:
        body_text = ""
    elif has_code:
        # Split into code and bullets
        code_block = []
        bullet_lines = []
        in_code = False
        for line in body_lines:
            stripped = line.strip()
            if stripped.startswith('•'):
                bullet_lines.append(stripped[1:].strip())
            elif stripped.startswith('#') or stripped.startswith('{') or stripped.startswith('}') or stripped.startswith('"') or 'export ' in stripped or stripped.startswith('git ') or stripped.startswith('opencode ') or stripped.startswith('npm ') or stripped.startswith('AWS_') or stripped.startswith('cd ') or stripped.startswith('brew ') or stripped.startswith('choco ') or stripped.startswith('scoop '):
                code_block.append(line)
            elif stripped.startswith('<'):
                code_block.append(line)
            elif stripped.startswith('•'):
                bullet_lines.append(stripped[1:].strip())
            elif stripped.startswith('-'):
                bullet_lines.append(stripped[1:].strip())
            else:
                # Heuristic: if it looks like a command or config
                if any(kw in stripped for kw in ['curl', 'docker', 'mise', 'npx', 'wget', 'code:', 'name:', 'on:', 'jobs:', 'steps:', 'if:', 'env:', 'with:', 'provider', 'model', 'permission']):
                    code_block.append(line)
                else:
                    bullet_lines.append(stripped)
        
        # Generate page with code and bullets
        code_text = "\n".join(code_block)
        bullet_text = "\n".join([f"<li>{b}</li>" for b in bullet_lines if b.strip()])
        
        if code_block and bullet_lines:
            content = f"""pageType: content
background:
  type: solid
  color: "$background"
elements:
  - elementId: title
    elementType: text
    bounds: [80, 50, 1120, 60]
    content:
      style: "$title"
      align: [left, middle]
      text: |
        <p><strong>{title}</strong></p>
  - elementId: code
    elementType: text
    bounds: [80, 140, 1100, 220]
    content:
      style: "$code"
      align: [left, top]
      text: |
{chr(10).join('        <p>' + l + '</p>' for l in code_block)}
  - elementId: bullets
    elementType: text
    bounds: [80, 380, 1100, 240]
    content:
      style: "$bullet"
      align: [left, top]
      text: |
        <ul>
{chr(10).join('        <li>' + b + '</li>' for b in bullet_lines if b.strip())}
        </ul>
"""
        elif code_block:
            content = f"""pageType: content
background:
  type: solid
  color: "$background"
elements:
  - elementId: title
    elementType: text
    bounds: [80, 50, 1120, 60]
    content:
      style: "$title"
      align: [left, middle]
      text: |
        <p><strong>{title}</strong></p>
  - elementId: code
    elementType: text
    bounds: [80, 140, 1100, 400]
    content:
      style: "$code"
      align: [left, top]
      text: |
{chr(10).join('        <p>' + l + '</p>' for l in code_block)}
"""
        else:
            content = f"""pageType: content
background:
  type: solid
  color: "$background"
elements:
  - elementId: title
    elementType: text
    bounds: [80, 50, 1120, 60]
    content:
      style: "$title"
      align: [left, middle]
      text: |
        <p><strong>{title}</strong></p>
  - elementId: bullets
    elementType: text
    bounds: [80, 140, 1100, 480]
    content:
      style: "$bullet"
      align: [left, top]
      text: |
        <ul>
{chr(10).join('        <li>' + b + '</li>' for b in bullet_lines if b.strip())}
        </ul>
"""
    else:
        # Regular bullet content
        bullets = []
        for line in body_lines:
            stripped = line.strip()
            if stripped.startswith('•'):
                bullets.append(stripped[1:].strip())
            elif stripped.startswith('-'):
                bullets.append(stripped[1:].strip())
            elif stripped:
                bullets.append(stripped)
        
        if not bullets:
            # Maybe it's a table or special content - just put as paragraphs
            body_text = "\n".join([f"<p>{l}</p>" for l in body_lines if l.strip()])
            content = f"""pageType: content
background:
  type: solid
  color: "$background"
elements:
  - elementId: title
    elementType: text
    bounds: [80, 50, 1120, 60]
    content:
      style: "$title"
      align: [left, middle]
      text: |
        <p><strong>{title}</strong></p>
  - elementId: body
    elementType: text
    bounds: [80, 140, 1100, 480]
    content:
      style: "$body"
      align: [left, top]
      text: |
{chr(10).join('        <p>' + l + '</p>' for l in body_lines if l.strip())}
"""
        else:
            content = f"""pageType: content
background:
  type: solid
  color: "$background"
elements:
  - elementId: title
    elementType: text
    bounds: [80, 50, 1120, 60]
    content:
      style: "$title"
      align: [left, middle]
      text: |
        <p><strong>{title}</strong></p>
  - elementId: bullets
    elementType: text
    bounds: [80, 140, 1100, 480]
    content:
      style: "$bullet"
      align: [left, top]
      text: |
        <ul>
{chr(10).join('        <li>' + b + '</li>' for b in bullets if b)}
        </ul>
"""
    
    write_file(out_path, content)

def generate_final_page(slide_lines, out_path):
    # Resumen slide with checkmarks
    checks = []
    for line in slide_lines[1:] if len(slide_lines) > 1 else []:
        stripped = line.strip()
        if stripped.startswith('✓'):
            checks.append(stripped[1:].strip())
        elif stripped.startswith('•') and '✓' in stripped:
            checks.append(stripped.replace('✓', '').replace('•', '').strip())
    
    if not checks:
        # Fallback: treat as regular content
        generate_content_page(slide_lines, out_path)
        return
    
    content = f"""pageType: final
background:
  type: solid
  color: "$background"
elements:
  - elementId: title
    elementType: text
    bounds: [80, 50, 1120, 60]
    content:
      style: "$title"
      align: [left, middle]
      text: |
        <p><strong>Resumen</strong></p>
  - elementId: checks
    elementType: text
    bounds: [80, 160, 1100, 420]
    content:
      style: "$check"
      align: [left, top]
      text: |
{chr(10).join('        <p><span style="color:$accent;">✓</span> ' + c + '</p>' for c in checks)}
"""
    write_file(out_path, content)

# Parse presentations
presentations = {}
current_pres = None
current_slide = None
slides = []
slide_lines = []

for line in content.split('\n'):
    line = line.rstrip()
    
    m = re.match(r'=== (.+\.pptx)$', line)
    if m:
        if current_pres and slides:
            presentations[current_pres] = slides
        current_pres = m.group(1)
        slides = []
        current_slide = None
        slide_lines = []
        continue
    
    m = re.match(r'--- Slide (\d+) ---', line)
    if m:
        if current_slide is not None and slide_lines:
            slides.append({'num': current_slide, 'lines': slide_lines})
        current_slide = int(m.group(1))
        slide_lines = []
        continue
    
    if line.startswith('===') or line.startswith('---') or (not line.strip() and current_slide is None):
        continue
    
    if current_slide is not None:
        slide_lines.append(line)

if current_pres and slides:
    presentations[current_pres] = slides

# Also add the last slide of the last presentation
if current_pres and slide_lines:
    slides.append({'num': current_slide, 'lines': slide_lines})
    presentations[current_pres] = slides

print(f"Parsed {len(presentations)} presentations")

# Generate .pptd and .page files
base_dir = 'curso-renumerado'
pages_dir = os.path.join(base_dir, 'pages')
os.makedirs(pages_dir, exist_ok=True)

# Copy design.md
with open('nuevas-clases/design.md', 'r') as f:
    design = f.read()
with open(os.path.join(base_dir, 'design.md'), 'w') as f:
    f.write(design)

for pres_name, slides in sorted(presentations.items()):
    slug = slugify(pres_name)
    pptd_path = os.path.join(base_dir, f'{slug}.pptd')
    
    # Generate page list
    page_files = []
    for i, slide in enumerate(slides):
        slide_num = i + 1
        page_name = f'{slug}_slide{slide_num:02d}.page'
        page_path = os.path.join(pages_dir, page_name)
        page_files.append(f'pages/{page_name}')
        
        if slide_num == 1:
            generate_cover_page(slide['lines'], page_path)
        elif i == len(slides) - 1 and 'Resumen' in slide['lines'][0] if slide['lines'] else False:
            generate_final_page(slide['lines'], page_path)
        else:
            generate_content_page(slide['lines'], page_path)
    
    # Generate .pptd
    pptd_content = f"""title: "{slides[0]['lines'][0] if slides else 'Clase'}"
size: [1280, 720]
{THEME}
pages:
{chr(10).join('  - ' + p for p in page_files)}
"""
    write_file(pptd_path, pptd_content)
    print(f"Generated {slug}: {len(slides)} slides -> {pptd_path}")

print("\nDone! All presentations generated.")
