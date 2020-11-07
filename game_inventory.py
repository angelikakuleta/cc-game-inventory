import csv
from pathlib import Path

# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for key, value in inventory.items():
        print(f"{key}: {value}")


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for x in added_items:
        if x in inventory:
            inventory[x] += 1
        else:
            inventory[x] = 1


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for x in removed_items:
        if x in inventory:
            if inventory[x] == 1:
                inventory.pop(x)
            else:
                inventory[x] -= 1


def print_table(inventory, order=""):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    if (order == "count,asc"):
        temp_inventory = dict(sorted(inventory.items(), key=lambda x: x[1]))
    elif (order == "count,desc"):
        temp_inventory = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))
    else:
        temp_inventory = inventory

    print("""-----------------
item name | count
-----------------""")
    for key, value in temp_inventory.items():
        print("{:>9} | {:>5}".format(key, value))
    print("-----------------")


def import_inventory(inventory, filename="import_inventory.csv"):
    """Import new inventory items from a CSV file."""

    path = Path(__file__).parent
    try:
        with open(f"{path}\\{filename}") as csv_file:
            csv_reader = csv.reader(csv_file)

            items = []
            for row in csv_reader:
                items += row
            add_to_inventory(inventory, items)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_inventory(inventory, filename="export_inventory.csv"):
    """Export the inventory into a CSV file."""

    try:
        file_name = open(filename, "w", newline="")
        csv_writer = csv.writer(file_name)

        inventory_to_export = []
        for item in inventory:
            for i in range(inventory[item]):
                inventory_to_export.append(item)
        inventory_to_export.sort()
        print(inventory_to_export)
        csv_writer.writerow(inventory_to_export)
        file_name.close()
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")
