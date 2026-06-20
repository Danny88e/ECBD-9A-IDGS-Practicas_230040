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

    # Fix 1: .groupby(...).mean() -> .groupby(...).mean(numeric_only=True)
    new_src = re.sub(
        r'\.groupby\(([^)]+)\)\.mean\(\)',
        r'.groupby(\1).mean(numeric_only=True)',
        new_src
    )

    # Fix 2: .groupby(...).sum() -> .groupby(...).sum(numeric_only=True)
    new_src = re.sub(
        r'\.groupby\(([^)]+)\)\.sum\(\)',
        r'.groupby(\1).sum(numeric_only=True)',
        new_src
    )

    # Fix 3: .corr() -> .corr(numeric_only=True)  (for heatmap)
    new_src = re.sub(
        r'\.corr\(\)',
        r'.corr(numeric_only=True)',
        new_src
    )

    # Fix 4: pokemons.drop(['#'],axis=1) needs select_dtypes for corr
    # Actually just corr(numeric_only=True) handles it

    if new_src != src:
        lines = new_src.split('\n')
        cell['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]
        fixed += 1
        print(f'Fixed Cell {i:03d}: {src[:60].replace(chr(10)," ")} ...')

print(f'\nTotal celdas corregidas: {fixed}')

# Guardar sin BOM
output = json.dumps(nb, ensure_ascii=False, indent=1)
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(output)

with open(path, 'rb') as f:
    first3 = f.read(3)

with open(path, 'r', encoding='utf-8') as f:
    test = json.load(f)

print(f'JSON valido: {len(test["cells"])} celdas')
print(f'Sin BOM: {first3 != b"\\xef\\xbb\\xbf"}')
print('DONE')
