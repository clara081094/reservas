
import sys
import telnetlib
import time

class Ussd:

	tn = ""
	mensaje = ""
	estado = 0

	def __init__(self):
		self.tn = telnetlib.Telnet('192.168.1.50',5038,10)

	def cargar(self,tx):
		tx.write("Action: Login\r\n")
		tx.write("UserName: admin\r\n")
		tx.write("Secret: amp111\r\n\r\n")

	def iniciarSesion(self):
		self.estado=1
		self.cargar(self.tn)
		self.tn.write("Action: DongleSendUSSD\r\n")
		self.tn.write("Device: dongle0\r\n")
		self.tn.write("USSD: *838#\r\n\r\n")
		time.sleep(5)
		self.tn.write("Action: Logoff\r\n\r\n")

		self.tn.read_until("AppData: Incoming USSD:")
		self.mensaje=self.tn.read_until("Uniqueid:")
		self.tn.write("Action: Logoff\r\n\r\n")
		self.mensaje=self.mensaje[:-10]
		#self.mensaje=self.tn.read_some()
		#self.mensaje="\nholi<br>holaaa<br>plap"

	def getMensajes(self):
		return self.mensaje

	def return_tn(self):
		return self.tn

	def respuesta(self,cod):
		self.mensaje=""
		self.cargar(self.tn)
		self.tn.write("Action: DongleSendUSSD\r\n")
		self.tn.write("Device: dongle0\r\n")
		print(str(cod))
		self.tn.write("USSD: "+str(cod)+"\r\n\r\n")
		time.sleep(5)
		self.tn.write("Action: Logoff\r\n\r\n")
		
		self.tn.read_until("AppData: Incoming USSD:")
		self.mensaje=self.tn.read_until("Uniqueid:")
		self.tn.write("Action: Logoff\r\n\r\n")
		self.mensaje=self.mensaje[:-10]

	def terminar(self):
		self.mensaje=""
		self.cargar(self.tn)
		self.tn.write("Action: DongleSendUSSD\r\n")
		self.tn.write("Device: dongle0\r\n")
		self.tn.write("USSD: 0\r\n\r\n")
		time.sleep(5)
		self.tn.write("Action: Logoff\r\n\r\n")
		self.mensaje=""


