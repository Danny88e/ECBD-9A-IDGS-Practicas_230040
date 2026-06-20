import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Dell\Downloads\ECBD-9A-IDGS-Practicas_230040\Practica 3\AnalisisDatos.ipynb'
with open(path, 'r', encoding='utf-8-sig') as f:
    nb = json.load(f)

cells = nb['cells']
fixed = 0

for i, cell in enumerate(cells):
    if cell['cell_type'] != 'code':
        continue
    src = ''.join(cell.get('source', []))
    new_src = src

    # Fix Bokeh 3.x: plot_width -> width, plot_height -> height
    if 'plot_width' in new_src or 'plot_height' in new_src:
        new_src = new_src.replace('plot_width=', 'width=')
        new_src = new_src.replace('plot_height=', 'height=')

    # Fix Bokeh 3.x: p.circle() -> p.scatter() or keep circle but use updated API
    # Actually circle() still works in Bokeh 3 but the glyph method signature changed
    # The simplest fix is width/height only

    if new_src != src:
        lines = new_src.split('\n')
        cell['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]
        fixed += 1
        print(f'Fixed Cell {i:03d}: Bokeh plot_width/plot_height -> width/height')

print(f'\nTotal fijas: {fixed}')

output = json.dumps(nb, ensure_ascii=False, indent=1)
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(output)

with open(path, 'r', encoding='utf-8') as f:
    test = json.load(f)
print(f'JSON valido: {len(test["cells"])} celdas | Sin BOM: OK')
print('DONE')
