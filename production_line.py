import os,random
from variables import materials, forming_queue, forming_prod
from variables import cnc_queue, cnc_prod
from variables import buffing_queue, buffing_prod
from variables import completed, turn
from variables import forming_min, forming_max
from variables import cnc_min, cnc_max
from variables import buffing_min, buffing_max

TICK_DEFAULT = 1

def advance():
    global materials, forming_queue, forming_prod
    global cnc_queue, cnc_prod
    global buffing_queue, buffing_prod
    global completed, turn

    #Materials supply
    incoming = materials
    forming_queue += incoming

    #Forming
    forming_prod = random.randint(forming_min, forming_max)
    forming_prod = min(forming_prod, forming_queue)
    forming_queue -= forming_prod
    cnc_queue += forming_prod

    #CNC
    cnc_prod = random.randint(cnc_min, cnc_max)
    cnc_prod = min(cnc_prod, cnc_queue)
    cnc_queue -= cnc_prod
    buffing_queue += cnc_prod

    #Buffing
    buffing_prod = random.randint(buffing_min, buffing_max)
    buffing_prod = min(buffing_prod, buffing_queue)
    buffing_queue -= buffing_prod
    completed += buffing_prod

    turn += 1

def make_box(title, queue, width=30, label="Queue"):
    top = "┌" + "─" * (width - 2) + "┐"
    inner = f"{label}: {queue}"
    stats = f"│{inner:^{width-2}}│"
    name  = f"│{title:^{width-2}}│"
    bottom = "└" + "─" * (width - 2) + "┘"
    return [top, stats, name, bottom]

def make_counter_box(title, value, width=30, label=None):
    label = label or title
    top = "┌" + "─" * (width - 2) + "┐"
    inner = f"{label}: {value}"
    stats = f"│{inner:^{width-2}}│"         
    name  = f"│{title:^{width-2}}│"
    bottom = "└" + "─" * (width - 2) + "┘"
    return [top, stats, name, bottom]


def render():
    forming_box = make_box("Forming", forming_queue , width=30)
    cnc_box = make_box("CNC", cnc_queue , width=30)
    buffing_box = make_box("Buffing", buffing_queue , width=30)
    completed_box = make_counter_box("Completed", completed, width=30)
                       
    print(f"\nTurn: {turn}\n")
    print(f"\nMin/Max:\n")
    print(f"Forming : {buffing_min}/{buffing_max}")
    print(f"CNC: {cnc_min}/{cnc_max}")
    print(f"Buffing: {buffing_min}/{buffing_max}\n")
    print(f"\nMaterials supplied per turn: {materials}\n")
    for lines in zip(forming_box, cnc_box, buffing_box, completed_box):
        print("  ->  ".join(lines))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def do_run():
    advance()
    clear()
    render()


def do_show():
    clear()
    render()

def settings():
    global materials
    global forming_min, forming_max, cnc_min, cnc_max, buffing_min, buffing_max

    while True:
        print("\n--- SETTINGS MENU ---")
        print("1) Adjust materials per turn")
        print("2) Adjust station min/max outputs")
        print("3) Back\n")

        choice = input("Select an option (1-3): ").strip().lower()
        if choice in ("3", "back"):
            break

        # Adjust materials
        elif choice in ("1", "materials", "m"):
            inp = input(f"Enter new materials per turn (current: {materials}): ").strip().lower()
            try:
                val = int(inp)
                if val > 0:
                    materials = val
                    print(f"Materials per turn set to {materials}.")
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input.")

        # Adjust station min/max
        elif choice in ("2", "station", "s"):
            print("\nChoose station to adjust:")
            print("1) Forming")
            print("2) CNC")
            print("3) Buffing")
            print("4) Back\n")

            station_choice = input("Select a station (1-4): ").strip().lower()
            if station_choice in ("4", "back"):
                continue

            if station_choice == "1":
                station_name = "Forming"
                min_var, max_var = "forming_min", "forming_max"
                cur_min, cur_max = forming_min, forming_max
            elif station_choice == "2":
                station_name = "CNC"
                min_var, max_var = "cnc_min", "cnc_max"
                cur_min, cur_max = cnc_min, cnc_max
            elif station_choice == "3":
                station_name = "Buffing"
                min_var, max_var = "buffing_min", "buffing_max"
                cur_min, cur_max = buffing_min, buffing_max
            else:
                print("Invalid choice.")
                continue

            print(f"\nAdjusting {station_name} (current min/max: {cur_min}/{cur_max})")
            try:
                new_min = int(input(f"Enter new MIN for {station_name}: ").strip())
                new_max = int(input(f"Enter new MAX for {station_name}: ").strip())
                if new_min > 0 and new_max >= new_min:
                    globals()[min_var] = new_min
                    globals()[max_var] = new_max
                    print(f"{station_name} range set to {new_min}-{new_max}.")
                else:
                    print("Invalid range. MAX must be ≥ MIN and both > 0.")
            except ValueError:
                print("Invalid input. Please enter integers.")
        else:
            print("Invalid choice. Try again.")


def do_reset():
    global materials, forming_queue, forming_prod, cnc_queue, cnc_prod
    global buffing_queue, buffing_prod, completed, turn
    materials = 30      
    forming_queue = forming_prod = 0
    cnc_queue = cnc_prod = 0
    buffing_queue = buffing_prod = 0
    completed = 0
    turn = 0
    clear()
    render()


def parse_cmd(s: str):
    parts = s.strip().split()
    if not parts:
        return ("noop", None)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else None
    return (cmd, arg)

if __name__ == "__main__":
    do_show()  
    while True:
        raw = input("\nPress Enter or type [run (r) | show (s) | reset (rs) | quit (q) | settings (st)]: ").strip().lower()
        
        if raw in ("", "run", "r"):            # Enter, "run", or "r"
            do_run()
        elif raw in ("show", "s"):
            do_show()
        elif raw in ("reset", "rs"):
            do_reset()
        elif raw in ("quit", "exit", "q"):
            break
        elif raw in ("settings", "st"):
            settings()
        else:
            print("Unknown command.")
