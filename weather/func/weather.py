async def weather_resp(temperature):
    fl_temp=float(temperature)
    if fl_temp <= 0:
        return "A cold isn't it?"
    elif fl_temp > 10:
        return "Nice weather we're having" 
    else:
        return "Cool"
    
    

