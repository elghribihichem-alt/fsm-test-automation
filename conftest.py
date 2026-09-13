"""
Configuration globale Pytest pour les tests Playwright.
Charge les variables d'environnement et fournit les fixtures de navigateur.
"""
import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

# Charge les variables du fichier .env
load_dotenv()

# Configuration depuis .env
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
USERNAME = os.getenv("USERNAME", "admin")
PASSWORD = os.getenv("PASSWORD", "admin123")


@pytest.fixture(scope="session")
def browser():
    """Lance un navigateur Playwright pour toute la session de test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    """Crée un nouveau contexte isolé pour chaque test."""
    context = browser.new_context(
        base_url=BASE_URL,
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True,
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Fournit une page vierge pour chaque test."""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def credentials():
    """Retourne les identifiants de connexion depuis .env."""
    return {"username": USERNAME, "password": PASSWORD}


# Hook pour ajouter le nom du test au rapport HTML
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Ajoute des informations supplémentaires au rapport."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Screenshot sauvegardé : {screenshot_path}")