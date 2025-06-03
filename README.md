# Programmierung verteilter Systeme: Mandelbrot

Dieses Projekt berechnet und visualisiert die Mandelbrotmenge. Mit Hilfe von Java RMI wird die Arbeitslast auf mehrere Server(Worker) verteilt. Die Benutzeroberfläche basiert auf Java Swing, und der Client folgt dem Model-View-Presenter Architekturmuster.

## Inhaltsverzeichnis

- [Gruppenmitglieder](#gruppenmitglieder)
- [Projektstruktur](#projektstruktur)
- [Technologien](#technologien)
- [Starten des Programmes](#starten-des-programmes)
- [Alternative: Manuelle Ausführung](#alternative-manuelle-ausführung)
  - [1. Master starten](#1-master-starten)
  - [2. Worker starten](#2-worker-starten)
  - [3. Starten des Clients](#3-starten-des-clients)
- [Hinweise](#hinweise)

## Gruppenmitglieder

- Valine Richter s85875
- Anastasia Suglobow s84401
- Marlene Pannoscha s83814 (Gruppensprechen)

## Projektstruktur

```bash
Mandelbrot/
├── client/
│   ├── client.config               # Konfigurationsdatei für den Client
│   ├── Client.java                 # Einstiegspunkt für den Client
│   ├── ClientModel.java            # Model-Klasse (MVP)
│   ├── ClientPresenter.java        # Presenter-Klasse (MVP)
│   └── ClientView.java             # View-Klasse (MVP)
│
├── master/
│   └── Master.java                 # Einstiegspunkt für den Master-Server
│
├── worker/
│   └── Worker.java                 # Einstiegspunkt für den Worker
│
├── public/
│   ├── MasterInterface.java        # RMI-Remote Client → Master, Worker → Master
│   └── WorkerInterface.java        # RMI-Remote Master → Worker
│
├── Doc/
│   ├── assets/                     # Bilder und Medien für die Projektdokumentation
│   ├── template/                   # Dokumentationsvorlagen im AsciiDoc-Format
│   ├── main.pdf                    # Generierte Dokumentationsvorlagen
│   └── plot/
│       ├── gnuplot/                # Plots mit Gnuplot
│       └── python-plot/            # Plots mit Python
│
├── start_all.(bat/sh)              # Globales Startskript für Client, Master und Worker
├── start_client.(bat/sh)           # Startet den Client
├── start_master.(bat/sh)           # Startet den Master-Server
├── start_worker.(bat/sh)           # Startet einen Worker
├── README.md                       # Diese Dokumentation
└── .gitignore                      # Git-Ausschlussdateien
```

## Technologien

- Java 8+
- RMI
- Swing (BufferedImage)
- MVP-Muster (Model-View-Presenter)
- Visual Studio Code

## Starten des Programmes

### Für Windows (Shell):

Startskript ausführen:

```bash
./start_master.bat
```

```bash
./start_worker.bat
```

```bash
./start_client.bat
```

### Für Linux:

```bash
chmod +x *
```

```bash
./start_master.sh
```

```bash
./start_worker.sh
```

```bash
./start_client.sh
```

Das Skript kompiliert alle Java-Dateien.

## Alternative: Manuelle Ausführung

## 1. Master starten

```bash
javac -d build public/MasterInterface.java public/WorkerInterface.java master/Master.java
java -cp build Master --maddr localhost --mport 10000 --mserv MandelbrotServer
```

```bash
java -cp build Master --maddr <Master Address> --mport <Master Port> --mserv <Master Service>
```

## 2. Worker starten

Starte beliebig viele Worker, die sich bei dem Master registrieren. Jeder Worker benötigt die IP-Adresse und den Port des Masters.

```bash
javac -d build public/MasterInterface.java public/WorkerInterface.java worker/Worker.java
java -cp build Worker --maddr localhost --mport 10000 --mserv MandelbrotServer --waddr localhost
```

```bash
java -cp build Worker --maddr <Master Address> --mport <Master Port> --mserv <Master Service> --waddr <Worker Address>
```

## 3. Starten des Clients

Es können mehrere Clients gestartet werden. Der Client verbindet sich mit dem Master, öffnet die Benutzeroberfläche und startet die Berechnung.

```bash
javac -d build public/MasterInterface.java public/WorkerInterface.java client/*.java
java -cp build Client --maddr localhost --mport 10000 --mserv MandelbrotServer
```

```bash
java -cp build Client --maddr <Master Address> --mport <Master Port> --mserv <Master Service>
```

## Hinweise
- Die Anzahl der Client-Threads sollte mindestens so hoch sein wie die Gesamtanzahl der gestarteten Worker.
- Alle Parameter (z.B. Zoompunkt, Iterationsanzahl oder Auflösung) lassen sich mittels der Benutzeroberfläche oder über die Datei _client.config_ anpassen
