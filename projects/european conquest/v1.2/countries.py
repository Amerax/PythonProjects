borders = {
    "Albania": ["Greece", "Montenegro", "North Macedonia"],
    "Austria": ["Germany", "Czech Republic", "Slovakia", "Hungary", "Slovenia", "Italy", "Switzerland"],
    "Belarus": ["Latvia", "Lithuania", "Poland", "Ukraine"],
    "Belgium": ["France", "Germany", "Luxembourg", "Netherlands"],
    "Bulgaria": ["Greece", "Romania", "Serbia"],
    "Croatia": ["Hungary", "Montenegro", "Serbia", "Slovenia"],
    "Czech Republic": ["Austria", "Germany", "Poland", "Slovakia"],
    "Denmark": ["Germany"],
    "Finland": ["Norway", "Sweden"],
    "France": ["Belgium", "Germany", "Italy", "Luxembourg", "Spain", "Switzerland"],
    "Germany": ["Austria", "Belgium", "Czech Republic", "Denmark", "France", "Luxembourg", "Netherlands", "Poland", "Switzerland"],
    "Greece": ["Albania", "Bulgaria", "North Macedonia"],
    "Hungary": ["Austria", "Croatia", "Romania", "Serbia", "Slovakia", "Slovenia"],
    "Italy": ["Austria", "France", "Slovenia", "Switzerland"],
    "Latvia": ["Belarus", "Lithuania"],
    "Lithuania": ["Belarus", "Latvia", "Poland"],
    "Luxembourg": ["Belgium", "France", "Germany"],
    "Moldova": ["Romania", "Ukraine"],
    "Montenegro": ["Albania", "Croatia", "Serbia"],
    "Netherlands": ["Belgium", "Germany"],
    "North Macedonia": ["Albania", "Bulgaria", "Greece", "Serbia"],
    "Norway": ["Finland", "Sweden"],
    "Poland": ["Belarus", "Czech Republic", "Germany", "Lithuania", "Slovakia", "Ukraine"],
    "Portugal": ["Spain"],
    "Romania": ["Bulgaria", "Hungary", "Moldova", "Serbia", "Ukraine"],
    "Serbia": ["Bulgaria", "Croatia", "Hungary", "Montenegro", "North Macedonia", "Romania"],
    "Slovakia": ["Austria", "Czech Republic", "Hungary", "Poland", "Ukraine"],
    "Slovenia": ["Austria", "Croatia", "Hungary", "Italy"],
    "Spain": ["France", "Portugal"],
    "Sweden": ["Finland", "Norway"],
    "Switzerland": ["Austria", "France", "Germany", "Italy"],
    "Ukraine": ["Belarus", "Hungary", "Moldova", "Poland", "Romania", "Russian Federation", "Slovakia"]
}

country_codes = {
    "Albania": "al",
    "Austria": "at",
    "Belarus": "by",
    "Belgium": "be",
    "Bulgaria": "bg",
    "Switzerland": "ch",
    "Czech Republic": "cz",
    "Germany": "de",
    "Denmark": "dk",
    "Spain": "es",
    "Finland": "fi",
    "France": "fr",
    "Greece": "gr",
    "Croatia": "hr",
    "Hungary": "hu",
    "Italy": "it",
    "Lithuania": "lt",
    "Luxembourg": "lu",
    "Latvia": "lv",
    "Moldova": "md",
    "Montenegro": "me",
    "North Macedonia": "mk",
    "Netherlands": "nl",
    "Norway": "no",
    "Poland": "pl",
    "Portugal": "pt",
    "Romania": "ro",
    "Serbia": "rs",
    "Russian Federation": "ru",
    "Sweden": "se",
    "Slovenia": "si",
    "Slovakia": "sk",
    "Ukraine": "ua"
}

class country:
    def __init__(self, name, power, occupied, occupier, occupying):
        self.name = name
        self.power = power
        self.occupied = occupied
        self.occupier = occupier
        self.occupying = [occupying]
 