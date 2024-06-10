import importlib
try:
    importlib.import_module('plotly.express')
    print("plotly.express is installed")
except ModuleNotFoundError:
    print("plotly.express is not installed")