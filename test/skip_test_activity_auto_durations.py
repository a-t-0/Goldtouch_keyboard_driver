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
            description="", colour="yellow", duration=10, new_tag=0
        )
        paralel_child_one = Activity(
            description="",
            duration=2,
            new_tag=0,
            start=Start("0", True),
            parent=parent_activity,
        )
        paralel_child_two = Activity(
            description="",
            duration=6,
            new_tag=1,
            start=Start("0", True),
            parent=parent_activity,
        )

        # Call function to compute auto duration

        # Assert the parent autoduration is recomputed
        expected_result = 6
        result = parent_activity.auto_duration
        self.assertEqual(expected_result, result)

    def test_duration_of_children_with_one_in_serie_at_start(self):
        parent_activity = Activity(
            description="", colour="yellow", duration=10, new_tag=0
        )
        paralel_child_one = Activity(
            description="",
            duration=2,
            new_tag=0,
            start=Start("0", True),
            parent=parent_activity,
        )
        serie_child_two = Activity(
            description="",
            duration=6,
            new_tag=1,
            start=Start("0", True),
            parent=paralel_child_one,
        )

        # Call function to compute auto duration

        # Assert the parent autoduration is recomputed
        # even though the child is in serie, it starts at the start of the parent, so still runs in paralell.
        expected_result = 6
        result = parent_activity.auto_duration
        self.assertEqual(expected_result, result)

    def test_duration_of_children_with_one_in_serie_at_end(self):
        parent_activity = Activity(
            description="", colour="yellow", duration=10, new_tag=0
        )
        paralel_child_one = Activity(
            description="",
            duration=2,
            new_tag=0,
            start=Start("0", True),
            parent=parent_activity,
        )
        serie_child_two = Activity(
            description="",
            duration=6,
            new_tag=1,
            start=Start("0", False),
            parent=paralel_child_one,
        )

        # Call function to compute auto duration

        # Assert the parent autoduration is recomputed
        expected_result = 8
        result = parent_activity.auto_duration
        self.assertEqual(expected_result, result)

    def test_duration_of_children_with_grand_child(self):
        parent_activity = Activity(
            description="", colour="yellow", duration=10, new_tag=0
        )
        paralel_child_one = Activity(
            description="",
            duration=2,
            new_tag=0,
            start=Start("0", True),
            parent=parent_activity,
        )
        serie_child_two = Activity(
            description="",
            duration=6,
            new_tag=1,
            start=Start("0", True),
            parent=paralel_child_one,
        )
        grand_child_one = Activity(
            description="",
            duration=15,
            new_tag=0,
            start=Start("0", False),
            parent=serie_child_two,
        )

        # Call function to compute auto duration

        # Assert the parent autoduration is recomputed
        expected_result = 6 + 15
        result = parent_activity.auto_duration
        self.assertEqual(expected_result, result)

    def test_duration_of_children_with_grand_child_in_series(self):
        parent_activity = Activity(
            description="", colour="yellow", duration=10, new_tag=0
        )
        paralel_child_one = Activity(
            description="",
            duration=2,
            new_tag=0,
            start=Start("0", True),
            parent=parent_activity,
        )
        serie_child_two = Activity(
            description="",
            duration=6,
            new_tag=1,
            start=Start("0", False),
            parent=paralel_child_one,
        )
        grand_child_one = Activity(
            description="",
            duration=15,
            new_tag=0,
            start=Start("0", False),
            parent=serie_child_two,
        )

        # Call function to compute auto duration

        # Assert the parent autoduration is recomputed
        expected_result = 6 + 15
        result = parent_activity.auto_duration
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
