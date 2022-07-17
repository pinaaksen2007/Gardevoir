# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

NATURES = [
    "Adamant",
    "Bashful",
    "Bold",
    "Brave",
    "Calm",
    "Careful",
    "Docile",
    "Gentle",
    "Hardy",
    "Hasty",
    "Impish",
    "Jolly",
    "Lax",
    "Lonely",
    "Mild",
    "Modest",
    "Naive",
    "Naughty",
    "Quiet",
    "Quirky",
    "Rash",
    "Relaxed",
    "Sassy",
    "Serious",
    "Timid",
]

# == soon feature
EFFECTIVENESS_MULTIPLIERS = {
    "fire": {
        "water": .5,
        "fire": .5,
        "grass": 2,
        "ice": 2,
        "rock": .5,
        "bug": 2,
        "dragon": .5,
        "steel": 2
    },
    "normal": {
        "rock": .5,
        "ghost": .25,
        "steel": .5
    },
    "water": {
        "fire": 2,
        "water": .5,
        "grass": .5,
        "ground": 2,
        "rock": 2,
        "dragon": .5
    },
    "electric": {
        "water": 2,
        "electric": .5,
        "grass": .5,
        "ground": .25,
        "fly": 2,
        "dragon": .5
    },
    "grass": {
        "fire": .5,
        "water": 2,
        "grass": .5,
        "poison": .5,
        "ground": 2,
        "flying": .5,
        "bug": .5,
        "rock": 2,
        "dragon": .5,
        "steel": .5
    },
    "ice": {
        "fire": .5,
        "water": .5,
        "grass": 2,
        "ice": .5,
        "ground": 2,
        "fly": 2,
        "dragon": 2,
        "steel": .5
    },
    "fighting": {
        "normal": 2,
        "ice": 2,
        "poison":.5,
        "flying": .5,
        "psychic": .5,
        "bug": .5,
        "rock": 2,
        "ghost": .25,
        "dark": 2,
        "steel": 2,
        "fairy": .5
    },
    "poison": {
        "grass": 2,
        "poison": .5,
        "ground": .5,
        "rock": .5,
        "ghost": .5,
        "steel": .25,
        "fairy": 2
    },
    "ground": {
        "fire": .5,
        "electric": 2,
        "grass": .5,
        "poison": 2,
        "flying": .25,
        "bug": .5,
        "rock": 2,
        "steel": 2
    },
    "flying": {
        "electric": .5,
        "grass": 2,
        "fighting": 2,
        "bug": 2,
        "rock": .5,
        "steel": .5
    },
    "psychic": {
        "fighting": 2,
        "poison": 2,
        "psychic": .5,
        "dark": .25,
        "steel": .5
    },
    "bug": {
        "fire": .5,
        "grass": 2,
        "fighting": .5,
        "poison": .5,
        "flying": .5,
        "psychic": 2,
        "ghost": .5,
        "dark": 2,
        "steel": .5,
        "fairy": .5
    },
    "rock": {
        "fire": 2,
        "ice": 2,
        "fighting": .5,
        "ground": .5,
        "flying": 2,
        "bug": 2,
        "steel": .5
    },
    "ghost": {
        "normal": .25,
        "psychic": 2,
        "ghost": 2,
        "dark": .5
    },
    "dragon": {
        "dragon": 2,
        "steel": .5,
        "fairy": .25
    },
    "dark": {
        "fighting": .5,
        "psychic": 2,
        "ghost": 2,
        "dark": .5,
        "fairy": .5
    },
    "steel": {
        "fire": .5,
        "water": .5,
        "electric": .5,
        "ice": 2,
        "rock": 2,
        "steel": .5,
        "fairy": 2
    },
    "fairy": {
        "fire": .5,
        "fighting": 2,
        "poison": .5,
        "dragon": 2,
        "dark": 2,
        "steel": .5
    }
}

# == soon feature
NATURE_MULTIPLIERS = {
    "Hardy": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1,
        "sdef": 1,
        "spd": 1,
    },
    "Lonely": {
        "hp": 1,
        "atk": 1.1,
        "defn": 0.9,
        "satk": 1,
        "sdef": 1,
        "spd": 1,
    },
    "Brave": {
        "hp": 1,
        "atk": 1.1,
        "defn": 1,
        "satk": 1,
        "sdef": 1,
        "spd": 0.9,
    },
    "Adamant": {
        "hp": 1,
        "atk": 1.1,
        "defn": 1,
        "satk": 0.9,
        "sdef": 1,
        "spd": 1,
    },
    "Naughty": {
        "hp": 1,
        "atk": 1.1,
        "defn": 1,
        "satk": 1,
        "sdef": 0.9,
        "spd": 1,
    },
    "Bold": {
        "hp": 1,
        "atk": 0.9,
        "defn": 1.1,
        "satk": 1,
        "sdef": 1,
        "spd": 1,
    },
    "Docile": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1,
        "sdef": 1,
        "spd": 1,
    },
    "Relaxed": {
        "hp": 1,
        "atk": 1,
        "defn": 1.1,
        "satk": 1,
        "sdef": 1,
        "spd": 0.9,
    },
    "Impish": {
        "hp": 1,
        "atk": 1,
        "defn": 1.1,
        "satk": 0.9,
        "sdef": 1,
        "spd": 1,
    },
    "Lax": {
        "hp": 1,
        "atk": 1,
        "defn": 1.1,
        "satk": 1,
        "sdef": 0.9,
        "spd": 1,
    },
    "Timid": {
        "hp": 1,
        "atk": 0.9,
        "defn": 1,
        "satk": 1,
        "sdef": 1,
        "spd": 1.1,
    },
    "Hasty": {
        "hp": 1,
        "atk": 1,
        "defn": 0.9,
        "satk": 1,
        "sdef": 1,
        "spd": 1.1,
    },
    "Serious": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1,
        "sdef": 1,
        "spd": 1,
    },
    "Jolly": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 0.9,
        "sdef": 1,
        "spd": 1.1,
    },
    "Naive": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1,
        "sdef": 0.9,
        "spd": 1.1,
    },
    "Modest": {
        "hp": 1,
        "atk": 0.9,
        "defn": 1,
        "satk": 1.1,
        "sdef": 1,
        "spd": 1,
    },
    "Mild": {
        "hp": 1,
        "atk": 1,
        "defn": 0.9,
        "satk": 1.1,
        "sdef": 1,
        "spd": 1,
    },
    "Quiet": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1.1,
        "sdef": 1,
        "spd": 0.9,
    },
    "Bashful": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1,
        "sdef": 1,
        "spd": 1,
    },
    "Rash": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1.1,
        "sdef": 0.9,
        "spd": 1,
    },
    "Calm": {
        "hp": 1,
        "atk": 0.9,
        "defn": 1,
        "satk": 1,
        "sdef": 1.1,
        "spd": 1,
    },
    "Gentle": {
        "hp": 1,
        "atk": 1,
        "defn": 0.9,
        "satk": 1,
        "sdef": 1.1,
        "spd": 1,
    },
    "Sassy": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1,
        "sdef": 1.1,
        "spd": 0.9,
    },
    "Careful": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 0.9,
        "sdef": 1.1,
        "spd": 1,
    },
    "Quirky": {
        "hp": 1,
        "atk": 1,
        "defn": 1,
        "satk": 1,
        "sdef": 1,
        "spd": 1,
    },
}