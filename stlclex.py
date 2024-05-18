import ply.lex as lex # type: ignore

reserved = {
   'assert': 'ASSERT',
}

# Define the list of token names
tokens = list(set(reserved.values())) + [
    'VAR',        # variable names
    'LAMBDA',     # Lambda symbol (λ)
    'SEMI',       # semicolon (;)
    'DOT',        # Dot (.)
    'EQ',         # equal (=)
    'LPAREN',     # Left parenthesis
    'RPAREN',     # Right parenthesis
]

# Define regular expressions for the tokens
# t_VAR = r'[a-z][a-zA-Z0-9_\']*'
t_LAMBDA = r'λ'
t_SEMI = r';'
t_DOT = r'\.'
t_EQ = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignore whitespace and comments
t_ignore = ' \t\r\n'


def t_VAR(t):
    r'[a-z][a-zA-Z0-9_\']*'
    t.type = reserved.get(t.value, 'VAR')    # Check for reserved words
    return t


def t_COMMENT(t):
    r'%.*'


# Define a function for tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling
def t_error(t):
    print(f"Lexer Error: Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Create the lexer
lexer = lex.lex()
