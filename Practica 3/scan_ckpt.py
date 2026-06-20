import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Revisar el checkpoint
ckpt_path = r'C:\Users\Dell\Downloads\ECBD-9A-IDGS-Practicas_230040\Practica 3\.ipynb_checkpoints\AnalisisDatos-checkpoint.ipynb'
with open(ckpt_path, 'r', encoding='utf-8-sig') as f:
    ckpt = json.load(f)

print(f'CHECKPOINT - Total celdas: {len(ckpt["cells"])}')
for i, cell in enumerate(ckpt['cells']):
    src = ''.join(cell.get('source', []))
    preview = src[:80].replace('\n', ' ')
    print(f'  Cell {i:02d} [{cell["cell_type"][:4]}]: {preview}')
