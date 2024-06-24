# Usando la imagen base de Python
FROM python:3

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    binutils \
    gdal-bin \
    libproj-dev \
    libgdal-dev \
    postgresql-client \
    postgresql-contrib \
    postgis

# Crear el directorio de trabajo
RUN mkdir /warehouse_manager
WORKDIR /warehouse_manager

# Copiar el contenido del proyecto al contenedor
COPY . /warehouse_manager/

# Actualizar pip e instalar dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Establecer la variable de entorno GDAL
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8001

# Comando para correr la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "authProject.wsgi:application"]
