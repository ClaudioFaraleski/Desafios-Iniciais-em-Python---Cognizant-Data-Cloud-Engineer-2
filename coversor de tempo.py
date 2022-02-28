segundos = int(input())

horas = segundos // 3600
res = segundos % 3600
minutos = res // 60
segundos = res % 60




print("{}:{}:{}".format(horas, minutos, segundos))



# converter horas = segundos // 3600
#           res = segundos % 3600
#           minutos = rest // 60
#           segundos = rest % 60
