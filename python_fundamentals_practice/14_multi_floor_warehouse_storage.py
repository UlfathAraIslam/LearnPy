def place_item(warehouse, floor, shelf, slot, item_id):
    warehouse[floor][shelf][slot] = item_id
    return warehouse[floor][shelf][slot]

def count_floor_items(warehouse, floor):
    count = 0
    shelves = warehouse[floor]
    shelf_idx = 0
    while shelf_idx < len(shelves):
        slot_idx = 0
        while slot_idx < len(shelves[shelf_idx]):
            if shelves[shelf_idx][slot_idx] is not None:
                count += 1
            slot_idx += 1
        shelf_idx += 1
    return count
warehouse = [
    [[None, None], [101, None]],
    [[None, 202], [None, None]]
]
print (place_item(warehouse, 0, 0, 1, 305))
print (count_floor_items(warehouse, 0))