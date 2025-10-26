Here’s a rewritten **`README.md`** that assumes both `production_line.py` and `variables.py` live together in the same GitHub repository (not separate folders). It’s written in standard GitHub Markdown formatting, clean and professional.

---

```markdown
# 🏭 Production Line Simulation

A Python-based terminal simulation of a simple **multi-stage production line**.  
Each “turn” (or cycle) moves items through the stages of a manufacturing process:

```

Materials  →  Forming  →  CNC  →  Buffing  →  Completed

```

Each station has its own configurable **minimum and maximum output**, and a set number of new materials is added to the line every turn.  
This lets you visualize flow, bottlenecks, and throughput in a compact, terminal-based dashboard.

---

## 📂 Repository Structure

```

production-line-simulator/
├── production_line.py   # Main simulation logic and CLI
├── variables.py         # Global state and configuration values
└── README.md            # Project documentation

````

---

## ⚙️ Requirements

- Python **3.10+**  
- macOS, Linux, or Windows terminal with **UTF-8** support (for box-drawing characters)  
- No external dependencies — uses only built-in modules (`os`, `random`).

---

## ▶️ Running the Simulation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/production-line-simulator.git
   cd production-line-simulator
````

2. Run the simulation:

   ```bash
   python3 production_line.py
   ```

3. The terminal will display the current state of the production line.
   You can then control the simulation interactively using simple commands.

---

## ⌨️ Commands

| Command      | Alias | Description                                                    |
| ------------ | ----- | -------------------------------------------------------------- |
| **Enter**    | —     | Advance the production line by one turn                        |
| **run**      | `r`   | Same as pressing Enter — runs one cycle                        |
| **show**     | `s`   | Redraws the current system state                               |
| **reset**    | `rs`  | Resets all queues, counters, and totals                        |
| **settings** | `st`  | Opens configuration menu (materials per turn, station min/max) |
| **quit**     | `q`   | Exits the simulation                                           |

---

## ⚙️ Settings Menu

When you type `settings` (or `st`), a configuration interface opens:

```
--- SETTINGS MENU ---
1) Adjust materials per turn
2) Adjust station min/max outputs
3) Back
```

### Adjusting Materials per Turn

Sets how many new units of raw material enter the system each cycle.

### Adjusting Station Min/Max

Lets you pick a station (`Forming`, `CNC`, or `Buffing`) and set its random output range.

Example:

```
Choose station to adjust:
1) Forming
2) CNC
3) Buffing

Select a station (1-3): 2
Adjusting CNC (current min/max: 32/35)
Enter new MIN for CNC: 20
Enter new MAX for CNC: 28
CNC range set to 20–28.
```

---

## 🧮 Simulation Logic

Each turn proceeds as follows:

1. **Material Input**
   A fixed number of materials (default: 30) are added to the forming queue.

2. **Forming → CNC → Buffing → Completed**
   Each station processes items based on its random min/max output.
   Processed items move to the next queue; unfinished ones remain waiting.

3. **Turn Counter**
   Increments each time the system advances.

---

## 📊 Example Output

```
Turn: 12
Materials supplied per turn: 30

┌────────────────────────────┐  ->  ┌────────────────────────────┐  ->  ┌────────────────────────────┐  ->  ┌────────────────────────────┐
│Queue:  15                  │      │Queue:   8                  │      │Queue:   2                  │      │Completed:  210             │
│          Forming           │      │           CNC              │      │          Buffing           │      │        Completed           │
└────────────────────────────┘      └────────────────────────────┘      └────────────────────────────┘      └────────────────────────────┘
```

Press **Enter** to advance one cycle, or type any command from the list above.

---

## 🧾 Configuration (`variables.py`)

`variables.py` defines all global state and configuration values:

```python
# Materials added each cycle
materials = 30

# Queues and totals
forming_queue = 0
forming_prod = 0
cnc_queue = 0
cnc_prod = 0
buffing_queue = 0
buffing_prod = 0
completed = 0
turn = 0

# Output ranges for each station
forming_min = 29
forming_max = 30
cnc_min = 32
cnc_max = 35
buffing_min = 28
buffing_max = 29
```

These values are imported directly into `production_line.py` and can be adjusted at runtime through the **Settings Menu**.

---

## 🧠 Notes

* Each station’s random output simulates variability in production rate.
* You can add new steps (e.g., *Painting*, *Packaging*) by following the same queue→process→output pattern.
* The display uses Unicode box-drawing characters; if they appear misaligned, ensure your terminal font supports them.

---

## 🏁 License

This project is open-source under the **MIT License**.
Feel free to modify, extend, and share.

---

## 👤 Author

**Eliot Mortimore**
Moscow, Idaho
[github.com/<your-username>](https://github.com/<your-username>)
