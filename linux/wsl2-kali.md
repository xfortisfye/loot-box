# Install WSL2 (w Kali Linux)

## Table of Contents <!-- omit in toc -->
- [WSL2 Installation](#wsl2-installation)
- [Install Linux distribution](#install-linux-distribution) 
- [Move WSL2 file system to another drive](#move-wsl2-file-system-to-another-drive)
- [Install Kali GUI](#install-kali-gui)

## WSL2 Installation

1. Follow this [guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

> *Note: Ensure that the entire filesystem is not compressed or it may cause issue. [Reference](https://superuser.com/questions/1624548/wsl2-has-all-network-interfaces-down-and-has-no-connectivity)*

## Install Linux distribution

1. Install e.g. from Microsoft Store (P.s Windows Terminal is great)
2. As Kali Linux installation is minimal, it is possible to install [default packages](https://www.kali.org/docs/general-use/metapackages/).
```bash
> sudo apt update && sudo apt install -y kali-linux-default 
```
3. Remember to update and upgrade all packages thereafter.
```bash
> sudo apt update && sudo apt upgrade
```

## Move WSL2 File System to another drive

1. Use powershell to check the distro name
```powershell
> wsl -l -v
```
> in this scenario, it is kali-linux
2. Export Kali
```powershell
> mkdir D:\backup
> wsl --export kali-linux D:\backup\kali.tar
```
3. Unregister the same distribution to remove it from the C: drive:
```powershell
> wsl --unregister kali-linux
```
4. Import Kali
```powershell
> mkdir D:\wsl
> wsl --import kali-linux D:\wsl\ D:\backup\kali.tar
```
5. As Kali will use root as the default user, go to the Kali App Folder run command to set default user as previously registered user.
```powershell
> cd %userprofile%\AppData\Local\Microsoft\WindowsApps
> kali config --default-user <username>
```

[Reference](https://superuser.com/questions/1550622/move-wsl2-file-system-to-another-drive).

## Install Kali GUI

1. Install Kali Win Kex
```bash
> sudo apt upgrade && sudo apt install -y kali-win-kex
```

2. Launch it using
   1. Win-Kex Window Mode (Generate a full-screen Kali): `kex --win -s`
   2. Win-Kex SL Mode (Generate a task-bar Kali): `kex --sl -s`
   3. Win-Kex ESM Mode (Remote Host Connection + Windowed version): `kex --esm -s`

3. Ensure that public network traffic is allowed through the Windows Defender Firewall when prompted (to enable SL mode and sound).
4. To end process, `kex --kill`

[Official Documentation](https://www.kali.org/docs/wsl/win-kex/)
[Video Reference](https://www.youtube.com/watch?v=nXThnFxwH9c&ab_channel=DavidBombal)
