import tkinter as tk
from tkinter import ttk, messagebox
from frame_gui import DatabaseFrame, CSVInputFrame  
import traceback
from util.constants import CSV_INPUT, DATABASE_RELATED


class RunApp:
    def __init__(self, master):
        self.master = master
        master.title("motionboard_v0.1")
        
        # Configure grid weights
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        
        self.current_app = None
        self.create_widgets()

    def create_widgets(self):
        # Mode Selection Frame
        mode_frame = tk.Frame(self.master)
        mode_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        mode_frame.grid_columnconfigure(1, weight=1)

        # Mode Selection
        self.mode_label = tk.Label(mode_frame, text="モードを選択")
        self.mode_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.mode_choices = [CSV_INPUT, DATABASE_RELATED]
        self.mode_var = tk.StringVar(value=self.mode_choices[0])
        self.mode_dropdown = ttk.Combobox(mode_frame, textvariable=self.mode_var, 
                                        values=self.mode_choices, state="readonly")
        self.mode_dropdown.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.mode_dropdown.bind("<<ComboboxSelected>>", self.switch_mode)

        # App Container Frame
        self.app_frame = tk.Frame(self.master)
        self.app_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_rowconfigure(0, weight=1)

        # Initialize with MotionBoardApp
        self.switch_mode()

    def switch_mode(self, event=None):
        # Clean up current app if it exists
        if self.current_app:
            self.current_app.destroy() 
            self.current_app = None

        selected_mode = self.mode_var.get()
        
        try:
            if selected_mode == CSV_INPUT:
                self.current_app = CSVInputFrame(self.app_frame)
            elif selected_mode == DATABASE_RELATED:
                self.current_app = DatabaseFrame(self.app_frame)
            
            if self.current_app:
                self.current_app.pack(fill=tk.BOTH, expand=True)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize {selected_mode}: {str(e)}")
            traceback.print_exc()

if __name__ == "__main__":
    root = tk.Tk()
    app = RunApp(root)
    root.mainloop()