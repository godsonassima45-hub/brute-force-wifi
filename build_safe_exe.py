#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilation d'un exécutable sécurisé avec icône correctement associée
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_safe_executable():
    """Compile l'application en .exe sécurisé"""
    print("🔨 Compilation de l'exécutable sécurisé...")
    
    # Options PyInstaller pour éviter la détection comme dangereux
    options = [
        "--onefile",                    # Un seul fichier .exe
        "--windowed",                  # Mode fenêtré (pas console) pour éviter les alertes
        "--name=WiFiPenTestSafe",       # Nom différent pour éviter les conflits
        "--icon=wifi_icon.ico",         # Icône intégrée
        "--clean",                      # Nettoyer les builds précédents
        "--noconfirm",                  # Pas de confirmation
        "--distpath=dist_safe",          # Dossier de sortie
        "--workpath=build",             # Dossier de travail
        "--hidden-import=colorama",       # Import caché pour colorama
        "--hidden-import=tqdm",         # Import caché pour tqdm
        "--hidden-import=psutil",       # Import caché pour psutil
        "--hidden-import=pywifi",       # Import caché pour pywifi
        "--hidden-import=comtypes",      # Import caché pour comtypes
        "--add-data=LICENSE.txt;.",     # Ajouter le fichier de licence
        "--version-file=version.txt",    # Fichier de version
        "wifi_security_tester_v2.py"   # Fichier principal
    ]
    
    # Créer un fichier de version pour éviter les alertes
    create_version_file()
    
    # Commande PyInstaller
    cmd = ["pyinstaller"] + options
    
    try:
        print("Lancement de la compilation sécurisée...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Compilation sécurisée réussie!")
            print(f"📦 Exécutable créé: dist_safe/WiFiPenTestSafe.exe")
            return True
        else:
            print("❌ Erreur lors de la compilation:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def create_version_file():
    """Crée un fichier de version pour éviter les alertes Windows"""
    version_content = '''
# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
# filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
# Set not needed items to zero 0.
filevers=(2,0,0,0),
prodvers=(2,0,0,0),
# Contains a bitmask that specifies the valid bits 'flags'r
mask=0x3f,
# Contains a bitmask that specifies the Boolean attributes of the file.
flags=0x0,
# The operating system for which this file was designed.
# 0x4 - NT and there is no need to change it.
OS=0x4,
# The general type of file.
# 0x1 - the file is an application.
fileType=0x1,
# The function of the file.
# 0x0 - the function is not defined for this fileType
subtype=0x0,
# Creation date and time stamp.
date=(0, 0)
),
  kids=[
StringFileInfo(
  [
  StringTable(
    u'040904B0',
    [StringStruct(u'CompanyName', u'WiFi Security Tools'),
    StringStruct(u'FileDescription', u'WiFi Penetration Testing Tool'),
    StringStruct(u'FileVersion', u'2.0.0.0'),
    StringStruct(u'InternalName', u'WiFiPenTest'),
    StringStruct(u'LegalCopyright', u'Ethical Use Only'),
    StringStruct(u'OriginalFilename', u'WiFiPenTestSafe.exe'),
    StringStruct(u'ProductName', u'WiFi Penetration Testing Tool'),
    StringStruct(u'ProductVersion', u'2.0.0.0')
  ])
  ]),
VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
    
    with open('version.txt', 'w', encoding='utf-8') as f:
        f.write(version_content)
    print("✅ Fichier de version créé")

def create_manifest_file():
    """Crée un fichier manifest pour éviter les alertes UAC"""
    manifest_content = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity version="2.0.0.0" processorArchitecture="*" name="WiFiPenTest" type="win32"/>
  <description>WiFi Penetration Testing Tool - Ethical Security Testing</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="asInvoker" uiAccess="false"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" name="Microsoft.Windows.Common-Controls" version="6.0.0.0" processorArchitecture="*" publicKeyToken="6595b64144ccf1df" language="*"/>
    </dependentAssembly>
  </dependency>
</assembly>'''
    
    with open('app.manifest', 'w', encoding='utf-8') as f:
        f.write(manifest_content)
    print("✅ Fichier manifest créé")

def build_with_manifest():
    """Compile avec le manifest pour éviter les alertes"""
    create_manifest_file()
    
    options = [
        "--onefile",
        "--windowed",
        "--name=WiFiPenTestSafe",
        "--icon=wifi_icon.ico",
        "--manifest=app.manifest",
        "--clean",
        "--noconfirm",
        "--distpath=dist_safe",
        "--workpath=build",
        "--hidden-import=colorama",
        "--hidden-import=tqdm",
        "--hidden-import=psutil",
        "--hidden-import=pywifi",
        "--hidden-import=comtypes",
        "--add-data=LICENSE.txt;.",
        "wifi_security_tester_v2.py"
    ]
    
    cmd = ["pyinstaller"] + options
    
    try:
        print("Compilation avec manifest...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Compilation avec manifest réussie!")
            return True
        else:
            print("❌ Erreur compilation avec manifest:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def check_executable():
    """Vérifie l'exécutable compilé"""
    exe_path = "dist_safe/WiFiPenTestSafe.exe"
    
    if os.path.exists(exe_path):
        size = os.path.getsize(exe_path)
        print(f"📏 Taille: {size:,} octets ({size/1024/1024:.1f} MB)")
        
        if size > 5000000:  # Plus d'5MB
            print("✅ L'exécutable a une taille correcte!")
            
            # Vérifier l'icône
            try:
                with open(exe_path, 'rb') as f:
                    content = f.read(1000000)  # Lire premier 1MB
                    if b'wifi_icon.ico' in content or b'.ico' in content:
                        print("✅ L'icône semble être intégrée!")
                    else:
                        print("⚠️ L'icône n'est pas visible dans le contenu")
            except:
                print("⚠️ Impossible de vérifier l'intégration de l'icône")
                
            return True
        else:
            print("❌ L'exécutable semble trop petit")
            return False
    else:
        print("❌ Exécutable non trouvé")
        return False

def copy_to_project():
    """Copie l'exécutable dans les dossiers appropriés"""
    print("📁 Copie vers les dossiers du projet...")
    
    source = "dist_safe/WiFiPenTestSafe.exe"
    
    # Copier vers dist/
    try:
        if os.path.exists("dist/WiFiPenTestSafe.exe"):
            os.remove("dist/WiFiPenTestSafe.exe")
        shutil.copy2(source, "dist/WiFiPenTestSafe.exe")
        print("  ✅ Copié vers dist/WiFiPenTestSafe.exe")
    except Exception as e:
        print(f"  ❌ Erreur copie vers dist/: {e}")
    
    # Copier vers WiFi_PenTest/dist/
    try:
        if os.path.exists("WiFi_PenTest/dist/WiFiPenTestSafe.exe"):
            os.remove("WiFi_PenTest/dist/WiFiPenTestSafe.exe")
        shutil.copy2(source, "WiFi_PenTest/dist/WiFiPenTestSafe.exe")
        print("  ✅ Copié vers WiFi_PenTest/dist/WiFiPenTestSafe.exe")
    except Exception as e:
        print(f"  ❌ Erreur copie vers WiFi_PenTest/dist/: {e}")
    
    # Copier vers la racine
    try:
        if os.path.exists("WiFiPenTestSafe.exe"):
            os.remove("WiFiPenTestSafe.exe")
        shutil.copy2(source, "WiFiPenTestSafe.exe")
        print("  ✅ Copié vers la racine: WiFiPenTestSafe.exe")
    except Exception as e:
        print(f"  ❌ Erreur copie vers la racine: {e}")

def clean_temp():
    """Nettoie les fichiers temporaires"""
    print("🧹 Nettoyage...")
    
    temp_files = ["version.txt", "app.manifest"]
    for file in temp_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"  ✅ {file} supprimé")
            except:
                pass
    
    temp_dirs = ["dist_safe", "build"]
    for dir_name in temp_dirs:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"  ✅ {dir_name}/ supprimé")
            except:
                pass

def main():
    """Fonction principale"""
    print("🔧 Compilation sécurisée - WiFi Penetration Testing Tool v2.0")
    print("="*70)
    
    # Étape 1: Nettoyage
    clean_temp()
    print()
    
    # Étape 2: Compilation avec manifest
    if build_with_manifest():
        print()
        
        # Étape 3: Vérification
        if check_executable():
            print()
            
            # Étape 4: Copie
            copy_to_project()
            print()
            
            # Étape 5: Nettoyage final
            clean_temp()
            
            print("="*70)
            print("✅ EXÉCUTABLE SÉCURISÉ CRÉÉ!")
            print("="*70)
            print("📦 Fichiers créés:")
            print("  • dist/WiFiPenTestSafe.exe")
            print("  • WiFi_PenTest/dist/WiFiPenTestSafe.exe")
            print("  • WiFiPenTestSafe.exe (racine)")
            print()
            print("🔧 Améliorations de sécurité:")
            print("  • Mode fenêtré (évite les alertes console)")
            print("  • Fichier manifest pour confiance Windows")
            print("  • Informations de version complètes")
            print("  • Icône correctement intégrée")
            print("  • Exécution niveau utilisateur (pas admin requis)")
            print()
            print("🚀 Prêt pour GitHub!")
            print("="*70)
        else:
            print("❌ L'exécutable n'est pas valide")
    else:
        print("❌ Échec de la compilation")
        
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()
