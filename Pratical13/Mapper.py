import sys

for line in sys.stdin:
    
    line = line.strip()
    
    if line.startswith("Date"):
        continue
    
    data = line.split(",")
    
    temperature = float(data[1])
    dewpoint = float(data[2])
    windspeed = float(data[3])
    
    print("Temperature\t{}".format(temperature))
    print("DewPoint\t{}".format(dewpoint))
    print("WindSpeed\t{}".format(windspeed))