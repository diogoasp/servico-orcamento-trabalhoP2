Feature: Budget Register
    In order to send a id and a product list
    As salesman
    we'll register a new budget

    Scenario Outline: budget register
        Given I have a budget id <id> And a product id <p_id> And product quantity <p_qtd>
        When I register the budget
        Then I see the text <result>

    Examples:
          | id | p_id | p_qtd | result  |
          | 1  |   1  |   5   |"success"|
          | 1  |   2  |   4   |"success"|
          | 1  |   5  |   0   |  "fail" |
          | 2  |   4  |   2   |"success"|
          | 2  |   3  |   2   |"success"|
          | 2  |   1  |   0   |  "fail" |
          | 3  |   3  |   2   |"success"|
