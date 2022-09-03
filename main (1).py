#A01412171 Alan Herrera Martínez 
puntaje = 0
respuesta = ""
jugadores = 0

print("Cuantos jugadores son?")
jugadores = int(input())

while jugadores != 0:
  puntaje = 0
  print("Jugador " + str(jugadores) + ": El presidente de Mexico es Andres Manuel Lopez Obrador?")
  respuesta = input()
  if respuesta == "si":
   puntaje = puntaje + 1
  else:
   puntaje = puntaje - 1

  print("Jugador " + str(jugadores) + " Puntuaje es igual a " + str(puntaje))
  jugadores = jugadores - 1
  





