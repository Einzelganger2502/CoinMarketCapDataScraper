import re
class Utils:
    def _get_text(self, element):
        return element.text.strip() if element else None

    def _parse_int(self, text):
        if text:
            text = re.sub(r'[^\d.]', '', text)  # Remove non-numeric characters
            try:
                return int(float(text))
            except ValueError:
                return None
        return None

    def _parse_float(self, text):
        if text:
            text = re.sub(r'[^\d.]', '', text)  # Remove non-numeric characters
            try:
                return float(text)
            except ValueError:
                return None
        return None

    def _parse_percentage(self, text):
        if text:
            text = text.replace('%', '').strip()
            try:
                return float(text)
            except ValueError:
                return None
        return None
    