class Pokemon():
    name: str
    level: int
    attack: int
    defense: int
    sp_attack: int
    spe_defense: int


def calculate_attack_damag(attaker: Pokemon, defender: Pokemon):
    damage = ( ( ( ( (2*attaker.level)/5 + 2) * attaker.attack /defender.defense) / 50) +1) * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 