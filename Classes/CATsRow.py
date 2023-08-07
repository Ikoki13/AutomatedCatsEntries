from typing import List
from Classes.CATsCell import CATsCell


class CATsRow:
    def __init__(self, timeEntries):
        self.listOfTimeEntries = []
        catsCell = CATsCell()

        for e in timeEntries:
            if (not catsCell.addTimeEntry(e)):
                self.listOfTimeEntries.append(catsCell)
                catsCell = CATsCell()
                catsCell.addTimeEntry(e)
        self.listOfTimeEntries.append(catsCell)