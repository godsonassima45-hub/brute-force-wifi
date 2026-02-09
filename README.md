<<<<<<< HEAD
# 🔐 WiFi Penetration Testing Tool v2.0

Outil professionnel de test de sécurité WiFi avec interface style Kali Linux, conçu pour des tests éthiques sur vos propres réseaux.

![WiFi PenTest](https://img.shields.io/badge/Version-2.0-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-Ethical%20Use-orange.svg)

## ⚠️ AVERTISSEMENT ÉTHIQUE

Cet outil est destiné **UNIQUEMENT** à des tests de sécurité éthiques sur les réseaux dont vous avez l'autorisation explicite. Le piratage de réseaux WiFi est illégal et punissable par la loi.

## 🚀 FONCTIONNALITÉS

### 📡 **Scan WiFi Avancé**
- **Détection complète**: SSID, BSSID/MAC, Signal, Encryption, Authentication
- **Analyse de sécurité**: Identification automatique des types de cryptage
- **Coloration par sécurité**: 
  - 🔴 Open = Dangereux
  - 🟡 WEP = Vulnérable  
  - 🟡 WPA = Faible
  - 🟢 WPA2/WPA3 = Sécurisé
- **Statistiques détaillées**: Compteurs par type de cryptage

### 🔐 **Brute Force Réel**
- **Connexion automatique**: Se connecte réellement au WiFi si mot de passe trouvé
- **Arrêt immédiat**: Stoppe dès que le mot de passe est découvert
- **Affichage du mot de passe**: Montre le mot de passe en clair quand trouvé
- **Déconnexion automatique**: Se déconnecte après le test réussi

### 📝 **Générateur de Wordlist Complet**
- **200 000+ mots de passe**: Génération massive et intelligente
- **8+ caractères uniquement**: Conforme aux standards WiFi modernes
- **Patterns variés**:
  - Numériques (00000000-99999999)
  - Alphanumériques (lettres + chiffres)
  - Caractères spéciaux (symboles complets)
  - Mots de passe courants avec variations
  - Patterns basés sur SSID
  - Patterns de clavier (qwerty, etc.)

### 📊 **Rapports Professionnels**
- **Format JSON**: Rapports structurés et détaillés
- **Organisation automatique**: Sauvegarde dans le dossier `reports/`
- **Statistiques complètes**: Temps, vitesse, tentatives, score de résistance
- **Historique**: Conservation de tous les tests

### 🎨 **Interface Professionnelle**
- **Style Kali Linux**: Interface inspirée des outils de pentest professionnels
- **Code couleur**: Vert (succès), Rouge (erreur), Jaune (warning), Bleu (info)
- **Bannière ASCII**: Design impressionnant
- **Barres de progression**: Suivi en temps réel

## 📋 PRÉREQUIS

### Système
- **Windows 10/11** (recommandé)
- **Linux** (Ubuntu, Kali, etc.)
- **Python 3.7+**

### Dépendances
```bash
pip install -r requirements.txt
```

### Dépendances principales
- `pywifi` - Gestion des interfaces WiFi
- `colorama` - Couleurs dans la console
- `tqdm` - Barres de progression
- `psutil` - Statistiques système
- `Pillow` - Gestion des icônes

## 🛠️ INSTALLATION

### Méthode 1: Cloner le dépôt
```bash
git clone https://github.com/VOTRE_USERNAME/brute-force-wifi.git
cd brute-force-wifi
pip install -r requirements.txt
```

### Méthode 2: Télécharger l'exécutable
1. Téléchargez l'un des exécutables depuis le dossier `dist/`:
   - `WiFiPenTestWorking.exe` - **Version fonctionnelle (recommandée)**
   - `WiFiPenTestSafe.exe` - Version sécurisée (mode fenêtré)
   - `WiFiPenTest.exe` - Version standard
2. Exécutez le fichier
3. Suivez les instructions

### 🚨 **IMPORTANT - SÉCURITÉ WINDOWS**

**Pour éviter les alertes de sécurité Windows:**

**Option 1 - Exécutable fonctionnel (Recommandé):**
- **WiFiPenTestWorking.exe** - Mode console, interface complète
- **Clic droit → Propriétés → Débloquer** si nécessaire

**Option 2 - Exécutable sécurisé:**
- **WiFiPenTestSafe.exe** - Mode fenêtré, pas de droits admin requis
- **Clic droit → Propriétés → Débloquer** si nécessaire

**Option 3 - Exécutable standard:**
- **WiFiPenTest.exe** - Mode console, nécessite droits administrateur
- **Clic droit → Exécuter en tant qu'administrateur**

**Option 4 - Si Windows bloque l'exécution:**
1. Clic droit sur l'exécutable → **Propriétés**
2. Cochez **"Débloquer"** (si présent)
3. Cliquez sur **OK**
4. Relancez l'exécutable

## 🚀 UTILISATION

### Lancement
```bash
python wifi_security_tester_v2.py
```

### Menu Principal
```
============================================================
MENU PRINCIPAL - WiFi Penetration Testing Tool
============================================================
1. 🔍 Scanner les réseaux WiFi (SSID, MAC, IP)
2. 📝 Générer wordlist COMPLÈTE (200k+ mots de passe)
3. 🚨 BRUTE FORCE RÉEL (Connexion automatique)
4. 🎮 Simulation de brute force
5. 📊 Afficher les statistiques système
6. 🛡️ Recommandations de sécurité
7. ❌ Quitter
============================================================
```

### Exemples d'utilisation

#### Scan WiFi
```python
from wifi_security_tester_v2 import WiFiSecurityTester

tester = WiFiSecurityTester()
networks = tester.scan_wifi_networks()
tester.display_networks_table(networks)
```

#### Brute Force
```python
report = tester.brute_force_wifi_real("Target_SSID", max_attempts=1000)
tester.save_brute_force_report(report)
```

## 📁 STRUCTURE DU PROJET

```
brute-force-wifi/
├── wifi_security_tester_v2.py    # Script principal
├── requirements.txt               # Dépendances Python
├── wifi_icon.ico                # Icône de l'application
├── LICENSE.txt                  # Licence d'utilisation
├── README.md                   # Documentation
├── dist/                       # Exécutables compilés
│   ├── WiFiPenTest.exe         # Exécutable standard (8MB)
│   ├── WiFiPenTestSafe.exe     # Exécutable sécurisé (20.5MB)
│   └── WiFiPenTestWorking.exe  # Exécutable fonctionnel (20.5MB)
├── WiFi_PenTest/               # Package propre
│   ├── wifi_security_tester_v2.py
│   ├── requirements.txt
│   ├── wifi_icon.ico
│   ├── LICENSE.txt
│   ├── README.md
│   ├── dist/WiFiPenTest.exe
│   ├── dist/WiFiPenTestSafe.exe
│   ├── dist/WiFiPenTestWorking.exe
│   ├── reports/
│   ├── wordlists/
│   └── logs/
├── reports/                    # Rapports JSON
├── wordlists/                  # Wordlists personnalisées
├── logs/                       # Logs d'application
├── build_final.py              # Script de compilation
├── build_safe_exe.py          # Script compilation sécurisée
├── build_working_exe_fixed.py # Script compilation fonctionnelle
├── installer.nsi               # Script d'installation NSIS
├── WiFiPenTest_Final.exe     # Exécutable alternatif (21.5MB)
├── WiFiPenTestSafe.exe       # Exécutable sécurisé (21.5MB)
└── WiFiPenTestWorking.exe    # Exécutable fonctionnel (21.5MB)
```

## 🔧 COMPILATION

Pour compiler en .exe:
```bash
pip install pyinstaller
python build_final.py          # Version standard
```

Pour compiler l'exécutable sécurisé:
```bash
python build_safe_exe.py         # Version sécurisée
```

Pour compiler l'exécutable fonctionnel:
```bash
python build_working_exe_fixed.py # Version fonctionnelle (recommandée)
```

Ou manuellement:
```bash
# Version standard
pyinstaller --onefile --console --icon=wifi_icon.ico --name=WiFiPenTest wifi_security_tester_v2.py

# Version sécurisée
pyinstaller --onefile --windowed --icon=wifi_icon.ico --name=WiFiPenTestSafe --manifest=app.manifest wifi_security_tester_v2.py

# Version fonctionnelle
pyinstaller --onefile --console --icon=wifi_icon.ico --name=WiFiPenTestWorking --hidden-import=colorama --hidden-import=tqdm --hidden-import=psutil --hidden-import=pywifi --hidden-import=comtypes wifi_security_tester_v2.py
```

## 📊 RAPPORTS

Les rapports sont sauvegardés au format JSON dans le dossier `reports/`:

```json
{
  "target_ssid": "TP-Link_A9B4",
  "test_date": "2026-02-07T01:02:53.184099",
  "brute_force_mode": true,
  "passwords_tested": 47,
  "password_found": true,
  "found_password": "004504",
  "elapsed_time": 524.95,
  "attempts_per_second": 0.09,
  "security_resistance": {
    "time_to_crack": "524.95s",
    "attempts_needed": 47,
    "resistance_score": 99.53
  }
}
```

## 🛡️ SÉCURITÉ

### Recommandations
- Utilisez un mot de passe d'au moins 12 caractères
- Combinez lettres majuscules, minuscules, chiffres et symboles
- Évitez les mots du dictionnaire et informations personnelles
- Changez régulièrement votre mot de passe WiFi
- Activez le cryptage WPA3 si disponible
- Désactivez le WPS (WiFi Protected Setup)

### Score de résistance
- **0-25**: Très faible
- **26-50**: Faible  
- **51-75**: Moyen
- **76-90**: Fort
- **91-100**: Très fort

## 🤝 CONTRIBUTION

Les contributions sont les bienvenues! Veuillez suivre ces étapes:

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 CHANGELOG

### v2.0 (2026-02-07)
- ✨ Interface style Kali Linux complète
- 🔍 Scan WiFi avec analyse de sécurité avancée
- 🔐 Brute force réel avec connexion automatique
- 📝 Générateur de wordlist 200k+ mots de passe
- 📊 Rapports JSON organisés automatiquement
- 🎨 Icône de hacking personnalisée
- 📦 Exécutable .exe inclus
- 📁 Package WiFi_PenTest propre
- 🔧 Exécutable sécurisé (WiFiPenTestSafe.exe)
- 🛡️ Protection contre les alertes Windows

## ⚖️ LICENCE

Ce projet est sous licence "Usage Éthique Uniquement". Voir le fichier [LICENSE.txt](LICENSE.txt) pour plus de détails.

## ⚠️ DISCLAIMER

Cet outil est fourni à des fins éducatives et de tests de sécurité éthiques uniquement. L'utilisateur est responsable de se conformer à toutes les lois et réglementations applicables. L'auteur n'est pas responsable de toute utilisation malveillante de ce logiciel.

## 📞 SUPPORT

Pour toute question ou problème:
- 🐛 Signalez les bugs sur [GitHub Issues](https://github.com/VOTRE_USERNAME/brute-force-wifi/issues)
- 📧 Contact: [votre-email@example.com]

## 🙏 REMERCIEMENTS

- Merci à la communauté de cybersécurité pour les outils et techniques
- Inspiré par les outils de pentest professionnels
- Développé avec ❤️ pour des tests de sécurité responsables

---

**⚠️ RAPPEL**: Cet outil doit être utilisé uniquement à des fins éthiques et légales sur vos propres réseaux.

---

## 🚨 **NOTE SUR L'EXÉCUTABLE**

**Problème d'accès refusé résolu:**
- L'exécutable `WiFiPenTest.exe` nécessite des droits administrateur
- **Solution**: Clic droit → "Exécuter en tant qu'administrateur"
- **Alternative**: Lancer depuis une invite de commandes administrateur

**Exécutables disponibles:**
- `dist/WiFiPenTest.exe` (8MB) - Version standard (console, admin requis)
- `dist/WiFiPenTestSafe.exe` (20.5MB) - **Version sécurisée (recommandée)**
- `WiFiPenTest_Final.exe` (21.5MB) - Version alternative
- `WiFiPenTestSafe.exe` (21.5MB) - Version sécurisée racine
- `WiFi_PenTest/dist/WiFiPenTestSafe.exe` - Package propre sécurisé

**Différences:**
- **WiFiPenTestSafe.exe**: Mode fenêtré, icône intégrée, pas d'alertes Windows
- **WiFiPenTest.exe**: Mode console, droits admin requis, alertes possibles

**Si l'accès est toujours refusé:**
1. Clic droit sur l'exécutable → **Propriétés**
2. Cochez **"Débloquer"** (si présent)
3. Cliquez sur **OK**
4. Relancez l'exécutable
=======
# brute-force-wifi
>>>>>>> 04e0340da756461fb092aed71bcb2182b100a65a
