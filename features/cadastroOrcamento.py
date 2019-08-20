import xmlrpclib

budgetServer = xmlrpclib.ServerProxy("http://localhost:8000/")

def cadastrarOrcamento(id, p_id, p_qtd):
    id_p_qtd = [p_id, p_qtd]
    if(budgetServer.setBudget(id, id_p_qtd)):
        return "success"
    else:
        return "fail"
