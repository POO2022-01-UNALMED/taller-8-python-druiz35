from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
	listaFutbolistas = []
	def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
		self._golesMarcados = golesMarcados
		self._tarjetasRojas = tarjetasRojas
		self._piernaHabil = piernaHabil
		Futbolista.listaFutbolistas.append(self)
		Persona.__init__(self, nombre, edad, altura, sexo)
		Deportista.__init__(self, "Futbol", añosPracticando)

	def getGolesMarcados(self):
		return self._golesMarcados

	def setGolesMarcados(self, golesMarcados):
		self._golesMarcados = golesMarcados

	def getTarjetasRojas(self):
		return self._tarjetasRojas

	def setTarjetasRojas(self, tarjetasRojas):
		self._tarjetasRojas = tarjetasRojas

	def getPiernaHabil(self):
		return self._piernaHabil

	def setPiernaHabil(self, piernaHabil):
		self._piernaHabil = piernaHabil

	def __str__(self):
		mensaje_1 = "Mi nombre es " + self.getNombre()
		mensaje_2 = " soy profesional en el deporte " + self.getDeporte()
		mensaje_3 = " Tengo " + str(self.getEdad()) + " años de edad "
		mensaje_4 = "y llevo " + str(self.getAñosPracticando()) + " años en el deporte"
		return mensaje_1 + mensaje_2 + mensaje_3 + mensaje_4