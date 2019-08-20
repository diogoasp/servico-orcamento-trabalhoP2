from lettuce import *
import cadastroOrcamento


@step('I have a budget id (\d+) And a product id (\d+) And product quantity (\d+)')
def given_i_have_id_and_products(step, id, p_id, p_qtd):
    world.id = int(id)
    world.p_id = int(p_id)
    world.p_qtd = int(p_qtd)

@step('I register the budget')
def register(step):
    world.result = str(cadastroOrcamento.cadastrarOrcamento(world.id, world.p_id, world.p_qtd))

@step('I see the text "([^"]*)"')
def check_operation(step, expected):
    assert (expected == world.result)
