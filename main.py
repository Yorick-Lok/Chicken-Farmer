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
        bonus_eggs = 10

        # Total eggs laid
        total_eggs = chickens_laid_eggs * 5

        # Calculate initial boxes and leftover
        initial_boxes = total_eggs // 12
        initial_leftover = total_eggs % 12
        boxes_filled = initial_boxes
        

        # Calculate eggs to give as bonus:

        # Start with leftover eggs
        bonus_from_leftover = min(initial_leftover, bonus_eggs)
        eggs_needed = bonus_eggs - bonus_from_leftover

        boxes_removed = 0

        # If leftover not enough to make 10 bonus eggs
        if eggs_needed > 0:
            # Check if removing 1 box (12 eggs) can help reach bonus
            if initial_boxes > 0:
                # Remove 1 box
                boxes_removed = 1
                initial_boxes -= 1
                initial_leftover += 12
                # Recalculate bonus from leftover with added box eggs
                bonus_from_leftover = min(initial_leftover, bonus_eggs)
                eggs_needed = bonus_eggs - bonus_from_leftover
            else:
                # No boxes to remove, eggs_needed remains (worker bonus is just leftover eggs)
                # eggs_needed won't matter since no boxes left
                eggs_needed = 0  # worker only gets what's there (less than 10)


        # Total bonus eggs worker gets
        worker_bonus_eggs = bonus_from_leftover + eggs_needed

        # Deduct worker bonus eggs from eggs sold
        eggs_for_sale = total_eggs - worker_bonus_eggs

        # Calculate boxes and leftover sold to customer after bonus eggs removed
        boxes_sold = eggs_for_sale // 12
        leftover_sold = eggs_for_sale % 12

        # Calculate amounts
        boxes_income = boxes_sold * price_per_box
        deposit_income = boxes_sold * deposit_per_box
        leftover_income = leftover_sold * single_egg

        total_customer_due = boxes_income + deposit_income + leftover_income

        # Payment to worker based on hours only (no deduction for bonus eggs)
        payment_to_worker = hours_worked * payment_hour

        lines = "-" * 45 + "\n"

        # Output
        self.output_area.insert(tk.END, f"Week {num_week} Statistics:\n")
        self.output_area.insert(tk.END, lines)

        # Chickens
        self.output_area.insert(tk.END, "Chickens:\n\n")
        self.output_area.insert(tk.END, f"Total Chickens: {chickens}\n")
        self.output_area.insert(tk.END, f"Chickens That Laid Eggs: {chickens_laid_eggs}\n\n")
        self.output_area.insert(tk.END, lines)

        # Eggs
        self.output_area.insert(tk.END, "Eggs:\n\n")
        self.output_area.insert(tk.END, f"Total Eggs Laid: {total_eggs}\n")
        self.output_area.insert(tk.END, f"Bonus Eggs Given to Worker: {worker_bonus_eggs}\n")
        if boxes_removed > 0:
            self.output_area.insert(tk.END, f"Boxes Removed for Bonus: {boxes_removed}\n")
        self.output_area.insert(tk.END, f"Eggs Sold in Boxes: {boxes_sold * 12}\n")
        self.output_area.insert(tk.END, f"Amount of Boxes Filled: {boxes_filled}\n")
        self.output_area.insert(tk.END, f"Leftover Eggs Sold: {leftover_sold}\n")
        self.output_area.insert(tk.END, lines)

        # Payment to worker
        self.output_area.insert(tk.END, "Worker Payment:\n\n")
        self.output_area.insert(tk.END, f"Hours Worked: {hours_worked}\n")
        self.output_area.insert(tk.END, f"Hourly Rate: €{payment_hour:.2f}\n")
        self.output_area.insert(tk.END, f"Total Payment: €{payment_to_worker:.2f}\n")
        self.output_area.insert(tk.END, lines)

        # Customer receipt
        self.output_area.insert(tk.END, "Customer Receipt:\n\n")
        self.output_area.insert(tk.END, f"Boxes Purchased: {boxes_sold} x €{price_per_box:.2f} = €{boxes_income:.2f}\n")
        self.output_area.insert(tk.END, f"Box Deposits: {boxes_sold} x €{deposit_per_box:.2f} = €{deposit_income:.2f}\n")
        self.output_area.insert(tk.END, f"Leftover Eggs: {leftover_sold} x €{single_egg:.2f} = €{leftover_income:.2f}\n")
        self.output_area.insert(tk.END, f"\nTotal Due: €{total_customer_due:.2f}\n")
        self.output_area.insert(tk.END, lines)

    def clear_output(self):
        """Clear the output area."""
        self.output_area.delete("1.0", tk.END)


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChickenFarm(root)
    root.mainloop()
