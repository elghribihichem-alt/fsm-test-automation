# fsm-test-automation
# fsm-test-automation

Tests automatisés pour une application FSM (Field Service Management).

Suite de tests end-to-end basée sur **Python**, **Playwright** et **Pytest**, structurée selon le patron **Page Object Model (POM)**.

## 📋 Prérequis

| Outil | Version |
|---|---|
| Python | 3.11+ |
| Node.js | LTS (18+) — requis par l'outillage CI |
| Git | Dernière version |

> **NB :** Assurez-vous que l'application FSM est démarrée et accessible à l'URL définie dans le fichier `.env` avant de lancer les tests.

## 🚀 Installation

### Cloner le dépôt
\`\`\`bash
git clone https://github.com/elghribihichem-alt/fsm-test-automation.git
cd fsm-test-automation
\`\`\`

### Créer et activer un environnement virtuel
\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows
\`\`\`

### Installer les dépendances
\`\`\`bash
pip install -r requirements.txt
playwright install
\`\`\`

## ⚙️ Configuration

Créer un fichier `.env` à la racine (non versionné) :

\`\`\`env
BASE_URL=http://localhost:3000
USERNAME=admin
PASSWORD=admin123
\`\`\`

## ▶️ Lancer les tests

\`\`\`bash
pytest                              # Tous les tests (headless)
pytest --headed                     # Navigateur visible
pytest --headed --slowmo 1000       # Mode debug ralenti
pytest --browser chromium           # Navigateur spécifique
pytest -n 4                         # Parallèle (4 workers)
pytest -m smoke                     # Filtrer par marqueur
pytest --html=reports/report.html --self-contained-html
\`\`\`

## 🏗 Structure du projet

\`\`\`
fsm-test-automation/
├── pages/               # Page Objects (POM)
│   └── base_page.py
├── tests/               # Scénarios de test
├── conftest.py          # Fixtures Pytest globales
├── pytest.ini           # Configuration Pytest
├── requirements.txt     # Dépendances
├── .env                 # Variables d'environnement (non versionné)
└── README.md
\`\`\`

## 🏷 Marqueurs

| Marqueur | Description |
|---|---|
| `@pytest.mark.smoke` | Suite de fumée — chemin critique rapide |
| `@pytest.mark.regression` | Suite de régression complète |
| `@pytest.mark.modules` | Tests dédiés aux modules métier |