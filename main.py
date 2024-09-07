import tkinter as tk
from tkinter import messagebox

def calculate_pp():
    try:
        star_rating = float(star_rating_entry.get())
        accuracy = float(accuracy_entry.get())
        combo = int(combo_entry.get())
        misses = int(misses_entry.get())
        mod_multiplier = float(mod_multiplier_entry.get())

        if accuracy < 0 or accuracy > 100:
            raise ValueError("Accuracy must be from 0 to 100")

        base_pp = (star_rating ** 2.2) * 2
        accuracy_factor = (accuracy / 100) ** 1.1
        combo_factor = (combo / (combo + misses)) ** 0.8
        pp = base_pp * accuracy_factor * combo_factor * mod_multiplier

        result_label.config(text=f"Your PP: {round(pp, 2)}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("osu! PP Calculator")

tk.Label(window, text="Star rating:").grid(row=0, column=0)
star_rating_entry = tk.Entry(window)
star_rating_entry.grid(row=0, column=1)

tk.Label(window, text="Accuracy (%):").grid(row=1, column=0)
accuracy_entry = tk.Entry(window)
accuracy_entry.grid(row=1, column=1)

tk.Label(window, text="Combo:").grid(row=2, column=0)
combo_entry = tk.Entry(window)
combo_entry.grid(row=2, column=1)

tk.Label(window, text="Misses:").grid(row=3, column=0)
misses_entry = tk.Entry(window)
misses_entry.grid(row=3, column=1)

tk.Label(window, text="Modifier:").grid(row=4, column=0)
mod_multiplier_entry = tk.Entry(window)
mod_multiplier_entry.grid(row=4, column=1)

calculate_button = tk.Button(window, text="Calculate PP", command=calculate_pp)
calculate_button.grid(row=5, columnspan=2)

result_label = tk.Label(window, text="Your PP: ")
result_label.grid(row=6, columnspan=2)

window.mainloop()