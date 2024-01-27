name = "Andressa Carvalho"
first_name=name[0:8] #primeiro index inclusivo, segundo exclusivo
last_name=name[9:]
print(first_name)
print(last_name)

funky_name=name[0:15:2]
print(funky_name)

reversed_name=name[::-1]
print(reversed_name)

website = "http://google.com"
slice=slice(7,-4) #segundo parametro conta negativo da direita pra esquerda
print(website[slice])

