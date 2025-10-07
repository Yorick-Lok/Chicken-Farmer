import tkinter as tk
from tkinter import messagebox, scrolledtext


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
            self.root, text="Enter the information of the week here."
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

        # Eggs Entry
        tk.Label(self.root, text="Chickens that laid eggs:").pack()
        self.laid_eggs_entry = tk.Entry(self.root, width=5)
        self.laid_eggs_entry.pack()

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

        # Clear output button (optional)
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
                messagebox.showerror(
                    "Invalid Input", "Please choose a number between 1 and 54"
                )
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid week number.")
            return

        try:
            chickens = int(self.chickens_entry.get())
            if chickens < 2450 or chickens > 2525:
                messagebox.showerror(
                    "Invalid Input", "Please choose a number between 2450 and 2525"
                )
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid chicken number.")
            return

        try:
            laid_eggs = int(self.laid_eggs_entry.get())
            if laid_eggs < 0 or laid_eggs > chickens:
                messagebox.showerror(
                    "Invalid Input",
                    "Laid eggs must be between 0 and total chickens.",
                )
                return
        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Please enter a valid number for laid eggs."
            )
            return

        # Clear entries
        self.week_entry.delete(0, tk.END)
        self.chickens_entry.delete(0, tk.END)
        self.laid_eggs_entry.delete(0, tk.END)
        self.week_entry.focus_set()

        # Display output
        self.output_area.insert(tk.END, f"Week {num_week} Statistics:\n")
        self.output_area.insert(tk.END, "-" * 45 + "\n")
        self.output_area.insert(tk.END, f"Total Chickens: {chickens}\n")
        self.output_area.insert(tk.END, f"Chickens That Laid Eggs: {laid_eggs}\n")
        self.output_area.insert(tk.END, "-" * 45 + "\n")
        self.output_area.see(tk.END)

    def clear_output(self):
        """Clear the output area."""
        self.output_area.delete("1.0", tk.END)


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChickenFarm(root)
    root.mainloop()
