import unittest
from AbstractClassDeveloper import Invocador, AbstractLOL, AbstractSummoner 
from Summoner import *
from SqlCRUD import *
from unittest.mock import Mock
from time import sleep

#test que verifica que el invocador consultado regrese los parametros correctos
class Test_Lol(unittest.TestCase):
	
	def setUp(self):
		self.Summ = AppInvocador()
		self.sql = SqlCRUD()
		self.sumock=Mock(Id=12345, Name='Friky', Level=115, Wins=25, Losses=4, Tier="PLATINUM", Comportamiento='boring')
		self.sumoner=Invocador(self.sumock.Id,self.sumock.Name,self.sumock.Level,self.sumock.Wins,self.sumock.Losses,self.sumock.Tier, self.sumock.Comportamiento)
		#self.sql.CrearInvocador(self.sumock)
	
		self.sumock2=Mock(Id=123456, Name='hittler', Level=11, Wins=100, Losses=45, Tier="GOLD", Comportamiento='assassin')
		#self.sql.CrearInvocador(self.sumock2)
	
	def test_ShowInvocadorReal(self):
		self.Summ = AppInvocador()
		self.sql = SqlCRUD()
		self.assertTrue(self.sql.ConsultarInvocador('Taligar'))
		print("Mostrando Test")
		sleep(3)	
	
	def test_newSum(self):
		print("Realizando test")
		sleep(3)
		Player = self.Summ.DatosSummoner('Friky')
		self.assertEqual(Player.Id, self.sumoner.Id)
		self.assertEqual(Player.Name, self.sumoner.Name)
		self.assertEqual(Player.Level, self.sumoner.Level)
		self.assertEqual(Player.Wins, self.sumoner.Wins)
		self.assertEqual(Player.Losses, self.sumoner.Losses)
		self.assertEqual(Player.Tier, self.sumoner.Tier)
		self.assertEqual(Player.Comportamiento, self.sumoner.Comportamiento)

		Player2 = self.Summ.DatosSummoner('hittler')
		self.assertEqual(Player2.Id, self.sumoner.Id)
		self.assertEqual(Player2.Name, self.sumoner.Name)
		self.assertEqual(Player2.Level, self.sumoner.Level)
		self.assertEqual(Player2.Wins, self.sumoner.Wins)
		self.assertEqual(Player2.Losses, self.sumoner.Losses)
		self.assertEqual(Player2.Tier, self.sumoner.Tier)
		self.assertEqual(Player2.Comportamiento, self.sumoner.Comportamiento)
	"""
	def test_CreateInvocador(self):
		self.assertIsInstance(self.sql.CrearInvocador(self.sumoner), Invocador)
		print("Mostrando Resultado de -TEST CREATE- ")
		sleep(3)
	"""
	def test_DeleteInvocador(self):
		self.assertTrue(self.sql.BorrarInvocador('Friky'))
		print("Mostrando Resultado de -TEST DELETE- ")
		sleep(3)
	 
	def test_ShowInvocador(self):
		self.Summ = AppInvocador()
		self.sql = SqlCRUD()
		self.assertTrue(self.sql.ConsultarInvocador('hittler'))
		print("Mostrando Resultado de -TEST SHOW- ")
		sleep(3)
		
if __name__ == '__main__':
    unittest.main()
