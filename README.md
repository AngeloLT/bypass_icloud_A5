# bypass_icloud_A5
Esta Herrmienta hace la peticion al servidor para realizar el desbloqueo del ipod touch 5

![imagen](https://github.com/AngeloLT/bypass_icloud_A5/assets/13395727/4d046d46-1edc-4669-88fa-7bf08fff25e0)

se requiere compilar la aplicacion cambiando la ruta con su seervidor deceado


comando para compilar, esta compilacion se puede realizar para cualquier sistema operativo, esta herramienta solo contiene la libreria para windows, puedes agregar las librerias necesarias 
para el sistema operativo de tu preferecia
pyinstaller --add-data "lib;." --windowed --onefile --icon=./logo.ico index.py

tambien dejo el codigo del servidor que se puede ejecutar tanto en local como en linea teniendo un hosting
