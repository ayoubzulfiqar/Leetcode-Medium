class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26  # 'A' through 'Z'
        self.grid = [[0] * self.cols for _ in range(self.rows)]

    def _parse_cell(self, cell_ref: str):
        col_char = cell_ref[0]
        row_num_str = cell_ref[1:]

        col_idx = ord(col_char) - ord('A')
        row_idx = int(row_num_str) - 1

        return row_idx, col_idx

    def setCell(self, cell: str, value: int) -> None:
        row_idx, col_idx = self._parse_cell(cell)
        self.grid[row_idx][col_idx] = value

    def resetCell(self, cell: str) -> None:
        row_idx, col_idx = self._parse_cell(cell)
        self.grid[row_idx][col_idx] = 0

    def getValue(self, formula: str) -> int:
        expression = formula[1:]
        
        parts = expression.split('+')
        operand1_str = parts[0]
        operand2_str = parts[1]

        val1 = self._get_operand_value(operand1_str)
        val2 = self._get_operand_value(operand2_str)

        return val1 + val2

    def _get_operand_value(self, operand_str: str) -> int:
        if operand_str.isdigit():
            return int(operand_str)
        else:
            row_idx, col_idx = self._parse_cell(operand_str)
            return self.grid[row_idx][col_idx]