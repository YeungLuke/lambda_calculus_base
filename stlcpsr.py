import ply.yacc as yacc # type: ignore

# Get the token list from the lexer
from stlclex import tokens

from stlc_cmd import Eval, Bind, Assert
from stlc_bind import TmAbbBind

# Define the start symbol
start = 'commands'


# Grammar rules
def p_commands(p):
    '''commands : command
                | command SEMI
                | command SEMI commands
    '''
    if len(p) in [2, 3]:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]


def p_command(p):
    '''command : term
               | VAR binder
               | ASSERT term EQ term
    '''
    if len(p) == 2:
        p[0] = Eval(p[1])
    elif len(p) == 3:
        p[0] = Bind(p[1], p[2])
    elif len(p) == 5:
        p[0] = Assert(p[2], p[4])


# Binder :
#   EQ Term
def p_binder(p):
    '''binder : EQ term
    '''
    p[0] = TmAbbBind(p[2])


def p_term(p):
    '''term : appterm
            | LAMBDA VAR DOT term
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_appterm(p):
    '''appterm : pathterm
               | appterm pathterm
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_pathterm(p):
    '''pathterm : LPAREN term RPAREN
                | VAR
    '''
    pass


# Error handling
def p_error(p):
    print(f"Parser Error: Unexpected token '{p.value}'")


# Create the parser
parser = yacc.yacc()
