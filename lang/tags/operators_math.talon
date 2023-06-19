tag: user.code_operators_math
-

# math operators
op minus: user.code_operator_subtraction()
op plus: user.code_operator_addition()
op times: user.code_operator_multiplication()
op divide: user.code_operator_division()
op mod: user.code_operator_modulo()
(op (power | exponent) | to the power [of]): user.code_operator_exponent()

# comparison operators
is equal: user.code_operator_equal()
is not equal: user.code_operator_not_equal()
is greater: user.code_operator_greater_than()
is less: user.code_operator_less_than()
is greater [or] equal: user.code_operator_greater_than_or_equal_to()
is less [or] equal: user.code_operator_less_than_or_equal_to()

# logical operators
op and: user.code_operator_and()
op or: user.code_operator_or()

# set operators
is in: user.code_operator_in()
is not in: user.code_operator_not_in()
