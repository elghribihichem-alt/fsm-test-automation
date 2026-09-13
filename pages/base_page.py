"""
Classe de base pour tous les Page Objects.
Fournit des méthodes communes réutilisables par tous les modules FSM.
"""
from playwright.sync_api import Page, expect
from typing import Optional


class BasePage:
    """Page Object de base dont héritent tous les autres modules."""

    def __init__(self, page: Page):
        self.page = page

    # ---------- Navigation ----------
    def goto(self, url: str) -> None:
        """Navigue vers une URL (relative ou absolue)."""
        self.page.goto(url)

    def get_url(self) -> str:
        """Retourne l'URL actuelle."""
        return self.page.url

    def get_title(self) -> str:
        """Retourne le titre de la page."""
        return self.page.title()

    # ---------- Interactions ----------
    def click(self, selector: str, timeout: int = 5000) -> None:
        """Clique sur un élément identifié par son sélecteur."""
        self.page.locator(selector).click(timeout=timeout)

    def fill(self, selector: str, value: str, timeout: int = 5000) -> None:
        """Remplit un champ de saisie."""
        self.page.locator(selector).fill(value, timeout=timeout)

    def select_option(self, selector: str, value: str) -> None:
        """Sélectionne une option dans un <select>."""
        self.page.locator(selector).select_option(value)

    def check(self, selector: str) -> None:
        """Coche une case à cocher."""
        self.page.locator(selector).check()

    def uncheck(self, selector: str) -> None:
        """Décoche une case à cocher."""
        self.page.locator(selector).uncheck()

    def press_key(self, selector: str, key: str) -> None:
        """Appuie sur une touche dans un champ."""
        self.page.locator(selector).press(key)

    # ---------- Attentes ----------
    def wait_for_element(self, selector: str, timeout: int = 10000) -> None:
        """Attend qu'un élément soit visible."""
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    def wait_for_url(self, url_pattern: str, timeout: int = 10000) -> None:
        """Attend que l'URL corresponde à un motif."""
        self.page.wait_for_url(url_pattern, timeout=timeout)

    # ---------- Vérifications ----------
    def is_visible(self, selector: str) -> bool:
        """Vérifie si un élément est visible."""
        return self.page.locator(selector).is_visible()

    def get_text(self, selector: str) -> str:
        """Récupère le texte d'un élément."""
        return self.page.locator(selector).inner_text()

    def get_attribute(self, selector: str, attribute: str) -> Optional[str]:
        """Récupère la valeur d'un attribut d'un élément."""
        return self.page.locator(selector).get_attribute(attribute)

    def expect_visible(self, selector: str) -> None:
        """Assertion : l'élément doit être visible."""
        expect(self.page.locator(selector)).to_be_visible()

    def expect_text(self, selector: str, text: str) -> None:
        """Assertion : l'élément doit contenir le texte donné."""
        expect(self.page.locator(selector)).to_contain_text(text)

    # ---------- Utilitaires ----------
    def screenshot(self, path: str, full_page: bool = True) -> None:
        """Prend une capture d'écran."""
        self.page.screenshot(path=path, full_page=full_page)

    def scroll_to_bottom(self) -> None:
        """Fait défiler jusqu'en bas de la page."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def reload(self) -> None:
        """Recharge la page."""
        self.page.reload()