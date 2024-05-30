# Flask

* Flask es un micro framework para Python
* Permite crear aplicaciones web de todo tipo rapidamente.

## Crear proyecto e instalación

```sh
mkdir flask_01_apis
cd flask_01_apis
pip install flask
touch index.py 
```

## Ejecución

```sh
export FLASK_APP=index.py   # En Linux/Mac
set "FLASK_APP=index.py"    # En Windows
flask run
```

* Entrar al browser e introducir: http://localhost:5000
* Para cambiar de puerto

```sh
# Alternativa 1
export FLASK_RUN_PORT=3000
flask run

# Alternativa 2
flask run --port 6000
```
