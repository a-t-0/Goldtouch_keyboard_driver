import unittest
import os
from ..src.Main import Main
from ..src.Activity import *
import testbook


class Test_main(unittest.TestCase):

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super(Test_main, self).__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()

        self.main = Main(6)
        print(f"self.main.addTwo(3)={self.main.addTwo(3)}")

    # returns the directory of this script regardles of from which level the code is executed
    def get_script_dir(self):
        return os.path.dirname(__file__)

    # tests unit test on addTwo function of main class
    def test_addTwo(self):

        expected_result = 7
        result = self.main.addTwo(5)
        self.assertEqual(expected_result, result)

    def test_duration_of_children(self):
        parent_activity = Activity(
            description="parent_activity",
            colour="yellow",
            root_id=0,
        )
        paralel_child_one = Activity(
            description="paralel_child_one",
            duration=2,
            root_id=0,
            relative_start=Relative_start(True),
            parent=parent_activity,
        )
        paralel_child_two = Activity(
            description="paralel_child_two",
            duration=6,
            root_id=1,
            relative_start=Relative_start(True),
            parent=parent_activity,
        )

        # Call function to compute auto duration
        parent_activity.set_durations(parent_activity, [parent_activity])

        # Assert the parent autoduration is recomputed
        expected_result = 6
        result = parent_activity.duration
        self.assertEqual(expected_result, result)

    def test_duration_of_children_with_one_in_serie_at_start(self):
        parent_activity = Activity(
            description="root",
            colour="yellow",
            root_id=0,
        )
        paralel_child_one = Activity(
            description="paralel_child_one",
            duration=2,
            root_id=0,
            relative_start=Relative_start(True),
            parent=parent_activity,
        )
        serie_child_two = Activity(
            description="paralel_child_two",
            duration=6,
            root_id=1,
            relative_start=Relative_start(False, paralel_child_one),
            parent=parent_activity,
        )

        # Call function to compute auto duration
        parent_activity.set_durations(parent_activity, [parent_activity])

        # Assert the parent autoduration is recomputed
        # even though the child is in serie, it starts at the start of the parent, so still runs in paralell.
        expected_result = 8
        result = parent_activity.duration
        self.assertEqual(expected_result, result)

    def test_duration_of_children_with_one_in_serie_at_end(self):
        parent_activity = Activity(
            description="root",
            colour="yellow",
            root_id=0,
        )
        paralel_child_one = Activity(
            description="",
            duration=2,
            root_id=0,
            relative_start=Relative_start(True),
            parent=parent_activity,
        )

        grand_child = Activity(
            description="",
            duration=6,
            root_id=0,
            # Assert this throws an error.
            # A grand child can not start at the end
            # of its parents.
            relative_start=Relative_start(False, paralel_child_one),
            parent=paralel_child_one,
        )

        with self.assertRaises(Exception) as context:
            # Call function to compute auto duration
            parent_activity.set_durations(parent_activity, [parent_activity])
        self.assertTrue(
            "Child cannot start after a parent is done." in str(context.exception)
        )

    def test_child_cannot_start_after_parent_is_caught(self):
        parent_activity = Activity(
            description="root",
            colour="yellow",
            root_id=0,
        )

        with self.assertRaises(Exception) as context:
            # Call function to compute auto duration
            paralel_child_one = Activity(
                description="paralel_child_one",
                duration=2,
                root_id=0,
                relative_start=Relative_start(False),
                parent=parent_activity,
            )
        self.assertTrue(
            "A child activity cannot start at the end of its parent."
            in str(context.exception)
        )

    def test_duration_of_children_with_grand_child(self):
        parent_activity = Activity(
            description="root",
            colour="yellow",
            root_id=0,
        )
        paralel_child_one = Activity(
            description="paralel_child_one",
            root_id=0,
            relative_start=Relative_start(True),
            parent=parent_activity,
        )
        grand_child_one = Activity(
            description="grand_child_one",
            duration=6,
            root_id=0,
            relative_start=Relative_start(True),
            parent=paralel_child_one,
        )
        grand_child_two = Activity(
            description="grand_child_two",
            duration=15,
            root_id=1,
            relative_start=Relative_start(False, grand_child_one),
            parent=paralel_child_one,
        )

        # Call function to compute auto duration
        parent_activity.set_durations(parent_activity, [parent_activity])

        # Assert the parent autoduration is recomputed
        expected_result = 6 + 15
        result = parent_activity.duration
        self.assertEqual(expected_result, result)

    def test_duration_of_children_with_grand_child_in_paralel(self):
        parent_activity = Activity(
            description="root",
            colour="yellow",
            root_id=0,
        )
        paralel_child_one = Activity(
            description="paralel_child_one",
            root_id=0,
            relative_start=Relative_start(True),
            parent=parent_activity,
        )
        grand_child_one = Activity(
            description="grand_child_one",
            duration=6,
            root_id=0,
            relative_start=Relative_start(True),
            parent=paralel_child_one,
        )
        grand_child_two = Activity(
            description="grand_child_two",
            duration=15,
            root_id=1,
            relative_start=Relative_start(True, grand_child_one),
            parent=paralel_child_one,
        )

        # Call function to compute auto duration
        parent_activity.set_durations(parent_activity, [parent_activity])

        # Assert the parent autoduration is recomputed
        expected_result = 15
        result = parent_activity.duration
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
