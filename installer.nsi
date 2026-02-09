; Script d'installation pour WiFi Penetration Testing Tool
; Require NSIS (Nullsoft Scriptable Install System)

!define APPNAME "WiFi Penetration Testing Tool"
!define VERSION "2.0"
!define PUBLISHER "Pentester Éthique"
!define DESCRIPTION "Outil de test de sécurité WiFi éthique"

Name "${APPNAME} v${VERSION}"
OutFile "${APPNAME}_Setup_${VERSION}.exe"
InstallDir "$PROGRAMFILES\${APPNAME}"
RequestExecutionLevel admin

; Interface moderne
!include "MUI2.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

; Pages d'installation
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; Pages de désinstallation
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; Langue
!insertmacro MUI_LANGUAGE "French"

; Section d'installation
Section "MainSection" SEC01
    SetOutPath "$INSTDIR"
    
    ; Fichiers principaux
    File "dist\WiFiPenTest.exe"
    
    ; Dossiers
    File /r "reports"
    File /r "wordlists" 
    File /r "logs"
    
    ; Raccourcis
    CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\WiFiPenTest.exe"
    CreateShortCut "$STARTMENU\Programs\${APPNAME}.lnk" "$INSTDIR\WiFiPenTest.exe"
    
    ; Entrées de registre
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$INSTDIR\uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayVersion" "${VERSION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Publisher" "${PUBLISHER}"
    
    ; Créer le désinstallateur
    WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

; Section de désinstallation
Section "Uninstall"
    Delete "$INSTDIR\WiFiPenTest.exe"
    Delete "$INSTDIR\uninstall.exe"
    RMDir /r "$INSTDIR\reports"
    RMDir /r "$INSTDIR\wordlists"
    RMDir /r "$INSTDIR\logs"
    RMDir "$INSTDIR"
    
    Delete "$DESKTOP\${APPNAME}.lnk"
    Delete "$STARTMENU\Programs\${APPNAME}.lnk"
    
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
SectionEnd
