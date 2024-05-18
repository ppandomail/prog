"""

Fakers:

. Genera datos falsos.

. Instalación: pip install Faker
. Doc: https://faker.readthedocs.io/en/master/
"""

from faker import Faker
fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())

for _ in range(10):
  print(fake.name())
  
fake = Faker('it_IT')
for _ in range(10):
    print(fake.name())