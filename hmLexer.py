# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,4,4,28,8,4,
        11,4,12,4,29,1,5,1,5,5,5,34,8,5,10,5,12,5,37,9,5,1,6,1,6,1,7,4,7,
        42,8,7,11,7,12,7,43,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,1,0,5,1,0,48,57,2,0,65,90,97,122,3,0,48,57,65,90,97,122,2,0,
        43,43,45,45,3,0,9,10,13,13,32,32,49,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,22,1,0,0,0,7,24,1,0,0,0,9,27,1,
        0,0,0,11,31,1,0,0,0,13,38,1,0,0,0,15,41,1,0,0,0,17,18,5,92,0,0,18,
        2,1,0,0,0,19,20,5,45,0,0,20,21,5,62,0,0,21,4,1,0,0,0,22,23,5,40,
        0,0,23,6,1,0,0,0,24,25,5,41,0,0,25,8,1,0,0,0,26,28,7,0,0,0,27,26,
        1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,10,1,0,0,0,
        31,35,7,1,0,0,32,34,7,2,0,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,
        0,0,0,35,36,1,0,0,0,36,12,1,0,0,0,37,35,1,0,0,0,38,39,7,3,0,0,39,
        14,1,0,0,0,40,42,7,4,0,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,
        0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,6,7,0,0,46,16,1,0,0,0,4,0,29,
        35,43,1,6,0,0
    ]

class hmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUMBER = 5
    VARIABLE = 6
    OPERATOR = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "'->'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "VARIABLE", "OPERATOR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "VARIABLE", 
                  "OPERATOR", "WS" ]

    grammarFileName = "hm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


