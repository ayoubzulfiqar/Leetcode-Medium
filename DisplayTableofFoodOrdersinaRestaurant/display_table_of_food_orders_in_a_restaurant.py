import collections

class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        food_items = set()
        table_orders = collections.defaultdict(lambda: collections.defaultdict(int))

        for customer_name, table_number_str, food_item in orders:
            food_items.add(food_item)
            table_number_int = int(table_number_str)
            table_orders[table_number_int][food_item] += 1

        sorted_food_items = sorted(list(food_items))
        
        header = ["Table"] + sorted_food_items

        display_table_rows = []
        
        sorted_table_numbers = sorted(list(table_orders.keys()))

        for table_num in sorted_table_numbers:
            row = [str(table_num)]
            for food_item in sorted_food_items:
                count = table_orders[table_num][food_item]
                row.append(str(count))
            display_table_rows.append(row)

        return [header] + display_table_rows