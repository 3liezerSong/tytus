import re
from graphviz import Digraph

varGramatical = []
varSemantico =[]
reservadas = {
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'numeric': 'NUMERIC',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'real': 'REAL',
    'money': 'MONEY',
    'text': 'TEXT',
    'varying': 'VARYING',
    'varchar': 'VARCHAR',
    'character': 'CHARACTER',
    'char': 'CHAR',
    'timestamp': 'TIMESTAMP',
    'date': 'DATE',
    'time': 'TIME',
    'interval': 'INTERVAL',
    'year': 'YEAR',
    'month': 'MONTH',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'to': 'TO',
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'create': 'CREATE',
    'type': 'TYPE',
    'as': 'AS',
    'enum': 'ENUM',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'is': 'IS',
    'null': 'NULL',
    'between': 'BETWEEN',
    'in': 'IN',
    'like': 'LIKE',
    'ilike': 'ILIKE',
    'similar': 'SIMILAR',
    'table': 'TABLE',
    'replace': 'REPLACE',
    'database': 'DATABASE',
    'databases': 'DATABASES',
    'show': 'SHOW',
    'if': 'IF',
    'exists': 'EXISTS',
    'alter': 'ALTER',
    'rename': 'RENAME',
    'owner': 'OWNER',
    'mode': 'MODE',
    'drop': 'DROP',
    'constraint': 'CONSTRAINT',
    'unique': 'UNIQUE',
    'check': 'CHECK',
    'references': 'REFERENCES',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'foreign': 'FOREIGN',
    'add': 'ADD',
    'column': 'COLUMN',
    'set': 'SET',
    'select': 'SELECT',
    'from': 'FROM',
    'delete': 'DELETE',
    'where': 'WHERE',
    'default': 'DEFAULT',
    'insert': 'INSERT',
    'into': 'INTO',
    'values': 'VALUES',
    'update': 'UPDATE',
    'count': 'COUNT',
    'avg': 'AVG',
    'sum': 'SUM',
    'distinct': 'DISTINCT',
    'abs': 'ABS',
    'cbrt': 'CBRT',
    'ceil': 'CEIL',
    'ceiling': 'CEILING',
    'degrees': 'DEGREES',
    'div': 'DIV',
    'exp': 'EXP',
    'factorial': 'FACTORIAL',
    'floor': 'FLOOR',
    'gcd': 'GCD',
    'lcm': 'LCM',
    'ln': 'LN',
    'log': 'LOG',
    'log10': 'LOG10',
    'min_scale': 'MIN_SCALE',
    'mod': 'MOD',
    'pi': 'PI',
    'power': 'POWER',
    'radians': 'RADIANS',
    'round': 'ROUND',
    'scale': 'SCALE',
    'sign': 'SIGN',
    'sqrt': 'SQRT',
    'trim_scale': 'TRIM_SCALE',
    'truc': 'TRUC',
    'width_bucket': 'WIDTH_BUCKET',
    'random': 'RANDOM',
    'setseed': 'SETSEED',
    'max': 'MAX',
    'min': 'MIN',
    'having': 'HAVING',
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'except': 'EXCEPT',
    'all': 'ALL',
    'acos': 'ACOS',
    'acosd': 'ACOSD',
    'asin': 'ASIN',
    'asind': 'ASIND',
    'atan': 'ATAN',
    'atand': 'ATAND',
    'atan2': 'ATAN2',
    'atan2d': 'ATAN2D',
    'cos': 'COS',
    'cosd': 'COSD',
    'cot': 'COT',
    'cotd': 'COTD',
    'sin': 'SIN',
    'sind': 'SIND',
    'tan': 'TAN',
    'tand': 'TAND',
    'sinh': 'SINH',
    'cosh': 'COSH',
    'tanh': 'TANH',
    'asinh': 'ASINH',
    'acosh': 'ACOSH',
    'atanh': 'ATANH',
    'group': 'GROUP',
    'by': 'BY',
    'now': 'NOW',
    'current_date': 'CURRENT_DATE',
    'current_time': 'CURRENT_TIME',
    'date_part': 'date_part',
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',
    'unknown': 'UNKNOWN',
    'extract': 'EXTRACT',
    'inherits':'INHERITS'
}




tokens = [
             'PTCOMA',
             'COMA',
             'LLIZQ',
             'LLDR',
             'PARIZQ',
             'PARDR',
             'IGUAL',
             'MAS',
             'MENOS',
             'GNOT',
             'MULT',
             'DIVI',
             'ANDO',
             'ORO',
             'NOTO',
             'MENOR',
             'MAYOR',
             'IGUALIGUAL',
             'NOIGUAL',
             'NUMDECIMAL',
             'ENTERO',
             'CADENA',

             'ID',
             'MODU',
             'PUNTO',
             'EXPO',
             'MAYORIGUAL',
             'MENORIGUAL',
             'MENMEN',
             'MAYMAY',
             'MENMAY',
             'CRIZQ',
             'CRDR',

         ] + list(reservadas.values())

# Tokens
t_PTCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDR = r'\)'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_GNOT = r'~'
t_MULT = r'\*'
t_DIVI = r'/'
t_ANDO = r'\&'
t_ORO = r'\|'
t_NOTO = r'!'
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUALIGUAL = r'=='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_MENMEN = r'<<'
t_MAYMAY = r'>>'
t_NOIGUAL = r'!='
t_MENMAY = r'<>'
t_MODU = r'%'
t_PUNTO = r'\.'
t_EXPO = r'\^'
t_LLIZQ = r'\{'
t_LLDR = r'\}'
t_CRIZQ = r'\['
t_CRDR = r'\]'


def t_NUMDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor no es parseable a decimal %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor no es parseable a integer %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter irreconocible! '%s'" % t.value[0])
    # meter a tabla de errores!

    t.lexer.skip(1)


import ply.lex as lex

lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE)

# from expresion import *
from tytus.parser.team21.Analisis_Ascendente.expresion import *
from tytus.parser.team21.Analisis_Ascendente.instruccion import *

precedence = (
    ('left', 'OR'),
    ('left', 'AND', 'BETWEEN', 'NOT', 'LIKE', 'ILIKE', 'IN'),
    ('left', 'ORO'),
    ('left', 'ANDO'),
    ('left', 'NOIGUAL', 'MENMAY', 'IGUALIGUAL'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAYMAY', 'MENMEN'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIVI', 'MODU'),
    ('left', 'EXPO'),
    ('left', 'NOTO', 'GNOT'),
    ('left', 'PARIZQ', 'PARDR')
)



#varSemantico.append('SEMANTICO')
def p_s(t):
    's               : instrucciones'
    t[0] = t[1]
    print(t[0])
    varGramatical.append('s ::= intrucciones')
    varSemantico.append('g ')

def p_instrucciones(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]
    varGramatical.append('instrucciones ::= instrucciones instruccion')
    varSemantico.append('f ')

def p_instruccion(t):
    'instrucciones      : instruccion'
    t[0] = [t[1]]
    varGramatical.append('instrucciones ::= instruccion')
    varSemantico.append('e ')

# CREATE
def p_create(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR PTCOMA'

    t[0] = CreateTable(t[3], t[5], None)
    varGramatical.append('instruccion :: = CREATE TABLE ID PARIZQ campos PARDR PTCOMA')
    varSemantico.append('t ')



def p_create2(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR INHERITS PARIZQ ID PARDR PTCOMA'
    t[0] = CreateTable(t[3], t[5], t[9])


def p_campos(t):
    '''campos           : campos COMA campo'''
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('campos :: = campos COMA campo')
    varSemantico.append('y ')

def p_campos2(t):
    'campos             : campo'
    t[0] = [t[1]]
    varGramatical.append('campos :: = campo')
    varSemantico.append(' p')

def p_campoSimple(t):
    'campo              : ID tipo'
    t[0] = Campo(1, t[1], t[2], None, None, None, None)
    varGramatical.append('campo :: = ID tipo')
    varSemantico.append(' q')

def p_campo(t):
    '''campo            : ID tipo acompaniamiento'''
    t[0] = Campo(1, t[1], t[2], t[3], None, None, None)
    varGramatical.append('campo :: = ID tipo acompaniamiento')
    varSemantico.append('m ')

def p_foreign(t):
    'campo              : CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR'
    t[0] = Campo(2, t[2], None, None, t[6], t[9], t[11])
    varGramatical.append('campo :: = CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR')
    varSemantico.append('z ')

def p_foreign2(t):
    'campo              : FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR'
    t[0] = Campo(3, None, None, None, t[4], t[7], t[9])
    varGramatical.append('campo :: = FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR')
    varSemantico.append(' x')

def p_primary(t):
    'campo              : PRIMARY KEY PARIZQ ID PARDR'
    t[0] = Campo(4, t[4], None, None, None, None, None)
    varGramatical.append('campo :: = PRIMARY KEY PARIZQ ID PARDR')
    varSemantico.append('c ')

def p_listacampo(t):
    '''acompaniamiento  : acompaniamiento acom'''
    t[1].append(t[2])
    t[0] = t[1]
    # print(t[0])
    varGramatical.append('acompaniamiento :: = acompaniamiento acom')
    varSemantico.append(' v')

def p_listacampo2(t):
    'acompaniamiento    : acom'
    t[0] = [t[1]]
    varGramatical.append('acompaniamiento :: = acom')
    varSemantico.append('b ')

def p_acompaniamiento(t):
    '''acom             : NOT NULL
                        | NULL
                        | UNIQUE PARIZQ listaID PARDR
                        | DEFAULT valores
                        | PRIMARY KEY'''
    if t[1].lower() == 'not'         :
        t[0] = Acompaniamiento('NOT', None)
        varGramatical.append('acom :: = NOT NULL')
        varSemantico.append(' n')
    elif t[1].lower() == 'null'      :
        t[0] = Acompaniamiento('NULL', None)
        varGramatical.append('acom :: = NULL')
        varSemantico.append('re ')
    elif t[1].lower() == 'unique'    :
        t[0] = Acompaniamiento('UNIQUE', t[3])
        varGramatical.append('acom :: = UNIQUE')
        varSemantico.append(' we')
    elif t[1].lower() == 'default'   :
        t[0] = Acompaniamiento('DEFAULT', t[2])
        varGramatical.append('acom :: = DEFAULT')
        varSemantico.append(' qw')
    elif t[1].lower() == 'primary'   :
        t[0] = Acompaniamiento('PRIMARY', None)
        varGramatical.append('acom :: = PRIMARY')
        varSemantico.append('yt ')


def p_acompaniamiento2(t):
    'acom               : UNIQUE'
    t[0] = Acompaniamiento('UNIQUE', None)


def p_acompaniamiento3(t):
    'acom               : UNIQUE ID'
    t[0] = Acompaniamiento('UNIQUE', t[2])

def p_tipos(t):
    '''tipo             : SMALLINT
                        | INTEGER
                        | BIGINT
                        | DECIMAL
                        | NUMERIC
                        | REAL
                        | DOUBLE
                        | MONEY
                        | TEXT
                        | TIMESTAMP
                        | DATE
                        | TIME
                        | INTERVAL
                        | BOOLEAN'''
    t[0] = Tipo(t[1].upper(), None)
    varGramatical.append('tipo :: ='+str(t[1]))
    varSemantico.append('fr ')


def p_tiposTexto(t):
    '''tipo             : CHARACTER PARIZQ ENTERO PARDR
                        | VARCHAR PARIZQ ENTERO PARDR
                        | CHAR PARIZQ ENTERO PARDR
                        | CHARACTER VARYING PARIZQ ENTERO PARDR'''
    varGramatical.append('tipo :: =' + str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]))
    varSemantico.append('yt ')
    if t[2] == '(':
        t[0] = Tipo(t[1].upper(), Primitivo(t[3]))
    else:
        t[0] = Tipo(t[1].upper() + ' ' + t[2].upper(), Primitivo(t[4]))

    if t[3]=='(':
        varGramatical.append('tipo :: =' + str(t[1]) + str(t[2]) + str(t[3])+ str(t[4]) + str(t[5]))
        varSemantico.append('gt ')

# INSERT INTO
def p_insertInto(t):
    'instruccion        : INSERT INTO ID PARIZQ listaID PARDR VALUES values PTCOMA'
    t[0] = t[1]
    varGramatical.append('instruccion :: = INSERT INTO ID PARIZQ listaID PARDR VALUES values PTCOMA')
    varSemantico.append('ot ')


def p_insertInto2(t):
    'instruccion        : INSERT INTO ID VALUES values PTCOMA'
    t[0] = InsertInto(t[3], None, t[5])
    varGramatical.append('instruccion :: = INSERT INTO ID VALUES values PTCOMA')
    varSemantico.append('yg ')


# lista de id
def p_listaID(t):
    'listaID            : listaID COMA var'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('listaID :: = listaID COMA ID')
    varSemantico.append('io ')



def p_listaID2(t):
    'listaID            : var'
    t[0] = [t[1]]
    varGramatical.append('listaID :: = ID')
    varSemantico.append('iq ')



def p_values(t):
    'values             : values COMA value'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('values :: = values COMA value')
    varSemantico.append('iw ')



def p_values2(t):
    'values             : value'
    t[0] = [t[1]]
    varGramatical.append('values :: = value')
    varSemantico.append('ie ')

def p_value(t):
    'value              : PARIZQ listaValores PARDR'
    t[0] = t[2]
    varGramatical.append('value :: = PARIZQ listaValores PARDR')
    varSemantico.append('ir ')

# lista de valores
def p_listaValores(t):
    'listaValores       : listaValores COMA valores'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('listaValores :: = listaValores COMA valores')
    varSemantico.append('it ')



def p_listaValores2(t):
    'listaValores       : valores'
    t[0] = [t[1]]
    varGramatical.append('listaValores :: = valores')
    varSemantico.append('iy ')



# VALORES
def p_valores(t):
    '''valores          : ENTERO '''
    t[0] = Primitivo(t[1])
    #varGramatical.append('valores ::= '+)
    #varSemantico.append('iu ')

def p_valoresDec(t):
    '''valores          : NUMDECIMAL  '''
    t[0] = Primitivo(t[1])


def p_valoresCad(t):
    '''valores          : CADENA  '''
    t[0] = Primitivo(t[1])
    varGramatical.append('valores ::= CADENA')
    varSemantico.append('ii ')


#def p_valores2(t):
 #   '''valores2         : valores
  #                      | var'''
   # t[0] = Primitivo(t[1])



# UPDATE
def p_update(t):
    'instruccion        : UPDATE ID SET asignaciones PTCOMA'
    t[0] = Update(t[2], t[4], None)
    varGramatical.append('instruccion ::= UPDATE ID SET asignaciones PTCOMA')
    varSemantico.append('ip ')



def p_update2(t):
    'instruccion        : UPDATE ID SET asignaciones WHERE andOr PTCOMA'
    t[0] = Update(t[2], t[4], t[6])
    varGramatical.append('instruccion ::= UPDATE ID SET asignaciones WHERE andOr PTCOMA')
    varSemantico.append('is ')



def p_asignaciones(t):
    'asignaciones       : asignaciones COMA asignacion'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('asignaciones ::= asignaciones COMA asignacion')
    varSemantico.append('id ')



def p_asignaciones2(t):
    'asignaciones       : asignacion'
    t[0] = [t[1]]
    varGramatical.append('asignaciones ::= asignacion')
    varSemantico.append('if ')


def p_where(t):
    '''where            : asignacion
                        '''
    t[0] = t[1]
    varGramatical.append('where ::= asignacion')
    varSemantico.append('ig ')



def p_where7(t):
    '''where            : boolean
                        '''
    t[0] = t[1]
    varGramatical.append('where ::= boolean')
    varSemantico.append('in ')


def p_where0(t):
    '''where            : boolean
                        '''
    t[0] = t[1]

def p_whereN(t):
    '''where            : NOT boolean
                        | ID IN PARIZQ listaValores PARDR 
                        | ID BETWEEN valores AND valores'''
    if t[1].upper() == 'NOT'     : t[0] = Where(1, t[2], None, None, None)
    elif t[2].upper() == 'IN'    : t[0] = Where(2, None, t[4], None, None)
    else                         : t[0] = Where(3, None, None, t[3], t[5])


def p_where1(t):
    '''where            : valores  comparisonP2
                        | var comparisonP2
                        | boolean  comparisonP
                        '''
    t[0] = t[1]
    varGramatical.append('where ::= NOT boolean')
    varSemantico.append('ih ')

def p_where2(t):
    '''where            : valores2  comparisonP2
                        '''
    t[0] = t[1]
    varGramatical.append('where ::= valores2  comparisonP2')
    varSemantico.append('ih ')


def p_where3(t):
    '''where            : ID IS DISTINCT FROM valores
                        '''
    t[0] = t[1]


def p_ComparisonP(t):
    ''' comparisonP     : IS TRUE
                        | IS FALSE
                        | IS UNKNOWN
    '''
    varGramatical.append('comparisonP ::= '+str(t[1])+str(t[2]))
    varSemantico.append('ix ')

def p_ComparisonP1(t):
    ''' comparisonP     : IS NOT TRUE
                        | IS NOT FALSE
                        | IS NOT UNKNOWN
    '''
    varGramatical.append('comparisonP ::= ' + str(t[1])+str(t[2])+str(t[3]))
    varSemantico.append('ix ')


def p_ComparisonP2(t):
    ''' comparisonP2    : IS NULL
    '''
    varGramatical.append('comparisonP2 ::= IS NULL')
    varSemantico.append('zx ')


def p_ComparisonP3(t):
    ''' comparisonP2    : IS NOT NULL
    '''
    varGramatical.append('comparisonP2 ::=  IS NOT NULL')
    varSemantico.append('cx ')


def p_ComparisonP4(t):
    ''' comparisonP2    : NOTNULL
                        | ISNULL
    '''
    varGramatical.append('comparisonP2 ::= ' + str(t[1]))
    varSemantico.append('iv ')


def p_andOr(t):
    '''andOr            : andOr AND andOr
                        | andOr OR andOr
                        '''
    t[0] = Expresion(t[1], t[3], t[2])

def p_andOr2(t):
    'andOr              : where'
    t[0] = t[1]

def p_asignacion(t):
    '''asignacion       : var IGUAL E
    '''
    t[0] = Asignacion(t[1], t[3])

def p_E(t):
    '''E                : operando
	                    | boolean
                        | unario
                        | valores
                        | var
                        | pnum
                        | math'''


def p_E1(t):
    '''E                : PARIZQ E PARDR '''


#    print("expresion")
#    if t[1] == '('  : t[0] = t[2]
#    else            : t[0] = t[1]

def p_E2(t):
    '''boolean          : FALSE
                        | TRUE'''
    t[0] = t[1]


def p_oper(t):
    '''operando         : E MAS E
	                    | E MENOS E
	                    | E MULT E
 	                    | E DIVI E
                        | E MODU E
                        | E EXPO E
	                    | E MENMEN E
	                    | E MAYMAY E
	                    | E ANDO E
	                    | E ORO E
	                '''
    t[0] = Expresion(t[1], t[3], t[2])


def p_booleanos(t):
    '''boolean          : E IGUALIGUAL E
	                    | E NOIGUAL E
                        | E MENMAY E
	                    | E MENOR E
	                    | E MAYOR E
	                    | E MENORIGUAL E
	                    | E MAYORIGUAL E'''
    t[0] = Expresion(t[1], t[3], t[2])


def p_unarios(t):
    '''unario           : NOTO E
	                    | MENOS E
	                    | GNOT E
                        | MAS E '''
    t[0] = Unario(t[1], t[2])


def p_var(t):
    'var                : ID'
    t[0] = Id(t[1])

def p_alias(t):
    'var                : ID PUNTO ID'
    print(t[1] +t[2]+t[3])
    t[0] = IdId(Id(t[1]), Id(t[2]))


def p_pnum2(t):
    '''pnum                : PUNTO E'''
    print('punto')
    # t[0] = Id(t[1])


# DELETE
def p_delete(t):
    'instruccion        : DELETE FROM ID WHERE andOr PTCOMA'
    t[0] = Delete(t[3], t[5])

def p_delete2(t):
    'instruccion        : DELETE FROM ID PTCOMA'
    t[0] = Delete(t[3], None)


# DROP
def p_drop(t):
    '''instruccion      : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA
                        | DROP TABLE ID PTCOMA'''
    if t[2].upper() == 'TABLE'  : t[0] = Drop(2, False, t[3])
    elif t[3].upper() == 'IF'   : t[0] = Drop(1, True, t[5])
    else                        : t[0] = Drop(1, False, t[3])           



# CREATE or REPLACE DATABASE
def p_createDB(t):
    '''instruccion      : opcionCR ID PTCOMA
                        | opcionCR IF NOT EXISTS ID PTCOMA'''
    if t[2] == 'IF'     : t[0] = CreateTable(t[1], True, t[5], None)
    else                : t[0] = CreateTable(t[1], False, t[2], None)


def p_createDB2(t):
    '''instruccion      : opcionCR ID complemento PTCOMA
                        | opcionCR IF NOT EXISTS ID complemento PTCOMA'''
    if t[2] == 'IF'     : t[0] = CreateTable(t[1], True, t[5], t[6])
    else                : t[0] = CreateTable(t[1], False, t[2], t[3])

def p_opcionCR(t):
    '''opcionCR         : CREATE DATABASE
                        | CREATE OR REPLACE DATABASE'''
    if t[2].upper() == 'OR'     : t[0] = 2
    else                        : t[0] = 1 

def p_complementoCR(t):
    '''complemento      : OWNER IGUAL ID
                        | OWNER ID'''
    if t[2] == '='      : t[0] = ComplementoCR(t[3], None)
    else                : t[0] = ComplementoCR(t[2], None)

def p_complementoCR2(t):
    '''complemento      : OWNER IGUAL ID MODE IGUAL ENTERO
                        | OWNER ID MODE IGUAL ENTERO
                        | OWNER IGUAL ID MODE ENTERO
                        | OWNER ID MODE ENTERO
                        '''
    if t[2] == '='      : 
        if t[5] == '='  : t[0] = ComplementoCR(t[3], t[6])
        else            : t[0] = ComplementoCR(t[3], t[5])
    else                : 
        if t[4] == '='  : t[0] = ComplementoCR(t[2], t[5])
        else            : t[0] = ComplementoCR(t[2], t[4])


# SHOW
def p_showDB(t):
    'instruccion        : SHOW DATABASES PTCOMA'
    t[0] = Show(True)


# ALTER
def p_alterDB(t):
    '''instruccion      : ALTER DATABASE ID RENAME TO ID PTCOMA
                        | ALTER DATABASE ID OWNER TO LLIZQ ID LLDR''' #
    if t[4].upper() == 'RENAME'     : t[0] = AlterDatabase(1, t[3], t[6])
    else                            : t[0] = AlterDatabase(2, t[3], t[7].upper())


def p_alterT(t):
    '''instruccion      : ALTER TABLE ID ADD COLUMN ID tipo PTCOMA
                        ''' 
    t[0] = AlterTable(1, t[3], None, t[6], t[7], None, None, None, None, None, None, None)

def p_alterT2(t):
    'instruccion        : ALTER TABLE ID DROP COLUMN ID PTCOMA'
    t[0] = AlterTable(2, t[3], 'COLUMN', None, None, None, None, None, None, None, t[6], None)

def p_alterT3(t):
    'instruccion        : ALTER TABLE ID ADD CHECK ID PTCOMA'
    t[0] = AlterTable(1, t[3], None, None, None, t[6], None, None, None, None, None, None)

def p_alterT4(t):
    'instruccion        : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDR PTCOMA'
    t[0] = AlterTable(1, t[3], None, None, None, None, t[6], t[9], None, None, None, None)#

def p_alterT5(t):
    'instruccion        : ALTER TABLE ID ADD FOREIGN KEY PARIZQ listaID PARDR REFERENCES listaID PTCOMA'
    t[0] = AlterTable(1, t[3], None, None, None, None, None, None, t[8], t[11], None, None)

def p_alterT6(t):
    'instruccion        : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA'
    t[0] = AlterTable(3, t[3], None, None, None, None, None, None, None, None, None, t[6])

def p_alterT7(t):
    'instruccion        : ALTER TABLE ID DROP CONSTRAINT ID PTCOMA'
    t[0] = AlterTable(2, t[3], 'CONSTRAINT', None, None, None, None, None, None, None, t[6], None)


##################################################################
# SELECT
def p_selectTime(t):
    ''' instruccion     : SELECT Time PTCOMA'''


def p_selectTime2(t):
    ''' Time            : EXTRACT PARIZQ momento FROM TIMESTAMP  CADENA PARDR
                        | date_part PARIZQ CADENA COMA INTERVAL CADENA PARDR
    '''
    t[0] = t[1]


def p_selectTime3(t):
    ''' Time            : NOW PARIZQ PARDR
                        | TIMESTAMP CADENA
    '''
    t[0] = t[1]


def p_selectTime4(t):
    ''' Time            : CURRENT_TIME
                        | CURRENT_DATE
    '''
    t[0] = t[1]


def p_momento(t):
    ''' momento         : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND
    '''
    t[0] = t[1]


def p_instruccionSELECT(t):
    '''instruccion : select2 inst_union
                    '''
    # t[0]=t[1]


def p_instruccionSELECT2(t):
    '''instruccion : select2 PTCOMA
                     '''


def p_union2(t):
    '''inst_union : UNION ALL select2 PTCOMA
              '''


def p_union3(t):
    '''inst_union : INTERSECT ALL select2 PTCOMA
             '''


def p_union4(t):
    '''inst_union : EXCEPT ALL select2 PTCOMA
          '''


def p_union5(t):
    '''inst_union : UNION select2 PTCOMA
              '''


def p_union6(t):
    '''inst_union : INTERSECT select2 PTCOMA
              '''


def p_union7(t):
    '''inst_union : EXCEPT select2 PTCOMA
              '''


def p_groupBy(t):
    '''compSelect           : table_expr
    '''
    # t[0] = t[3]


def p_groupBy1(t):
    '''compSelect           : table_expr GROUP BY  compGroup
    '''


def p_having(t):
    '''compGroup        : list
    '''


def p_having1(t):
    '''compGroup        :  list HAVING andOr
    '''


def p_instselect(t):
    '''select2 : SELECT DISTINCT select_list FROM compSelect
                    '''
    # t[0] = t[1]+' '+t[2]+' '+t[3]+' '+t[4]+ ' '+t[5]


def p_instselect2(t):
    '''select2 : SELECT select_list FROM compSelect
    '''


def p_instselect3(t):
    '''select2 : SELECT select_list
                    '''


def p_instselect4(t):
    '''select2 : SELECT select_list FROM table_expr WHERE complemSelect
                    '''


def p_instselect5(t):
    '''complemSelect : andOr
    '''


def p_instselect6(t):
    '''complemSelect : andOr GROUP BY  compGroup
                    '''


def p_instselect7(t):
    '''select2 : SELECT DISTINCT select_list FROM table_expr WHERE complemSelect
                    '''


def p_selectList(t):
    '''select_list : MULT
                    | list'''


def p_list2(t):
    '''list : list COMA columna '''


def p_list3(t):
    '''list : columna '''


def p_columna2(t):
    '''columna : ID opcionID
                '''


def p_columna3(t):
    '''columna : ID AS ID
                '''


def p_columna4(t):
    '''columna : ID
                '''


def p_columna5(t):
    '''columna : ID AS CADENA
                '''


def p_columna6(t):
    '''columna : math AS ID
                '''


def p_columna7(t):
    '''columna : math AS CADENA
                '''


def p_columna8(t):
    '''columna : math
                '''


def p_columna9(t):
    '''columna : trig AS CADENA
                '''


def p_columna10(t):
    '''columna : trig
                '''


def p_columna11(t):
    '''columna : trig AS ID
                '''


def p_opcionID2(t):
    '''opcionID : PUNTO ascolumnaux
                | ID'''


def p_opcionID3(t):
    '''ascolumnaux : ID AS ID
                    '''


def p_opcionID4(t):
    '''ascolumnaux : ID
                    '''


def p_opcionID5(t):
    '''ascolumnaux : ID AS CADENA
                '''


def p_math2(t):
    ''' math  : ABS PARIZQ E PARDR
                | CBRT PARIZQ E PARDR
                | CEIL PARIZQ E PARDR
                | CEILING PARIZQ E PARDR
                | DEGREES PARIZQ E PARDR
                | EXP PARIZQ E PARDR
                | FACTORIAL PARIZQ E PARDR
                | FLOOR PARIZQ E PARDR
                | LCM PARIZQ E PARDR
                | LN PARIZQ E PARDR
                | LOG PARIZQ E PARDR
                | LOG10 PARIZQ E PARDR
                | RADIANS PARIZQ E PARDR
                | ROUND PARIZQ E PARDR
                | SIGN PARIZQ E PARDR
                | SQRT PARIZQ E PARDR
                | TRUC PARIZQ E PARDR
                | WIDTH_BUCKET PARIZQ E PARDR
                | SETSEED PARIZQ E PARDR
                | SUM PARIZQ E PARDR
                | AVG PARIZQ E PARDR
                | COUNT PARIZQ E PARDR
                | MIN PARIZQ E PARDR
                | MAX PARIZQ E PARDR '''


def p_math3(t):
    ''' math  :  DIV PARIZQ E COMA E PARDR
                | GCD PARIZQ E COMA E PARDR
                | MOD PARIZQ E COMA E PARDR
                | POWER PARIZQ E COMA E PARDR
                '''


def p_math4(t):
    ''' math  :  PI PARIZQ PARDR
                | RANDOM PARIZQ PARDR
                '''


def p_math6(t):
    ''' math  : MIN_SCALE
                | SCALE
                | TRIM_SCALE
                '''


def p_trig2(t):
    ''' trig : ACOS PARIZQ E PARDR
              | ACOSD PARIZQ E PARDR
              | ASIN PARIZQ E PARDR
              | ASIND PARIZQ E PARDR
              | ATAN PARIZQ E PARDR
              | ATAND PARIZQ E PARDR
              | ATAN2 PARIZQ E PARDR
              | ATAN2D PARIZQ E PARDR
              | COS PARIZQ E PARDR
              | COSD PARIZQ E PARDR
              | COT PARIZQ E PARDR
              | COTD PARIZQ E PARDR
              | SIN PARIZQ E PARDR
              | SIND PARIZQ E PARDR
              | TAN PARIZQ E PARDR
              | TAND PARIZQ E PARDR
              | SINH PARIZQ E PARDR
              | COSH PARIZQ E PARDR
              | TANH PARIZQ E PARDR
              | ASINH PARIZQ E PARDR
              | ACOSH PARIZQ E PARDR
              | ATANH PARIZQ E PARDR '''


def p_tableexpr2(t):
    '''table_expr : table_expr COMA tablaR
                    '''


def p_tableexpr3(t):
    '''table_expr : tablaR
                    '''


def p_tablaR2(t):
    '''tablaR : ID ID
                '''


def p_tablaR3(t):
    '''tablaR : ID AS ID
                '''


def p_tablaR4(t):
    '''tablaR : ID
                '''


# def p_condicion2(t):
#   '''condicion : andOr HAVING
#              | andOr'''
####################################################################
# MODO PANICO ***************************************
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    if not t:
        print("Fin del Archivo!")
        return

    # Read ahead looking for a closing '}'
    while True:
        tok = parser.token()  # Get the next token
        if not tok or tok.type == 'PTCOMA':
            print("Se recupero con ;")
            break
    parser.restart()


import ply.yacc as yacc

parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)


def graphstack(stack,stack2):
    varGramatical.append('PRODUCCIONES')

    varSemantico.append('SEMANTICO')

    s = Digraph('structs', filename='reporteGramatica.gv', node_attr={'shape': 'plaintext'})
    u = len(stack)
    g = 'stack [label =  <<TABLE>'
    for x in range(0, u):
        g += '<TR>'+'\n'+'<TD>'+str(stack.pop())+'</TD>'+'\n'+'<TD>'+str(stack2.pop())+'</TD>'+'\n'+'</TR>'

    g += '</TABLE>>, ];'

    #s.node(   g + "}")
    s.body.append(g)
    s.view()


graphstack(varGramatical,varSemantico)

