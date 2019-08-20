# encoding: utf-8
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

#Status:
#0 - Iniciado
#1 - Em andamento
#2 - Finalizado
#3 - Cancelado

budget = []

def set(id, id_p_qtd):
	if id < 0 or id_p_qtd[1] < 1:
		return 0
	for orc in budget:
		_id = orc[0]
		_status = orc[1]
		if _id == id:
			if _status > 1:
				return 0
			else:
				orc[2].append(id_p_qtd)
				return 1
	budget.append([id, 0, [id_p_qtd]])
	return 1

def get(id):
	for orc in budget:
		_id = orc[0]
		if _id == id:
			return orc
	return []

def update(id, status):
	for orc in budget:
		_id = orc[0]
		if _id == id:
			orc[1] = status
			return 1
	return 0

server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(set,"setBudget")
server.register_function(get,"getBudget")
server.register_function(update,"updateBudgetStatus")
server.serve_forever()
