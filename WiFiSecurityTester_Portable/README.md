# 🔐 WiFi Security Tester

Outil de test de sécurité WiFi éthique créé pour des tests de sécurité sur vos propres réseaux WiFi uniquement.

## ⚠️ Avertissement Éthique

Cet outil est destiné **uniquement** à des tests de sécurité éthiques sur les réseaux dont vous avez l'autorisation explicite. Le piratage de réseaux WiFi est illégal et punissable par la loi.

## 🚀 Fonctionnalités

- **Scan WiFi**: Détecte les réseaux WiFi disponibles
- **Générateur de Wordlist**: Crée des listes de mots de passe pour les tests
- **Test de Force**: Évalue la robustesse des mots de passe
- **Rapports de Sécurité**: Génère des rapports détaillés
- **Interface Console**: Interface utilisateur simple et intuitive
- **Compilation .exe**: Peut être compilé en exécutable Windows

## 📋 Prérequis

- Python 3.7 ou supérieur
- Windows/Linux/macOS
- Droits administrateur (pour le scan WiFi)

## 🛠️ Installation

### 1. Cloner ou télécharger les fichiers

```bash
git clone <repository-url>
cd brute-force_wifi
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l'outil

```bash
python wifi_security_tester.py
```

## 🔧 Utilisation

### Menu Principal

1. **Scanner les réseaux WiFi**: Détecte les réseaux à portée
2. **Générer une wordlist**: Crée une liste de mots de passe de test
3. **Tester la sécurité**: Teste la robustesse d'un mot de passe
4. **Afficher les recommandations**: Conseils de sécurité
5. **Quitter**: Ferme l'application

### Exemple d'utilisation

```python
# Import de la classe
from wifi_security_tester import WiFiSecurityTester

# Création de l'instance
tester = WiFiSecurityTester()

# Scan des réseaux
networks = tester.scan_wifi_networks()

# Génération de wordlist
wordlist = tester.generate_wordlist(complexity="high", length=12)

# Test de sécurité
report, weak_passwords = tester.test_network_security("MonWiFi", max_passwords=1000)
```

## 📦 Compilation en .exe

### Méthode 1: Script automatique

```bash
python build_exe.py
```

### Méthode 2: Manuel

```bash
# Installer PyInstaller
pip install pyinstaller

# Compiler
pyinstaller --onefile --windowed --name=WiFiSecurityTester wifi_security_tester.py
```

Le fichier exécutable sera créé dans le dossier `dist/`.

## 📁 Structure des fichiers

```
brute-force_wifi/
├── wifi_security_tester.py    # Script principal
├── config.py                  # Configuration
├── requirements.txt           # Dépendances
├── build_exe.py              # Script de compilation
├── README.md                 # Documentation
├── reports/                  # Rapports générés
├── wordlists/                # Wordlists personnalisées
└── dist/                     # Exécutables compilés
```

## ⚙️ Configuration

Le fichier `config.py` contient tous les paramètres configurables:

- `SCAN_TIMEOUT`: Timeout du scan WiFi
- `MAX_TEST_COUNT`: Nombre maximum de mots de passe à tester
- `TEST_DELAY`: Délai entre chaque test
- `SECURITY_LEVELS`: Niveaux de sécurité
- `ETHICAL_WARNINGS`: Messages d'avertissement

## 🔍 Fonctionnalités détaillées

### Scan WiFi

- Compatible Windows (netsh)
- Compatible Linux (iwlist)
- Affiche SSID, force du signal, type de sécurité

### Générateur de Wordlist

- 3 niveaux de complexité (low/medium/high)
- Génération aléatoire basée sur des patterns
- Support des caractères spéciaux
- Personnalisable

### Test de Sécurité

- Analyse de la force des mots de passe
- Score de sécurité 0-5
- Recommandations personnalisées
- Rapports JSON détaillés

### Rapports

Les rapports sont sauvegardés en format JSON avec:
- Résumé du test
- Mots de passe faibles détectés
- Score de sécurité global
- Recommandations

## 🛡️ Mesures de sécurité

- Avertissements éthiques obligatoires
- Confirmation requise avant les tests
- Logging des activités
- Limitation des tentatives
- Pas de connexion réseau réelle (simulation)

## 📝 Notes importantes

1. **Usage éthique uniquement**: Testez uniquement vos réseaux
2. **Responsabilité**: Vous êtes responsable de l'utilisation
3. **Légalité**: Respectez les lois locales
4. **Performance**: Les tests peuvent prendre du temps
5. **Ressources**: Utilisez modérément les ressources système

## 🐛 Dépannage

### Problèmes courants

**"Aucun réseau détecté"**
- Vérifiez les droits administrateur
- Assurez-vous que le WiFi est activé
- Redémarrez l'outil

**"Erreur de compilation"**
- Installez Visual C++ Redistributable
- Vérifiez l'installation de PyInstaller
- Essayez en mode administrateur

**"Performance lente"**
- Réduisez MAX_TEST_COUNT
- Augmentez TEST_DELAY
- Utilisez une wordlist plus petite

## 📞 Support

Pour toute question ou problème:
- Vérifiez la documentation
- Consultez les logs d'erreur
- Signalez les bugs sur GitHub

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 👨‍💻 Auteur

Créé par un pentester éthique pour des tests de sécurité responsables.

---

**⚠️ RAPPEL**: Cet outil doit être utilisé uniquement à des fins éthiques et légales sur vos propres réseaux.
