# Odoo Dockerized Development Environment
This project provides a ready-to-use **Odoo development environment** using **Docker** and **VS Code Dev Containers**.


## Prerequisites

Ensure you have the following installed on your host machine:
* **Visual Studio Code**

* Extension: **Remote – Containers** (Dev Containers)
* **Docker**
* **Docker Compose**



## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/simonseleli/odoo-dockerized.git
```

### 2. Open the Project in VS Code

* Open the cloned folder in **VS Code**
* Open the **Command Palette** (`Ctrl + Shift + P`)
* Select **Remote-Containers: Reopen in Container**

This will:

* Build and start the dev container using:

  * `.devcontainer/devcontainer.json`
  * `docker-compose.yml`
  * `Dockerfile`
* Open the workspace at `/workspace` inside the container
* Provide a terminal as user `vscode` (with `sudo` access)

---

## Running the App

Once inside the dev container
(terminal prompt looks like: `vscode ➜ /workspace (your-branch) $`):

---

### Method 1: Simple Foreground Run

```bash
command: odoo
```

---

### Method 2: Simple Foreground Run (Recommended for Development)

Run Odoo in the foreground with live reload:

```bash
command: odoo -c /etc/odoo/odoo.conf --dev=reload
```

* `--dev=reload` enables auto-reloading on code changes
* The config file `/etc/odoo/odoo.conf` is mounted from `./conf/odoo.conf`
* The config includes paths for both built-in and custom addons

---

### Method 3: Verbose Logging

For more detailed logs:

```bash
command: /usr/bin/odoo -c /etc/odoo/odoo.conf --log-level=debug --dev=reload
```

---

### Method 4: Background Run

Run Odoo in the background and free the terminal:

```bash
command: odoo -c /etc/odoo/odoo.conf --dev=reload &
```

Use this if you need the terminal for other tasks while Odoo runs.

---

## Accessing Services

* **Odoo Web Interface**
  [http://localhost:8069](http://localhost:8069)

* **Default Admin Password**
  `admin` (from `odoo.conf`)

* **Database Management**
  Create or restore databases via the web interface

* **PostgreSQL Connection**

```bash
psql -h db -U odoo -d postgres
```

Password: `odoo`

---

## Stopping the App

* **Foreground run**:
  Press `Ctrl + C`
  
* **Reload mode**:
  Press `Ctrl + C` **twice**

---

## Viewing Logs

* **Inside the container**
  Logs appear in real time when running in the foreground

* **From the host machine**

```bash
docker compose -f .devcontainer/docker-compose.yml logs -f odoo
```

---

## Customization

### Custom Addons

* Place your custom modules in:

./custom-addons/


* They are mounted to `/mnt/extra-addons`
* Included in `addons_path` via `odoo.conf`

### Configuration

* Edit:

```text
./conf/odoo.conf
```

* Examples:

  * Database settings
  * Log levels
* Rebuild the container if required

### Rebuilding the Container

If you update dev container files:

* Open **Command Palette**
* Select **Remote-Containers: Rebuild Container**

---