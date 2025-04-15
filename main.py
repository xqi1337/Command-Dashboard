import tkinter as tk
from tkinter import ttk
import sv_ttk
from PIL import Image, ImageTk


class CommandDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Command Dashboard")
        self.root.geometry("1200x700")
        self.root.attributes('-alpha', 0.95)

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
        # Clear existing frames
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.destroy()

        # Hauptcontainer
        self.main_frame = ttk.Frame(self.root, style='Card.TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Menüleiste links
        self.menu_frame = ttk.Frame(self.main_frame, width=200, style='Card.TFrame')
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))

        ttk.Label(
            self.menu_frame,
            text="MENU",
            font=('Segoe UI', 12, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=10, anchor='w')

        # Hauptmenü-Buttons
        menu_buttons = [
            ("LINUX COMMANDS", self.show_linux_categories),
            ("SQL COMMANDS", self.show_sql_categories),
            ("DATENTYPEN", self.show_datentypen_categories),
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

        # Hauptinhalt rechts (Command Auswahl)
        self.content_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Ausgabebereich unten (Command + Erklärung)
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

        # Standardansicht (Beschreibung)
        self.show_welcome_message()

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
        # Lösche alle Buttons im Menüframe
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.destroy()

        # Füge MENU-Label und RETURN-Button hinzu
        ttk.Label(
            self.menu_frame,
            text="MENU",
            font=('Segoe UI', 12, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=10, anchor='w')

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
        self.create_main_menu()

    def show_linux_categories(self):
        self.clear_content_frame()
        self.clear_output_frame()
        self.add_return_button()

        # Füge Linux-Kategorien zum Menüframe hinzu
        categories = [
            ("File Operations\n(Dateiverwaltung)", self.show_file_operations_commands),
            ("System Info\n(Systeminformationen)", self.show_system_info_commands),
            ("Process Control\n(Prozesssteuerung)", self.show_process_control_commands),
            ("Networking\n(Netzwerkbefehle)", self.show_networking_commands),
            ("Permissions\n(Berechtigungen)", self.show_permissions_commands),
            ("Package Management\n(Paketverwaltung)", self.show_package_management_commands),
            ("Text Processing\n(Textverarbeitung)", self.show_text_processing_commands),
            ("Disk Usage\n(Festplattennutzung)", self.show_disk_usage_commands),
            ("SSH & Remote\n(Remote-Zugriff)", self.show_ssh_remote_commands)
        ]

        for text, command in categories:
            btn = ttk.Button(
                self.menu_frame,
                text=text,
                style='Menu.TButton',
                command=command
            )
            btn.pack(fill=tk.X, pady=2, padx=10)

        ttk.Label(
            self.content_frame,
            text="Wählen Sie eine Befehlskategorie aus dem Menü links",
            font=('Segoe UI', 14, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=20, anchor='w')

    def show_file_operations_commands(self):
        self.clear_content_frame()

        commands = [
            ("Datei kopieren", "cp file1 file2", "Kopiert Datei1 zu Datei2"),
            ("Datei verschieben", "mv file verzeichnis/", "Verschiebt Datei in verzeichnis/"),
            ("Datei löschen", "rm file", "Löscht eine Datei"),
            ("Verzeichnis erstellen", "mkdir verzeichnis", "Erstellt ein neues Verzeichnis"),
            ("Datei erstellen", "touch file", "Erstellt eine leere Datei oder aktualisiert Zeitstempel"),
            ("Dateien suchen", "find / -name '*.txt'", "Sucht nach .txt-Dateien im gesamten System"),
            ("Dateien auflisten", "ls -l", "Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.")
        ]

        ttk.Label(
            self.content_frame,
            text="File Operations - Befehle",
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

    def show_system_info_commands(self):
        self.clear_content_frame()

        commands = [
            ("Systeminformationen", "uname -a", "Zeigt Systeminformationen (Kernel, Hostname etc.)"),
            ("Speicherbelegung", "df -h", "Zeigt Speicherbelegung der Dateisysteme (human readable)"),
            ("Speichernutzung", "free -m", "Zeigt Speichernutzung in MB"),
            ("Prozessliste", "top", "Dynamische Anzeige der laufenden Prozesse"),
            ("CPU-Informationen", "lscpu", "Zeigt CPU-Informationen"),
            ("Systemlaufzeit", "uptime", "Zeigt Systemlaufzeit und Auslastung")
        ]

        ttk.Label(
            self.content_frame,
            text="System Info - Befehle",
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

    # Weitere Command-Show-Methoden (analog zu show_file_operations_commands)
    def show_process_control_commands(self):
        self.clear_content_frame()

        commands = [
            ("Prozessliste", "ps aux", "Zeigt alle laufenden Prozesse"),
            ("Prozess beenden", "kill -9 PID", "Beendet einen Prozess mit der angegebenen Prozess-ID"),
            ("Prozess nach Name beenden", "killall processname", "Beendet alle Prozesse mit diesem Namen"),
            ("Priorität ändern", "nice -n 10 command", "Startet einen Befehl mit angepasster Priorität"),
            ("Hintergrundprozess", "bg", "Setzt einen gestoppten Prozess im Hintergrund fort"),
            ("Vordergrundprozess", "fg", "Bringt einen Hintergrundprozess in den Vordergrund")
        ]

        ttk.Label(
            self.content_frame,
            text="Process Control - Befehle",
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

    def show_networking_commands(self):
        self.clear_content_frame()

        commands = [
            ("Netzwerkkonfiguration", "ifconfig", "Zeigt Netzwerkschnittstellen und Konfiguration"),
            ("Verbindung testen", "ping host", "Sendet ICMP-Pakete zum angegebenen Host"),
            ("Verbindungsweg", "traceroute host", "Zeigt den Weg der Pakete zum Zielhost"),
            ("Offene Ports", "netstat -tuln", "Zeigt alle offenen Ports und Verbindungen"),
            ("SSH Verbindung", "ssh user@host", "Stellt eine SSH-Verbindung zum entfernten Host her"),
            ("Dateien kopieren", "scp file user@host:path", "Kopiert Dateien über SSH")
        ]

        ttk.Label(
            self.content_frame,
            text="Networking - Befehle",
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

    def show_permissions_commands(self):
        self.clear_content_frame()

        commands = [
            ("Berechtigungen ändern", "chmod 755 file", "Ändert Dateiberechtigungen (rwx für Owner, r-x für Gruppe und Andere)"),
            ("Datei ausführbar machen", "chmod +x file", "Macht eine Datei ausführbar"),
            ("Besitzer ändern", "chown user:group file", "Ändert Besitzer und Gruppe einer Datei"),
            ("Gruppe ändern", "chgrp group file", "Ändert die Gruppe einer Datei"),
            ("Standard-Berechtigungen", "umask 022", "Setzt Standard-Berechtigungen für neue Dateien"),
            ("ACL anzeigen", "getfacl file", "Zeigt erweiterte ACL-Berechtigungen")
        ]

        ttk.Label(
            self.content_frame,
            text="File Operations - Befehle",
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

    def show_package_management_commands(self):
        self.clear_content_frame()

        commands = [
            ("Paketliste aktualisieren", "apt update", "Aktualisiert die Paketliste (Debian/Ubuntu)"),
            ("Paket installieren", "apt install package", "Installiert ein Paket"),
            ("Paket entfernen", "apt remove package", "Deinstalliert ein Paket"),
            ("Pakete aktualisieren", "apt upgrade", "Aktualisiert alle installierten Pakete"),
            ("RPM-Paket installieren", "yum install package", "Installiert ein Paket (RHEL/CentOS)"),
            ("DEB-Paket installieren", "dpkg -i package.deb", "Installiert eine .deb-Datei")
        ]

        ttk.Label(
            self.content_frame,
            text="File Operations - Befehle",
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

    def show_text_processing_commands(self):
        self.clear_content_frame()

        commands = [
            ("Datei kopieren", "cp datei1 datei2", "Kopiert datei1 zu datei2"),
            ("Datei verschieben", "mv datei1 verzeichnis/", "Verschiebt datei1 in verzeichnis/"),
            ("Datei löschen", "rm datei", "Löscht eine Datei"),
            ("Verzeichnis erstellen", "mkdir verzeichnis", "Erstellt ein neues Verzeichnis"),
            ("Datei erstellen", "touch datei", "Erstellt eine leere Datei oder aktualisiert Zeitstempel"),
            ("Dateien suchen", "find / -name '*.txt'", "Sucht nach .txt-Dateien im gesamten System"),
            ("Dateien auflisten", "ls -l", "Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.")
        ]

        ttk.Label(
            self.content_frame,
            text="File Operations - Befehle",
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

    def show_disk_usage_commands(self):
        self.clear_content_frame()

        commands = [
            ("Speicherbelegung", "df -h", "Zeigt Speicherbelegung aller Dateisysteme"),
            ("Verzeichnisgröße", "du -sh dir", "Zeigt Gesamtgröße eines Verzeichnisses"),
            ("Blockgeräte", "lsblk", "Listet alle Blockgeräte (Festplatten, Partitionen) auf"),
            ("Partitionen", "fdisk -l", "Zeigt Partitionstabellen an"),
            ("Eingehängte Dateisysteme", "mount", "Zeigt alle eingehängten Dateisysteme"),
            ("Dateisystem aushängen", "umount /mnt", "Hängt ein Dateisystem aus")
        ]

        ttk.Label(
            self.content_frame,
            text="File Operations - Befehle",
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

    def show_ssh_remote_commands(self):
        self.clear_content_frame()

        commands = [
            ("SSH Verbindung", "ssh user@host", "Stellt eine SSH-Verbindung zum entfernten Host her"),
            ("SSH Schlüssel erstellen", "ssh-keygen", "Erstellt ein SSH-Schlüsselpaar"),
            ("SSH Schlüssel kopieren", "ssh-copy-id user@host", "Kopiert den öffentlichen Schlüssel zum Host"),
            ("Dateien kopieren", "scp file user@host:path", "Kopiert Dateien über SSH"),
            ("Verzeichnisse synchronisieren", "rsync -avz src/ user@host:dest/", "Synchronisiert Verzeichnisse effizient"),
            ("SSH Tunnel", "ssh -L 8080:localhost:80 user@host", "Erstellt einen SSH-Tunnel")
        ]

        ttk.Label(
            self.content_frame,
            text="File Operations - Befehle",
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

    # SQL und Datentypen Methoden (analog zu Linux)
    def show_sql_categories(self):
        self.clear_content_frame()
        self.clear_output_frame()
        self.add_return_button()

        categories = [
            ("Datenbanken verwalten", self.show_db_management_commands),
            ("Tabellen verwalten", self.show_table_management_commands),
            ("Daten bearbeiten", self.show_data_manipulation_commands),
            ("Datenabfragen", self.show_data_queries_commands),
            ("Joins", self.show_joins_commands),
            ("Funktionen", self.show_functions_commands),
            ("Index", self.show_indexes_commands)
        ]

        for text, command in categories:
            btn = ttk.Button(
                self.menu_frame,
                text=text,
                style='Menu.TButton',
                command=command
            )
            btn.pack(fill=tk.X, pady=2, padx=10)

        ttk.Label(
            self.content_frame,
            text="Wählen Sie eine SQL-Kategorie aus dem Menü links",
            font=('Segoe UI', 14, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=20, anchor='w')

    def show_db_management_commands(self):
        self.clear_content_frame()

        commands = [
            ("Datenbank erstellen", "CREATE DATABASE dbname", "Erstellt eine neue Datenbank"),
            ("Datenbank verwenden", "USE dbname", "Wechselt zur angegebenen Datenbank"),
            ("Datenbanken anzeigen", "SHOW DATABASES", "Listet alle Datenbanken auf"),
            ("Datenbank löschen", "DROP DATABASE dbname", "Löscht eine Datenbank"),
            ("Datenbank mit Zeichensatz", "CREATE DATABASE dbname CHARACTER SET utf8mb4", "Erstellt DB mit UTF-8 Zeichensatz")
        ]

        ttk.Label(
            self.content_frame,
            text="Datenbanken verwalten - Befehle",
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


    def show_table_management_commands(self):
        self.clear_content_frame()

        commands = [
            ("Tabelle erstellen", "CREATE TABLE users (id INT, name VARCHAR(50))", "Erstellt eine neue Tabelle"),
            ("Spalte hinzufügen", "ALTER TABLE users ADD COLUMN email VARCHAR(100)", "Fügt eine Spalte hinzu"),
            ("Tabelle löschen", "DROP TABLE users", "Löscht eine Tabelle"),
            ("Tabellenstruktur", "DESCRIBE users", "Zeigt die Struktur einer Tabelle"),
            ("Tabellen auflisten", "SHOW TABLES", "Listet alle Tabellen in der aktuellen DB auf")
        ]

        ttk.Label(
            self.content_frame,
            text="Datenbanken verwalten - Befehle",
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

    def show_data_manipulation_commands(self):
        self.clear_content_frame()

        commands = [
            ("Daten einfügen", "INSERT INTO users VALUES (1, 'John')", "Fügt einen neuen Datensatz ein"),
            ("Daten aktualisieren", "UPDATE users SET name='Mike' WHERE id=1", "Aktualisiert einen Datensatz"),
            ("Daten löschen", "DELETE FROM users WHERE id=1", "Löscht einen Datensatz"),
            ("Alle Daten löschen", "TRUNCATE TABLE users", "Löscht alle Daten in der Tabelle"),
            ("Daten ersetzen", "REPLACE INTO users VALUES (1, 'John')", "Ersetzt oder fügt einen Datensatz ein")
        ]

        ttk.Label(
            self.content_frame,
            text="Datenbanken verwalten - Befehle",
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


    def show_data_queries_commands(self):
        self.clear_content_frame()

        commands = [
            ("Alle Daten auswählen", "SELECT * FROM users", "Wählt alle Spalten und Zeilen aus"),
            ("Spalten auswählen", "SELECT name, email FROM users", "Wählt bestimmte Spalten aus"),
            ("Mit Bedingung", "SELECT * FROM users WHERE id > 5", "Filtert Datensätze nach Bedingung"),
            ("Sortieren", "SELECT * FROM users ORDER BY name DESC", "Sortiert die Ergebnisse absteigend"),
            ("Paginierung", "SELECT * FROM users LIMIT 10 OFFSET 20", "Zeigt 10 Datensätze ab Position 20")
        ]

        ttk.Label(
            self.content_frame,
            text="Datenbanken verwalten - Befehle",
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


    def show_joins_commands(self):
        self.clear_content_frame()

        commands = [
            ("INNER JOIN", "SELECT u.name, o.amount FROM users u JOIN orders o ON u.id = o.user_id", "Nur übereinstimmende Datensätze"),
            ("LEFT JOIN", "SELECT u.name, o.amount FROM users u LEFT JOIN orders o ON u.id = o.user_id", "Alle Benutzer, auch ohne Bestellungen"),
            ("RIGHT JOIN", "SELECT u.name, o.amount FROM users u RIGHT JOIN orders o ON u.id = o.user_id", "Alle Bestellungen, auch ohne Benutzer"),
            ("CROSS JOIN", "SELECT u.name, o.amount FROM users u CROSS JOIN orders o", "Alle möglichen Kombinationen")
        ]

        ttk.Label(
            self.content_frame,
            text="Datenbanken verwalten - Befehle",
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


    def show_functions_commands(self):
        self.clear_content_frame()

        commands = [
            ("Aggregatfunktionen", "SELECT COUNT(*), AVG(price), MAX(date) FROM products", "Zählen, Durchschnitt, Maximum"),
            ("Textfunktion", "SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users", "Text verkettung"),
            ("Datumsfunktion", "SELECT DATE_FORMAT(created_at, '%Y-%m') AS month FROM orders", "Datumsformatierung"),
            ("NULL-Behandlung", "SELECT IFNULL(email, 'no email') FROM users", "Behandlung von NULL-Werten"),
            ("Gruppierung", "SELECT SUM(amount) FROM orders GROUP BY user_id", "Gruppierung und Summierung")
        ]

        ttk.Label(
            self.content_frame,
            text="Datenbanken verwalten - Befehle",
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


    def show_indexes_commands(self):
        self.clear_content_frame()

        commands = [
            ("Index erstellen", "CREATE INDEX idx_name ON users(name)", "Erstellt einen Index auf die name-Spalte"),
            ("Eindeutigen Index", "CREATE UNIQUE INDEX idx_email ON users(email)", "Erstellt einen eindeutigen Index"),
            ("Index löschen", "DROP INDEX idx_name ON users", "Löscht einen Index"),
            ("Indizes anzeigen", "SHOW INDEX FROM users", "Zeigt alle Indizes einer Tabelle an"),
            ("Abfrageplan", "EXPLAIN SELECT * FROM users WHERE name = 'John'", "Zeigt wie die Abfrage ausgeführt wird")
        ]

        ttk.Label(
            self.content_frame,
            text="Datenbanken verwalten - Befehle",
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

    def show_datentypen_categories(self):
        self.clear_content_frame()
        self.clear_output_frame()
        self.add_return_button()

        categories = [
            ("Numerische Typen", self.show_numeric_types_commands),
            ("Zeit/Datum Typen", self.show_time_types_commands),
            ("String Typen", self.show_string_types_commands),
            ("Räumliche Typen", self.show_spatial_types_commands),
            ("Sonstige Typen", self.show_other_types_commands)
        ]

        for text, command in categories:
            btn = ttk.Button(
                self.menu_frame,
                text=text,
                style='Menu.TButton',
                command=command
            )
            btn.pack(fill=tk.X, pady=2, padx=10)

        ttk.Label(
            self.content_frame,
            text="Wählen Sie eine Datentyp-Kategorie aus dem Menü links",
            font=('Segoe UI', 14, 'bold'),
            style='Inverse.TLabel'
        ).pack(pady=(20, 10), padx=20, anchor='w')



    def show_numeric_types_commands(self):
        self.clear_content_frame()

        commands = [
            ("TINYINT", "TINYINT", "Ganze Zahlen von -128 bis 127"),
            ("SMALLINT", "SMALLINT", "Ganze Zahlen von -32,768 bis 32,767"),
            ("MEDIUMINT", "MEDIUMINT", "Ganze Zahlen von -8,388,608 bis 8,388,607"),
            ("INT", "INT", "Ganze Zahlen von -2,147,483,648 bis 2,147,483,647"),
            ("BIGINT", "BIGINT", "Ganze Zahlen von -9,223,372,036,854,775,808 bis 9,223,372,036,854,775,807"),
            ("BOOLEAN", "BOOLEAN", "Boolesche Werte (true/false), Synonym für TINYINT(1)"),
            ("DECIMAL", "DECIMAL(p,s)", "Dezimalzahlen mit bis zu 65 Stellen (p=Gesamtstellen, s=Nachkommastellen)"),
            ("FLOAT", "FLOAT", "Gleitkommazahlen (±3.402823466E+38 bis ±1.175494351E-38)"),
            ("DOUBLE", "DOUBLE", "Gleitkommazahlen (±1.7976931348623157E+308 bis ±2.2250738585072014E-308)"),
            ("BIT", "BIT", "Ein einzelnes Bit (0 oder 1)"),
            ("INTEGER", "INTEGER", "Synonym für INT (Ganze Zahlen 32 Bit)"),
            ("SERIAL", "SERIAL", "Auto-increment Ganzzahl (Alias für BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE)")
        ]

        ttk.Label(
            self.content_frame,
            text="Numerische Datentypen",
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

    def show_time_types_commands(self):
        self.clear_content_frame()

        commands = [
            ("DATE", "DATE", "Speichert ein Datum (YYYY-MM-DD)"),
            ("TIME", "TIME", "Speichert eine Uhrzeit (HH:MM:SS)"),
            ("DATETIME", "DATETIME", "Speichert Datum und Uhrzeit (YYYY-MM-DD HH:MM:SS)"),
            ("TIMESTAMP", "TIMESTAMP", "Zeitstempel (automatische Aktualisierung möglich)"),
            ("YEAR", "YEAR", "Speichert ein Jahr (4-stellig)"),
            ("INTERVAL", "INTERVAL", "Zeitintervalle (z.B. für Berechnungen)")
        ]

        ttk.Label(
            self.content_frame,
            text="Numerische Datentypen",
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


    def show_string_types_commands(self):
        self.clear_content_frame()

        commands = [
            # Zeichenketten-Typen
            ("CHAR", "CHAR(n)", "Feste Zeichenkette (0-255 Zeichen, mit Leerzeichen aufgefüllt)"),
            ("VARCHAR", "VARCHAR(n)", "Variable Zeichenkette (0-65.535 Zeichen)"),

            # Binäre Typen
            ("BINARY", "BINARY(n)", "Feste Länge binärer Daten (0-255 Bytes)"),
            ("VARBINARY", "VARBINARY(n)", "Variable Länge binärer Daten (0-65.535 Bytes)"),
            ("TINYBLOB", "TINYBLOB", "Binärobjekt bis 255 Bytes"),
            ("BLOB", "BLOB", "Binärobjekt bis 65.535 Bytes"),
            ("MEDIUMBLOB", "MEDIUMBLOB", "Binärobjekt bis 16.777.215 Bytes"),
            ("LONGBLOB", "LONGBLOB", "Binärobjekt bis 4.294.967.295 Bytes"),

            # Text-Typen
            ("TINYTEXT", "TINYTEXT", "Text bis 255 Zeichen"),
            ("TEXT", "TEXT", "Text bis 65.535 Zeichen"),
            ("MEDIUMTEXT", "MEDIUMTEXT", "Text bis 16.777.215 Zeichen"),
            ("LONGTEXT", "LONGTEXT", "Text bis 4.294.967.295 Zeichen"),

            # Spezialtypen
            ("ENUM", "ENUM('val1','val2',...)", "Aufzählungstyp (nur vordefinierte Werte)"),
            ("SET", "SET('val1','val2',...)", "Menge unterschiedlicher Zeichenketten (kombinierbar)"),

        ]

        ttk.Label(
            self.content_frame,
            text="Numerische Datentypen",
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

    def show_spatial_types_commands(self):
        self.clear_content_frame()

        commands = [
            ("GEOMETRY", "GEOMETRY", "Basisklasse für räumliche Typen"),
            ("POINT", "POINT", "Punkt mit X/Y-Koordinaten"),
            ("LINESTRING", "LINESTRING", "Linie aus mehreren Punkten"),
            ("POLYGON", "POLYGON", "Geschlossene Fläche"),
            ("MULTIPOINT", "MULTIPOINT", "Mehrere Punkte"),
            ("MULTILINESTRING", "MULTILINESTRING", "Mehrere Linien"),
            ("MULTIPOLYGON", "MULTIPOLYGON", "Mehrere Polygone"),
            ("GEOMETRYCOLLECTION", "GEOMETRYCOLLECTION", "Sammlung verschiedener Geometrien")
        ]

        ttk.Label(
            self.content_frame,
            text="Numerische Datentypen",
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

    def show_other_types_commands(self):
        self.clear_content_frame()

        commands = [
            ("BLOB", "BLOB", "Binäre Daten (z.B. Bilder, Audiodateien)"),
            ("JSON", "JSON", "Speichert JSON-Dokumente (ab MariaDB 10.2)"),
            ("UUID", "UUID", "Universally Unique Identifier (als String)"),
            ("INET6", "INET6", "IPv6-Adressen"),
            ("BIT", "BIT", "Bit-Felder"),
            ("AUTO_INCREMENT", "AUTO_INCREMENT", "Automatisch hochzählender Wert (für Primärschlüssel)"),
            ("NULL", "NULL", "Kein Wert vorhanden (kein eigener Datentyp)")
        ]

        ttk.Label(
            self.content_frame,
            text="Numerische Datentypen",
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