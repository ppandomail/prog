from datetime import datetime
import pytz

print(datetime.now())                              # Fecha de hoy
print(datetime.now().strftime("%Y%m%d_%H%M%S"))    # Formatea fecha
print(datetime.now(pytz.timezone("America/Buenos_Aires")))
