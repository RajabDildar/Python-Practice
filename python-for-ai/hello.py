import random as rd
from math import sqrt, pi # importing built in modules
number = sqrt(16)

import requests # importing external libraries by installing with pip

print("Hello World!!")

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

