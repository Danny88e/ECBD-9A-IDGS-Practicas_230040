import json, sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Dell\Downloads\ECBD-9A-IDGS-Practicas_230040\Practica 3\AnalisisDatos.ipynb'
with open(path, 'r', encoding='utf-8-sig') as f:
    nb = json.load(f)

cells = nb['cells']
print(f'Total celdas antes: {len(cells)}')

def set_md(cell, text):
    lines = text.strip().split('\n')
    cell['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]

# ============================================================
# DESCRIPCIONES para Puntos 21-53 que estan como placeholder
# ============================================================
descriptions = {
    # Buscar por texto actual de la celda markdown
    'Punto 21.': """21. Obtención de Tipos Únicos como Lista Ordenada

Para facilitar la iteración y graficación por tipo de Pokémon, convertimos el arreglo de tipos únicos en una **lista de Python** usando `.tolist()`, y la ordenamos alfabéticamente con `.sort()`. Esto nos permite recorrer los tipos en un orden consistente al generar gráficos con bucles `for`. El resultado es una lista ordenada con todos los tipos únicos presentes en el dataset.""",

    'Punto 22.': """22. Visualización de Barras: Total de Estadísticas por Tipo

Utilizamos **sns.barplot()** dentro de un bucle `for` para generar **7 gráficas de barras horizontales**, una por cada estadística (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed y Evolve). Cada gráfica muestra el total acumulado de esa estadística agrupado por tipo de Pokémon. Usamos un arreglo de paletas de colores (`magma`, `ocean`, `vlag`, `copper`, `mako`, `winter`, `rocket`) para diferenciar visualmente cada gráfico con el estilo `seaborn-v0_8-darkgrid`.""",

    'Punto 26.': """26. Análisis de Distribución Individual por Tipo usando Swarmplot

Un **swarmplot** muestra todos los puntos de datos individuales distribuidos de forma que no se superpongan, revelando la densidad y dispersión real de los valores. En esta visualización creamos una cuadrícula de subplots (uno por cada tipo de Pokémon) con la paleta `gist_stern`. Cada subplot presenta las estadísticas como puntos individuales, permitiendo identificar si un tipo tiene Pokémon muy variables (dispersos) o uniformes (compactos), así como detectar valores atípicos.""",

    'Punto 31': """31. Ranking de Tipos por Total de Estadísticas Acumuladas

Utilizamos **sns.barplot()** para visualizar la suma total de todas las estadísticas (`Total`) agrupadas por tipo de Pokémon, ordenadas de mayor a menor. Esta gráfica nos permite identificar qué tipos de Pokémon son los más poderosos en términos de estadísticas base acumuladas. El eje X muestra el tipo y el eje Y la suma total, lo que revela cuáles tipos concentran más poder estadístico en el dataset.""",

    'Punto 32': """32. Ranking de Tipos por Promedio de Estadísticas Totales

Complementando el análisis anterior, esta visualización muestra el **promedio** del Total de estadísticas base por tipo de Pokémon, ordenado de mayor a menor. A diferencia de la suma, el promedio nos indica la fortaleza estadística **por individuo** de cada tipo, eliminando el sesgo producido por tipos con más Pokémon. Esto permite una comparación más justa entre tipos con diferente cantidad de representantes.""",

    'Punto 33': """33. Identificación de la Estadística Dominante por Tipo

Para cada tipo de Pokémon, calculamos cuál es su **estadística más alta en promedio** usando el DataFrame de promedios y el método `.sort_values()`. El resultado es una lista `best_stats` que contiene la estadística con mayor valor promedio para cada tipo, revelando el "punto fuerte" natural de cada categoría (por ejemplo, si los Pokémon de tipo Dragon destacan en Attack, o los Psychic en Sp. Atk).""",

    'Punto 34': """34. Impresión de la Estadística Dominante por Tipo

Imprimimos de forma legible los resultados del análisis anterior: para cada tipo de Pokémon mostramos cuál es su estadística base más alta en promedio. Este análisis permite identificar el **perfil de combate** de cada tipo — si es ofensivo (Attack/Sp. Atk), defensivo (Defense/Sp. Def), resistente (HP) o veloz (Speed). Es información valiosa para entender las estrategias de juego de cada tipo.""",

    'Punto 35': """35. Identificación de Pokémon Mega Evolución

Filtramos el dataset para identificar todos los Pokémon que tienen una **Mega Evolución**, usando `.str.contains('Mega')`. Las Mega Evoluciones son formas temporales con estadísticas superiores a sus versiones base. Este análisis nos permite cuantificar cuántas Mega Evoluciones existen en el dataset y observar sus características estadísticas. La visualización del DataFrame filtrado muestra solo las filas correspondientes a estos Pokémon especiales.""",

    'Punto 36': """36. Extracción de Nombres de Mega Evoluciones

Construimos una lista limpia de nombres para los Pokémon Mega usando **comprensión de listas** y el método `.split('Mega')`. El proceso divide el nombre combinado (e.g., "CharizardMega Charizard X") por la palabra "Mega" y extrae la segunda parte, resultando en el nombre correcto de la Mega Evolución (e.g., "Mega Charizard X"). Esta lista normalizada facilita el análisis y la visualización posterior de estos Pokémon especiales.""",

    'Punto 37': """37. Reemplazar Nombres de Mega Evoluciones en el Dataset

Usamos **.replace()** de pandas para sustituir los nombres originales de los Pokémon con Mega Evolución por los nombres correctos extraídos en el punto anterior. Esta limpieza de datos asegura que los nombres sean consistentes y legibles en las visualizaciones. Al usar `.values` del DataFrame filtrado y la lista de nombres corregidos, realizamos el reemplazo de forma vectorizada sobre toda la columna `Name`.""",

    'Punto 38': """38. Análisis del Top Pokémon por Estadística dentro de cada Tipo

Para cada tipo de Pokémon y para cada estadística principal (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed), identificamos el **Pokémon con el valor más alto**. Usamos `.idxmax()` del DataFrame agrupado por tipo para obtener el nombre del Pokémon dominante en cada categoría. Este análisis revela cuáles son los "mejores" representantes de cada tipo en cada aspecto de combate.""",

    'Punto 39': """39. Distribución de Pokémon por Generación (Actualizado)

Regraficamos el **countplot de generaciones** con `sns.countplot()` usando la paleta `seismic` para mostrar la distribución de Pokémon por generación en el dataset actualizado (que incluye los cambios del Ejercicio 6). Esta visualización nos permite confirmar que los datos fueron actualizados correctamente y observar si la distribución por generación cambió tras agregar los nuevos Pokémon artificiales.""",

    'Punto 40': """40. Suma de Estadísticas por Generación

Usando **pandas.groupby()** agrupamos todos los Pokémon por generación y calculamos la **suma total** de cada estadística base (HP, Attack, Defense, etc.) para cada generación. El resultado es un DataFrame donde cada fila representa una generación y cada columna la suma acumulada de esa estadística. Esto permite identificar qué generaciones introdujeron Pokémon globalmente más poderosos.""",

    'Punto 41': """41. Swarmplot por Estadística y Generación

Creamos una serie de **swarmplots** (uno por estadística) que muestran la distribución individual de valores para cada generación de Pokémon. Usando una cuadrícula de subplots 3x2, cada gráfico representa una estadística diferente (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed). Los puntos individuales permiten ver la dispersión y densidad de valores dentro de cada generación, revelando qué generaciones tienen mayor variabilidad estadística.""",

    'Punto 42': """42. Boxplot por Estadística y Generación

Complementando el análisis anterior, generamos **boxplots** para cada estadística agrupada por generación de Pokémon. Los boxplots muestran la mediana, cuartiles y valores atípicos de forma compacta. La comparación entre generaciones permite identificar si algunas generaciones tienen Pokémon con estadísticas más extremas o si sus distribuciones son más compactas. La paleta de colores diferencia visualmente cada generación.""",

    'Punto 43': """43. Visualización Interactiva con Bokeh (Gráfica de Dispersión)

Utilizamos la librería **Bokeh** para crear una visualización interactiva que permite explorar las relaciones entre estadísticas de Pokémon. A diferencia de matplotlib/seaborn (estáticos), Bokeh genera gráficos HTML interactivos con zoom, pan y tooltips. Esta celda configura el entorno de Bokeh para notebooks (`output_notebook`) y crea un scatter plot donde cada punto representa un Pokémon, permitiendo identificar patrones y correlaciones entre estadísticas de forma interactiva.""",

    'Punto 44': """44. Conteo de Pokémon Legendarios

Calculamos el **número total de Pokémon legendarios** en el dataset usando filtrado booleano con `pokemons.Legendary==True`. El resultado nos da el conteo exacto y el porcentaje que representa sobre el total del dataset. Los Pokémon legendarios son especiales por sus altas estadísticas y rareza en los juegos. Este análisis establece la base para comparar las estadísticas de legendarios vs. no legendarios.""",

    'Punto 45': """45. Suma de Legendarios por Generación

Agrupamos el dataset por generación y sumamos la columna `Legendary` (booleanos `True/False` que suman como 1/0) para obtener el **número de Pokémon legendarios en cada generación**. Esto nos revela qué generaciones de los videojuegos introdujeron más Pokémon legendarios. Las generaciones con más legendarios suelen tener tramas más complejas y mayor variedad de Pokémon especiales para capturar.""",

    'Punto 46': """46. Visualización de Legendarios por Generación

Creamos un **barplot** con seaborn que muestra visualmente la cantidad de Pokémon legendarios en cada generación. El eje X representa la generación (1-6) y el eje Y la cantidad de legendarios. Esta visualización facilita la comparación entre generaciones y permite identificar rápidamente cuáles son las generaciones más ricas en Pokémon legendarios, información relevante para jugadores y analistas del juego.""",

    'Punto 47': """47. Ranking de Tipos con Más Pokémon Legendarios

Utilizamos **groupby('Type').sum().Legendary** para calcular cuántos Pokémon legendarios tiene cada tipo, ordenados de mayor a menor. Esta serie nos muestra qué tipos de Pokémon concentran más legendarios en el dataset. Los tipos con más legendarios suelen tener mayor poder estadístico promedio. El ordenamiento descendente facilita identificar de inmediato los tipos más "legendarios" del juego.""",

    'Punto 48': """48. Visualización Horizontal de Legendarios por Tipo

Creamos un **barplot horizontal** que muestra la cantidad de Pokémon legendarios por tipo, ordenado de mayor a menor. Usamos `figsize=(15,10)` para una visualización clara con los 19 tipos. Los valores se muestran en el eje Y (tipos) y la cantidad en el eje X. Esta orientación horizontal facilita la lectura de los nombres de tipo y permite una comparación visual inmediata de cuáles tipos dominan entre los Pokémon legendarios del dataset.""",

    'Punto 49': """49. Análisis Estadístico Comparativo: Legendarios vs. No Legendarios por Tipo

Generamos una serie de **subplots** (uno por estadística) que comparan la distribución de cada estadística base entre Pokémon legendarios y no legendarios, separados por tipo usando barplots. Esto nos permite identificar qué estadísticas diferencian más a los Pokémon legendarios de los ordinarios en cada tipo. Los legendarios típicamente tienen valores mucho más altos, especialmente en estadísticas ofensivas y defensivas especiales.""",

    'Punto 50': """50. Swarmplot Comparativo: Distribución por Tipo con Diferenciación de Legendarios

Creamos una cuadrícula de **swarmplots** (uno por tipo de Pokémon, grilla 6x3) donde cada punto representa un Pokémon individual. La diferenciación visual por color (`hue='Legendary'`) permite distinguir Pokémon legendarios de no legendarios dentro de cada tipo. Esto facilita identificar si los legendarios de un tipo siguen la distribución general o son claros valores atípicos. La paleta `Dark2` proporciona colores contrastantes para la distinción.""",

    'Punto 51': """51. Estadísticas Comparativas de Pokémon Legendarios

Calculamos y mostramos las **estadísticas comparativas** de los Pokémon legendarios vs. el promedio general del dataset. Para cada estadística principal (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed) determinamos cuántos Pokémon legendarios superan el promedio general de esa estadística y qué porcentaje representan. Este análisis cuantifica la "superioridad" estadística de los Pokémon legendarios y confirma su naturaleza excepcional dentro del juego.""",

    'Punto 52': """52. Mapa de Calor de Correlaciones entre Estadísticas

Utilizamos **sns.heatmap()** junto con `.corr()` para visualizar la **matriz de correlación** entre todas las estadísticas numéricas del dataset. Cada celda muestra el coeficiente de correlación de Pearson (-1 a 1) entre dos estadísticas. El parámetro `annot=True` muestra los valores numéricos en cada celda y `cmap="YlGnBu"` usa una paleta de color azul-verde. Las correlaciones altas positivas (cercanas a 1) sugieren que estadísticas tienden a ser altas juntas en el mismo Pokémon.""",

    'Punto 53': """53. Pairplot: Análisis Multivariado de Relaciones entre Estadísticas

El **pairplot** de seaborn genera una matriz de gráficos de dispersión para cada combinación de pares de estadísticas numéricas del dataset. La diagonal muestra la distribución individual de cada estadística (histogramas o KDE). Los gráficos off-diagonal muestran la relación entre pares de variables. Este análisis multivariado permite identificar patrones, clusters y correlaciones entre múltiples estadísticas simultáneamente, dando una visión comprensiva de la estructura del dataset de Pokémon."""
}

# Aplicar descripciones a las celdas
updated = 0
for i, cell in enumerate(cells):
    if cell['cell_type'] == 'markdown':
        src = ''.join(cell.get('source', []))
        src_stripped = src.strip()
        for key, desc in descriptions.items():
            if src_stripped == key or src_stripped == key + '.':
                set_md(cell, desc)
                print(f'OK Cell {i:03d}: {key} -> descripcion agregada')
                updated += 1
                break

print(f'\nTotal actualizadas: {updated}')
print(f'Total celdas: {len(cells)}')

# Guardar sin BOM
output = json.dumps(nb, ensure_ascii=False, indent=1)
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(output)

# Verificar
with open(path, 'rb') as f:
    first3 = f.read(3)
bom_free = first3 != b'\xef\xbb\xbf'
print(f'Guardado: {len(output):,} bytes | Sin BOM: {bom_free}')

with open(path, 'r', encoding='utf-8') as f:
    test = json.load(f)
print(f'JSON valido: {len(test["cells"])} celdas')
print('DONE')
