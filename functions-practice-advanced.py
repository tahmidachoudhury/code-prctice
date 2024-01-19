def as_sun_lover(temperature):
    if temperature >= 25:
        return 'great'
    else: 
        return 'not great'

def as_snow_lover(temperature):
    if temperature <= 0:
        return 'great'
    else:
        return 'not great'
    
def report_weather(temperature, preference):
    report = preference(temperature)
    return report

print("How does Tahmid feel about 8.C")
print(report_weather(8, as_snow_lover)) 