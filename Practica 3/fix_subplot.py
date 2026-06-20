import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Dell\Downloads\ECBD-9A-IDGS-Practicas_230040\Practica 3\AnalisisDatos.ipynb'
with open(path, 'r', encoding='utf-8-sig') as f:
    nb = json.load(f)

# Change cell 113's subplot size
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        new_source = []
        modified = False
        for line in cell['source']:
            if 'plt.subplot(6,3,k)' in line:
                new_source.append(line.replace('plt.subplot(6,3,k)', 'plt.subplot(7,3,k)'))
                modified = True
            else:
                new_source.append(line)
        if modified:
            cell['source'] = new_source
            print(f"Modified subplot in cell {i}")

with open(path, 'w', encoding='utf-8-sig') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    # add trailing newline to match jupyter behavior
    f.write('\n')

print("Notebook updated successfully.")
