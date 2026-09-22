# SchaltungsZeichner (CircuitSketcher)

**[Deutsch](#deutsch)** | **[English](#english)**

---

<a name="deutsch"></a>

## Deutsch

Ein visuelles Drag-and-Drop-Werkzeug zum Zeichnen elektrischer Schaltpläne,
geschrieben in Python mit PyQt5.

> Hinweis: Der interne Fenstertitel lautet „SchaltungsZeichner". CircuitSketcher
> ist der Projekt-/Verzeichnisname.

### Funktionen

- Rasterbasierte, unendliche Zeichenfläche (20 px-Raster) mit magnetischem Snapping
- Datengetriebene Symbol-Bibliothek: Bauteile werden aus `symbols/*.symbol.json` geladen
- Eigener grafischer Symbol-Editor zum Erstellen neuer Bauteile ohne Code-Änderung
- **4-stufige Rotation** (0° / 90° / 180° / 270°)
- Skalieren, Verschieben, Löschen von Bauteilen und Leitungen
- Leitungen in mehreren Farben zeichnen (Klick-Klick-Verfahren mit Live-Vorschau)
- Bearbeitbare Platzhalter pro Bauteil (Name, Spannung, Strom, Widerstand)
- **Undo/Redo** (snapshot-basiert, alle Aktionen)
- Speichern/Laden als JSON, Export als PNG und SVG
- Pan mit mittlerer Maustaste, Zoom mit dem Mausrad

### Installation

```bash
pip install -r requirements.txt
```

### Start

```bash
python main.py
```

### Setup.exe bauen (Windows, Inno Setup)

Ein Befehl erstellt die komplette Installer-Datei (benötigt einmalig
[Inno Setup](https://jrsoftware.org/isdl.php) auf dem Build-Rechner):

```bash
python make_release.py
```

Ergebnis: **`release/SchaltungsZeichner-Setup.exe`** — eine einzige Datei zum
Weitergeben. Der Empfänger führt sie per Doppelklick aus (deutscher Assistent,
Lizenzseite GPL, Installation pro Benutzer nach
`%LOCALAPPDATA%\Programs\SchaltungsZeichner`, **keine Admin-Rechte**,
optionale Desktop-Verknüpfung).

- Startmenü-Eintrag mit Icon, Eintrag unter „Apps & Features" inkl. Deinstaller
- **Symbole liegen als echte Dateien unter `<Programmordner>\symbols`** —
  Änderungen/Neue Symbole aus dem Symbol-Editor bleiben dauerhaft erhalten.
  **Updates überschreiben benutzerdefinierte Symbole nicht** (`onlyifdoesntexist`).
- Stille Installation/Deinstallation möglich:
  `SchaltungsZeichner-Setup.exe /VERYSILENT /DIR=...` bzw. `unins000.exe /VERYSILENT`
- Inno-Skript: `installer/setup.iss` (Onedir-Build via PyInstaller, EXE-Icon
  aus `assets/favicon.ico`)

> Hinweis: Der frühere Onefile-Build entpackte Symbole bei jedem Start in ein
> temporäres Verzeichnis — Änderungen gingen verloren. Der Onedir-Installer
> löst das; die Pfad-Logik (`src/symbols/library.py`) bevorzugt einen
> `symbols`-Ordner neben der EXE.

### Projektstruktur

```
main.py                  Einstiegspunkt
requirements.txt         Abhängigkeiten (PyQt5)
symbols/                 Symboldefinitionen (JSON, editierbar im Symbol-Editor)
src/
├── canvas/grid_canvas.py            QGraphicsView mit Raster, Pan, Zoom
├── components/
│   ├── base_component.py            Abstrakte Basisklasse + Platzhalter
│   ├── symbol_component.py          Aus JSON gerendertes Bauteil (4er-Rotation)
│   └── wire.py                      Verbindungslinie mit Farbauswahl
├── symbols/library.py               Lädt/validiert die *.symbol.json-Dateien
└── ui/
    ├── main_window.py               Hauptfenster, Menüs, Toolbar, Undo/Redo
    ├── component_toolbar.py         Dynamische Bauteil-Palette
    └── symbol_editor.py             Grafischer Editor für eigene Symbole
```

Siehe auch [FEATURES.md](FEATURES.md), [QUICKSTART.md](QUICKSTART.md),
[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) und
[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md).

### Lizenz

Copyright (c) 2026 fentrax (<https://github.com/fentrax>)

Dieses Programm ist freie Software: Sie können es unter den Bedingungen der
**GNU General Public License Version 3** (wie von der Free Software Foundation
veröffentlicht) weitergeben und/oder modifizieren. Den vollständigen Lizenztext
siehe [LICENSE](LICENSE) bzw. <https://www.gnu.org/licenses/gpl-3.0.html>.

**Hinweis zur Lizenzwahl:** Diese Software nutzt [PyQt5](https://www.riverbankcomputing.com/software/pyqt/),
das unter der GPL v3 bzw. einer kommerziellen Riverbank-Lizenz steht. Die freie
Weitergabe dieser Anwendung setzt daher die GPL v3 voraus.

**Quellcode (GPL §6):** Der vollständige Quellcode ist öffentlich verfügbar auf
GitHub: <https://github.com/fentrax/CircuitSketcher>. Probleme und Anfragen bitte als
[Issue](https://github.com/fentrax/CircuitSketcher/issues) melden. Beim Weiterleiten
bitte die LICENSE-Datei mitbeigeben.

---

<a name="english"></a>

## English

A visual drag-and-drop tool for drawing electrical circuit diagrams,
written in Python with PyQt5.

> Note: The internal window title is “SchaltungsZeichner”. CircuitSketcher is
> the project/directory name.

### Features

- Grid-based, infinite canvas (20 px grid) with magnetic snapping
- Data-driven symbol library: components are loaded from `symbols/*.symbol.json`
- Custom graphical symbol editor for creating new parts without code changes
- **4-step rotation** (0° / 90° / 180° / 270°)
- Scale, move and delete components and wires
- Draw wires in multiple colors (click-click with live preview)
- Editable placeholders per component (name, voltage, current, resistance)
- **Undo/Redo** (snapshot-based, all actions)
- Save/load as JSON, export as PNG and SVG
- Pan with middle mouse button, zoom with the mouse wheel

### Installation

```bash
pip install -r requirements.txt
```

### Start

```bash
python main.py
```

### Building Setup.exe (Windows, Inno Setup)

A single command builds the complete installer (requires
[Inno Setup](https://jrsoftware.org/isdl.php) on the build machine):

```bash
python make_release.py
```

Result: **`release/SchaltungsZeichner-Setup.exe`** — a single file to share.
Recipients run it with a double click (German wizard, GPL license page,
per-user installation to `%LOCALAPPDATA%\Programs\SchaltungsZeichner`,
**no admin rights**, optional desktop shortcut).

- Start menu entry with icon, entry under “Apps & Features” including uninstaller
- **Symbols are stored as real files under `<program folder>\symbols`** —
  changes and new symbols from the symbol editor are kept permanently.
  **Updates never overwrite custom symbols** (`onlyifdoesntexist`).
- Silent install/uninstall supported:
  `SchaltungsZeichner-Setup.exe /VERYSILENT /DIR=...` or `unins000.exe /VERYSILENT`
- Inno script: `installer/setup.iss` (onedir build via PyInstaller, EXE icon
  from `assets/favicon.ico`)

> Note: The former onefile build extracted symbols into a temporary folder on
> every start — changes were lost. The onedir installer fixes this; the path
> logic (`src/symbols/library.py`) prefers a `symbols` folder next to the EXE.

### Project Structure

```
main.py                  Entry point
requirements.txt         Dependencies (PyQt5)
symbols/                 Symbol definitions (JSON, editable in the symbol editor)
src/
├── canvas/grid_canvas.py            QGraphicsView with grid, pan, zoom
├── components/
│   ├── base_component.py            Abstract base class + placeholders
│   ├── symbol_component.py          Component rendered from JSON (4-way rotation)
│   └── wire.py                      Connection line with color selection
├── symbols/library.py               Loads/validates the *.symbol.json files
└── ui/
    ├── main_window.py               Main window, menus, toolbar, undo/redo
    ├── component_toolbar.py         Dynamic component palette
    └── symbol_editor.py             Graphical editor for custom symbols
```

See also [FEATURES.md](FEATURES.md), [QUICKSTART.md](QUICKSTART.md),
[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) and
[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md).

### License

Copyright (c) 2026 fentrax (<https://github.com/fentrax>)

This program is free software: you can redistribute it and/or modify it under
the terms of the **GNU General Public License Version 3** as published by the
Free Software Foundation. See [LICENSE](LICENSE) or
<https://www.gnu.org/licenses/gpl-3.0.html> for the full license text.

**License note:** This software uses [PyQt5](https://www.riverbankcomputing.com/software/pyqt/),
which is licensed under GPL v3 or a commercial Riverbank license. Free
redistribution of this application therefore requires GPL v3.

**Source code (GPL §6):** The complete source code is publicly available on
GitHub: <https://github.com/fentrax/CircuitSketcher>. Please report problems
and questions as an [issue](https://github.com/fentrax/CircuitSketcher/issues).
When sharing, please include the LICENSE file.
