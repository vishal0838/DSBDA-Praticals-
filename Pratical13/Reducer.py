import sys

temp_total = 0
temp_count = 0

dew_total = 0
dew_count = 0

wind_total = 0
wind_count = 0

for line in sys.stdin:
    
    key, value = line.strip().split("\t")
    
    value = float(value)
    
    if key == "Temperature":
        temp_total += value
        temp_count += 1
        
    elif key == "DewPoint":
        dew_total += value
        dew_count += 1
        
    elif key == "WindSpeed":
        wind_total += value
        wind_count += 1

print("Average Temperature:", temp_total / temp_count)
print("Average Dew Point:", dew_total / dew_count)
print("Average Wind Speed:", wind_total / wind_count)