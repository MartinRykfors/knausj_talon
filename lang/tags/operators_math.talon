tag: user.code_operators_math
-

# math operators
operate minus: user.code_operator_subtraction()
operate plus: user.code_operator_addition()
operate times: user.code_operator_multiplication()
operate (divide | division): user.code_operator_division()
operate mod: user.code_operator_modulo()
(operate (power | exponent) | to the power [of]): user.code_operator_exponent()

# comparison operators
is equal: user.code_operator_equal()
is not equal: user.code_operator_not_equal()
is greater: user.code_operator_greater_than()
is less: user.code_operator_less_than()
is greater [or] equal: user.code_operator_greater_than_or_equal_to()
is less [or] equal: user.code_operator_less_than_or_equal_to()

# logical operators
logical and: user.code_operator_and()
logical or: user.code_operator_or()

# set operators
is in: user.code_operator_in()
is not in: user.code_operator_not_in()
