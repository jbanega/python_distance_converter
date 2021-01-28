import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from windows import set_dpi_awareness


set_dpi_awareness()


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        self.resizable(False, False)
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")


        for FrameClass in (MetersToFeet, FeetToMeters):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        
        self.show_frame(MetersToFeet)



    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
    
        self.meter_value = tk.StringVar()
        self.foot_value = tk.StringVar(value="Feet shown here.")


        meters_label = ttk.Label(self, text="Meters:")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meter_value, font=("Calibri", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.foot_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(FeetToMeters)
        )

        #Arrange by grid method
        meters_label.grid(row=0, column=0, sticky="W")
        meters_input.grid(row=0, column=1, sticky="EW")
        meters_input.focus()

        feet_label.grid(row=1, column=0, sticky="W")
        feet_display.grid(row=1, column=1, sticky="EW")

        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")
        switch_page_button.grid(row=3, column=0, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)
    

    def calculate(self, *args):
        try:
            meters = float(self.meter_value.get())
            feet = meters * 3.28084
            self.foot_value.set(f"{feet: .3f}")
        except ValueError:
            pass



class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
    
        self.feet_value = tk.StringVar()
        self.meter_value = tk.StringVar(value="Meters shown here.")


        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Calibri", 15))
        meter_label = ttk.Label(self, text="Meters:")
        meter_display = ttk.Label(self, textvariable=self.meter_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to meters conversion",
            command=lambda: controller.show_frame(MetersToFeet)
        )

        #Arrange by grid method
        feet_label.grid(row=0, column=0, sticky="W")
        feet_input.grid(row=0, column=1, sticky="EW")
        feet_input.focus()

        meter_label.grid(row=1, column=0, sticky="W")
        meter_display.grid(row=1, column=1, sticky="EW")

        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")
        switch_page_button.grid(row=3, column=0, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)
    

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meter_value.set(f"{meters: .3f}")
        except ValueError:
            pass



root = DistanceConverter()


font.nametofont("TkDefaultFont").configure(size=15)


root.mainloop()