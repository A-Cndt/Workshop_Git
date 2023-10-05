[![GitHub contributors](https://img.shields.io/github/contributors/A-Cndt/Workshop_Git?color=blue&label=Contributors&logo=GitHub)](https://github.com/A-Cndt/Workshop_Git/graphs/contributors)
[![Branchs](https://badgen.net/badge/Branchs/3/blue?icon=github)](https://github.com/A-Cndt/Workshop_Git/branches)
![GitHub repo size](https://img.shields.io/github/repo-size/A-Cndt/Workshop_Git?color=blue&label=Repo%20Size&logo=git&logoColor=white)

[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/A-Cndt/Workshop_Git/main?label=Last%20Commit)](https://github.com/A-Cndt/Workshop_Git/commit/main)
[![GitHub issues](https://img.shields.io/github/issues/A-Cndt/Workshop_Git?label=Issues)](https://github.com/A-Cndt/Workshop_Git/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/A-Cndt/Workshop_Git?label=Pull%20request)](https://github.com/A-Cndt/Workshop_Git/pulls)
[![GitHub milestones](https://img.shields.io/github/milestones/open/A-Cndt/Workshop_Git?label=Open%20Milestones)](https://github.com/A-Cndt/Workshop_Git/milestones)

![GitHub top language](https://img.shields.io/github/languages/top/A-Cndt/Workshop_Git?color=blueviolet&label=Python&logo=Python&logoColor=white)
[![GitHub Release Date](https://img.shields.io/github/release-date/A-Cndt/Workshop_Git?color=blueviolet&label=Release%20Date)](https://github.com/A-Cndt/Workshop_Git/releases/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/A-Cndt/Workshop_Git?color=blueviolet&label=Lastest%20Release)](https://github.com/A-Cndt/Workshop_Git/tags)
![GitHub](https://img.shields.io/github/license/A-Cndt/Workshop_Git?color=blueviolet&label=License)

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/A-Cndt/Workshop_Git/documentation.yml?logo=sphynx&label=Documentation%20Sphynx&link=https%3A%2F%2Fa-cndt.github.io%2FWorkshop_Git%2F)

# Introduction à l'usage de Git pour le contrôle de version
**IPSA 2023 - 2024**

Alexandre Condette - alexandre2.condette@ipsa.fr
---
*Introduction à Git pour les étudiants d'Aéro 3*
____

## Installer Git
Avant de lancer cette procédure, vérifiez que Git n'est pas déjà installé sur votre PC :
- Ouvrer un terminal
- Executer la commande suivante : 
```console
git --version
```

### Windows 
Télécharger l'exécutable directement depuis le site de GitHub : https://gitforwindows.org/

Pour installer l’outil, double cliquez simplement sur l’icone du fichier téléchargé. Une interface se lance alors et vous propose, page après page, de configurer l’installation de Git. Je vous conseil alors de laisser les valeurs par défaut et de simplement cliquer sur suivant.

Une fois arrivé sur la dernière page, il ne vous reste plus qu’à cliquer sur installer.

Vous venez alors d’installer les éléments suivants sur votre machine:
- L’outil Git.
- Git bash: terminal qui vous permet d’utiliser git en ligne de commande.
- Git gui: interface graphique qui permet de gérer les commits.
- Gitk: interface graphique qui permet de gérer l’historique de votre dépôt.

### Linux
#### Debian / Ubuntu 

```console
sudo apt-get update
sudo apt-get install git
```

#### Fedora

```console
sudo dnf install git
```

#### RedHat / CentOS

```console
sudo yum install git
```

### MacOs
Télécharger l'exécutable directement depuis le site de GitHub :  https://git-scm.com/download/mac (binary Installer)

#### Homebrew 
```console
brew install git
```

#### MacPorts
- Ouvrez le terminal et mettez à jour MacPorts
```console
sudo port selfupdate
```
- Recherchez les derniers ports Git disponibles et leurs variantes
```console
port search git
port variants git
```
- Installez Git
```console
sudo port install git +bash_completion +credential_osxkeychain +doc
```

