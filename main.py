import tkinter as tk
from tkinter import messagebox, scrolledtext
import math

class ChickenFarm:
    """The class for the chicken farm."""

    def __init__(self, root):
        self.root = root
        self.root.title("Chicken Farm")
        self.root.geometry("400x550")
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets."""

        # Week prompt
        self.instruction_label = tk.Label(
            self.root, text="Enter the information of the week here"
        )
        self.instruction_label.pack(pady=10)

        # Week Entry
        tk.Label(self.root, text="Week Number (1 - 54):").pack()
        self.week_entry = tk.Entry(self.root, width=5)
        self.week_entry.pack()

        # Chickens Entry
        tk.Label(self.root, text="Total Chickens (2450 - 2525):").pack()
        self.chickens_entry = tk.Entry(self.root, width=5)
        self.chickens_entry.pack()

        # Laid Eggs Entry
        tk.Label(self.root, text="Chickens that laid eggs:").pack()
        self.laid_eggs_entry = tk.Entry(self.root, width=5)
        self.laid_eggs_entry.pack()

        # Hours Worked Entry
        tk.Label(self.root, text="Hours worked (1-40):").pack()
        self.hours_worked_entry = tk.Entry(self.root, width=5)
        self.hours_worked_entry.pack()

        # Button to view week
        self.week_view_button = tk.Button(
            self.root, text="View Week", command=self.view_week
        )
        self.week_view_button.pack(pady=10)

        # Output box
        self.output_area = scrolledtext.ScrolledText(
            self.root, width=45, height=20, wrap=tk.WORD
        )
        self.output_area.pack(pady=10)

        # Clear output button
        self.clear_button = tk.Button(
            self.root, text="Clear Output", command=self.clear_output
        )
        self.clear_button.pack()

        # Quit button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=5)

        # Autofocus
        self.week_entry.focus_set()

    def view_week(self):
        """View the week and display statistics."""

        try:
            num_week = int(self.week_entry.get())
            if num_week < 1 or num_week > 54:
                messagebox.showerror("Invalid Input", "Please choose a number between 1 and 54")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid week number.")
            return

        try:
            chickens = int(self.chickens_entry.get())
            if chickens < 2450 or chickens > 2525:
                messagebox.showerror("Invalid Input", "Please choose a number between 2450 and 2525")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid chicken number.")
            return

        try:
            chickens_laid_eggs = int(self.laid_eggs_entry.get())
            if chickens_laid_eggs < 0 or chickens_laid_eggs > chickens:
                messagebox.showerror("Invalid Input", "Chickens that laid eggs must be between 0 and total chickens.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the chickens that laid eggs.")
            return

        try:
            hours_worked = int(self.hours_worked_entry.get())
            if hours_worked < 1 or hours_worked > 40:
                messagebox.showerror("Invalid Input", "Please select an appropriate amount of hours.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        # Clear previous output
        self.output_area.delete("1.0", tk.END)

        # Clear entries
        self.week_entry.delete(0, tk.END)
        self.chickens_entry.delete(0, tk.END)
        self.laid_eggs_entry.delete(0, tk.END)
        self.hours_worked_entry.delete(0, tk.END)
        self.week_entry.focus_set()

        # Constants
        price_per_box = 6.00
        deposit_per_box = 1.00
        single_egg = 1.00
        payment_hour = 3.50

        # Calculations
        egg_count = chickens_laid_eggs * 5
        boxes_filled = math.floor(egg_count / 12)
        eggs_in_box = boxes_filled * 12
        eggs_left = egg_count - eggs_in_box

        final_payment = payment_hour * hours_worked
        maximum_income = (boxes_filled * (price_per_box + deposit_per_box)) + (eggs_left * single_egg)

        # Apply 10 free eggs to worker (bonus worth €10)
        bonus_eggs = 10
        bonus_value = bonus_eggs * single_egg
        final_payment = max(0, final_payment - bonus_value)  # Deduct from worker payment only

        lines = "-" * 45 + "\n"

        # Display output
        self.output_area.insert(tk.END, f"Week {num_week} Statistics:\n")
        self.output_area.insert(tk.END, lines)

        # Chickens
        self.output_area.insert(tk.END, "Chickens:\n\n")
        self.output_area.insert(tk.END, f"Total Chickens: {chickens}\n")
        self.output_area.insert(tk.END, f"Chickens That Laid Eggs: {chickens_laid_eggs}\n\n")
        self.output_area.insert(tk.END, lines)

        # Eggs
        self.output_area.insert(tk.END, "Eggs:\n\n")
        self.output_area.insert(tk.END, f"Laid Eggs: {egg_count} eggs\n")
        self.output_area.insert(tk.END, f"Filled Boxes: {boxes_filled} ({eggs_in_box} eggs)\n")
        self.output_area.insert(tk.END, f"Leftover Eggs: {eggs_left} eggs\n")
        self.output_area.insert(tk.END, lines)

        # Payment
        self.output_area.insert(tk.END, "Payment:\n\n")
        self.output_area.insert(tk.END, f"Hours Worked: {hours_worked} hours\n")
        self.output_area.insert(tk.END, f"Payment Rate: €{payment_hour:.2f}/hour\n")

        self.output_area.insert(tk.END, f"10 Free Eggs Bonus: -€{bonus_value:.2f}\n")
        self.output_area.insert(tk.END, f"Final Payment: €{final_payment:.2f}\n")
        self.output_area.insert(tk.END, lines)

        # Bonus Section
        self.output_area.insert(tk.END, "Worker Bonus:\n\n")
        self.output_area.insert(tk.END, f"Worker received 10 free eggs (worth €{bonus_value:.2f})\n")
        self.output_area.insert(tk.END, lines)

        # Receipt Section (Customer still pays full)
        self.output_area.insert(tk.END, "Customer Receipt:\n\n")
        self.output_area.insert(tk.END, f"Boxes Purchased: {boxes_filled} x €{price_per_box:.2f} = €{boxes_filled * price_per_box:.2f}\n")
        self.output_area.insert(tk.END, f"Box Deposits: {boxes_filled} x €{deposit_per_box:.2f} = €{boxes_filled * deposit_per_box:.2f}\n")
        self.output_area.insert(tk.END, f"Leftover Eggs: {eggs_left} x €{single_egg:.2f} = €{eggs_left * single_egg:.2f}\n")
        self.output_area.insert(tk.END, f"\nTotal Due: €{maximum_income:.2f}\n")
        self.output_area.insert(tk.END, lines)

    def clear_output(self):
        """Clear the output area."""
        self.output_area.delete("1.0", tk.END)


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChickenFarm(root)
    root.mainloop()
