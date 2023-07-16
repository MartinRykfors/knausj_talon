tag: user.code_operators_math
-

# math operators
(operator | operate) minus: user.code_operator_subtraction()
(operator | operate) plus: user.code_operator_addition()
(operator | operate) times: user.code_operator_multiplication()
(operator | operate) divide: user.code_operator_division()
(operator | operate) mod: user.code_operator_modulo()
((operator | operate) (power | exponent) | to the power [of]): user.code_operator_exponent()

# comparison operators
is equal: user.code_operator_equal()
is not equal: user.code_operator_not_equal()
is greater: user.code_operator_greater_than()
is less: user.code_operator_less_than()
is greater [or] equal: user.code_operator_greater_than_or_equal_to()
is less [or] equal: user.code_operator_less_than_or_equal_to()

# logical operators
(operator | operate) and: user.code_operator_and()
(operator | operate) or: user.code_operator_or()

# set operators
is in: user.code_operator_in()
is not in: user.code_operator_not_in()
