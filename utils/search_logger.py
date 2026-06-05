def clear_search_tree_file():
    file = open("search_tree.txt", "w", encoding="utf-8")
    file.write("SEARCH TREE GENERATED STATES\n")
    file.write("=" * 80 + "\n")
    file.close()


def format_load(load):
    if len(load) == 0:
        return "empty"

    current = f"{load[0][1]} {load[0][2]} x{load[0][3]}"

    if len(load) == 1:
        return current

    return current + " + " + format_load(load[1:])


def format_delivered(delivered_keys):
    if len(delivered_keys) == 0:
        return "none"

    current = f"{delivered_keys[0]}"

    if len(delivered_keys) == 1:
        return current

    return current + ", " + format_delivered(delivered_keys[1:])


def log_state(action, x, y, load, load_count, g, h, f, depth, delivered_keys):
    file = open("search_tree.txt", "a", encoding="utf-8")

    file.write("\nGenerated State\n")
    file.write("-" * 80 + "\n")
    file.write(f"Action: {action}\n")
    file.write(f"Robot Position: ({x}, {y})\n")
    file.write(f"Load: {format_load(load)}\n")
    file.write(f"Load Count: {load_count}\n")
    file.write(f"g(n): {g}\n")
    file.write(f"h(n): {h}\n")
    file.write(f"f(n): {f}\n")
    file.write(f"Depth: {depth}\n")
    file.write(f"Delivered: {format_delivered(delivered_keys)}\n")

    file.close()