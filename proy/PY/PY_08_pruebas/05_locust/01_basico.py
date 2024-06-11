'''

Locust

. Es una herramienta de prueba de carga/rendimiento de código abierto para HTTP y otros protocolos
. Las pruebas de Locust se pueden ejecutar desde línea de comandos o mediante su interfaz de usuario basada en web 

. URL: https://docs.locust.io/en/stable/quickstart.html

. Instalación  pip install locust
. Validación   locust -V

'''
from locust import HttpUser, task

class TestUser(HttpUser):
  
    @task
    def test_xxx(self):
        self.client.get("https://docs.locust.io/en/stable/quickstart.html")

# Se ejecuta: locust -f 01_basico.py
# Abrir http://localhost:8089
# Número de usuarios: 100
# Usuarios iniciando por seg: 5
# Host: https://example.com

