# Guia para Trabajar

## Antes de empezar
- Crear un nuevo proyecto (carpeta vacia) para trabajar con GIT

## Descargar repositorio
1. Instalar [git](https://git-scm.com/downloads) si no esta instalado
  - Comprobar si esta instalado (Terminal)
    ```
    git --version
    ```
2. Abrir la Terminal del VSCode o Pycharm
3. Clonar el repositorio
    ```
    git clone https://github.com/AlanBogarin/sgth.git
    ```

## Actualizar repositorio
1. Desde la web
  1. Ir la pagina principal del repositorio
  2. Seleccionar las opciones `Add file` > `Upload files`
  3. Arrastrar todos los archivos del proyecto (solo python `.py`)
  4. Una vez verificado los archivos seleccionados son los correctos, hacer un `commit`
  5. Hacer un `pull` para actualizar las configuraciones de Git

## Recomendaciones
1. Cada vez que abren el IDE (VSCode o Pycharm), actualizar los archivos locales con el comando [pull](#actualizar-archivos-locales)
2. Cada vez que editen un archivo, hacer un [commit](#actualizar-repositorio)
