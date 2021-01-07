from analizer_pl.abstract.instruction import Instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo

class UseDataBase(Instruction):
    def __init__(self, db, row, column):
        Instruction.__init__(self, row, column)
        self.db = db

    def execute(self, environment):
        out = "dbtemp = "
        out += '"'
        out += "USE "
        out += self.db + ";"
        out += '"\n'
        return code.C3D(out, "use_database", self.row, self.column)
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_USE")