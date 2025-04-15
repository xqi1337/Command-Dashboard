import tkinter as tk
from tkinter import ttk
import sv_ttk
from PIL import Image, ImageTk
from command_data import COMMAND_DATA


class CommandDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("GET GOOD GET COPYSENSE")
        self.root.geometry("1200x700")
        self.root.attributes('-alpha', 0.95)

        self.command_data = COMMAND_DATA

        sv_ttk.set_theme("dark")
        self.setup_background()
        self.create_main_menu()

    def setup_background(self):
        try:
            bg_color = "#2d2d2d"
            self.bg_image = Image.new('RGBA', (1, 1), bg_color)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()
        except:
            pass

    def create_main_menu(self):
        # Clear existing frames except menu_frame
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Frame) and widget != getattr(self, 'menu_frame', None):
                widget.destroy()

        # Hauptcontainer
        if not hasattr(self, 'main_frame'):
            self.main_frame = ttk.Frame(self.root, style='Card.TFrame')
            self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Menüleiste links (nur erstellen wenn nicht vorhanden)
        if not hasattr(self, 'menu_frame'):
            self.menu_frame = ttk.Frame(self.main_frame, width=200, style='Card.TFrame')
            self.menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))

            # MENU-Label oben fest einfügen
            self.menu_title = ttk.Label(
                self.menu_frame,
                text="MENU",
                font=('Segoe UI', 12, 'bold'),
                style='Inverse.TLabel'
            )
            self.menu_title.pack(pady=(20, 10), padx=10, anchor='w')

        # Hauptinhalt rechts (Command Auswahl)
        if not hasattr(self, 'content_frame'):
            self.content_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
            self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Ausgabebereich unten (Command + Erklärung)
        if not hasattr(self, 'output_frame'):
            self.output_frame = ttk.Frame(self.root, style='Card.TFrame')
            self.output_frame.pack(fill=tk.BOTH, expand=False, padx=20, pady=(0, 20), ipady=10)

            # Command Anzeige (links)
            self.command_display = tk.Text(
                self.output_frame,
                wrap=tk.WORD,
                font=('Consolas', 12),
                bg='#3d3d3d',
                fg='white',
                insertbackground='white',
                height=10,
                width=40
            )
            self.command_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

            # Erklärungsbereich (rechts)
            self.explanation_display = tk.Text(
                self.output_frame,
                wrap=tk.WORD,
                font=('Segoe UI', 11),
                bg='#3d3d3d',
                fg='white',
                insertbackground='white',
                height=10,
                width=60
            )
            self.explanation_display.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Hauptmenü-Buttons oder Kategorie-Buttons anzeigen
        self.show_main_buttons()

        # Standardansicht (Beschreibung)
        self.show_welcome_message()

    def show_main_buttons(self):
        # Lösche alle Buttons unter dem MENU-Label
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.destroy()

        # Hauptmenü-Buttons hinzufügen
        menu_buttons = [
            ("LINUX COMMANDS", lambda: self.show_categories('linux')),
            ("SQL COMMANDS", lambda: self.show_categories('sql')),
            ("DATENTYPEN", lambda: self.show_categories('datentypen')),
            ("Exit", self.root.quit)
        ]

        for text, command in menu_buttons:
            btn = ttk.Button(
                self.menu_frame,
                text=text,
                style='Menu.TButton',
                command=command
            )
            btn.pack(fill=tk.X, pady=2, padx=10)

    def show_welcome_message(self):
        self.clear_content_frame()
        ttk.Label(
            self.content_frame,
            text="Willkommen im Command Dashboard von xqi",
            font=('Segoe UI', 14, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=20, anchor='w')

        ttk.Label(
            self.content_frame,
            text="Wählen Sie eine Kategorie aus dem Menü links",
            font=('Segoe UI', 11),
            style='Inverse.TLabel'
        ).pack(pady=10, padx=20, anchor='w')

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def clear_output_frame(self):
        self.command_display.config(state=tk.NORMAL)
        self.command_display.delete(1.0, tk.END)
        self.explanation_display.config(state=tk.NORMAL)
        self.explanation_display.delete(1.0, tk.END)

    def add_return_button(self):
        # Lösche alle Buttons unter dem MENU-Label
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.destroy()

        # RETURN-Button hinzufügen
        return_btn = ttk.Button(
            self.menu_frame,
            text="RETURN",
            style='Menu.TButton',
            command=self.return_to_main_menu
        )
        return_btn.pack(fill=tk.X, pady=2, padx=10)

    def return_to_main_menu(self):
        self.clear_content_frame()
        self.clear_output_frame()
        self.show_main_buttons()
        self.show_welcome_message()

    def show_categories(self, category_type):
        self.clear_content_frame()
        self.clear_output_frame()
        self.add_return_button()

        categories = self.command_data[category_type]['categories']

        for text, command_key in categories.items():
            btn = ttk.Button(
                self.menu_frame,
                text=text,
                style='Menu.TButton',
                command=lambda key=command_key: self.show_commands(category_type, key)
            )
            btn.pack(fill=tk.X, pady=2, padx=10)

        ttk.Label(
            self.content_frame,
            text="Wählen Sie eine Befehlskategorie aus dem Menü links",
            font=('Segoe UI', 14, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=20, anchor='w')

    def show_commands(self, category_type, command_group):
        self.clear_content_frame()
        commands = self.command_data[category_type]['commands'][command_group]

        # Get the title from categories
        title = next((k for k, v in self.command_data[category_type]['categories'].items() if v == command_group),
                     "Commands")

        ttk.Label(
            self.content_frame,
            text=f"{title} - Befehle",
            font=('Segoe UI', 14, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=20, anchor='w')

        for btn_text, command, explanation in commands:
            btn = ttk.Button(
                self.content_frame,
                text=btn_text,
                style='Accent.TButton',
                command=lambda c=command, e=explanation: self.display_command(c, e)
            )
            btn.pack(fill=tk.X, padx=50, pady=5)

    def display_command(self, command, explanation):
        self.clear_output_frame()
        self.command_display.insert(tk.END, command)
        self.command_display.config(state=tk.DISABLED)
        self.explanation_display.insert(tk.END, explanation)
        self.explanation_display.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style()
    style.configure('Card.TFrame', background='#3d3d3d', borderwidth=2, relief='raised')
    style.configure('Transparent.TFrame', background='')
    style.configure('Inverse.TLabel', background='#3d3d3d', foreground='white')
    style.configure('Menu.TButton', font=('Segoe UI', 10), width=20, anchor='w')
    style.configure('Accent.TButton', font=('Segoe UI', 10))

    app = CommandDashboard(root)
    root.mainloop()
