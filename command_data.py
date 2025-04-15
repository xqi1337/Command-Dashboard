# command_data.py
COMMAND_DATA = {
    'linux': {
                'categories': {
                    "Dateiverwaltung": "file_operations",
                    "Systeminformationen": "system_info",
                    "Prozesssteuerung": "process_control",
                    "Netzwerkbefehle": "networking",
                    "Berechtigungen": "permissions",
                    "Paketverwaltung": "package_management",
                    "Textverarbeitung": "text_processing",
                    "Festplattennutzung": "disk_usage",
                    "Remote-Zugriff": "ssh_remote"
                },
                'commands': {
                    "file_operations": [
                        ("Datei kopieren", "cp file1 file2", "Kopiert Datei1 zu Datei2"),
                        ("Datei verschieben", "mv file verzeichnis/", "Verschiebt Datei in verzeichnis/"),
                        ("Datei löschen", "rm file", "Löscht eine Datei"),
                        ("Verzeichnis erstellen", "mkdir verzeichnis", "Erstellt ein neues Verzeichnis"),
                        ("Datei erstellen", "touch file", "Erstellt eine leere Datei oder aktualisiert Zeitstempel"),
                        ("Dateien suchen", "find / -name '*.txt'", "Sucht nach .txt-Dateien im gesamten System"),
                        ("Dateien auflisten", "ls -l", "Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.")
                    ],
                    "system_info": [
                        ("Systeminformationen", "uname -a", "Zeigt Systeminformationen (Kernel, Hostname etc.)"),
                        ("Speicherbelegung", "df -h", "Zeigt Speicherbelegung der Dateisysteme (human readable)"),
                        ("Speichernutzung", "free -m", "Zeigt Speichernutzung in MB"),
                        ("Prozessliste", "top", "Dynamische Anzeige der laufenden Prozesse"),
                        ("CPU-Informationen", "lscpu", "Zeigt CPU-Informationen"),
                        ("Systemlaufzeit", "uptime", "Zeigt Systemlaufzeit und Auslastung")
                    ],
                    "process_control": [
                        ("Prozessliste", "ps aux", "Zeigt alle laufenden Prozesse"),
                        ("Prozess beenden", "kill -9 PID", "Beendet einen Prozess mit der angegebenen Prozess-ID"),
                        ("Prozess nach Name beenden", "killall processname", "Beendet alle Prozesse mit diesem Namen"),
                        ("Priorität ändern", "nice -n 10 command", "Startet einen Befehl mit angepasster Priorität"),
                        ("Hintergrundprozess", "bg", "Setzt einen gestoppten Prozess im Hintergrund fort"),
                        ("Vordergrundprozess", "fg", "Bringt einen Hintergrundprozess in den Vordergrund")
                    ],
                    "networking": [
                        ("Netzwerkkonfiguration", "ifconfig", "Zeigt Netzwerkschnittstellen und Konfiguration"),
                        ("Verbindung testen", "ping host", "Sendet ICMP-Pakete zum angegebenen Host"),
                        ("Verbindungsweg", "traceroute host", "Zeigt den Weg der Pakete zum Zielhost"),
                        ("Offene Ports", "netstat -tuln", "Zeigt alle offenen Ports und Verbindungen"),
                        ("SSH Verbindung", "ssh user@host", "Stellt eine SSH-Verbindung zum entfernten Host her"),
                        ("Dateien kopieren", "scp file user@host:path", "Kopiert Dateien über SSH")
                    ],
                    "permissions": [
                        ("Berechtigungen ändern", "chmod 755 file",
                         "Ändert Dateiberechtigungen (rwx für Owner, r-x für Gruppe und Andere)"),
                        ("Datei ausführbar machen", "chmod +x file", "Macht eine Datei ausführbar"),
                        ("Besitzer ändern", "chown user:group file", "Ändert Besitzer und Gruppe einer Datei"),
                        ("Gruppe ändern", "chgrp group file", "Ändert die Gruppe einer Datei"),
                        ("Standard-Berechtigungen", "umask 022", "Setzt Standard-Berechtigungen für neue Dateien"),
                        ("ACL anzeigen", "getfacl file", "Zeigt erweiterte ACL-Berechtigungen")
                    ],
                    "package_management": [
                        ("Paketliste aktualisieren", "apt update", "Aktualisiert die Paketliste (Debian/Ubuntu)"),
                        ("Paket installieren", "apt install package", "Installiert ein Paket"),
                        ("Paket entfernen", "apt remove package", "Deinstalliert ein Paket"),
                        ("Pakete aktualisieren", "apt upgrade", "Aktualisiert alle installierten Pakete"),
                        ("RPM-Paket installieren", "yum install package", "Installiert ein Paket (RHEL/CentOS)"),
                        ("DEB-Paket installieren", "dpkg -i package.deb", "Installiert eine .deb-Datei")
                    ],
                    "text_processing": [
                        ("Datei kopieren", "cp datei1 datei2", "Kopiert datei1 zu datei2"),
                        ("Datei verschieben", "mv datei1 verzeichnis/", "Verschiebt datei1 in verzeichnis/"),
                        ("Datei löschen", "rm datei", "Löscht eine Datei"),
                        ("Verzeichnis erstellen", "mkdir verzeichnis", "Erstellt ein neues Verzeichnis"),
                        ("Datei erstellen", "touch datei", "Erstellt eine leere Datei oder aktualisiert Zeitstempel"),
                        ("Dateien suchen", "find / -name '*.txt'", "Sucht nach .txt-Dateien im gesamten System"),
                        ("Dateien auflisten", "ls -l", "Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.")
                    ],
                    "disk_usage": [
                        ("Speicherbelegung", "df -h", "Zeigt Speicherbelegung aller Dateisysteme"),
                        ("Verzeichnisgröße", "du -sh dir", "Zeigt Gesamtgröße eines Verzeichnisses"),
                        ("Blockgeräte", "lsblk", "Listet alle Blockgeräte (Festplatten, Partitionen) auf"),
                        ("Partitionen", "fdisk -l", "Zeigt Partitionstabellen an"),
                        ("Eingehängte Dateisysteme", "mount", "Zeigt alle eingehängten Dateisysteme"),
                        ("Dateisystem aushängen", "umount /mnt", "Hängt ein Dateisystem aus")
                    ],
                    "ssh_remote": [
                        ("SSH Verbindung", "ssh user@host", "Stellt eine SSH-Verbindung zum entfernten Host her"),
                        ("SSH Schlüssel erstellen", "ssh-keygen", "Erstellt ein SSH-Schlüsselpaar"),
                        ("SSH Schlüssel kopieren", "ssh-copy-id user@host",
                         "Kopiert den öffentlichen Schlüssel zum Host"),
                        ("Dateien kopieren", "scp file user@host:path", "Kopiert Dateien über SSH"),
                        ("Verzeichnisse synchronisieren", "rsync -avz src/ user@host:dest/",
                         "Synchronisiert Verzeichnisse effizient"),
                        ("SSH Tunnel", "ssh -L 8080:localhost:80 user@host", "Erstellt einen SSH-Tunnel")
                    ]
                }
            },
            'sql': {
                'categories': {
                    "Datenbanken verwalten": "db_management",
                    "Tabellen verwalten": "table_management",
                    "Daten bearbeiten": "data_manipulation",
                    "Datenabfragen": "data_queries",
                    "Joins": "joins",
                    "Funktionen": "functions",
                    "Index": "indexes"
                },
                'commands': {
                    "db_management": [
                        ("Datenbank erstellen", "CREATE DATABASE dbname", "Erstellt eine neue Datenbank"),
                        ("Datenbank verwenden", "USE dbname", "Wechselt zur angegebenen Datenbank"),
                        ("Datenbanken anzeigen", "SHOW DATABASES", "Listet alle Datenbanken auf"),
                        ("Datenbank löschen", "DROP DATABASE dbname", "Löscht eine Datenbank"),
                        ("Datenbank mit Zeichensatz", "CREATE DATABASE dbname CHARACTER SET utf8mb4",
                         "Erstellt DB mit UTF-8 Zeichensatz")
                    ],
                    "table_management": [
                        ("Tabelle erstellen", "CREATE TABLE users (id INT, name VARCHAR(50))",
                         "Erstellt eine neue Tabelle"),
                        ("Spalte hinzufügen", "ALTER TABLE users ADD COLUMN email VARCHAR(100)",
                         "Fügt eine Spalte hinzu"),
                        ("Tabelle löschen", "DROP TABLE users", "Löscht eine Tabelle"),
                        ("Tabellenstruktur", "DESCRIBE users", "Zeigt die Struktur einer Tabelle"),
                        ("Tabellen auflisten", "SHOW TABLES", "Listet alle Tabellen in der aktuellen DB auf")
                    ],
                    "data_manipulation": [
                        ("Daten einfügen", "INSERT INTO users VALUES (1, 'John')", "Fügt einen neuen Datensatz ein"),
                        ("Daten aktualisieren", "UPDATE users SET name='Mike' WHERE id=1",
                         "Aktualisiert einen Datensatz"),
                        ("Daten löschen", "DELETE FROM users WHERE id=1", "Löscht einen Datensatz"),
                        ("Alle Daten löschen", "TRUNCATE TABLE users", "Löscht alle Daten in der Tabelle"),
                        ("Daten ersetzen", "REPLACE INTO users VALUES (1, 'John')",
                         "Ersetzt oder fügt einen Datensatz ein")
                    ],
                    "data_queries": [
                        ("Alle Daten auswählen", "SELECT * FROM users", "Wählt alle Spalten und Zeilen aus"),
                        ("Spalten auswählen", "SELECT name, email FROM users", "Wählt bestimmte Spalten aus"),
                        ("Mit Bedingung", "SELECT * FROM users WHERE id > 5", "Filtert Datensätze nach Bedingung"),
                        ("Sortieren", "SELECT * FROM users ORDER BY name DESC", "Sortiert die Ergebnisse absteigend"),
                        ("Paginierung", "SELECT * FROM users LIMIT 10 OFFSET 20", "Zeigt 10 Datensätze ab Position 20")
                    ],
                    "joins": [
                        ("INNER JOIN", "SELECT u.name, o.amount FROM users u JOIN orders o ON u.id = o.user_id",
                         "Nur übereinstimmende Datensätze"),
                        ("LEFT JOIN", "SELECT u.name, o.amount FROM users u LEFT JOIN orders o ON u.id = o.user_id",
                         "Alle Benutzer, auch ohne Bestellungen"),
                        ("RIGHT JOIN", "SELECT u.name, o.amount FROM users u RIGHT JOIN orders o ON u.id = o.user_id",
                         "Alle Bestellungen, auch ohne Benutzer"),
                        ("CROSS JOIN", "SELECT u.name, o.amount FROM users u CROSS JOIN orders o",
                         "Alle möglichen Kombinationen")
                    ],
                    "functions": [
                        ("Aggregatfunktionen", "SELECT COUNT(*), AVG(price), MAX(date) FROM products",
                         "Zählen, Durchschnitt, Maximum"),
                        ("Textfunktion", "SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users",
                         "Text verkettung"),
                        ("Datumsfunktion", "SELECT DATE_FORMAT(created_at, '%Y-%m') AS month FROM orders",
                         "Datumsformatierung"),
                        (
                        "NULL-Behandlung", "SELECT IFNULL(email, 'no email') FROM users", "Behandlung von NULL-Werten"),
                        ("Gruppierung", "SELECT SUM(amount) FROM orders GROUP BY user_id", "Gruppierung und Summierung")
                    ],
                    "indexes": [
                        ("Index erstellen", "CREATE INDEX idx_name ON users(name)",
                         "Erstellt einen Index auf die name-Spalte"),
                        ("Eindeutigen Index", "CREATE UNIQUE INDEX idx_email ON users(email)",
                         "Erstellt einen eindeutigen Index"),
                        ("Index löschen", "DROP INDEX idx_name ON users", "Löscht einen Index"),
                        ("Indizes anzeigen", "SHOW INDEX FROM users", "Zeigt alle Indizes einer Tabelle an"),
                        ("Abfrageplan", "EXPLAIN SELECT * FROM users WHERE name = 'John'",
                         "Zeigt wie die Abfrage ausgeführt wird")
                    ]
                }
            },
            'datentypen': {
                'categories': {
                    "Numerische Typen": "numeric_types",
                    "Zeit/Datum Typen": "time_types",
                    "String Typen": "string_types",
                    "Räumliche Typen": "spatial_types",
                    "Sonstige Typen": "other_types"
                },
                'commands': {
                    "numeric_types": [
                        ("TINYINT", "TINYINT", "Ganze Zahlen von -128 bis 127"),
                        ("SMALLINT", "SMALLINT", "Ganze Zahlen von -32,768 bis 32,767"),
                        ("MEDIUMINT", "MEDIUMINT", "Ganze Zahlen von -8,388,608 bis 8,388,607"),
                        ("INT", "INT", "Ganze Zahlen von -2,147,483,648 bis 2,147,483,647"),
                        ("BIGINT", "BIGINT",
                         "Ganze Zahlen von -9,223,372,036,854,775,808 bis 9,223,372,036,854,775,807"),
                        ("BOOLEAN", "BOOLEAN", "Boolesche Werte (true/false), Synonym für TINYINT(1)"),
                        ("DECIMAL", "DECIMAL(p,s)",
                         "Dezimalzahlen mit bis zu 65 Stellen (p=Gesamtstellen, s=Nachkommastellen)"),
                        ("FLOAT", "FLOAT", "Gleitkommazahlen (±3.402823466E+38 bis ±1.175494351E-38)"),
                        (
                        "DOUBLE", "DOUBLE", "Gleitkommazahlen (±1.7976931348623157E+308 bis ±2.2250738585072014E-308)"),
                        ("BIT", "BIT", "Ein einzelnes Bit (0 oder 1)"),
                        ("INTEGER", "INTEGER", "Synonym für INT (Ganze Zahlen 32 Bit)"),
                        ("SERIAL", "SERIAL",
                         "Auto-increment Ganzzahl (Alias für BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE)")
                    ],
                    "time_types": [
                        ("DATE", "DATE", "Speichert ein Datum (YYYY-MM-DD)"),
                        ("TIME", "TIME", "Speichert eine Uhrzeit (HH:MM:SS)"),
                        ("DATETIME", "DATETIME", "Speichert Datum und Uhrzeit (YYYY-MM-DD HH:MM:SS)"),
                        ("TIMESTAMP", "TIMESTAMP", "Zeitstempel (automatische Aktualisierung möglich)"),
                        ("YEAR", "YEAR", "Speichert ein Jahr (4-stellig)"),
                        ("INTERVAL", "INTERVAL", "Zeitintervalle (z.B. für Berechnungen)")
                    ],
                    "string_types": [
                        ("CHAR", "CHAR(n)", "Feste Zeichenkette (0-255 Zeichen, mit Leerzeichen aufgefüllt)"),
                        ("VARCHAR", "VARCHAR(n)", "Variable Zeichenkette (0-65.535 Zeichen)"),
                        ("BINARY", "BINARY(n)", "Feste Länge binärer Daten (0-255 Bytes)"),
                        ("VARBINARY", "VARBINARY(n)", "Variable Länge binärer Daten (0-65.535 Bytes)"),
                        ("TINYBLOB", "TINYBLOB", "Binärobjekt bis 255 Bytes"),
                        ("BLOB", "BLOB", "Binärobjekt bis 65.535 Bytes"),
                        ("MEDIUMBLOB", "MEDIUMBLOB", "Binärobjekt bis 16.777.215 Bytes"),
                        ("LONGBLOB", "LONGBLOB", "Binärobjekt bis 4.294.967.295 Bytes"),
                        ("TINYTEXT", "TINYTEXT", "Text bis 255 Zeichen"),
                        ("TEXT", "TEXT", "Text bis 65.535 Zeichen"),
                        ("MEDIUMTEXT", "MEDIUMTEXT", "Text bis 16.777.215 Zeichen"),
                        ("LONGTEXT", "LONGTEXT", "Text bis 4.294.967.295 Zeichen"),
                        ("ENUM", "ENUM('val1','val2',...)", "Aufzählungstyp (nur vordefinierte Werte)"),
                        ("SET", "SET('val1','val2',...)", "Menge unterschiedlicher Zeichenketten (kombinierbar)")
                    ],
                    "spatial_types": [
                        ("GEOMETRY", "GEOMETRY", "Basisklasse für räumliche Typen"),
                        ("POINT", "POINT", "Punkt mit X/Y-Koordinaten"),
                        ("LINESTRING", "LINESTRING", "Linie aus mehreren Punkten"),
                        ("POLYGON", "POLYGON", "Geschlossene Fläche"),
                        ("MULTIPOINT", "MULTIPOINT", "Mehrere Punkte"),
                        ("MULTILINESTRING", "MULTILINESTRING", "Mehrere Linien"),
                        ("MULTIPOLYGON", "MULTIPOLYGON", "Mehrere Polygone"),
                        ("GEOMETRYCOLLECTION", "GEOMETRYCOLLECTION", "Sammlung verschiedener Geometrien")
                    ],
                    "other_types": [
                        ("BLOB", "BLOB", "Binäre Daten (z.B. Bilder, Audiodateien)"),
                        ("JSON", "JSON", "Speichert JSON-Dokumente (ab MariaDB 10.2)"),
                        ("UUID", "UUID", "Universally Unique Identifier (als String)"),
                        ("INET6", "INET6", "IPv6-Adressen"),
                        ("BIT", "BIT", "Bit-Felder"),
                        ("AUTO_INCREMENT", "AUTO_INCREMENT", "Automatisch hochzählender Wert (für Primärschlüssel)"),
                        ("NULL", "NULL", "Kein Wert vorhanden (kein eigener Datentyp)")
                    ]
        }
    }
}