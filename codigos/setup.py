from sys import executable, version
from xml.etree.ElementInclude import include
import cx_Freeze

executables = [cx_Freeze.Executable('MainForm.py', base="Win32GUI", target_name="Otimização Não Linear.exe")]


cx_Freeze.setup(
    name = "Otimização Não Linear",
    version = "1.0",
    options = {"build_exe": {'packages':['sympy'],
    'include':['pandas','matplotlib','numpy','delphifmx'],
    'include_files': ['MainForm.pyfmx', 'metodo_newton.py','metod_newton_modificado.py','search_result.py','solucao_grafica.py','utils.py','__pycache__','metodo_gradiente.py']}},

    executables = executables    
    
)