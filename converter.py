import tkinter as tk
from tkinter import ttk, messagebox

class MeasurementConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Measurement Converter")
        self.root.geometry("400x200")
        
        self.create_widgets()

    def create_widgets(self):
        # Input frame
        input_frame = ttk.Frame(self.root, padding="10 10 10 10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(input_frame, text="Enter Length:").grid(row=0, column=0, sticky=tk.W)
        self.length_entry = ttk.Entry(input_frame, width=10)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Select Unit:").grid(row=1, column=0, sticky=tk.W)
        self.unit_var = tk.StringVar()
        self.unit_combobox = ttk.Combobox(input_frame, textvariable=self.unit_var)
        self.unit_combobox['values'] = ('Meters', 'Feet', 'Kilometers')
        self.unit_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.unit_combobox.current(0)

        convert_button = ttk.Button(input_frame, text="Convert", command=self.convert)
        convert_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Output frame
        output_frame = ttk.Frame(self.root, padding="10 10 10 10")
        output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(output_frame, text="Meters:").grid(row=0, column=0, sticky=tk.W)
        self.meters_var = tk.StringVar()
        ttk.Label(output_frame, textvariable=self.meters_var).grid(row=0, column=1, sticky=tk.W)

        ttk.Label(output_frame, text="Feet:").grid(row=1, column=0, sticky=tk.W)
        self.feet_var = tk.StringVar()
        ttk.Label(output_frame, textvariable=self.feet_var).grid(row=1, column=1, sticky=tk.W)

        ttk.Label(output_frame, text="Kilometers:").grid(row=2, column=0, sticky=tk.W)
        self.kilometers_var = tk.StringVar()
        ttk.Label(output_frame, textvariable=self.kilometers_var).grid(row=2, column=1, sticky=tk.W)

    def convert(self):
        try:
            length = float(self.length_entry.get())
            unit = self.unit_var.get()

            if unit == 'Meters':
                self.meters_var.set(f"{length:.2f}")
                self.feet_var.set(f"{length * 3.28084:.2f}")
                self.kilometers_var.set(f"{length / 1000:.5f}")
            elif unit == 'Feet':
                self.meters_var.set(f"{length / 3.28084:.2f}")
                self.feet_var.set(f"{length:.2f}")
                self.kilometers_var.set(f"{(length / 3.28084) / 1000:.5f}")
            elif unit == 'Kilometers':
                self.meters_var.set(f"{length * 1000:.2f}")
                self.feet_var.set(f"{length * 3280.84:.2f}")
                self.kilometers_var.set(f"{length:.5f}")
            else:
                raise ValueError("Unsupported unit type")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MeasurementConverter(root)
    root.mainloop()
