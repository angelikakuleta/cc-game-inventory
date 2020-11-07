
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


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
