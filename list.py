num_of_items = raw_input("How many items in your list? ")
def item_list(x):
    items = []
    for i in range(1, int(x), 2):
        item = raw_input("Enter list %r " % (i))
        items.append(item)
    return "Item List: %r" % (items)

print item_list(num_of_items)
