#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import tempfile
from os import environ

from PyQt4 import QtGui
from PyQt4 import QtCore

rc_file_name = environ.get('HOME') + '/.config/apt-notifierrc'
message_status = "not displayed"

def set_translations():
    script = '''#!/bin/sh
    locale|grep ^LANG=|cut -f2 -d=|cut -f1 -d_
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(["echo -n `sh %s`" % script_file.name],shell=True, stdout=subprocess.PIPE)
    locale = run.stdout.read(128)
    script_file.close()

    global tooltip_0_updates_available
    global tooltip_1_new_update_available
    global tooltip_multiple_new_updates_available
    global popup_title
    global popup_msg_1_new_update_available
    global popup_msg_multiple_new_updates_available_begin
    global popup_msg_multiple_new_updates_available_end
    global Upgrade_using_Synaptic
    global View_and_Upgrade
    global Hide_until_updates_available
    global Quit_Apt_Notifier
    global Apt_Notifier_Help
    global Synaptic_Help
    global Apt_Notifier_Preferences    
    global Apt_History
    global Check_for_Updates
    global Check_for_Updates_by_User
    Check_for_Updates_by_User = 'false'
    global ignoreClick
    ignoreClick = '0'
    global RepoListsHashNow
    RepoListsHashNow = ''
    global RepoListsHashPrevious
    RepoListsHashPrevious= ''
    global AptConfsAndPrefsNow
    AptConfsAndPrefsNow = ''
    global AptConfsAndPrefsPrevious
    AptConfsAndPrefsPrevious = ''
    global AptPkgCacheHashNow
    AptPkgCacheHashNow = ''
    global AptPkgCacheHashPrevious
    AptPkgCacheHashPrevious = ''
    global text
    text = ''

    tooltip_0_updates_available = u"0 updates available"
    tooltip_1_new_update_available = u"1 new update available"
    tooltip_multiple_new_updates_available = u" new updates available"
    popup_title = u"Updates"
    popup_msg_1_new_update_available = u"You have 1 new update available"
    popup_msg_multiple_new_updates_available_begin = u"You have "
    popup_msg_multiple_new_updates_available_end = u" new updates available"
    Upgrade_using_Synaptic = u"Upgrade using Synaptic"
    View_and_Upgrade = u"View and Upgrade"
    Hide_until_updates_available = u"Hide until updates available"
    Quit_Apt_Notifier = u"Quit Apt-Notifier"
    Apt_Notifier_Help = u"Apt-Notifier Help"
    Synaptic_Help = u"Synaptic Help"
    Apt_Notifier_Preferences = u"Apt Notifier Preferences"
    Apt_History = u"Apt History"
    Check_for_Updates = u"Check for Updates (apt-get update)"
    
    if locale == "ca":
        tooltip_0_updates_available = u"No hi ha actualitzacions disponibles"
        tooltip_1_new_update_available = u"1 actualització disponible"
        tooltip_multiple_new_updates_available = u" noves actualitzacions disponibles"
        popup_title = u"Actualitzacions"
        popup_msg_1_new_update_available = u"Teniu 1 actualització disponible"
        popup_msg_multiple_new_updates_available_begin = u"Teniu "
        popup_msg_multiple_new_updates_available_end = u" noves actualitzacions disponibles"
        Upgrade_using_Synaptic = u"Actualitza usant Synaptic"
        View_and_Upgrade = u"Veure i actualitzar"
        Hide_until_updates_available = u"Amagar fins que hi hagi actualitzacions disponibles"
        Quit_Apt_Notifier = u"Surt d'Apt-Notifier"
        Apt_Notifier_Help = u"Ajuda d'Apt-Notifier"
        Synaptic_Help = u"Ajuda de Synaptic"
        Apt_Notifier_Preferences = u"Preferències d'Apt Notifier"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"
        
    elif locale == "de":
        tooltip_0_updates_available = u"0 Updates verfügbar"
        tooltip_1_new_update_available = u"1 neues Update verfügbar"
        tooltip_multiple_new_updates_available = u" neue Updates verfügbar"
        popup_title = u"Updates"
        popup_msg_1_new_update_available = u"Sie haben ein neues Update verfügbar"
        popup_msg_multiple_new_updates_available_begin = u"Sie haben "
        popup_msg_multiple_new_updates_available_end = u" neue Updates verfügbar"
        Upgrade_using_Synaptic = u"Durch Synaptic aufrüsten"
        View_and_Upgrade = u"Anschauen and aufrüsten"
        Hide_until_updates_available = u"Verstercken bis Updates verfügbar"
        Quit_Apt_Notifier = u"Apt-Notifier abbrechen "
        Apt_Notifier_Help = u"Apt-Notifier Hilfe"
        Synaptic_Help = u"Synaptic Hilfe"
        Apt_Notifier_Preferences = u"Apt Notifier Einstellungen"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "el":
        tooltip_0_updates_available = u"0 διαθέσιμες ενημερώσεις"
        tooltip_1_new_update_available = u"0 διαθέσιμες ενημερώσεις"
        tooltip_multiple_new_updates_available = u" νέες διαθέσιμες ενημερώσεις"
        popup_title = u"Ενημερώσεις"
        popup_msg_1_new_update_available = u"Έχετε 1 νέα διαθέσιμη ενημέρωση"
        popup_msg_multiple_new_updates_available_begin = u"Έχετε "
        popup_msg_multiple_new_updates_available_end = u" νέες διαθέσιμες ενημερώσεις"
        Upgrade_using_Synaptic = u"Αναβάθμιση χρησιμοποιώντας το Synaptic"
        View_and_Upgrade = u"Προβολή και Αναβάθμιση"
        Hide_until_updates_available = u"Απόκρυψη μέχρι διαθέσιμες ενημερώσεις"
        Quit_Apt_Notifier = u"Κλείστε το Apt-Notifier"
        Apt_Notifier_Help = u"Apt-Notifier Βοήθεια"
        Synaptic_Help = u"Synaptic Βοήθεια"
        Apt_Notifier_Preferences = u"Apt Notifier Προτιμήσεις"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "es":
        tooltip_0_updates_available = u"0 actualizaciones disponibles"
        tooltip_1_new_update_available = u"1 nueva actualización disponible"
        tooltip_multiple_new_updates_available = u" nuevas actualizaciones disponibles"
        popup_title = u"Updates"
        popup_msg_1_new_update_available = u"Tiene 1 nueva actualización disponible"
        popup_msg_multiple_new_updates_available_begin = u"Tiene "
        popup_msg_multiple_new_updates_available_end = u" nuevas actualizaciones disponibles"
        Upgrade_using_Synaptic = u"Actualizar usando Synaptic"
        View_and_Upgrade = u"Ver y Actualizar"
        Hide_until_updates_available = u"Ocultar hasta que haya actualizaciones"
        Quit_Apt_Notifier = u"Salir de Apt-Notifier"
        Apt_Notifier_Help = u"Ayuda de Apt-Notifier"
        Synaptic_Help = u"Ayuda de Synaptic"
        Apt_Notifier_Preferences = u"Preferencias de Apt Notifier"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "fr":
        tooltip_0_updates_available = u"0 mises à jour disponibles"
        tooltip_1_new_update_available = u"1 nouvelle mise à jour disponible"
        tooltip_multiple_new_updates_available = u" nouvelles mises à jour disponibles"
        popup_title = u"Mises à jour"
        popup_msg_1_new_update_available = u"Vous avez une nouvelle mise à jour disponible"
        popup_msg_multiple_new_updates_available_begin = u"Vous avez "
        popup_msg_multiple_new_updates_available_end = u" nouvelles mises à jour disponibles"
        Upgrade_using_Synaptic = u"Mettre à niveau avec Synaptic"
        View_and_Upgrade = u"Voir et mettre à niveau"
        Hide_until_updates_available = u"Cacher jusqu'à ce que des mises à niveau soient disponibles"
        Quit_Apt_Notifier = u"Annuler Apt-Notifier"
        Apt_Notifier_Help = u"Aide sur Apt-Notifier"
        Synaptic_Help = u"Aide sur Synaptic"
        Apt_Notifier_Preferences = u"Préferences pour Apt Notifier"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "it":
        tooltip_0_updates_available = u"0 aggiornamenti disponibili"
        tooltip_1_new_update_available = u"1 nuovo aggiornamento disponibile"
        tooltip_multiple_new_updates_available = u" nuovi aggiornamenti disponibili"
        popup_title = u"Aggiornamenti"
        popup_msg_1_new_update_available = u"Hai 1 nuovo aggiornamento disponibile"
        popup_msg_multiple_new_updates_available_begin = u"Hai "
        popup_msg_multiple_new_updates_available_end = u" nuovi aggiornamenti disponibili"
        Upgrade_using_Synaptic = u"Aggiornare tramite Synaptic"
        View_and_Upgrade = u"Mostra e aggiorna"
        Hide_until_updates_available = u"Nascondi finchè non hai aggiornamenti disponibili"
        Quit_Apt_Notifier = u"Chiudi Apt-Notifier"
        Apt_Notifier_Help = u"Aiuto su Apt-Notifier"
        Synaptic_Help = u"Aiuto su Synaptic"
        Apt_Notifier_Preferences = u"Preferenze per Apt Notifier"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "ja":
        tooltip_0_updates_available = u"0 新たな更新はありません"
        tooltip_1_new_update_available = u"1 つの新たな更新が入手可能です"
        tooltip_multiple_new_updates_available = u"つの新たな更新が入手可能です"
        popup_title = u"更新"
        popup_msg_1_new_update_available = u"1 つの新たな更新が入手可能です"
        popup_msg_multiple_new_updates_available_begin = u""
        popup_msg_multiple_new_updates_available_end = u"つの新たな更新が入手可能です"
        Upgrade_using_Synaptic = u"更新に Synaptic を使用する"
        View_and_Upgrade = u"表示・更新"
        Hide_until_updates_available = u"入手可能な更新の非表示"
        Quit_Apt_Notifier = u"Apt-Notifier を終了"
        Apt_Notifier_Help = u"Apt-Notifier ヘルプ"
        Synaptic_Help = u"Synaptic ヘルプ"
        Apt_Notifier_Preferences = u"Apt Notifier 設定"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "nl":
        tooltip_0_updates_available = u"0 updates beschikbaar"
        tooltip_1_new_update_available = u"1 nieuwe update beschikbaar"
        tooltip_multiple_new_updates_available = u" nieuwe updates beschikbaar"
        popup_title = u"Updates"
        popup_msg_1_new_update_available = u"U heeft 1 nieuwe update beschikbaar"
        popup_msg_multiple_new_updates_available_begin = u"U heeft "
        popup_msg_multiple_new_updates_available_end = u" nieuwe updates beschikbaar"
        Upgrade_using_Synaptic = u"Upgrade met gebruik van Synaptic"
        View_and_Upgrade = u"Bekijk en Upgrade"
        Hide_until_updates_available = u"Verberg totdat updates beschikbaar zijn"
        Quit_Apt_Notifier = u"Beëindig Apt-Notifier"
        Apt_Notifier_Help = u"Apt-Notifier Help"
        Synaptic_Help = u"Synaptic Help"
        Apt_Notifier_Preferences = u"Apt Notifier Voorkeuren"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "pl":
        tooltip_0_updates_available = u"0 Aktualizacje są dostępne"
        tooltip_1_new_update_available = u"1 Aktualizacja dostępna"
        tooltip_multiple_new_updates_available = u" Dostępne nowe aktualizacje"
        popup_title = u"Aktualizacje"
        popup_msg_1_new_update_available = u"Dostępna jest nowa aktualizacja"
        popup_msg_multiple_new_updates_available_begin = u"Masz dostępnych "
        popup_msg_multiple_new_updates_available_end = u" nowych aktualizacji"
        Upgrade_using_Synaptic = u"Aktualizuj korzystając z Synaptic"
        View_and_Upgrade = u"Przeglądaj i Aktualizować"
        Hide_until_updates_available = u"Ukryj aż będą dostępne aktualizacje"
        Quit_Apt_Notifier = u"Wyjdź z Apt-Notifier"
        Apt_Notifier_Help = u"Pomoc Apt-Notifier"
        Synaptic_Help = u"Pomoc Synaptic"
        Apt_Notifier_Preferences = u"Apt Notifier Ustawienia"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "ru":
        tooltip_0_updates_available = u"Нет доступных обновлений"
        tooltip_1_new_update_available = u"1 обновление доступно"
        tooltip_multiple_new_updates_available = u" обновлений доступно"
        popup_title = u"Обновления"
        popup_msg_1_new_update_available = u"Имеется одно доступное обновление"
        popup_msg_multiple_new_updates_available_begin = u"Имеется "
        popup_msg_multiple_new_updates_available_end = u" доступных обновлений"
        Upgrade_using_Synaptic = u"Обновить, используя Synaptic"
        View_and_Upgrade = u"Просмотр и обновление"
        Hide_until_updates_available = u"Не показывать, если нет обновлений"
        Quit_Apt_Notifier = u"Выйти из Apt-Notifier"
        Apt_Notifier_Help = u"Apt Notifier Помощь"
        Synaptic_Help = u"Synaptic Помощь"
        Apt_Notifier_Preferences = u"Настройки Apt Notifier"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    elif locale == "sv":
        tooltip_0_updates_available = u"0 uppdateringar tillgängliga"
        tooltip_1_new_update_available = u"1 ny updatering tillgänglig"
        tooltip_multiple_new_updates_available = u" nya uppdateringar tillgängliga"
        popup_title = u"Updateringar"
        popup_msg_1_new_update_available = u"Du har 1 ny uppdatering tillgänglig"
        popup_msg_multiple_new_updates_available_begin = u"Du har "
        popup_msg_multiple_new_updates_available_end = u" nya uppdatering tillgänglig"
        Upgrade_using_Synaptic = u"Uppgradera med Synaptic"
        View_and_Upgrade = u"Granska och Uppgradera"
        Hide_until_updates_available = u"Göm tills uppdateringar är tillgängliga"
        Quit_Apt_Notifier = u"Avsluta Apt-Notifier"
        Apt_Notifier_Help = u"Apt-Notifier Hjälp"
        Synaptic_Help = u"Synaptic Hjälp"
        Apt_Notifier_Preferences = u"Apt Notifier Inställningar"
        Apt_History = u"Apt History"
        Check_for_Updates = u"Check for Updates (apt-get update)"

    else:
        pass

# Check for updates, using subprocess.Popen
def check_updates():
    global message_status
    global text
    global RepoListsHashNow
    global RepoListsHashPrevious
    global AptConfsAndPrefsNow
    global AptConfsAndPrefsPrevious
    global AptPkgCacheHashNow
    global AptPkgCacheHashPrevious
    global Check_for_Updates_by_User
    
    """
    Don't bother checking for updates when /var/lib/apt/periodic/update-stamp
    isn't present. This should only happen in a Live session before the repository
    lists have been loaded for the first time.
    """ 
    command_string = "[ ! -e /var/lib/apt/periodic/update-stamp ]"
    exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
    if exit_state == 0:
        if text == '':
            text = '0'
        message_status = "not displayed"  # Resets flag once there are no more updates
        add_hide_action()
        if icon_config != "show":
            AptIcon.hide()
        else:
            AptIcon.setIcon(NoUpdatesIcon)
            AptIcon.setToolTip(tooltip_0_updates_available)
        return
    
    """
    Don't bother checking for updates if processes for other package management tools
    appear to be runninng.
    """ 
    command_string = "ps aux | grep -v grep | grep -E 'apt-get|aptitude|dpkg|gdebi|synaptic' -q"
    exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
    if exit_state == 0:
        return
    
    """
    Get a hash of the /var/lib/apt/lists folder.
    """
    script = '''#!/bin/sh
    find /var/lib/apt/lists/* 2>/dev/null | xargs md5sum 2>/dev/null | md5sum
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(["echo -n `bash %s`" % script_file.name],shell=True, stdout=subprocess.PIPE)
    RepoListsHashNow = run.stdout.read(128)
    script_file.close()

    """
    Get a hash of the /etc/apt/conf file and files in the .d folder,
    and /etc/apt/preferences file and files in the .d folder.
    """    
    script = '''#!/bin/sh
    find /etc/apt/{apt.conf*,preferences*} 2>/dev/null | grep -v .d$ | xargs md5sum  2>/dev/null | md5sum
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(["echo -n `bash %s`" % script_file.name],shell=True, stdout=subprocess.PIPE)
    AptConfsAndPrefsNow = run.stdout.read(128)
    script_file.close()
    
    """
    Get a hash of /var/cache/apt/pkgcache.bin.
    """    
    script = '''#!/bin/sh
    md5sum  /var/cache/apt/pkgcache.bin 2>/dev/null | md5sum
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(["echo -n `bash %s`" % script_file.name],shell=True, stdout=subprocess.PIPE)
    AptPkgCacheHashNow = run.stdout.read(128)
    script_file.close()

    """
    If
        no changes in the Repo List hashes since last checked
            AND 
        the Apt Conf & Apt Preferences hashes same since last checked
            AND
        pkgcache.bin same since last checked
            AND
        the call to check_updates wasn't initiated by user   
    then don't bother checking for updates.
    """
    if RepoListsHashNow == RepoListsHashPrevious:
        if AptConfsAndPrefsNow == AptConfsAndPrefsPrevious:
            if AptPkgCacheHashNow == AptPkgCacheHashPrevious:
                if Check_for_Updates_by_User == 'false':
                    if text == '':
                        text = '0'
                    return

    RepoListsHashPrevious = RepoListsHashNow
    RepoListsHashNow = ''

    AptConfsAndPrefsPrevious = AptConfsAndPrefsNow
    AptConfsAndPrefsNow = ''
    
    AptPkgCacheHashPrevious = AptPkgCacheHashNow
    AptPkgCacheHashNow = ''
    
    Check_for_Updates_by_User = 'false'
    
    #Create an inline script (what used to be /usr/bin/apt-notifier-check-Updates) and then run it to get the number of updates.
    script = '''#!/bin/sh
    sorted_list_of_upgrades() 
    {
        #Create a sorted list of the names of the packages that are upgradeable.
        LC_ALL=en_US apt-get -o 'Debug::NoLocking=true' --trivial-only -V $(grep ^UpgradeType ~/.config/apt-notifierrc | cut -f2 -d=) 2>/dev/null \
        |  sed -n '/upgraded:/,$p' | grep ^'  ' | awk '{ print $1 }' | sort
    }
    
    #suppress updates available indication if 2 or more Release.reverify entries found
    #if [ $(ls -1 /var/lib/apt/lists/partial/ | grep Release.reverify$ | wc -l) -ge 2 ]; then echo 0; exit; fi 
    
    if [ -s /var/lib/synaptic/preferences ]; 
        then 
            #/var/lib/synaptic/preferences is a non-zero size file, which means there are packages pinned in Synaptic. 
            #Remove from the sorted_list_of_upgrades, packages that are pinned in Synaptic, and then get a count of remaining.
            
            sorted_list_of_upgrades | grep -vx $(grep 'Package:' /var/lib/synaptic/preferences 2>/dev/null | awk {'print "-e " $2'}) | wc -l
        
        else 
            #/var/lib/synaptic/preferences is either a zero byte file, meaning packages were pinned in Synaptic at some time in 
            # the past but none are currently pinned. Or the file is not present, meaning packages have never been pinned using 
            # Synaptic. In either case, just get a count of how many upgradeable packages are in the list.
            
            sorted_list_of_upgrades | wc -l
    fi
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(["echo -n `sh %s`" % script_file.name],shell=True, stdout=subprocess.PIPE)
    # Read the output into a text string
    text = run.stdout.read(128)
    script_file.close()

    # Alter both Icon and Tooltip, depending on updates available or not 
    if text == "0":
        message_status = "not displayed"  # Resets flag once there are no more updates
        add_hide_action()
        if icon_config != "show":
            AptIcon.hide()
        else:
            AptIcon.setIcon(NoUpdatesIcon)
            AptIcon.setToolTip(tooltip_0_updates_available)
    else:
        if text == "1":
            AptIcon.setIcon(NewUpdatesIcon)
            AptIcon.show()
            AptIcon.setToolTip(tooltip_1_new_update_available)
            add_rightclick_actions()
            # Shows the pop up message only if not displayed before 
            if message_status == "not displayed":
                def show_message():
                    AptIcon.showMessage(popup_title, popup_msg_1_new_update_available)
                Timer.singleShot(1000, show_message)
                message_status = "displayed"
        else:
            AptIcon.setIcon(NewUpdatesIcon)
            AptIcon.show()
            AptIcon.setToolTip(text + tooltip_multiple_new_updates_available)
            add_rightclick_actions()
            # Shows the pop up message only if not displayed before 
            if message_status == "not displayed":
                def show_message():
                    AptIcon.showMessage(popup_title, popup_msg_multiple_new_updates_available_begin + text + popup_msg_multiple_new_updates_available_end)
                Timer.singleShot(1000, show_message)
                message_status = "displayed"
   
def start_synaptic():
    global Check_for_Updates_by_User
    run = subprocess.Popen(['/usr/bin/su-to-root -X -c synaptic'],shell=True).wait()
    Check_for_Updates_by_User = 'true'
    check_updates()

def viewandupgrade():
    global Check_for_Updates_by_User
    initialize_aptnotifier_prefs()
    script = '''#!/bin/bash
    
    #cancel updates available indication if 2 or more Release.reverify entries found
    #if [ $(ls -1 /var/lib/apt/lists/partial/ | grep Release.reverify$ | wc -l) -ge 2 ]; then exit; fi 


             window_title="MX Apt Notifier--View and Upgrade, previewing: apt-get "
             use_apt_get_dash_dash_yes="use apt-get's --yes option for "
             auto_close_term_window1="automatically close terminal window when apt-get "
             auto_close_term_window2=" complete"
             switch_to1="switch to 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Reload"
             reload_tooltip="Reload the package information to become informed about new, removed or upgraded software packages. \n(apt-get update)"
             rootPasswordRequestMsg="The action you requested needs <b>root privileges</b>. Please enter <b>root's</b> password below."
             done0="" 
             done1=' complete (or was canceled)"' 
             done2="'this terminal window can now be closed '" 
             done3="'(press any key to close)'"
             autoremovable_packages_msg1="Unneeded packages are installed that can be removed."
             autoremovable_packages_msg2="'Running apt-get autoremove, if you are unsure type "'"'"n"'"'".'"

    case $(locale|grep ^LANG=|cut -f2 -d=|cut -f1 -d_) in

      ca)    window_title="MX Apt Notifier--Veure i actualitzar, vista prèvia: apt-get "
             use_apt_get_dash_dash_yes="usa l'opció d'apt-get --yes per a "
             auto_close_term_window1="tanca automàticament la finestra del terminal quan s'ha completat apt-get "
             auto_close_term_window2=""
             switch_to1="canvia a 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Refresca"
             reload_tooltip="Refresqueu la informació dels paquets per a informar-vos de paquets de programari nous, eliminats o actualitzats. \n(apt-get update)"
             rootPasswordRequestMsg="A l'acció que heu demanat li calen <b>privilegis de root</b>. Si us plau, introduïu la contrasenya de <b>root</b> tot seguit."
             done0="s'ha completat (o cancel·lat) "
             done1='"'
             done2="'ara podeu tancar la finestra '"
             done3="'(prement qualsevol tecla)'"
             autoremovable_packages_msg1="Unneeded packages are installed that can be removed."
             autoremovable_packages_msg2="'Running apt-get autoremove, if you are unsure type "'"'"n"'"'".'"
             ;;

      de)    window_title="MX Apt Notifier--Anschauen and aufrüsten, vorprüfend: apt-get "
             use_apt_get_dash_dash_yes="Option --yes von apt-get's benutzen bei "
             auto_close_term_window1="Shellfenster automatiisch schliessen nach Ende von apt-get "
             auto_close_term_window2=""
             switch_to1="Zu 'apt-get "
             switch_to2=" wechseln"
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Neu laden"
             reload_tooltip="Die Paketinformationen neu laden, um über neue, entfernte oder aktualisierte Softwarepakete informiert zu werden. \n(apt-get update)"
             rootPasswordRequestMsg="Die Aktion benötigt <b>Systemverwalterrechte</b>. Bitte geben Sie das Passwort des Benutzers <b>root</b> ein."
             done0=""
             done1=' fertig (oder beendet)"'
             done2="'Dieses Shellfenster darf jetzt geschlossen werden '" 
             done3="'(drücken Sie eine beliebige Taste zu schliessen)'"
             autoremovable_packages_msg1="Unnötige Pakete sind installiert, die entfernt werden können"
             autoremovable_packages_msg2="'Apt-get autoremove wird ausgeführt, tippen Sie "'"'"n"'"'" wenn unsicher.'"
             ;;

      el)    window_title="MX Apt Notifier--Προβολή και Αναβάθμιση, προεπισκόπηση: apt-get "
             use_apt_get_dash_dash_yes="χρησιμοποιήσετε την επιλογή του apt-get --yes option για την "
             auto_close_term_window1="Να κλείσει αυτόματα το παράθυρο τερματικού όταν το apt-get "
             auto_close_term_window2=" έχει ολοκληρωθεί"
             switch_to1="αλλαγή σε 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Ανανέωση"
             reload_tooltip="Ανανέωση των πληροφοριών του πακέτου ώστε να γίνει ενημέρωση για νέα, αναβαθμισμένα ή απομακρυθέντα πακέτα λογισμικού. \n(apt-get update)"
             rootPasswordRequestMsg="Η ενέργεια που ζητήσατε απαιτεί <b>προνόμια root</b>. Παρακαλώ εισάγετε τον κωδικό πρόσβασης του <b>root</b> παρακάτω."
             done0="" 
             done1=' ολοκληρώθηκε (ή ακυρώθηκε)"' 
             done2="'Αυτό το παράθυρο τερματικού μπορεί να κλείσει '" 
             done3="'(πατήστε οποιοδήποτε πλήκτρο να κλείσει)'"
             autoremovable_packages_msg1="Περιττά εγκαταστημένα πακέτα που μπορεί να αφαιρεθούν"
             autoremovable_packages_msg2="'Εκτέλεση του apt-get autoremove, αν δεν είστε σίγουροι, πληκτρολογήστε "'"'"ο"'"'".'"
             ;;

      es)    window_title="MX Apt Notifier--Ver y Actualizar, vista previa: apt-get "
             use_apt_get_dash_dash_yes="usar la opción --yes de apt-get para "
             auto_close_term_window1="Cerrar automáticamente la terminal cuando se completa apt-get "
             auto_close_term_window2=""
             switch_to1="cambiar a 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Recargar"
             reload_tooltip="Recargar la información de los paquetes para informarse acerca de los paquetes de software nuevos, eliminados o actualizados. \n(apt-get update)"
             rootPasswordRequestMsg="La acción que solicitó necesita <b>privilegios de superusuario</b> («root»). Introduzca la contraseña del <b>superusuario</b>."
             done0="se completó "
             done1=' (o se canceló)"' 
             done2="'esta ventana de terminal ya puede cerrarse '" 
             done3="'(oprima cualquier tecla para cerrarla)'" 
             autoremovable_packages_msg1="Los paquetes instalados pero no necesitados pueden ser removidos."
             autoremovable_packages_msg2="'Ejecutando apt-get autoremove; si no está seguro, ingrese "'"'"n"'"'".'"
             ;;

      fr)    window_title="MX Apt Notifier--Voir et mettre à niveau, survol du programme apt-get "
             use_apt_get_dash_dash_yes="utiliser l'option --yes de apt-get pour "
             auto_close_term_window1="fermer automatiquement la fenêtre de terminal quand apt-get "
             auto_close_term_window2=" se termine"
             switch_to1="passer à apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Recharger"
             reload_tooltip="Recharger les informations des paquets pour être informé des nouveaux paquets, des suppressions de paquets ou des paquets mis à jour. \n(apt-get update)"
             rootPasswordRequestMsg="L'action requise nécessite <b>les droits du superutilisateur</b>. Veuillez saisir ci-dessous le mot de passe du <b>superutilisateur</b>."
             done0=""
             done1=" s'est terminé (ou a été annulé)"'"' 
             done2="'vous pouvez maintenant fermer cette fenêtre de terminal '" 
             done3='"(appuyez sur n'"'"'importe quelle touche pour fermer)"'
             autoremovable_packages_msg1="Il existe des paquets installés superflus; on peut les mettre au rebut."
             autoremovable_packages_msg2="'On lancera apt-get autoremove; si vous n'êtes pas certain, tapez le "'"'"n"'"'".'"
             ;;

      it)    window_title="MX Apt Notifier--Mostra e Aggiorna, presentazione di: apt-get "
             use_apt_get_dash_dash_yes="usare l'opzione --yes di apt-get per l' "
             auto_close_term_window1="chiudere automaticamente la finestra del terminale quando apt-get "
             auto_close_term_window2=" ha terminato"
             switch_to1="passare a 'apt-get upgrade"
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Aggiorna"
             reload_tooltip="Aggiorna le informazioni sui pacchetti per informare di pacchetti nuovi, rimossi o aggiornati. \n(apt-get update)"
             rootPasswordRequestMsg="L'azione che hai richiesto richiede i <b>privilegi di root</b>. Per piacere, inserisci la password di <b>root</b>."
             done0=""
             done1=' ha terminato (o è stato annullato)"'
             done2="'Ora è possibile chiudere questa finestra del terminale '"
             done3="'(premi un tasto qualsiasi per chiudere)'"
             autoremovable_packages_msg1="I pacchetti installati non necessari possono essere rimossi."
             autoremovable_packages_msg2="'Si sta per avviare apt-get autoremove, se non sei sicuro digita "'"'"n"'"'".'"
             ;;

      ja)    window_title="MX Apt Notifier--表示・更新 これを試す: apt-get "
             use_apt_get_dash_dash_yes="で apt-get's --yes オプションを使用する "
             auto_close_term_window1="apt-get "
             auto_close_term_window2=" が完了した後自動的に端末ウインドウを閉じる"
             switch_to1="'apt-get "
             switch_to2=" へ切り替える"
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="再読込"
             reload_tooltip="新規、削除あるいはアップグレードされたパッケージについて情報が得られるように、パッケージ情報を再読込してください。 \n(apt-get update)"
             rootPasswordRequestMsg="実行には <b>root</b> 権限が必要です。下に <b>root</b> のパスワードを入力してください。"
             done0="" 
             done1=' 完了 (またはキャンセル)時に"' 
             done2="'この端末ウインドウを閉じる '" 
             done3="'(何かキーを押して閉じる)'"
             autoremovable_packages_msg1="Unneeded packages are installed that can be removed."
             autoremovable_packages_msg2="'Running apt-get autoremove, if you are unsure type "'"'"n"'"'".'"
             ;;

      nl)    window_title="MX Apt Notifier--Bekijk en Upgrade, voorbeeld: apt-get "
             use_apt_get_dash_dash_yes="gebruik apt-get's --yes optie voor "
             auto_close_term_window1="automatisch terminal scherm sluiten wanneer apt-get "
             auto_close_term_window2=" klaar is"
             switch_to1="wijzig naar 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Herladen"
             reload_tooltip="Ververs de pakketinformatie om ingelicht te worden over nieuwe, verwijderde of opgewaardeerde pakketten. \n(apt-get update)"
             rootPasswordRequestMsg="Voor de handeling die u wilt verrichten hebt u <b>root-privileges</b> nodig. Voer hieronder het <b>root-wachtwoord</b> in."
             done0="" 
             done1=' klaar (of was geannuleerd)"' 
             done2="'dit terminal scherm kan nu gesloten worden '" 
             done3="'(druk op een toets om te sluiten)'"
             autoremovable_packages_msg1="Onnodige pakketten die zijn geïnstalleerd en kunnen worden verwijderd."
             autoremovable_packages_msg2="'Uitvoeren apt-get autoremove, als je niet zeker bent tik "'"'"n"'"'".'"
             ;;

      pl)    window_title="MX Apt Notifier--Przeglądaj i Aktualizować, podglądu: apt-get "
             use_apt_get_dash_dash_yes="stosować apt-get --yes opcję  dla "
             auto_close_term_window1="zostały automatycznie zamknięte okno terminalu przy apt-get "
             auto_close_term_window2=" gotowy"
             switch_to1="Przełącz na 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Odśwież"
             reload_tooltip="Odświeża bazę informacji o pakietach, aby otrzymać informacje o nowych, usuniętych, zaktualizowanych pakietach oprogramowania. \n(apt-get update)"
             rootPasswordRequestMsg="Polecenie, które chcesz wykonać, wymaga <b>uprawnień administratora</b>. Wpisz poniżej <b>hasło administratora</b>."
             done0="Komenda " 
             done1=' została wykonana (lub przerwana)"' 
             done2="'Okno to można zamknąć teraz '" 
             done3="'(naciśnij dowolny klawisz, aby zamknąć)'"
             autoremovable_packages_msg1="Unneeded packages are installed that can be removed."
             autoremovable_packages_msg2="'Running apt-get autoremove, if you are unsure type "'"'"n"'"'".'"
             ;;

      ru)    window_title="MX Apt Notifier--Просмотр и обновление, предпросмотр: apt-get "
             use_apt_get_dash_dash_yes="Использовать опцию apt-get's --yes для "
             auto_close_term_window1="Автоматически закрыть окно терминала после выполнения apt-get "
             auto_close_term_window2=""
             switch_to1="Перейти к 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Обновить"
             reload_tooltip="Обновление сведений о пакетах информирует о новых, удалённых или обновлённых пакетах программ \n(apt-get update)"
             rootPasswordRequestMsg="Для выполнения данного действия необходимы <b>привилегии пользователя «root»</b>. Введите его пароль."
             done0="" 
             done1=' Выполнено (или было отменено)"' 
             done2="'Это окно терминала теперь может быть закрыто '" 
             done3="'(нажмите любую клавишу, чтобы закрыть)'"
             autoremovable_packages_msg1="Более ненужные установленные пакеты могут быть удалены."
             autoremovable_packages_msg2="'Запуск apt-get autoremove, если вы не уверены, нажмите "'"'"n"'"'".'" 
             ;;

      sv)    window_title="MX Apt Notifier--Granska och Uppgradera, förhandsgranskning: apt-get "
             use_apt_get_dash_dash_yes="använd apt-get's --yes möjlighet för "
             auto_close_term_window1="stäng automatiskt terminalfönstret när apt-get "
             auto_close_term_window2=" är slutförd"
             switch_to1="byt till 'apt-get "
             switch_to2=""
             switch_tooltip="Switches the type of Upgrade that will be performed, alternating back and forth between \n'apt-get upgrade' and 'apt-get dist-upgrade'"
             reload="Läs om"
             reload_tooltip="Läs om paketinformationen för att få information om nya, borttagna eller uppgraderade programpaket. \n(apt-get update)"
             rootPasswordRequestMsg="Åtgärden du har begärt kräver <b>administratörsbehörighet</b>. Ange lösenordet för <b>root</b>nedan."
             done0="" 
             done1=' färdig (eller stoppades)"' 
             done2="'detta terminalfönster kan nu stängas '" 
             done3="'(tryck på valfri tangent för att stänga)'"
             autoremovable_packages_msg1="Onödiga paket som är installerade och kan tas bort."
             autoremovable_packages_msg2="'Kör apt-get autoremove, om du är osäker skriv "'"'"n"'"'".'"
             ;;

       *)    : ;;

    esac

    RunAptScriptInTerminal(){
    #for MEPIS remove "MX" branding from the $window_title string
    window_title=$(echo "$1"|sed 's/MX /'$(grep -o MX-[1-9][0-9] /etc/issue|cut -c1-2)" "'/')

        TermXOffset="$(xwininfo -root|awk '/Width/{print $2/4}')"
        TermYOffset="$(xwininfo -root|awk '/Height/{print $2/4}')"
        G=" --geometry=80x25+"$TermXOffset"+"$TermYOffset
        I=" --icon=mnotify-some"
        if [ "$2" = "" ]; then T=""; I=""; else T=" --title='""$(grep -o MX-[1-9][0-9] /etc/issue|cut -c1-2)"" apt-notifier: apt-get "$2"'"; fi
        if (xprop -root | grep -q -i kde)
          then

            # Running KDE
            #
            # Can't get su-to-root to work in newer KDE's, so use kdesu for 
            # authentication.
            #  
            # If x-terminal-emulator is set to xfce4-terminal.wrapper, use     
            # xfce4-terminal instead because the --hold option doesn't work with
            # the wrapper. Also need to enclose the apt-get command in single 
            # quotes.
            #
            # If x-terminal-emulator is set to xterm, use konsole instead, if 
            # it's available (it should be).

            case $(readlink -e /usr/bin/x-terminal-emulator | xargs basename) in

              gnome-terminal.wrapper) if [ -e /usr/bin/konsole ]
                                        then
                                          $(kde4-config --path libexec)kdesu -c "konsole -e $3"
                                          sleep 5
                                          while [ "$(ps aux | grep [0-9]' konsole -e apt-get update')" != "" ]
                                            do
                                              sleep 1
                                            done
                                          sleep 1 
                                        else
                                          :
                                      fi
                                      ;;

                             konsole) $(kde4-config --path libexec)kdesu -c "konsole -e $3"
                                      sleep 5
                                      while [ "$(ps aux | grep [0-9]' konsole -e apt-get update')" != "" ]
                                        do
                                          sleep 1
                                        done
                                      sleep 1 
                                      ;;

                             roxterm) $(kde4-config --path libexec)kdesu -c "roxterm$G$T --separate -e $3"
                                      ;;

              xfce4-terminal.wrapper) $(kde4-config --path libexec)kdesu -n --noignorebutton -d -c "xfce4-terminal$G$I$T -e $3"
                                      ;;

                               xterm) if [ -e /usr/bin/konsole ]
                                        then
                                          $(kde4-config --path libexec)kdesu -c "konsole -e $3"
                                          sleep 5
                                          while [ "$(ps aux | grep [0-9]' konsole -e apt-get update')" != "" ]
                                            do
                                              sleep 1
                                            done
                                          sleep 1 
                                        else
                                          $(kde4-config --path libexec)kdesu -c "xterm -e $3"
                                      fi
                                      ;;

                                   *) $(kde4-config --path libexec)kdesu -c "x-terminal-emulator -e $3"
                                      sleep 5
                                      while [ "$(ps aux | grep [0-9]' konsole -e apt-get update')" != "" ]
                                        do
                                          sleep 1
                                        done
                                      sleep 1 
                                      ;;
            esac

          else

            # Running a non KDE desktop
            # 
            # Use su-to-root for authentication, it should end up using gksu.
            # 
            # If x-terminal-emulator is set to xfce4-terminal.wrapper, use 
            # xfce4-terminal instead because the --hold option doesn't work
            # with the wrapper. Also need to enclose the apt-get command in
            # single quotes.
            #
            # If x-terminal-emulator is set to xterm, use xfce4-terminal 
            # instead, if it's available (it is in MX)

            case $(readlink -e /usr/bin/x-terminal-emulator | xargs basename) in

              gnome-terminal.wrapper) su-to-root -X -c "gnome-terminal$G$T -e $3"
                                      ;;

                             konsole) su-to-root -X -c "konsole -e $3"
                                      sleep 5
                                      while [ "$(ps aux | grep [0-9]' konsole -e apt-get update')" != "" ]
                                        do
                                          sleep 1
                                        done
                                      sleep 1 
                                      ;;

                             roxterm) su-to-root -X -c "roxterm$G$T --separate -e $3"
                                      ;;

              xfce4-terminal.wrapper) if [ -x $(whereis gksu | awk '{print $2}') ]
                                        then
                                          gksu -m "$rootPasswordRequestMsg""\n\n'apt-get $2'" "xfce4-terminal$G$I$T -e $3"
                                        else
                                          su-to-root -X -c "xfce4-terminal$G$I$T -e $3"
                                      fi                                      
                                      ;;

                               xterm) if [ -e /usr/bin/xfce4-terminal ]
                                        then
                                          su-to-root -X -c "xfce4-terminal$G$I$T -e $3"
                                        else
                                          su-to-root -X -c "xterm -e $3"
                                      fi
                                      ;;

                                   *) su-to-root -X -c "x-terminal-emulator -e $3"
                                      ;;

            esac
        fi
    }    
        
    DoUpgrade(){
      case $1 in
        0)
        BP="1"
        chmod +x $TMP/upgradeScript
        RunAptScriptInTerminal "$window_title" "$UpgradeType" "$TMP/upgradeScript"
        ;;

        2)
        BP="1"
        ;;
        
        4)
        BP="0"
        sed -i 's/UpgradeType='$UpgradeType'/UpgradeType='$OtherUpgradeType'/' ~/.config/apt-notifierrc
        ;;
        
        8)
        BP="0"
        #chmod +x $TMP/upgradeScript
        RunAptScriptInTerminal "" "update" "'apt-get update'"
        sleep 1
        ;;
        
        *)
        BP="1"
        ;;
        
       esac 
    }

    BP="0"
    while [ $BP != "1" ]
      do

        UpgradeType=$(grep ^UpgradeType ~/.config/apt-notifierrc | cut -f2 -d=)
        if [ "$UpgradeType" = "upgrade"      ]; then
          OtherUpgradeType="dist-upgrade"
        fi
        if [ "$UpgradeType" = "dist-upgrade" ]; then
          OtherUpgradeType="upgrade"
        fi
  
        UpgradeAssumeYes=$(grep ^UpgradeAssumeYes ~/.config/apt-notifierrc | cut -f2 -d=)
        UpgradeAutoClose=$(grep ^UpgradeAutoClose ~/.config/apt-notifierrc | cut -f2 -d=)
      
        TMP=$(mktemp -d /tmp/apt-notifier.XXXXXX)
        echo "apt-get $UpgradeType" > "$TMP"/upgrades
        
        #The following 40 or so lines (down to the "APT_CONFIG" line) create a temporary etc/apt folder and subfolders
        #that for the most part match the root owned /etc/apt folder and it's subfolders.
        #
        #A symlink to /var/synaptic/preferences symlink ("$TMP"/etc/apt/preferences.d/synaptic-pins) will be created
        #if there isn't one already (note: the non-root user wouldn't be able to create one in /etc/apt/preferences.d/).
        #
        #With a /var/synaptic/preferences symlink in place, no longer need to remove the lines with Synaptic pinned packages
        #from the "$TMP"/upgrades file to keep them from being displayed in the 'View and Upgrade' window, also no longer
        #need to correct the upgrades count after removing the lines with the pinned updates.
        
        #create the etc/apt/*.d subdirectories in the temporary directory ("$TMP")
        for i in $(find /etc/apt -name *.d); do mkdir -p "$TMP"/$(echo $i | cut -f2- -d/); done

        #create symlinks to the files in /etc/apt and it's subdirectories with exception of /etc/apt and /etc/apt/apt.conf  
        for i in $(find /etc/apt | grep -v -e .d$ -e apt.conf$ -e apt$); do ln -s $i "$TMP"/$(echo $i | cut -f2- -d/) 2>/dev/null; done

        #in etc/preferences test to see if there's a symlink to /var/lib/synaptic/preferences
        ls -l /etc/apt/preferences* | grep ^l | grep -m1 /var/lib/synaptic/preferences$ -q

        #if there isn't, create one if there are synaptic pinned packages
        if [ $? -eq 1 ]
          then
            if [ -s /var/lib/synaptic/preferences ]
              then ln -s /var/lib/synaptic/preferences "$TMP"/etc/apt/preferences.d/synaptic-pins 2>/dev/null
            fi
        fi

        #create a apt.conf in the temp directory by copying existing /etc/apt/apt.conf to it
        [ ! -e /etc/apt/apt.conf ] || cp /etc/apt/apt.conf "$TMP"/apt.conf

        #in apt.conf file set Dir to the path of the temp directory
        echo 'Dir "'"$TMP"'/";' >> "$TMP"/apt.conf
        #set Dir::State::* and Dir::Cache::* to the existing ones in /var/lib/apt, /var/lib/dpkg and /var/cache/apt
        echo 'Dir::State "/var/lib/apt/";' >> "$TMP"/apt.conf
        echo 'Dir::State::Lists "/var/lib/apt/lists/";' >> "$TMP"/apt.conf
        echo 'Dir::State::status "/var/lib/dpkg/status";' >> "$TMP"/apt.conf
        echo 'Dir::State::extended_states "/var/lib/apt/extended_states";' >> "$TMP"/apt.conf
        echo 'Dir::Cache "/var/cache/apt/";' >> "$TMP"/apt.conf
        echo 'Dir::Cache::Archives "/var/cache/apt/archives";' >> "$TMP"/apt.conf
        echo 'Dir::Cache::srcpkgcache "/var/cache/apt/srcpkgcache.bin";' >> "$TMP"/apt.conf
        echo 'Dir::Cache::pkgcache "/var/cache/apt/pkgcache.bin";' >> "$TMP"/apt.conf

        APT_CONFIG="$TMP"/apt.conf apt-get -o Debug::NoLocking=true --trivial-only -V $UpgradeType 2>/dev/null >> "$TMP"/upgrades

        #fix to display epochs
        #for i in $(grep [[:space:]]'=>'[[:space:]] "$TMP"/upgrades | awk '{print $1}')
        #do
        #  withoutEpoch="$(grep [[:space:]]$i[[:space:]] "$TMP"/upgrades | awk '{print $2}')"
        #  withEpoch="(""$(apt-cache policy $i | head -2 | tail -1 | awk '{print $NF}')"
        #  sed -i 's/'"$withoutEpoch"'/'"$withEpoch"'/' "$TMP"/upgrades
        #  withoutEpoch="$(grep [[:space:]]$i[[:space:]] "$TMP"/upgrades | awk '{print $4}')"
        #  withEpoch="$(apt-cache policy $i | head -3 | tail -1 | awk '{print $NF}')"")"
        #  sed -i 's/'"$withoutEpoch"'/'"$withEpoch"'/' "$TMP"/upgrades
        #done

        yad \
        --window-icon=/usr/share/icons/mnotify-some.png \
        --width=640 \
        --height=480 \
        --center \
        --title "$window_title$UpgradeType" \
        --form \
          --field :TXT "$(sed 's/^/  /' "$TMP"/upgrades)" \
          --field="$use_apt_get_dash_dash_yes$UpgradeType":CHK $UpgradeAssumeYes \
          --field="$auto_close_term_window1$UpgradeType$auto_close_term_window2":CHK $UpgradeAutoClose \
        --button "$switch_to1$OtherUpgradeType'$switch_to2"!!"$switch_tooltip":4 \
        --button 'apt-get '"$UpgradeType"!mnotify-some!:0 \
        --button "$reload"!reload!"$reload_tooltip":8 \
        --button gtk-cancel:2 \
        --buttons-layout=spread \
        2>/dev/null \
        > "$TMP"/results 

        echo $?>>"$TMP"/results

        # if the View and Upgrade yad window was closed by one of it's 4 buttons, 
        # then update the UpgradeAssumeYes & UpgradeAutoClose flags in the 
        # ~/.config/apt-notifierrc file to match the checkboxes
        if [ $(tail -n1 "$TMP"/results) -eq 0 ]||\
           [ $(tail -n1 "$TMP"/results) -eq 2 ]||\
           [ $(tail -n1 "$TMP"/results) -eq 4 ]||\
           [ $(tail -n1 "$TMP"/results) -eq 8 ];
          then
            if [ "$(head -n1 "$TMP"/results | rev | awk -F \| '{ print $3}' | rev)" = "TRUE" ];
              then
                grep UpgradeAssumeYes=true  ~/.config/apt-notifierrc -q || sed -i 's/UpgradeAssumeYes=false/UpgradeAssumeYes=true/' ~/.config/apt-notifierrc
              else
                grep UpgradeAssumeYes=false ~/.config/apt-notifierrc -q || sed -i 's/UpgradeAssumeYes=true/UpgradeAssumeYes=false/' ~/.config/apt-notifierrc
            fi
            if [ "$(head -n1 "$TMP"/results | rev | awk -F \| '{ print $2}' | rev)" = "TRUE" ];
              then
                grep UpgradeAutoClose=true  ~/.config/apt-notifierrc -q || sed -i 's/UpgradeAutoClose=false/UpgradeAutoClose=true/' ~/.config/apt-notifierrc
              else
                grep UpgradeAutoClose=false ~/.config/apt-notifierrc -q || sed -i 's/UpgradeAutoClose=true/UpgradeAutoClose=false/' ~/.config/apt-notifierrc
            fi
          else
            :
        fi

        # refresh UpgradeAssumeYes & UpgradeAutoClose 
        UpgradeAssumeYes=$(grep ^UpgradeAssumeYes ~/.config/apt-notifierrc | cut -f2 -d=)
        UpgradeAutoClose=$(grep ^UpgradeAutoClose ~/.config/apt-notifierrc | cut -f2 -d=)
        
        if [ $(tail -n1 "$TMP"/results) -eq 8 ];
          then
            # build a upgrade script to do a apt-get update
            echo "#!/bin/bash"> "$TMP"/upgradeScript
            echo "echo 'apt-get update'">> "$TMP"/upgradeScript
            echo "apt-get update">> "$TMP"/upgradeScript

          else
            # build a upgrade script to do the apt-get upgrade (or dist-upgrade)
            echo "#!/bin/bash"> "$TMP"/upgradeScript
            echo "echo 'apt-get '"$UpgradeType>> "$TMP"/upgradeScript
            echo 'find /etc/apt/preferences.d | grep -E synaptic-[0-9a-zA-Z]{6}-pins | xargs rm -f'>> "$TMP"/upgradeScript 
            echo 'if [ -f /var/lib/synaptic/preferences -a -s /var/lib/synaptic/preferences ]'>> "$TMP"/upgradeScript
            echo '  then '>> "$TMP"/upgradeScript
            echo '    SynapticPins=$(mktemp /etc/apt/preferences.d/synaptic-XXXXXX-pins)'>> "$TMP"/upgradeScript
            echo '    ln -sf /var/lib/synaptic/preferences "$SynapticPins" 2>/dev/null'>> "$TMP"/upgradeScript
            echo 'fi'>> "$TMP"/upgradeScript
            echo 'file "$SynapticPins" | cut -f2- -d" " | grep -e"broken symbolic link" -e"empty" -q '>> "$TMP"/upgradeScript
            echo 'if [ $? -eq 0 ]; then find /etc/apt/preferences.d | grep -E synaptic-[0-9a-zA-Z]{6}-pins | xargs rm -f; fi'>> "$TMP"/upgradeScript
            if [ "$UpgradeAssumeYes" = "true" ];
              then
                echo "apt-get --assume-yes -V "$UpgradeType>> "$TMP"/upgradeScript
              else
                echo "apt-get -V "$UpgradeType>> "$TMP"/upgradeScript
            fi
            grep ^CheckForAutoRemoves=true ~/.config/apt-notifierrc -q
            if [ $? -eq 0 ]
              then
                echo "echo">> "$TMP"/upgradeScript
                echo 'apt-get autoremove -s | grep ^Remv -q'>> "$TMP"/upgradeScript
                echo 'if [ $? -eq 0 ]; '>> "$TMP"/upgradeScript
                echo '  then'>> "$TMP"/upgradeScript
                echo 'echo '"$autoremovable_packages_msg1">> "$TMP"/upgradeScript
                echo 'echo '"$autoremovable_packages_msg2">> "$TMP"/upgradeScript
                echo 'apt-get autoremove -qV'>> "$TMP"/upgradeScript
                echo '  else'>> "$TMP"/upgradeScript
                echo '    :'>> "$TMP"/upgradeScript
                echo 'fi'>> "$TMP"/upgradeScript
              else
                :
            fi
            echo "echo">> "$TMP"/upgradeScript
            echo 'find /etc/apt/preferences.d | grep -E synaptic-[0-9a-zA-Z]{6}-pins | xargs rm -f'>> "$TMP"/upgradeScript
            if [ "$UpgradeAutoClose" = "true" ];
              then
                echo 'echo "'$done0'apt-get '$UpgradeType$done1>> "$TMP"/upgradeScript
                echo "echo">> "$TMP"/upgradeScript
                echo "sleep 1">> "$TMP"/upgradeScript
                echo "exit 0">> "$TMP"/upgradeScript
              else
                echo 'echo "'$done0'apt-get '$UpgradeType$done1>> "$TMP"/upgradeScript
                echo "echo">> "$TMP"/upgradeScript
                echo "echo -n $done2">> "$TMP"/upgradeScript
                echo "read -sn 1 -p $done3 -t 999999999">> "$TMP"/upgradeScript
                echo "echo">> "$TMP"/upgradeScript
                echo "exit 0">> "$TMP"/upgradeScript
            fi
        fi

        DoUpgrade $(tail -n1 "$TMP"/results)

        rm -rf "$TMP"

      done

    sleep 2
    PID=`pidof apt-get | cut -f 1 -d " "`
    if [ $PID ]; then
        while (ps -p $PID > /dev/null); do
            sleep 2
        done
    fi
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(['sh %s' % script_file.name],shell=True).wait()
    script_file.close()
    Check_for_Updates_by_User = 'true'
    check_updates()

def initialize_aptnotifier_prefs():

    """Create/initialize preferences in the ~/.config/apt-notifierrc file  """
    """if they don't already exist. Remove multiple entries and those that """
    """appear to be invalid.                                               """ 

    script = '''#! /bin/bash

    #test if ~/.config/apt-notifierrc contains a UpgradeType=* line and that it's a valid entry
    grep -q -e ^"UpgradeType=upgrade" -e^"UpgradeType=dist-upgrade" ~/.config/apt-notifierrc
    if [ "$?" -eq 0 ]
      then
      #contains a valid entry so do nothing
        :
      else
      #
      #if a UpgradeType=* line not present,
      #or not equal to "upgrade" or "dist-upgrade"
      #initially set it to "UpgradeType=dist-upgrade"
      #also delete multiple entries or what appears to be invalid entries
      sed -i '/.*UpgradeType.*/Id' ~/.config/apt-notifierrc 
      echo "UpgradeType=dist-upgrade">> ~/.config/apt-notifierrc
    fi

    #test if ~/.config/apt-notifierrc contains a UpgradeAssumeYes=* line and that it's a valid entry
    grep -q -e ^"UpgradeAssumeYes=true" -e^"UpgradeAssumeYes=false" ~/.config/apt-notifierrc
    if [ "$?" -eq 0 ]
      then
      #contains a valid entry so do nothing
        :
      else
      #
      #if a UpgradeAssumeYes=* line not present,
      #or not equal to "true" or "false"
      #initially set it to "UpgradeAssumeYes=false"
      #also delete multiple entries or what appears to be invalid entries
      sed -i '/.*UpgradeAssumeYes.*/Id' ~/.config/apt-notifierrc 
      echo "UpgradeAssumeYes=false">> ~/.config/apt-notifierrc
    fi

    #test if ~/.config/apt-notifierrc contains a UpgradeAutoClose=* line and that it's a valid entry
    grep -q -e ^"UpgradeAutoClose=true" -e^"UpgradeAutoClose=false" ~/.config/apt-notifierrc
    if [ "$?" -eq 0 ]
      then
      #contains a valid entry so do nothing
        :
      else
      #
      #if a UpgradeAutoClose=* line not present,
      #or not equal to "true" or "false"
      #intially set it to "UpgradeAutoClose=false"
      #also delete multiple entries or what appears to be invalid entries
      sed -i '/.*UpgradeAutoClose.*/Id' ~/.config/apt-notifierrc 
      echo "UpgradeAutoClose=false">> ~/.config/apt-notifierrc
    fi

    #test if ~/.config/apt-notifierrc contains a LeftClick=* line and that it's a valid entry
    grep -q -e ^"LeftClick=ViewAndUpgrade" -e^"LeftClick=Synaptic" ~/.config/apt-notifierrc
    if [ "$?" -eq 0 ]
      then
      #contains a valid entry so do nothing
        :
      else
      #
      #if a LeftClick line not present,
      #or not equal to "ViewAndUpgrade" or "Synaptic"
      #initially set it to "LeftClick=ViewAndUpgrade"
      #also delete multiple entries or what appears to be invalid entries
      sed -i '/.*LeftClick.*/Id' ~/.config/apt-notifierrc 
      echo "LeftClick=ViewAndUpgrade">> ~/.config/apt-notifierrc
    fi

    #test if ~/.config/apt-notifierrc contains a CheckForAutoRemoves=* line and that it's a valid entry
    grep -q -e ^"CheckForAutoRemoves=true" -e^"CheckForAutoRemoves=false" ~/.config/apt-notifierrc
    if [ "$?" -eq 0 ]
      then
      #contains a valid entry so do nothing
        :
      else
      #
      #if a CheckForAutoRemoves=* line not present,
      #or not equal to "true" or "false"
      #intially set it to "CheckForAutoRemoves=false"
      #also delete multiple entries or what appears to be invalid entries
      sed -i '/.*CheckForAutoRemoves.*/Id' ~/.config/apt-notifierrc 
      echo "CheckForAutoRemoves=false">> ~/.config/apt-notifierrc
    fi

    #test to see if ~/.config/apt-notifierrc contains any blank lines or lines with only whitespace
    grep -q ^[[:space:]]*$ ~/.config/apt-notifierrc 
    if [ "$?" = "0" ]
      then
      #cleanup any blank lines or lines with only whitespace
        sed -i '/^[[:space:]]*$/d' ~/.config/apt-notifierrc
      else
      #no blank lines or lines with only whitespace so do nothing
        :
    fi

    '''

    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(['sh %s' % script_file.name],shell=True).wait()
    script_file.close()

def aptnotifier_prefs():
    global Check_for_Updates_by_User
    initialize_aptnotifier_prefs()
    script = '''#! /bin/bash

             window_title="MX Apt Notifier preferences"
             frame_upgrade_behaviour="Upgrade behaviour   (also affects notification count)   "
             frame_left_click_behaviour="Left-click behaviour   (when updates are available)   "
             frame_other_options="Other options"
             left_click_Synaptic="opens Synaptic "
             left_click_ViewandUpgrade='opens MX Apt Notifier "View and Upgrade" window'
             use_apt_get_dash_dash_yes="use apt-get's --yes option for upgrade/dist-upgrade"
             auto_close_term_window_when_complete="automatically close terminal window when apt-get upgrade/dist-upgrade complete"
             check_for_autoremoves="check for autoremovable packages after apt-get upgrade/dist-upgrade"

    case $(locale|grep ^LANG=|cut -f2 -d=|cut -f1 -d_) in

         ca) window_title="Preferències de MX Apt Notifier"
             frame_upgrade_behaviour="Comportament d'actualitzacions (també afecta el compte d'actualitzacions)   "
             frame_left_click_behaviour="Comportament del clic esquerre (quan hi ha actualitzacions)   "
             frame_other_options="Other options"
             left_click_Synaptic="obre Synaptic "
             left_click_ViewandUpgrade='obre la finestra de MX Apt Notifier "Veure i actualitzar"'
             use_apt_get_dash_dash_yes="usa l'opció d'apt-get --yes per a upgrade/dist-upgrade"
             auto_close_term_window_when_complete="tanca automàticament la finestra del terminal quan s'ha completat apt-get upgrade/dist-upgrade"
             check_for_autoremoves="check for autoremovable packages after apt-get upgrade/dist-upgrade"
             ;;

         de) window_title="MX Apt Notifier Einstellungen"
             frame_upgrade_behaviour="Upgrade-Verhalten (beeinflusst auch die Zählung der Meldung)   "
             frame_left_click_behaviour="Linksklick-Verhalten (wenn Updates verfügbar sind)   "
             frame_other_options="Other options"
             left_click_Synaptic="startet Synaptic "
             left_click_ViewandUpgrade='öffnet das Fenster im MX Apt Notifier "Anschauen and Aufrüsten"'
             use_apt_get_dash_dash_yes="Option --yes von apt-get's benutzen bei upgrade/dist-upgrade"
             auto_close_term_window_when_complete="Shellfenster automatiisch schliessen nach Ende von apt-get upgrade/dist-upgrade"
             check_for_autoremoves="nach apt-get upgrade/dist-upgrade überprüfen, ob autoremove Pakete vorhanden sind."
             ;;

         el) window_title="MX Apt Notifier προτιμήσεις"
             frame_upgrade_behaviour="αναβάθμιση (επηρεάζει επίσης καταμέτρηση κοινοποίηση)   "
             frame_left_click_behaviour="αριστερό κλικ (όταν υπάρχουν διαθέσιμες ενημερώσεις)   "
             frame_other_options="Other options"
             left_click_Synaptic="ανοίγει το  Synaptic "
             left_click_ViewandUpgrade='ανοίγει το παράθυρο "Προβολή και Αναβάθμιση" του MX Apt Notifier'
             use_apt_get_dash_dash_yes="χρησιμοποιήσετε την επιλογή του apt-get --yes option για την αναβάθμιση"
             auto_close_term_window_when_complete="Να κλείσει αυτόματα το παράθυρο τερματικού όταν το apt-get upgrade/dist-upgrade έχει ολοκληρωθεί"
             check_for_autoremoves="Έλεγχος για αυτόματα αφαιρούμενα πακέτα μετά το apt-get upgrade/dist-upgrade"
             ;;

         es) window_title="MX preferencias de Apt Notifier"
             frame_upgrade_behaviour="Comportamiento de actualización (también afecta la cuenta de notificaciones)   "
             frame_left_click_behaviour="Comportamiento del clic izquierdo (cuando hay actualizaciones disponibles)   "
             frame_other_options="Other options"
             left_click_Synaptic="abre Synaptic "
             left_click_ViewandUpgrade='abre la ventana "Ver y Actualizar" de MX Apt Notifier'
             use_apt_get_dash_dash_yes="usar la opción --yes de apt-get's para upgrade/dist-upgrade"
             auto_close_term_window_when_complete="Cerrar automáticamente la terminal cuando se completa apt-get upgrade/dist-upgrade"
             check_for_autoremoves="buscar los paquetes autoremovibles después del apt-get upgrade/dist-upgrade"
             ;;

         fr) window_title="Préferences pour MX Apt Notifier"
             frame_upgrade_behaviour="Comportement de la mise à niveau (influe aussi sur le compte dans la notification)   "
             frame_left_click_behaviour="Comportement du clic gauche (quand des mises à jour sont disponibles)   "
             frame_other_options="Other options"
             left_click_Synaptic="lance Synaptic "
             left_click_ViewandUpgrade='lance MX Apt Notifier "Voir et mettre à niveau" dans une fenêtre'
             use_apt_get_dash_dash_yes="utiliser l'option --yes de apt-get pour upgrade/dist-upgrade"
             auto_close_term_window_when_complete="fermer automatiquement la fenêtre de terminal quand apt-get upgrade/dist-upgrade se termine"
             check_for_autoremoves="chercher des paquets superflus après apt-get upgrade/dist-upgrade"
             ;;

         it) window_title="Preferenze per MX Apt Notifier"
             frame_upgrade_behaviour="Comportamento dell'aggiornamento (compresa la conta delle notifiche)   "
             frame_left_click_behaviour="Comportemento click sinistro (quando sono disponibili aggiornamenti)   "
             frame_other_options="Other options"
             left_click_Synaptic="apre Synaptic "
             left_click_ViewandUpgrade='apre la finestra "Mostra e Aggiorna" di MX Apt Notifier'
             use_apt_get_dash_dash_yes="usare l'opzione --yes di apt-get per l' upgrade/dist-upgrade"
             auto_close_term_window_when_complete="chiudere automaticamente la finestra del terminale quando apt-get upgrade/dist-upgrade ha terminato"
             check_for_autoremoves="verificare la presenza di pacchetti auto-rimovibili dopo aver eseguito apt-get upgrade/dist-upgrade"
             ;;

         ja) window_title="MX Apt Notifier 設定"
             frame_upgrade_behaviour="更新の動作 (通知数に影響があります)   "
             frame_left_click_behaviour="左クリックの動作 (更新が可能な場合)   "
             frame_other_options="Other options"
             left_click_Synaptic="Synaptic を開く"
             left_click_ViewandUpgrade="MX Apt Notifier '表示・更新' ウインドウを開く"
             use_apt_get_dash_dash_yes="upgrade/dist-upgrade に apt-get's --yes オプションを使用する"
             auto_close_term_window_when_complete="apt-get upgrade/dist-upgrade が完了した後自動的に端末ウインドウを閉じる"
             check_for_autoremoves="check for autoremovable packages after apt-get upgrade/dist-upgrade"
             ;;

         nl) window_title="MX Apt Notifier voorkeuren"
             frame_upgrade_behaviour="Upgrade gedrag (beïnvloedt ook notificatie aantal)   "
             frame_left_click_behaviour="Links-klik gedrag (wanneer updates beschikbaar zijn)   "
             frame_other_options="Other options"
             left_click_Synaptic="opent Synaptic "
             left_click_ViewandUpgrade='opent MX Apt Notifier "Bekijk en Upgrade" scherm'
             use_apt_get_dash_dash_yes="gebruik apt-get's --yes optie voor upgrade/dist-upgrade"
             auto_close_term_window_when_complete="automatisch terminal scherm sluiten wanneer apt-get upgrade/dist-upgrade klaar is"
             check_for_autoremoves="controleer voor automatisch verwijderbare pakketten na apt-get upgrade/dist-upgrade"
             ;;

         pl) window_title="MX Apt Notifier Ustawienia"
             frame_upgrade_behaviour="Zachowanie aktualizacji   (również wpływ na liczbę powiadomień)   "
             frame_left_click_behaviour="Zachowanie lewego przycisku myszy   (gdy dostępne są nowe aktualizacje)   "
             frame_other_options="Other options"
             left_click_Synaptic="otwiera Synaptic "
             left_click_ViewandUpgrade='otwiera MX Apt Notifier "Przeglądaj i Aktualizować" okno'
             use_apt_get_dash_dash_yes="stosować apt-get's --yes opcję  dla upgrade/dist-upgrade"
             auto_close_term_window_when_complete="zostały automatycznie zamknięte okno terminalu przy upgrade/dist-upgrade gotowy"
             check_for_autoremoves="check for autoremovable packages after apt-get upgrade/dist-upgrade"
             ;;

         ru) window_title="MX Apt Notifier Настройки"
             frame_upgrade_behaviour="Обновить поведение (также влияет на количество уведомлений)   "
             frame_left_click_behaviour="Поведение при нажатии ЛКМ (при наличии обновлений)   "
             frame_other_options="Other options"
             left_click_Synaptic="Открыть Synaptic "
             left_click_ViewandUpgrade='Открыть окно MX Apt Notifier "Просмотр и обновление"'
             use_apt_get_dash_dash_yes="Использовать опцию apt-get's --yes для upgrade/dist-upgrade"
             auto_close_term_window_when_complete="Автоматически закрыть окно терминала после выполнения apt-get upgrade/dist-upgrade"
             check_for_autoremoves="Проверка наличия автоудаляемых пакетов после apt-get upgrade/dist-upgrade"
             ;;

         sv) window_title="MX Apt Notifier inställningar"
             frame_upgrade_behaviour="Uppgraderingsbeteende (påverkar också antalet i meddelandena)   "
             frame_left_click_behaviour="Vänster-klicks beteende (när uppdateringar är tillgängliga)   "
             frame_other_options="Other options"
             left_click_Synaptic="öppnar Synaptic "
             left_click_ViewandUpgrade='öppnar MX Apt Notifier "Granska och uppgradera"-fönster'
             use_apt_get_dash_dash_yes="använd apt-get's --yes möjlighet för upgrade/dist-upgrade"
             auto_close_term_window_when_complete="stäng automatiskt terminalfönstret när apt-get upgrade/dist-upgrade är slutfört"
             check_for_autoremoves="sök efter automatiskt borttagbara paket efter apt-get upgrade/dist-upgrade"
             ;;

          *) : ;;
    esac

    #for MEPIS remove "MX" branding from the $window_title and $left_click_ViewandUpgrade strings
    window_title=$(echo "$window_title"|sed 's/MX /'$(grep -o MX-[1-9][0-9] /etc/issue|cut -c1-2)" "'/')
    left_click_ViewandUpgrade=$(echo "$left_click_ViewandUpgrade"|sed 's/MX /'$(grep -o MX-[1-9][0-9] /etc/issue|cut -c1-2)" "'/')

    TMP=$(mktemp -d /tmp/apt_notifier_preferences_dialog.XXXXXX)
    touch "$TMP"/output
    cat << EOF > "$TMP"/DIALOG
    <window title="@title@" icon-name="mnotify-some">
      <vbox>
        <frame @upgrade_behaviour@>
          <frame>
            <radiobutton active="@UpgradeBehaviourAptGetUpgrade@">
              <label>apt-get upgrade</label>
              <variable>UpgradeType_upgrade</variable>
              <action>:</action>
            </radiobutton>
            <radiobutton active="@UpgradeBehaviourAptGetDistUpgrade@">
              <label>apt-get dist-upgrade</label>
              <variable>UpgradeType_dist-upgrade</variable>
              <action>:</action>
            </radiobutton>
          </frame>
        </frame>
        <vseparator></vseparator>
        <frame @leftclick_behaviour@>
          <frame>
            <radiobutton active="@LeftClickBehaviourSynaptic@">
              <label>@opens_Synaptic@</label>
              <variable>LeftClickSynaptic</variable>
              <action>:</action>
            </radiobutton>
            <radiobutton active="@LeftClickBehaviourViewAndUpgrade@">
              <label>@opens_View_and_Upgrade@</label>
              <variable>LeftClickViewAndUpgrade</variable>
              <action>:</action>
            </radiobutton>
          </frame>
        </frame>
        <frame @Other_options@>
        <frame>
          <checkbox active="@UpgradeAssumeYes@">
            <label>@use_apt_get_yes@</label>
            <variable>UpgradeAssumeYes</variable>
            <action>:</action>
          </checkbox>
        </frame>
        <frame>
          <checkbox active="@UpgradeAutoClose@">
            <label>@auto_close_term_window@</label>
            <variable>UpgradeAutoClose</variable>
            <action>:</action>
          </checkbox>
        </frame>
        <frame>
          <checkbox active="@CheckForAutoRemoves@">
            <label>@check_for_autoremoves@</label>
            <variable>CheckForAutoRemoves</variable>
            <action>:</action>
          </checkbox>
        </frame>
        </frame>
      <hbox>
        <button ok> </button>
        <button cancel> </button>
      </hbox>
      </vbox>
    </window>
EOF

    # edit translateable strings placeholders in "$TMP"/DIALOG
    sed -i 's/@title@/'"$window_title"'/' "$TMP"/DIALOG
    sed -i 's/@upgrade_behaviour@/'"$frame_upgrade_behaviour"'/' "$TMP"/DIALOG
    sed -i 's/@leftclick_behaviour@/'"$frame_left_click_behaviour"'/' "$TMP"/DIALOG
    sed -i 's/@Other_options@/'"$frame_other_options"'/' "$TMP"/DIALOG
    sed -i 's/@opens_Synaptic@/'"$left_click_Synaptic"'/' "$TMP"/DIALOG
    sed -i 's/@opens_View_and_Upgrade@/'"$left_click_ViewandUpgrade"'/' "$TMP"/DIALOG
    sed -i 's|@use_apt_get_yes@|'"$use_apt_get_dash_dash_yes"'|' "$TMP"/DIALOG
    sed -i 's|@auto_close_term_window@|'"$auto_close_term_window_when_complete"'|' "$TMP"/DIALOG
    sed -i 's|@check_for_autoremoves@|'"$check_for_autoremoves"'|' "$TMP"/DIALOG

    # edit placeholders in "$TMP"/DIALOG to set initial settings of the radiobuttons & checkboxes 
    sed -i 's/@UpgradeBehaviourAptGetUpgrade@/'$(if [ $(grep UpgradeType=upgrade ~/.config/apt-notifierrc) ]; then echo -n true; else echo -n false; fi)'/' "$TMP"/DIALOG
    sed -i 's/@UpgradeBehaviourAptGetDistUpgrade@/'$(if [ $(grep UpgradeType=dist-upgrade ~/.config/apt-notifierrc) ]; then echo -n true; else echo -n false; fi)'/' "$TMP"/DIALOG
    sed -i 's/@LeftClickBehaviourSynaptic@/'$(if [ $(grep LeftClick=Synaptic ~/.config/apt-notifierrc) ]; then echo -n true; else echo -n false; fi)'/' "$TMP"/DIALOG
    sed -i 's/@LeftClickBehaviourViewAndUpgrade@/'$(if [ $(grep LeftClick=ViewAndUpgrade ~/.config/apt-notifierrc) ]; then echo -n true; else echo -n false; fi)'/' "$TMP"/DIALOG
    sed -i 's/@UpgradeAssumeYes@/'$(grep UpgradeAssumeYes ~/.config/apt-notifierrc | cut -f2 -d=)'/' "$TMP"/DIALOG
    sed -i 's/@UpgradeAutoClose@/'$(grep UpgradeAutoClose ~/.config/apt-notifierrc | cut -f2 -d=)'/' "$TMP"/DIALOG
    sed -i 's/@CheckForAutoRemoves@/'$(grep CheckForAutoRemoves ~/.config/apt-notifierrc | cut -f2 -d=)'/' "$TMP"/DIALOG


    gtkdialog --file="$TMP"/DIALOG >> "$TMP"/output

    grep -q EXIT=.*OK.* "$TMP"/output

    if [ "$?" -eq 0 ];
      then
        if [ $(grep UpgradeType_upgrade=.*true.*      "$TMP"/output) ]; then sed -i 's/UpgradeType=dist-upgrade/UpgradeType=upgrade/'       ~/.config/apt-notifierrc; fi
        if [ $(grep UpgradeType_dist-upgrade=.*true.* "$TMP"/output) ]; then sed -i 's/UpgradeType=upgrade/UpgradeType=dist-upgrade/'       ~/.config/apt-notifierrc; fi
        if [ $(grep LeftClickViewAndUpgrade=.*true.*  "$TMP"/output) ]; then sed -i 's/LeftClick=Synaptic/LeftClick=ViewAndUpgrade/'        ~/.config/apt-notifierrc; fi
        if [ $(grep LeftClickSynaptic=.*true.*        "$TMP"/output) ]; then sed -i 's/LeftClick=ViewAndUpgrade/LeftClick=Synaptic/'        ~/.config/apt-notifierrc; fi
        if [ $(grep UpgradeAssumeYes=.*false.*        "$TMP"/output) ]; then sed -i 's/UpgradeAssumeYes=true/UpgradeAssumeYes=false/'       ~/.config/apt-notifierrc; fi
        if [ $(grep UpgradeAssumeYes=.*true.*         "$TMP"/output) ]; then sed -i 's/UpgradeAssumeYes=false/UpgradeAssumeYes=true/'       ~/.config/apt-notifierrc; fi
        if [ $(grep UpgradeAutoClose=.*false.*        "$TMP"/output) ]; then sed -i 's/UpgradeAutoClose=true/UpgradeAutoClose=false/'       ~/.config/apt-notifierrc; fi
        if [ $(grep UpgradeAutoClose=.*true.*         "$TMP"/output) ]; then sed -i 's/UpgradeAutoClose=false/UpgradeAutoClose=true/'       ~/.config/apt-notifierrc; fi
        if [ $(grep CheckForAutoRemoves=.*false.*     "$TMP"/output) ]; then sed -i 's/CheckForAutoRemoves=true/CheckForAutoRemoves=false/' ~/.config/apt-notifierrc; fi
        if [ $(grep CheckForAutoRemoves=.*true.*      "$TMP"/output) ]; then sed -i 's/CheckForAutoRemoves=false/CheckForAutoRemoves=true/' ~/.config/apt-notifierrc; fi
     else
        :
    fi

    rm -rf "$TMP"

    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(['sh %s' % script_file.name],shell=True).wait()
    script_file.close()
    Check_for_Updates_by_User = 'true'
    check_updates()

def apt_history():
    global Check_for_Updates_by_User
    script = '''#! /bin/bash
    
    TMP=$(mktemp -d /tmp/apt_history.XXXXXX)
    
    apt-history | sed 's/:all/ all/;s/:i386/ i386/;s/:amd64/ amd64/' | column -t > "$TMP"/APT_HISTORY
    
    yad --window-icon=/usr/share/icons/mnotify-some.png \
        --width=$(xprop -root | grep _NET_DESKTOP_GEOMETRY\(CARDINAL\) | awk '{print $3*.75}' | cut -f1 -d.) \
        --height=480 \
        --center \
        --title "apt history" \
        --text-info \
        --filename="$TMP"/APT_HISTORY \
        --fontname=mono \
        --button=gtk-close \
        --margins=7 \
        --borders=5
        
    rm -rf "$TMP"    
    
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(['sh %s' % script_file.name],shell=True).wait()
    script_file.close()
    Check_for_Updates_by_User = 'true'
    check_updates()
    
def apt_get_update():
    global Check_for_Updates_by_User
    script = '''#! /bin/bash
    rootPasswordRequestMsg="The action you requested needs <b>root privileges</b>. Please enter <b>root's</b> password below."
    case $(locale|grep ^LANG=|cut -f2 -d=|cut -f1 -d_) in

      ca)    rootPasswordRequestMsg="A l'acció que heu demanat li calen <b>privilegis de root</b>. Si us plau, introduïu la contrasenya de <b>root</b> tot seguit."
             ;;

      de)    rootPasswordRequestMsg="Die Aktion benötigt <b>Systemverwalterrechte</b>. Bitte geben Sie das Passwort des Benutzers <b>root</b> ein."
             ;;

      el)    rootPasswordRequestMsg="Η ενέργεια που ζητήσατε απαιτεί <b>προνόμια root</b>. Παρακαλώ εισάγετε τον κωδικό πρόσβασης του <b>root</b> παρακάτω."
             ;;

      es)    rootPasswordRequestMsg="La acción que solicitó necesita <b>privilegios de superusuario</b> («root»). Introduzca la contraseña del <b>superusuario</b>."
             ;;

      fr)    rootPasswordRequestMsg="L'action requise nécessite <b>les droits du superutilisateur</b>. Veuillez saisir ci-dessous le mot de passe du <b>superutilisateur</b>."
             ;;

      it)    rootPasswordRequestMsg="L'azione che hai richiesto richiede i <b>privilegi di root</b>. Per piacere, inserisci la password di <b>root</b>."
             ;;

      ja)    rootPasswordRequestMsg="実行には <b>root</b> 権限が必要です。下に <b>root</b> のパスワードを入力してください。"
             ;;

      nl)    rootPasswordRequestMsg="Voor de handeling die u wilt verrichten hebt u <b>root-privileges</b> nodig. Voer hieronder het <b>root-wachtwoord</b> in."
             ;;

      pl)    rootPasswordRequestMsg="Polecenie, które chcesz wykonać, wymaga <b>uprawnień administratora</b>. Wpisz poniżej <b>hasło administratora</b>."
             ;;

      ru)    rootPasswordRequestMsg="Для выполнения данного действия необходимы <b>привилегии пользователя «root»</b>. Введите его пароль."
             ;;

      sv)    rootPasswordRequestMsg="Åtgärden du har begärt kräver <b>administratörsbehörighet</b>. Ange lösenordet för <b>root</b>nedan."
             ;;

       *)    : ;;

    esac
    
    
    #for MEPIS remove "MX" branding from the $window_title string
    window_title=$(echo "$window_title"|sed 's/MX /'$(grep -o MX-[1-9][0-9] /etc/issue|cut -c1-2)" "'/')

    TermXOffset="$(xwininfo -root|awk '/Width/{print $2/4}')"
    TermYOffset="$(xwininfo -root|awk '/Height/{print $2/4}')"
    G=" --geometry=80x25+"$TermXOffset"+"$TermYOffset
    #I=" --icon=mnotify-some"
    #T=" --title='""$(grep -o MX-[1-9][0-9] /etc/issue|cut -c1-2)"" apt-notifier: apt-get update'"
    if (xprop -root | grep -q -i kde)
      then
        # Running KDE
        #
        # Can't get su-to-root to work in newer KDE's, so use kdesu for authentication.
        #  
        # If x-terminal-emulator is set to xfce4-terminal.wrapper, use     
        # xfce4-terminal instead because the --hold option doesn't work with
        # the wrapper. Also need to enclose the apt-get command in single quotes.
        #
        # If x-terminal-emulator is set to gnome-terminal.wrapper, use konsole instead, if it's available (it should be), if not do nothing.
        # If x-terminal-emulator is set to xterm,                  use konsole instead, if it's available (it should be), if not use xterm.

        case $(readlink -e /usr/bin/x-terminal-emulator | xargs basename) in
        
          gnome-terminal.wrapper) if [ -e /usr/bin/konsole ]
                                    then
                                      $(kde4-config --path libexec)kdesu -c "konsole -e apt-get update"
                                      sleep 5
                                    else
                                      :
                                  fi
                                  ;;

                         konsole) $(kde4-config --path libexec)kdesu -c "konsole -e apt-get update"
                                  sleep 5
                                  ;;

                         roxterm) $(kde4-config --path libexec)kdesu -c "roxterm$G$T --separare -e apt-get update"
                                  ;;

          xfce4-terminal.wrapper) $(kde4-config --path libexec)kdesu -c "xfce4-terminal$G$I$T -e 'apt-get update'"
                                  ;;

                           xterm) if [ -e /usr/bin/konsole ]
                                    then
                                      $(kde4-config --path libexec)kdesu -c "konsole -e apt-get update"
                                      sleep 5
                                    else
                                      $(kde4-config --path libexec)kdesu -c "xterm -e apt-get update"
                                  fi
                                  ;;

                               *) $(kde4-config --path libexec)kdesu -c "x-terminal-emulator -e apt-get update"
                                  ;;
        esac

      else
        # Running a non KDE desktop
        # 
        # Use su-to-root for authentication, it should end up using gksu.
        # 
        # If x-terminal-emulator is set to xfce4-terminal.wrapper, use 
        # xfce4-terminal instead because the --hold option doesn't work
        # with the wrapper. Also need to enclose the apt-get command in
        # single quotes.
        #
        # If x-terminal-emulator is set to gnome-terminal.wrapper, use xfce4-terminal instead, if it's available (it is in MX), if not use gnome-terminal.
        # If x-terminal-emulator is set to xterm,                  use xfce4-terminal instead, if it's available (it is in MX), if not use xterm.

        case $(readlink -e /usr/bin/x-terminal-emulator | xargs basename) in

          gnome-terminal.wrapper) su-to-root -X -c "gnome-terminal$G$T -e 'apt-get update'"
                                  ;;

                         konsole) su-to-root -X -c "konsole -e apt-get update"
                                  sleep 5
                                  ;;

                         roxterm) su-to-root -X -c "roxterm$G$T --separate -e apt-get update"
                                  ;;

          xfce4-terminal.wrapper) if [ -x $(whereis gksu | awk '{print $2}') ]
                                    then
                                      gksu -m "$rootPasswordRequestMsg""\n\n'apt-get update'" "xfce4-terminal$G$I$T -e 'apt-get update'"
                                    else
                                      su-to-root -X -c "xfce4-terminal$G$I$T -e 'apt-get update"
                                  fi                                      
                                  ;;

                           xterm) if [ -e /usr/bin/xfce4-terminal ]
                                    then
                                      su-to-root -X -c "xfce4-terminal$G$I$T -e 'apt-get update'"
                                    else
                                      su-to-root -X -c "xterm -e apt-get update"
                                  fi
                                  ;;

                               *) su-to-root -X -c "x-terminal-emulator -e apt-get update"
                                  ;;

        esac
    fi
    
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(['sh %s' % script_file.name],shell=True).wait()
    script_file.close()
    Check_for_Updates_by_User = 'true'
    check_updates()

def re_enable_click():
    global ignoreClick
    ignoreClick = '0'

def start_synaptic0():
    global ignoreClick
    global Timer
    if ignoreClick != '1':
        start_synaptic()    
        ignoreClick = '1'
        Timer.singleShot(50, re_enable_click)
    else:
        pass

def viewandupgrade0():
    global ignoreClick
    global Timer
    if ignoreClick != '1':
        viewandupgrade()    
        ignoreClick = '1'
        Timer.singleShot(50, re_enable_click)
    else:
        pass

# Define the command to run when left clicking on the Tray Icon
def left_click():
    if text.startswith( "0" ):
        start_synaptic0()
    else:
        """Test ~/.config/apt-notifierrc for LeftClickViewAndUpgrade"""
        command_string = "cat " + rc_file_name + " | grep -q LeftClick=ViewAndUpgrade"
        exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
        if exit_state == 0:
            viewandupgrade0()
        else:
            start_synaptic0()

# Define the action when left clicking on Tray Icon
def left_click_activated(reason):
    if reason == QtGui.QSystemTrayIcon.Trigger:
        left_click()

def read_icon_config():
    """Reads ~/.config/apt-notifierrc, returns 'show' if file doesn't exist or does not contain DontShowIcon"""
    command_string = "cat " + rc_file_name + " | grep -q DontShowIcon"
    exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
    if exit_state != 0:
        return "show"

def set_noicon():
    """Reads ~/.config/apt-notifierrc. If "DontShowIcon blah blah blah" is already there, don't write it again"""
    command_string = "cat " + rc_file_name + " | grep -q DontShowIcon"
    exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
    if exit_state != 0:
        file = open(rc_file_name, 'a')
        file.write ('[DontShowIcon] #Remove this entry if you want the apt-notify icon to show even when there are no upgrades available\n')
        file.close()
        subprocess.call(["/usr/bin/apt-notifier"], shell=True, stdout=subprocess.PIPE)
    AptIcon.hide()
    icon_config = "donot show"

def add_rightclick_actions():
    ActionsMenu.clear()
    """Test ~/.config/apt-notifierrc for LeftClickViewAndUpgrade"""
    command_string = "cat " + rc_file_name + " | grep -q LeftClick=ViewAndUpgrade"
    exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
    if exit_state == 0:
        AptNotify.connect(ActionsMenu.addAction(View_and_Upgrade), QtCore.SIGNAL("triggered()"), viewandupgrade0)
        ActionsMenu.addSeparator()
        AptNotify.connect(ActionsMenu.addAction(Upgrade_using_Synaptic), QtCore.SIGNAL("triggered()"), start_synaptic0)
    else:
        AptNotify.connect(ActionsMenu.addAction(Upgrade_using_Synaptic), QtCore.SIGNAL("triggered()"), start_synaptic0)
        ActionsMenu.addSeparator()
        AptNotify.connect(ActionsMenu.addAction(View_and_Upgrade), QtCore.SIGNAL("triggered()"), viewandupgrade0)        
    add_apt_history_action()        
    add_apt_get_update_action()
    add_apt_notifier_help_action()
    add_synaptic_help_action()
    add_quit_action()
    add_aptnotifier_prefs_action()

def add_hide_action():
    ActionsMenu.clear()
    if icon_config == "show":
        hide_action = ActionsMenu.addAction(Hide_until_updates_available)
        AptNotify.connect(hide_action,QtCore.SIGNAL("triggered()"),set_noicon)
        ActionsMenu.addSeparator()
        AptNotify.connect(ActionsMenu.addAction(u"Synaptic"), QtCore.SIGNAL("triggered()"), start_synaptic0)        
    add_apt_history_action()    
    add_apt_get_update_action()
    add_apt_notifier_help_action()
    add_synaptic_help_action()
    add_quit_action()
    add_aptnotifier_prefs_action()

def add_quit_action():
    ActionsMenu.addSeparator()
    quit_action = ActionsMenu.addAction(QuitIcon,Quit_Apt_Notifier)
    AptNotify.connect(quit_action, QtCore.SIGNAL("triggered()"), exit)

def add_apt_notifier_help_action():
    ActionsMenu.addSeparator()
    apt_notifier_help_action = ActionsMenu.addAction(HelpIcon,Apt_Notifier_Help)
    apt_notifier_help_action.triggered.connect(open_apt_notifier_help)
    
def open_apt_notifier_help():
    """ check if mx-viewer is installed, if it is use it to display help, otherwise use xdg-open """
    command_string = "test -e /usr/bin/mx-viewer"
    exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
    if exit_state == 0:
        subprocess.Popen(['mx-viewer https://mxlinux.org/wiki/help-files/help-mx-apt-notifier'],shell=True)
    else:
        subprocess.Popen(['xdg-open  https://mxlinux.org/wiki/help-files/help-mx-apt-notifier'],shell=True) 

    
def add_synaptic_help_action():
    ActionsMenu.addSeparator()
    synaptic_help_action = ActionsMenu.addAction(HelpIcon,Synaptic_Help)
    synaptic_help_action.triggered.connect(open_synaptic_help)
    
def open_synaptic_help():
    """ check if mx-viewer is installed, if it is use it to display help, otherwise use xdg-open """
    command_string = "test -e /usr/bin/mx-viewer"
    exit_state = subprocess.call([command_string], shell=True, stdout=subprocess.PIPE)
    if exit_state == 0:
        subprocess.Popen(['mx-viewer https://mxlinux.org/user_manual_mx15/mxum.html#toc-Subsection-5.3'],shell=True)
    else:
        subprocess.Popen(['xdg-open  https://mxlinux.org/user_manual_mx15/mxum.html#toc-Subsection-5.3'],shell=True)

def add_aptnotifier_prefs_action():
    ActionsMenu.addSeparator()
    aptnotifier_prefs_action =  ActionsMenu.addAction(Apt_Notifier_Preferences)
    AptNotify.connect(aptnotifier_prefs_action,QtCore.SIGNAL("triggered()"), aptnotifier_prefs)

def add_apt_history_action():
    ActionsMenu.addSeparator()
    apt_history_action =  ActionsMenu.addAction(Apt_History)
    AptNotify.connect(apt_history_action,QtCore.SIGNAL("triggered()"), apt_history)

def add_apt_get_update_action():
    ActionsMenu.addSeparator()
    apt_get_update_action =  ActionsMenu.addAction(Check_for_Updates)
    AptNotify.connect(apt_get_update_action,QtCore.SIGNAL("triggered()"), apt_get_update)

# General application code  
def main():
    # Define Core objects, Tray icon and QTimer 
    global AptNotify
    global AptIcon
    global QuitIcon
    global icon_config
    global quit_action    
    global Timer
    global initialize_aptnotifier_prefs
    set_translations()
    initialize_aptnotifier_prefs()
    AptNotify = QtGui.QApplication(sys.argv)
    AptIcon = QtGui.QSystemTrayIcon()
    Timer = QtCore.QTimer()
    icon_config = read_icon_config()
    # Define the icons:
    global NoUpdatesIcon
    global NewUpdatesIcon
    global HelpIcon
    NoUpdatesIcon = QtGui.QIcon("/usr/share/icons/mnotify-none.png")
    NewUpdatesIcon  = QtGui.QIcon("/usr/share/icons/mnotify-some.png")
    HelpIcon = QtGui.QIcon("/usr/share/icons/oxygen/22x22/apps/help-browser.png")
    QuitIcon = QtGui.QIcon("/usr/share/icons/oxygen/22x22/actions/system-shutdown.png")
    # Create the right-click menu and add the Tooltip text
    global ActionsMenu
    ActionsMenu = QtGui.QMenu()
    AptIcon.connect( AptIcon, QtCore.SIGNAL( "activated(QSystemTrayIcon::ActivationReason)" ), left_click_activated)
    AptNotify.connect(Timer, QtCore.SIGNAL("timeout()"), check_updates)
    # Integrate it together,apply checking of updated packages and set timer to every 1 minute(s) (1 second = 1000)
    check_updates()
    AptIcon.setContextMenu(ActionsMenu)
    if icon_config == "show":
        AptIcon.show()
    Timer.start(60000)
    if AptNotify.isSessionRestored():
        sys.exit(1)
    sys.exit(AptNotify.exec_())


def check_updates_count():
    global updates_count
    
    script = '''#!/bin/sh
    sorted_list_of_upgrades() 
    {
        LC_ALL=en_US apt-get -o 'Debug::NoLocking=true' --trivial-only -V $(grep ^UpgradeType ~/.config/apt-notifierrc | cut -f2 -d=) 2>/dev/null \
        |  sed -n '/upgraded:/,$p' | grep ^'  ' | awk '{ print $1 }' | sort
    }
    if [ -s /var/lib/synaptic/preferences ]; 
        then 
            sorted_list_of_upgrades | grep -vx $(grep 'Package:' /var/lib/synaptic/preferences 2>/dev/null | awk {'print "-e " $2'}) | wc -l
        else 
            sorted_list_of_upgrades | wc -l
    fi
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    run = subprocess.Popen(["echo -n `sh %s`" % script_file.name],shell=True, stdout=subprocess.PIPE)
    updates_count = run.stdout.read(128)
    script_file.close()


if __name__ == '__main__':
    import sys
    from os.path import basename
    if len(sys.argv) == 2:
        command = basename(sys.argv[1])
        if command == "show":
            viewandupgrade()
        elif command == "updates":
            check_updates_count()
            print updates_count
    else:
        main()
