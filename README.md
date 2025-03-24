# Para iniciar con el testing, es necesario comenzar con la virtualización de python  del proyecto actual, para encapsular las dependencias del mismo.
Link de la documentación Unittest en Python
https://docs.python.org/es/3/library/unittest.html


comando en terminal para ejecutar las pruebas: 
python -m unittest discover -s tests  # 
-s es para indicar la carpeta donde están los tests

pip freeze | grep requests # usado para verificar si la librería requests está instalada en el entorno virtual

# Doctest Para documentación de pruebas unitarias
python -m doctest src/archivo.py

Para mantener actualizados el archivo requirements.txt se puede utilizr el comando 
    pip freeze > requirements.txt 
después de cada instalación.