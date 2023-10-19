# Inicialización del proyecto

Como buena practica suele ser conveniente realizar una actualización del gestor de paquetes de python.
```bash
python.exe -m pip install --upgrade pip
```

De primera intención si tenemos configurado **github** con un esquema de rama principal **master**, será necesario cambiar el esquema por esquema de rama principal **main**.

```bash
# Lucira asi  nuestra terminal
user@host user/proyectos (master)
```
Entonces sera necesario ejecutar el siguiente comando.
```bash
git branch -M main
```
Terminara luciendo así nuestra terminal.
```bash
user@host user/proyectos (main)
```
Para poder trabajar de manera correcta será necesario crear nuestro entorno virtual de trabajo para **Python**.
```bash
python -m venv py-GPX_alertNotifier
# Al terminar revisemos el contenido de la carpeta que debera lucir similar a lo siguiente.
ls
```
Se habran creado los siguiente elementos

* **Include/**: Directorio de control de archivos Python.
* **Lib/**: Directorio de librerías Python.
* **pyvenv.cfg**: Archivo de configuración de entorno virtual.
* **Scripts/**: Directorio de gestión de entorno virtual.


Una véz que se haya creado el entorno virtual, sera necesario asociar el repositorio de trabajo que contiene el código del proyecto.

```bash
git remote add GPX-Ntfy https://github.com/LeonardoGutierrezV/py-GPX_alertNotifier.git
# validemos que se agrego de forma correcta el repositorio remoto
git remote -v
# Para terminar sera necesario descargar los archivos
git pull https://github.com/LeonardoGutierrezV/py-GPX_alertNotifier.git
```

## Preparación del entorno de trabajo
Active el entorno virtual de trabajo.
```bash
source Scripts/activate
```
Una vez realizado el proceso sin inconvenientes su terminal lucira de la siguiente forma.
```bash
(py-GPX_alertNotifier) 
user@host proyectos/py-GPX_alertNotifier (main)
```
En la parte superior del **prompt** se mostrara el nombre del entorno virtual activo.
Es hora de instalar las dependencias.

```bash
pip install pywin32
```

Sirvase a integrar todas las dependencias que se agreguen posterior a la ultima actualización de este documento.