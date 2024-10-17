# Utiliza la imagen oficial de Jenkins LTS como base
FROM jenkins/jenkins:lts

# Si deseas ejecutar Jenkins como root (no recomendado en producción)
USER root

# Instalar dependencias adicionales que puedas necesitar, como el cliente de Docker
RUN apt-get update && \
    apt-get install -y sudo curl && \
    curl -fsSL https://get.docker.com | sh

# Configura el entorno, por ejemplo, agrega el Docker CLI a la ruta de Jenkins
RUN usermod -aG docker jenkins

# Si tienes configuraciones personalizadas o scripts de inicialización, los puedes copiar
# COPY ./config.xml /var/jenkins_home/config.xml
# COPY ./plugins.txt /usr/share/jenkins/ref/plugins.txt

# Agregar permisos adecuados si fuera necesario
RUN chown -R jenkins:jenkins /var/jenkins_home

# Exponer el puerto para Jenkins
EXPOSE 8080

# Exponer el puerto de esclavo para Jenkins (Jenkins agents)
EXPOSE 50000
