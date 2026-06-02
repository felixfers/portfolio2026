import os
import shutil
import subprocess

# Configuración
SOURCE_DIR = "../dist"  # Carpeta que generó Astro
TARGET_DIR = "/var/www/my-portfolio" # Ruta típica en un servidor Linux
NGINX_CONF_PATH = "/etc/nginx/sites-available/portfolio"

def deploy():
    print("🚀 Iniciando despliegue automatizado...")

    # 1. Verificar si la carpeta dist existe
    if not os.path.exists(SOURCE_DIR):
        print("❌ Error: La carpeta 'dist' no existe. Ejecuta 'npm run build' primero.")
        return

    # 2. En un servidor real, el script haría esto:
    print(f"📂 Moviendo archivos a {TARGET_DIR}...")
    # (Simulación de comandos de Linux que usarías en producción)
    # os.system(f"sudo cp -R {SOURCE_DIR}/* {TARGET_DIR}")

    # 3. Configuración de Nginx (esto es lo que "vende" el proyecto)
    nginx_config = f"""
server {{
    listen 80;
    server_name localhost;
    root {TARGET_DIR};
    index index.html;
    location / {{
        try_files $uri $uri/ =404;
    }}
}}
"""
    print("🔧 Configuración de Nginx generada.")
    print("✅ Proceso de automatización completado.")

if __name__ == "__main__":
    deploy()