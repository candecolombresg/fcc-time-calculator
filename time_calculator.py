def add_time(hora1, hora2, day=False):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    hora1_pm = hora1.split(" ")
    hora1_min = hora1_pm[0].split(":")
    hora1_min[0] = int(hora1_min[0])
    hora2_min = hora2.split(":")
    min_totales = int(hora1_min[1])+int(hora2_min[1])
    min = str(min_totales%60)
    min = min.zfill(2)
    if hora1_pm[1]=="PM":
        hora1_min[0] += 12
    hora = int(hora1_min[0])+int(hora2_min[0])+min_totales//60
    dias = 0

    if hora>=24 and hora<48:
        hora -= 24
        dias = 1
        devolver2 = " (next day)"
    elif hora>=48:
        dias = hora//24
        hora = hora%24
        devolver2 = " ("+ str(dias) +" days later)"      
    else:
        devolver2 = ""
    
    if hora>12:
        hora -=12
        devolver1 = str(hora) + ":" + str(min) + " PM"
    elif hora==12:
        devolver1 = str(hora) + ":" + str(min) + " PM"
    elif hora == 0:
        hora = 12
        devolver1 = str(hora) + ":" + str(min) + " AM"        
    else:
        devolver1 = str(hora) + ":" + str(min) + " AM"
    
    if day is not False:
        ind = week.index(day.capitalize())
        ind2 = (ind + dias)%7
        day = week[ind2]
        devolver = devolver1 + ", " + day + devolver2
    else:
        devolver = devolver1 + devolver2

    return devolver