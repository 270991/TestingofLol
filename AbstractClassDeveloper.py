from abc import ABC, abstractmethod

class Invocador():
	def __init__(self, Id, Name, Level, Wins, Losses, Tier, Comportamiento = None):
		self.Id = Id
		self.Name = Name
		self.Level = Level
		self.Wins = Wins
		self.Losses = Losses
		self.Tier = Tier
		self.Comportamiento = Comportamiento

	def __str__(self):

		return str(self.Id) +" - "+ str(self.Name) +" - "+ str(self.Level) +" - "+ str(self.Wins) +" - "+ str(self.Losses) +" - "+ str(self.Tier) +" - "+ str(self.Comportamiento)

###################################################################################################################

class Comportamiento():
	def __init__(self, Name, Comportamiento):
		self.Name = Name
		self.Comportamiento = Comportamiento

class AbstractSummoner(ABC):
	@abstractmethod
	def DatosSummoner(self, Name):
		pass
###################################################################################################################

class AbstractLOL(ABC):

	@abstractmethod
	def CrearInvocador(self, Name):
		pass

	@abstractmethod
	def MostrarLista(self):
		pass

	@abstractmethod
	def ConsultarInvocador(self, Name):
		pass

	@abstractmethod
	def ModificarInvocador(self):
		pass

	@abstractmethod
	def BorrarInvocador(self, Name):
		pass

###################################################################################################################
if __name__ == "__main__":
	comportamiento = Comportamiento('Nombre')
	print(comportamiento.Name)