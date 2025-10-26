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
                       
    print(f"\nTurn: {turn}")
    print(f"Materials supplied per turn: {materials}\n")
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
        raw = input("\nPress Enter or type [run | r | show | s | reset | rs | quit | q]: ").strip().lower()
        
        if raw in ("", "run", "r"):            # Enter, "run", or "r"
            do_run()
        elif raw in ("show", "s"):
            do_show()
        elif raw in ("reset", "rs"):
            do_reset()
        elif raw in ("quit", "exit", "q"):
            break
        else:
            print("Unknown command.")