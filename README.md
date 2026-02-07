# WiFi Penetration Testing Tool v2.0

Outil professionnel de test de sécurité WiFi avec interface style Kali Linux, conçu pour des tests éthiques sur vos propres réseaux.

![WiFi PenTest](https://img.shields.io/badge/Version-2.0-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-Ethical%20Use-orange.svg)

## AVERTISSEMENT ÉTHIQUE

Cet outil est destiné UNIQUEMENT à des tests de sécurité éthiques sur les réseaux dont vous avez l'autorisation explicite. Le piratage de réseaux WiFi est illégal et punissable par la loi.

## FONCTIONNALITÉS

### Scan WiFi Avancé
- Détection complète: SSID, BSSID/MAC, Signal, Encryption, Authentication
- Analyse de sécurité: Identification automatique des types de cryptage
- Coloration par sécurité: 
  - Open = Dangereux
  - WEP = Vulnérable  
  - WPA = Faible
  - WPA2/WPA3 = Sécurisé
- Statistiques détaillées: Compteurs par type de cryptage

### Brute Force Réel
- Connexion automatique: Se connecte réellement au WiFi si mot de passe trouvé
- Arrêt immédiat: Stoppe dès que le mot de passe est découvert
- Affichage du mot de passe: Montre le mot de passe en clair quand trouvé
- Déconnexion automatique: Se déconnecte après le test réussi

### Générateur de Wordlist Complet
- 200 000+ mots de passe: Génération massive et intelligente
- 8+ caractères uniquement: Conforme aux standards WiFi modernes
- Patterns variés:
  - Numériques (00000000-99999999)
  - Alphanumériques (lettres + chiffres)
  - Caractères spéciaux (symboles complets)
  - Mots de passe courants avec variations
  - Patterns basés sur SSID
  - Patterns de clavier (qwerty, etc.)

### Rapports Professionnels
- Format JSON: Rapports structurés et détaillés
- Organisation automatique: Sauvegarde dans le dossier reports/
- Statistiques complètes: Temps, vitesse, tentatives, score de résistance
- Historique: Conservation de tous les tests

### Interface Professionnelle
- Style Kali Linux: Interface inspirée des outils de pentest professionnels
- Code couleur: Vert (succès), Rouge (erreur), Jaune (warning), Bleu (info)
- Bannière ASCII: Design impressionnant
- Barres de progression: Suivi en temps réel

## PRÉREQUIS

### Système
- Windows 10/11 (recommandé)
- Linux (Ubuntu, Kali, etc.)
- Python 3.7+

### Dépendances
```bash
pip install -r requirements.txt
```

### Dépendances principales
- pywifi - Gestion des interfaces WiFi
- colorama - Couleurs dans la console
- tqdm - Barres de progression
- psutil - Statistiques système
- Pillow - Gestion des icônes

## INSTALLATION

### Méthode 1: Cloner le dépôt
```bash
git clone https://github.com/VOTRE_USERNAME/wifi-penetration-tool.git
cd wifi-penetration-tool
pip install -r requirements.txt
```

### Méthode 2: Télécharger l'exécutable
1. Téléchargez WiFiPenTest.exe depuis la section Releases
2. Exécutez le fichier
3. Suivez les instructions

### Méthode 3: Package Portable
1. Téléchargez WiFiPenTest_Portable.zip
2. Extrayez l'archive
3. Exécutez launch.bat

## UTILISATION

### Lancement
```bash
python wifi_security_tester_v2.py
```

### Menu Principal
```
============================================================
MENU PRINCIPAL - WiFi Penetration Testing Tool
============================================================
1. Scanner les réseaux WiFi (SSID, MAC, IP)
2. Générer wordlist COMPLÈTE (200k+ mots de passe)
3. BRUTE FORCE RÉEL (Connexion automatique)
4. Simulation de brute force
5. Afficher les statistiques système
6. Recommandations de sécurité
7. Quitter
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

## STRUCTURE DU PROJET

```
wifi-penetration-tool/
├── wifi_security_tester_v2.py    # Script principal
├── requirements.txt               # Dépendances Python
├── hack_icon.ico                # Icône de l'application
├── LICENSE.txt                  # Licence d'utilisation
├── README.md                   # Documentation
├── dist/                       # Exécutables compilés
│   └── WiFiPenTest.exe
├── WiFiPenTest_Portable/        # Package portable
├── reports/                    # Rapports JSON
├── wordlists/                  # Wordlists personnalisées
├── logs/                       # Logs d'application
└── build_final.py              # Script de compilation
```

## COMPILATION

### Compiler en .exe
```bash
python build_final.py
```

### Créer le package portable
Le script build_final.py crée automatiquement:
- dist/WiFiPenTest.exe - Exécutable principal
- WiFiPenTest_Portable/ - Package portable complet
- installer.nsi - Script d'installation NSIS

## RAPPORTS

Les rapports sont sauvegardés au format JSON dans le dossier reports/:

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

## SÉCURITÉ

### Recommandations
- Utilisez un mot de passe d'au moins 12 caractères
- Combinez lettres majuscules, minuscules, chiffres et symboles
- Évitez les mots du dictionnaire et informations personnelles
- Changez régulièrement votre mot de passe WiFi
- Activez le cryptage WPA3 si disponible
- Désactivez le WPS (WiFi Protected Setup)

### Score de résistance
- 0-25: Très faible
- 26-50: Faible  
- 51-75: Moyen
- 76-90: Fort
- 91-100: Très fort

## CONTRIBUTION

Les contributions sont les bienvenues! Veuillez suivre ces étapes:

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## CHANGELOG

### v2.0 (2026-02-07)
- Interface style Kali Linux complète
- Scan WiFi avec analyse de sécurité avancée
- Brute force réel avec connexion automatique
- Générateur de wordlist 200k+ mots de passe
- Rapports JSON organisés automatiquement
- Icône de hacking personnalisée
- Package portable et exécutable .exe

### v1.0 (2026-02-07)
- Version initiale
- Scan WiFi basique
- Simulation de brute force
- Générateur de wordlist simple

## LICENCE

Ce projet est sous licence "Usage Éthique Uniquement". Voir le fichier LICENSE.txt pour plus de détails.

## DISCLAIMER

Cet outil est fourni à des fins éducatives et de tests de sécurité éthiques uniquement. L'utilisateur est responsable de se conformer à toutes les lois et réglementations applicables. L'auteur n'est pas responsable de toute utilisation malveillante de ce logiciel.

## SUPPORT

Pour toute question ou problème:
- Signalez les bugs sur GitHub Issues
- Contact: votre-email@example.com
- Documentation: Wiki du projet

## REMERCIEMENTS

- Merci à la communauté de cybersécurité pour les outils et techniques
- Inspiré par les outils de pentest professionnels
- Développé avec pour des tests de sécurité responsables

---

RAPPEL: Cet outil doit être utilisé uniquement à des fins éthiques et légales sur vos propres réseaux.
