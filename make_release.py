"""Release bauen: Onedir-EXE + Inno-Setup → eine einzige Setup.exe.

Ergebnis: release/SchaltungsZeichner-Setup.exe
Weitergabe als einzelne Datei; Installation per Assistent ohne Admin-Rechte.

Aufruf:  python make_release.py
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST_APP = ROOT / "dist" / "SchaltungsZeichner"
RELEASE_DIR = ROOT / "release"
ISS = ROOT / "installer" / "setup.iss"

ISCC_CANDIDATES = [
    Path.home() / "AppData" / "Local" / "Programs" / "Inno Setup 7" / "ISCC.exe",
    Path.home() / "AppData" / "Local" / "Programs" / "Inno Setup 6" / "ISCC.exe",
    Path("C:/Program Files/Inno Setup 7/ISCC.exe"),
    Path("C:/Program Files (x86)/Inno Setup 7/ISCC.exe"),
    Path("C:/Program Files (x86)/Inno Setup 6/ISCC.exe"),
]


def find_iscc() -> Path:
    for candidate in ISCC_CANDIDATES:
        if candidate.exists():
            return candidate
    raise SystemExit(
        "FEHLER: Inno Setup (ISCC.exe) nicht gefunden.\n"
        "Bitte Inno Setup installieren: https://jrsoftware.org/isdl.php"
    )


def main() -> int:
    print("=== 1/3 PyInstaller-Build (onedir) ===")
    result = subprocess.run(
        [sys.executable, "-m", "PyInstaller", "SchaltungsZeichner.spec", "--noconfirm"],
        cwd=ROOT,
    )
    if result.returncode != 0:
        print("Build fehlgeschlagen.")
        return 1

    exe = DIST_APP / "SchaltungsZeichner.exe"
    if not exe.exists():
        print(f"FEHLER: {exe} nicht gefunden.")
        return 1

    print("=== 2/3 Inno-Setup kompilieren ===")
    iscc = find_iscc()
    print(f"ISCC: {iscc}")
    result = subprocess.run([str(iscc), str(ISS)], cwd=ROOT)
    if result.returncode != 0:
        print("Inno-Kompilierung fehlgeschlagen.")
        return 1

    setup_exe = RELEASE_DIR / "SchaltungsZeichner-Setup.exe"
    if not setup_exe.exists():
        print(f"FEHLER: {setup_exe} nicht erzeugt.")
        return 1

    print("=== 3/3 Fertig ===")
    print(f"Setup: {setup_exe} ({setup_exe.stat().st_size / 1024 / 1024:.1f} MB)")
    print("Weitergabe als einzelne Datei; Installation ohne Admin-Rechte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
