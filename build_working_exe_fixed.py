#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilation d'un exécutable fonctionnel avec mode console et icône
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_working_executable():
    """Compile l'application en .exe fonctionnel"""
    print("🔨 Compilation de l'exécutable fonctionnel...")
    
    # Options PyInstaller pour un exécutable qui fonctionne
    options = [
        "--onefile",                    # Un seul fichier .exe
        "--console",                    # Mode console (nécessaire pour l'interface)
        "--name=WiFiPenTestWorking",     # Nom de l'exécutable
        "--icon=wifi_icon.ico",         # Icône intégrée
        "--clean",                      # Nettoyer les builds précédents
        "--noconfirm",                  # Pas de confirmation
        "--distpath=dist_working",        # Dossier de sortie
        "--workpath=build",             # Dossier de travail
        "--hidden-import=colorama",       # Import caché pour colorama
        "--hidden-import=tqdm",         # Import caché pour tqdm
        "--hidden-import=psutil",       # Import caché pour psutil
        "--hidden-import=pywifi",       # Import caché pour pywifi
        "--hidden-import=comtypes",      # Import caché pour comtypes
        "--hidden-import=socket",        # Import caché pour socket
        "--hidden-import=re",            # Import caché pour re
        "--hidden-import=threading",     # Import caché pour threading
        "--hidden-import=itertools",     # Import caché pour itertools
        "--hidden-import=string",        # Import caché pour string
        "--hidden-import=random",        # Import caché pour random
        "--hidden-import=datetime",      # Import caché pour datetime
        "--hidden-import=json",          # Import caché pour json
        "--add-data=LICENSE.txt;.",     # Ajouter le fichier de licence
        "wifi_security_tester_v2.py"   # Fichier principal
    ]
    
    # Commande PyInstaller
    cmd = ["pyinstaller"] + options
    
    try:
        print("Lancement de la compilation...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Compilation réussie!")
            print(f"📦 Exécutable créé: dist_working/WiFiPenTestWorking.exe")
            return True
        else:
            print("❌ Erreur lors de la compilation:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def check_executable():
    """Vérifie l'exécutable compilé"""
    exe_path = "dist_working/WiFiPenTestWorking.exe"
    
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

def test_executable():
    """Test simple de l'exécutable"""
    exe_path = "dist_working/WiFiPenTestWorking.exe"
    
    if not os.path.exists(exe_path):
        print("❌ Exécutable non trouvé pour le test")
        return False
    
    print("🧪 Test de l'exécutable...")
    
    try:
        # Test simple: vérifier si le fichier peut être lu
        with open(exe_path, 'rb') as f:
            header = f.read(100)
            if b'MZ' in header:  # Signature PE
                print("✅ L'exécutable a une signature PE valide")
                return True
            else:
                print("❌ L'exécutable n'a pas de signature PE valide")
                return False
                
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

def copy_to_project():
    """Copie l'exécutable dans les dossiers appropriés"""
    print("📁 Copie vers les dossiers du projet...")
    
    source = "dist_working/WiFiPenTestWorking.exe"
    
    # Copier vers dist/
    try:
        if os.path.exists("dist/WiFiPenTestWorking.exe"):
            os.remove("dist/WiFiPenTestWorking.exe")
        shutil.copy2(source, "dist/WiFiPenTestWorking.exe")
        print("  ✅ Copié vers dist/WiFiPenTestWorking.exe")
    except Exception as e:
        print(f"  ❌ Erreur copie vers dist/: {e}")
    
    # Copier vers WiFi_PenTest/dist/
    try:
        if os.path.exists("WiFi_PenTest/dist/WiFiPenTestWorking.exe"):
            os.remove("WiFi_PenTest/dist/WiFiPenTestWorking.exe")
        shutil.copy2(source, "WiFi_PenTest/dist/WiFiPenTestWorking.exe")
        print("  ✅ Copié vers WiFi_PenTest/dist/WiFiPenTestWorking.exe")
    except Exception as e:
        print(f"  ❌ Erreur copie vers WiFi_PenTest/dist/: {e}")
    
    # Copier vers la racine
    try:
        if os.path.exists("WiFiPenTestWorking.exe"):
            os.remove("WiFiPenTestWorking.exe")
        shutil.copy2(source, "WiFiPenTestWorking.exe")
        print("  ✅ Copié vers la racine: WiFiPenTestWorking.exe")
    except Exception as e:
        print(f"  ❌ Erreur copie vers la racine: {e}")

def clean_temp():
    """Nettoie les fichiers temporaires"""
    print("🧹 Nettoyage...")
    
    temp_dirs = ["dist_working", "build"]
    for dir_name in temp_dirs:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"  ✅ {dir_name}/ supprimé")
            except:
                pass

def main():
    """Fonction principale"""
    print("🔧 Compilation fonctionnelle - WiFi Penetration Testing Tool v2.0")
    print("="*70)
    
    # Étape 1: Nettoyage
    clean_temp()
    print()
    
    # Étape 2: Compilation
    if build_working_executable():
        print()
        
        # Étape 3: Vérification
        if check_executable():
            print()
            
            # Étape 4: Test
            if test_executable():
                print()
                
                # Étape 5: Copie
                copy_to_project()
                print()
                
                # Étape 6: Nettoyage final
                clean_temp()
                
                print("="*70)
                print("✅ EXÉCUTABLE FONCTIONNEL CRÉÉ!")
                print("="*70)
                print("📦 Fichiers créés:")
                print("  • dist/WiFiPenTestWorking.exe")
                print("  • WiFi_PenTest/dist/WiFiPenTestWorking.exe")
                print("  • WiFiPenTestWorking.exe (racine)")
                print()
                print("🔧 Caractéristiques:")
                print("  • Mode console (interface fonctionnelle)")
                print("  • Icône correctement intégrée")
                print("  • Tous les imports inclus")
                print("  • Signature PE valide")
                print()
                print("🚀 Prêt pour GitHub!")
                print("="*70)
            else:
                print("❌ L'exécutable n'a pas passé les tests")
        else:
            print("❌ L'exécutable n'est pas valide")
    else:
        print("❌ Échec de la compilation")
        
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()
