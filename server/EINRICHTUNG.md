# Heim-Server einrichten

Die Konfiguration ist ungetestet: Sie wurde vorbereitet, bevor der Mini-PC da war.

## Vorher, am Laptop

1. Debian (Netzinstallations-Image) von debian.org laden und mit Rufus oder balenaEtcher auf einen USB-Stick schreiben (mindestens 4 GB).
2. Konten anlegen: Tailscale, Anthropic-Konsole (API-Schlüssel mit etwas Guthaben).
3. Netzwerkkabel bereitlegen.

## Installation am Fernseher

1. Mini-PC per HDMI an den Fernseher, Tastatur und Netzwerkkabel dran, vom Stick starten.
2. Im Installer das **Root-Passwort leer lassen**. Dann darf dein Benutzer `sudo` benutzen.
3. Bei der Softwareauswahl nur **SSH-Server** und **Standard-Systemwerkzeuge** anhaken, keine Desktop-Umgebung.
4. Im BIOS einstellen, dass der PC nach einem Stromausfall wieder startet.
5. Nach dem ersten Start `ip a` eingeben und die Adresse notieren. Ab jetzt reicht der Laptop.

## Erste Befehle per SSH

```bash
ssh benutzer@adresse

lscpu        # welche CPU?
free -h      # wie viel Arbeitsspeicher?
lsblk -f     # welche Laufwerke?

sudo apt update && sudo apt install -y curl git
```

## Docker und Tailscale

```bash
curl -fsSL https://get.docker.com | sudo sh      # offizielles Installationsskript von Docker
sudo usermod -aG docker $USER                    # danach einmal ab- und wieder anmelden

curl -fsSL https://tailscale.com/install.sh | sh # offizielles Installationsskript von Tailscale
sudo tailscale up
```

## Dienste starten

Den Ordner `server/` auf den Mini-PC bringen (per `git clone` oder mit `scp` vom Laptop), dann:

```bash
cd server
docker compose up -d
docker compose ps
```

| Dienst | Adresse |
|---|---|
| Home Assistant | `http://adresse:8123` |
| ESPHome | `http://adresse:6052` |
| Music Assistant | `http://adresse:8095` |

## In Home Assistant verbinden

1. Integration **Wyoming Protocol** zweimal hinzufügen: Host `127.0.0.1`, Port `10300` (Whisper) und Port `10200` (Piper).
2. Integration **Anthropic** hinzufügen und den API-Schlüssel eintragen.
3. Integration **Music Assistant** hinzufügen, dort Spotify verbinden.
4. Unter Einstellungen, Sprachassistenten einen Assistenten anlegen: Whisper, Anthropic, Piper.

## Später

- Werbeblocker und Passwort-Tresor: `docker compose --profile extras up -d`
- Fotos: Immich nach der offiziellen Anleitung (docs.immich.app) in einen eigenen Ordner. Die vorhandene Festplatte zuerst nur lesend einbinden.
