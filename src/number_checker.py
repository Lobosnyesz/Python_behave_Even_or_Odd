"""
Szám ellenőrző modul - páros/páratlan ellenőrzés

TODO: Implementáld a check_number függvényt!
"""


def check_number(number):
    """
    Ellenőrzi, hogy a szám páros vagy páratlan.
    
    Args:
        number (int): Az ellenőrizendő szám
        
    Returns:
        str: "even" ha páros, "odd" ha páratlan
    """
    # TODO: Implementáld a logikát!
    # Használd a modulo operátort (%)
    if number % 2 == 0:
        # Ha number % 2 == 0, akkor páros → "even"
        return "even"
    # Egyébként páratlan → "odd"
    return "odd"
