from dataclasses import dataclass

from Options import Choice, DeathLink, OptionGroup, PerGameCommonOptions, Range, Toggle


class Coinsanity(Toggle):
    """
    Adds every freestanding coin in the world as a location check.
    When enabled, Coins are added to the item pool as progression items,
    and shop purchases logically require receiving Coins.
    """

    display_name = "Coinsanity"


class EarlyScarecrowFace(Choice):
    """
    Determines how the Scarecrow Face is placed.

    - Early Local: Placed in an early sphere in your own world.
    - Early Global: Placed in an early sphere any world in the multiworld. (Default)
    - Shuffled: Placed anywhere in the multiworld. This will make you get stuck quickly.
    """

    display_name = "Early Scarecrow Face"

    option_early_local = 0
    option_early_global = 1
    option_shuffled = 2

    default = option_early_global


class CoopLevels(Toggle):
    """
    Adds the Piku & Niku co-op levels to the randomizer.
    A "Co-op Level Access" item is added to the item pool, which is required
    to access the co-op level completion checks and the Piku & Niku trophies.
    """

    display_name = "Co-op Levels"


class DeathLinkAmnesty(Range):
    """
    How many deaths it takes to send a DeathLink. DeathLinks only apply during the
    platforming challenges or bossfights.
    """

    display_name = "Death Link Amnesty"

    range_start = 1
    range_end = 30

    default = 10


@dataclass
class PikunikuOptions(PerGameCommonOptions):
    coinsanity: Coinsanity
    coop_levels: CoopLevels
    early_scarecrow_face: EarlyScarecrowFace
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty


option_groups = [
    OptionGroup(
        "Sanity Options",
        [Coinsanity, CoopLevels],
    ),
    OptionGroup(
        "Item Options",
        [EarlyScarecrowFace],
    ),
    OptionGroup(
        "Death Link Options",
        [DeathLink, DeathLinkAmnesty],
    ),
]

option_presets = {
    "everything": {
        "coinsanity": True,
        "coop_levels": True,
    },
}
