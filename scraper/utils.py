#regex
import re
class Utils:
    @staticmethod
    def clean_number(value):
        return float(value.replace('$', '').replace(',', '').replace('%', '').split()[0])

    @staticmethod
    def clean_integer(value):
        return int(value.replace(',', '').split()[0])
    
    @staticmethod
    def _get_text(self, element):
        return element.text.strip() if element else None
    
    @staticmethod
    def extract_number(value):
        # Use a regular expression to find the number after the dollar sign
        match = re.search(r'\$([\d,]+)', value)
        if match:
            # Remove any commas and convert to integer
            return int(match.group(1).replace(',', ''))
        return None

    @staticmethod
    def _parse_int(self, text):
        if text:
            text = re.sub(r'[^\d.]', '', text)  # Remove non-numeric characters
            try:
                return int(float(text))
            except ValueError:
                return None
        return None

    @staticmethod
    def _parse_float(self, text):
        if text:
            text = re.sub(r'[^\d.]', '', text)  # Remove non-numeric characters
            try:
                return float(text)
            except ValueError:
                return None
        return None

    @staticmethod
    def _parse_percentage(self, text):
        if text:
            text = text.replace('%', '').strip()
            try:
                return float(text)
            except ValueError:
                return None
        return None
