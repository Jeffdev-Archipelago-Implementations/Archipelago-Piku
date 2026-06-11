from BaseClasses import CollectionState
from Fill import distribute_items_restrictive

from .bases import PikunikuTestBase


class EarlyScarecrowFaceTestMixin:
    def assert_scarecrow_face_is_in_sphere_one(self) -> None:
        distribute_items_restrictive(self.multiworld)

        scarecrow_face_location = next(
            location
            for location in self.multiworld.get_filled_locations()
            if location.item.name == "Scarecrow Face" and location.item.player == self.player
        )

        empty_state = CollectionState(self.multiworld)
        self.assertTrue(scarecrow_face_location.can_reach(empty_state))


class TestEarlyLocalScarecrowFace(PikunikuTestBase, EarlyScarecrowFaceTestMixin):
    options = {
        "early_scarecrow_face": "early_local",
    }

    def test_scarecrow_face_is_in_sphere_one(self) -> None:
        self.assert_scarecrow_face_is_in_sphere_one()

    def test_scarecrow_face_is_local(self) -> None:
        self.assertIn("Scarecrow Face", self.multiworld.local_early_items[self.player])


class TestEarlyGlobalScarecrowFace(PikunikuTestBase, EarlyScarecrowFaceTestMixin):
    options = {
        "early_scarecrow_face": "early_global",
    }

    # In a solo multiworld, "early global" still means sphere 1 of this world.
    def test_scarecrow_face_is_in_sphere_one(self) -> None:
        self.assert_scarecrow_face_is_in_sphere_one()


class TestShuffledScarecrowFace(PikunikuTestBase):
    options = {
        "early_scarecrow_face": "shuffled",
    }

    def test_no_early_item_registered(self) -> None:
        self.assertNotIn("Scarecrow Face", self.multiworld.early_items[self.player])
        self.assertNotIn("Scarecrow Face", self.multiworld.local_early_items[self.player])
