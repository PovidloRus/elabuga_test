class Table():
    title = list
    body = list

    def __init__(self, title: list[str], body: list[list[int]] | None = None):
        self.title = title
        if body == None:
            body = []
        self.body = body

    def index_slice(self, index_row_list: list[int]):
        slice_body = []
        for i in index_row_list:
            slice_body.append(self.body[i])
        return Table(self.title, slice_body)


class Limit:
    col: str
    operator: str
    num: int

    def __init__(self, conditions: str):
        conditions = conditions.split()
        self.col = conditions[0]
        self.operator = conditions[1]
        self.num = int(conditions[2])

    def check(self, table: Table) -> list[int]:
        col_index = 0
        for i in table.title:
            if i == self.col:
                col_index = table.title.index(i)
        list_true_index = []
        if self.operator == '<':
            for row in table.body:
                if row[col_index] < self.num:
                    list_true_index.append(table.body.index(row))
        else:
            for row in table.body:
                if row[col_index] > self.num:
                    list_true_index.append(table.body.index(row))
        return list_true_index


if __name__ == '__main__':
    cols_count, rows_count, limits_count = list(map(int, input().split()))
    title = list(map(str, input().split()))
    table = Table(title, )
    counter = 0
    while counter < rows_count:
        row = list(map(int, input().split()))
        table.body.append(row)
        counter += 1
    limits = []
    counter = 0
    while counter < limits_count:
        limit = Limit(input())
        limits.append(limit)
        counter+=1
    for limit in limits:
        index_rows = limit.check(table)
        table = table.index_slice(index_rows)

    summ_value = 0
    for i in table.body:
        summ_value += sum(i)

    print(summ_value)