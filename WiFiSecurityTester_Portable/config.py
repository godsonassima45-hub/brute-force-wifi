#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fichier de configuration pour l'outil de test de sécurité WiFi
"""

# Configuration principale
CONFIG = {
    # Paramètres de scan
    "SCAN_TIMEOUT": 10,  # Secondes
    "MAX_NETWORKS": 50,   # Nombre maximum de réseaux à afficher
    
    # Paramètres de wordlist
    "DEFAULT_WORDLIST_SIZE": 10000,
    "MAX_PASSWORD_LENGTH": 20,
    "MIN_PASSWORD_LENGTH": 6,
    
    # Paramètres de test
    "DEFAULT_TEST_COUNT": 100,
    "MAX_TEST_COUNT": 10000,
    "TEST_DELAY": 0.01,   # Secondes entre chaque test
    
    # Paramètres de sécurité
    "MIN_STRENGTH_SCORE": 3,
    "WEAK_PASSWORD_THRESHOLD": 3,
    
    # Fichiers
    "REPORT_DIR": "reports",
    "WORDLIST_DIR": "wordlists",
    "DEFAULT_REPORT_NAME": "wifi_security_report.json",
    
    # Interface
    "CONSOLE_WIDTH": 80,
    "SHOW_PROGRESS": True,
    "COLOR_OUTPUT": True,
    
    # Sécurité éthique
    "ETHICAL_WARNING": True,
    "REQUIRE_CONFIRMATION": True,
    "LOG_ALL_ATTEMPTS": False,
    
    # Plateforme
    "SUPPORTED_PLATFORMS": ["win32", "linux", "darwin"],
}

# Messages d'avertissement éthique
ETHICAL_WARNINGS = [
    "Cet outil est destiné à des tests de sécurité éthiques uniquement",
    "Testez uniquement les réseaux dont vous avez l'autorisation",
    "Le piratage de réseaux WiFi est illégal et punissable par la loi",
    "Utilisez cet outil de manière responsable et professionnelle",
]

# Wordlist de base pour les tests
BASE_WORDLIST = [
    # Mots de passe courants
    "admin", "password", "12345678", "qwerty", "abc123",
    "password123", "admin123", "root", "toor", "pass",
    "wifi", "network", "home", "guest", "default",
    
    # Patterns numériques
    "123456789", "987654321", "11111111", "00000000",
    "12341234", "56785678", "qwerty123", "password1",
    
    # Patterns avec dates
    "2023", "2024", "2025", "janvier", "fevrier",
    
    # Patterns géographiques
    "paris", "france", "maison", "domicile", "bureau",
]

# Caractères pour la génération de mots de passe
CHARACTER_SETS = {
    "low": string.ascii_lowercase + string.digits,
    "medium": string.ascii_letters + string.digits,
    "high": string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
}

# Scores de sécurité
SECURITY_LEVELS = {
    0: "Très faible",
    1: "Très faible", 
    2: "Faible",
    3: "Moyen",
    4: "Fort",
    5: "Très fort"
}

# Recommandations de sécurité
SECURITY_RECOMMENDATIONS = [
    "Utilisez un mot de passe d'au moins 12 caractères",
    "Combinez lettres majuscules, minuscules, chiffres et symboles",
    "Évitez les mots du dictionnaire et les informations personnelles",
    "Changez régulièrement votre mot de passe WiFi",
    "Activez le cryptage WPA3 si disponible",
    "Désactivez le WPS (WiFi Protected Setup)",
    "Utilisez un mot de passe différent pour chaque réseau",
    "Activez le filtrage MAC si possible",
    "Surveillez les connexions suspectes",
    "Maintenez votre routeur à jour",
]

# Codes de couleur pour la console
COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m", 
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "PURPLE": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "END": "\033[0m",
}

def get_config(key, default=None):
    """Récupère une valeur de configuration"""
    return CONFIG.get(key, default)

def set_config(key, value):
    """Définit une valeur de configuration"""
    CONFIG[key] = value

def validate_config():
    """Valide la configuration"""
    errors = []
    
    if CONFIG["MAX_TEST_COUNT"] > 100000:
        errors.append("MAX_TEST_COUNT trop élevé (max: 100000)")
    
    if CONFIG["TEST_DELAY"] < 0.001:
        errors.append("TEST_DELAY trop bas (min: 0.001)")
    
    if CONFIG["MIN_PASSWORD_LENGTH"] >= CONFIG["MAX_PASSWORD_LENGTH"]:
        errors.append("MIN_PASSWORD_LENGTH doit être < MAX_PASSWORD_LENGTH")
    
    return errors

def print_ethical_warning():
    """Affiche l'avertissement éthique"""
    if CONFIG["ETHICAL_WARNING"]:
        print("\n" + "="*60)
        print(COLORS["YELLOW"] + COLORS["BOLD"] + "⚠️  AVERTISSEMENT ÉTHIQUE IMPORTANT ⚠️" + COLORS["END"])
        print("="*60)
        for warning in ETHICAL_WARNINGS:
            print(f"• {warning}")
        print("="*60)
        print()

if __name__ == "__main__":
    # Test de configuration
    print("Test de configuration...")
    errors = validate_config()
    if errors:
        print("Erreurs de configuration:")
        for error in errors:
            print(f"  ❌ {error}")
    else:
        print("✅ Configuration valide")
    
    print_ethical_warning()
