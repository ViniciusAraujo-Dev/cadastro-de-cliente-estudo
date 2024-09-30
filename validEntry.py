from modulos import*

class Validadores:
    def validate_entry3(self, text):
        if text =="": return True
        try:
            valor = int(text)
        except ValueError:
            return False
        return 0 <= valor <= 1000