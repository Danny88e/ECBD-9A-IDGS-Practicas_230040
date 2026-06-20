import json, sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Dell\Downloads\ECBD-9A-IDGS-Practicas_230040\Practica 3\AnalisisDatos.ipynb'
with open(path, 'r', encoding='utf-8-sig') as f:
    nb = json.load(f)

cells = nb['cells']
print(f'Archivo en disco - Total celdas: {len(cells)}')
print()
for i, cell in enumerate(cells):
    src = ''.join(cell.get('source', []))
    preview = src[:90].replace('\n', ' ')
    has_output = len(cell.get('outputs', [])) > 0
    has_png = any(o.get('data', {}).get('image/png') for o in cell.get('outputs', []))
    print(f'Cell {i:02d} [{cell["cell_type"][:4]}] out={has_output} png={has_png}: {preview}')
