import json, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

result = subprocess.run([
    r'C:\Users\Dell\anaconda3\python.exe', '-m', 'jupyter', 'nbconvert',
    '--to', 'notebook', '--execute', '--inplace',
    '--ExecutePreprocessor.timeout=900',
    '--ExecutePreprocessor.kernel_name=python3',
    r'C:\Users\Dell\Downloads\ECBD-9A-IDGS-Practicas_230040\Practica 3\AnalisisDatos.ipynb'
], capture_output=True, text=True,
   cwd=r'C:\Users\Dell\Downloads\ECBD-9A-IDGS-Practicas_230040\Practica 3')

print('RC:', result.returncode)
print('STDOUT:', result.stdout[:2000] if result.stdout else '(empty)')
print()
print('STDERR (full):')
print(result.stderr)
