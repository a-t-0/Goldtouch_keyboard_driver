import unittest
import os
from ..src.Main import Main
from ..src.Activity import *
from ..src.Print_wfd import *
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

    def get_real_test_activities(self):
        project_introduction = Activity(
            description="Project Introduction",
            # duration_days=6,
            relative_start=Relative_start(True),
            colour="Cyan",
            hourly_wage=40,
        )

        organogram = Activity(
            description="Organogram",
            duration_days=1,
            relative_start=Relative_start(True,),
            colour="Cyan",
            hourly_wage=40,
        )
        project_procedures = Activity(
            description="Project Procedures",
            duration_days=1,
            relative_start=Relative_start(False, organogram),
            colour="Cyan",
            hourly_wage=40,
            incoming_feed=project_introduction,
            outgoing_feed=organogram,
        )
        return [project_introduction, organogram, project_procedures]

    # tests unit test on addTwo function of main class
    def test_addTwo(self):

        expected_result = 7
        result = self.main.addTwo(5)
        self.assertEqual(expected_result, result)

    def test_wfl_lines(self):
        parent_activity = Activity(
            description="parent_activity", colour="yellow", root_id=0,
        )
        paralel_child_one = Activity(
            description="paralel_child_one",
            duration_hrs=2,
            root_id=0,
            relative_start=Relative_start(True),
            parent=parent_activity,
            incoming_feed=parent_activity,
        )
        paralel_child_two = Activity(
            description="paralel_child_two",
            duration_hrs=6,
            root_id=1,
            relative_start=Relative_start(True),
            parent=parent_activity,
            incoming_feed=parent_activity,
        )

        # Call function to get wfd lines
        lines = generate_wfd_lines(
            [parent_activity, paralel_child_one, paralel_child_two]
        )
        print(f"wfl lines={lines}")

        # Assert the parent autoduration is recomputed
        expected_result = [
            "@startuml",
            '(*) -right-> "parent_activity"',
            '"parent_activity" --> "paralel_child_one"',
            '"parent_activity" --> "paralel_child_two"',
            '"paralel_child_one" -right-> (*)',
            '"paralel_child_two" -right-> (*)',
            "@enduml",
        ]
        result = lines
        self.assertEqual(expected_result, result)

    def test_activity_order(self):
        activities = self.get_real_test_activities()

        # Call function to get wfd lines
        lines = generate_wfd_lines(activities)

        # Assert the parent autoduration is recomputed
        expected_result = [
            "@startuml",
            '(*) -right-> "Project Introduction"',
            '"Project Introduction" -right-> "Project Procedures"',
            '"Project Procedures" -right-> "Organogram"',
            '"Organogram" -right-> (*)',
            "@enduml",
        ]
        result = lines
        self.assertEqual(expected_result, result)

    def test_is_fed_description(self):

        [
            project_introduction,
            organogram,
            project_procedures,
        ] = self.get_real_test_activities()
        activities = [project_introduction, organogram, project_procedures]

        # Call function to is_fed and feeder activities
        is_fed, is_feeder = get_fed_and_feeders(activities)
        is_fed_description = list(map(lambda x: x.description, is_fed))

        # Assert the parent autoduration is recomputed

        expected_is_fed = [project_procedures, organogram]
        expected_is_fed_description = list(
            map(lambda x: x.description, expected_is_fed)
        )

        self.assertEqual(expected_is_fed_description, is_fed_description)

    # Tests whether a is_feeder contains a child that is not included
    # in the incoming list of desired activities. For example,
    # suppose an activity of a child a from another parent feeds
    # into the first child b of the next parent, then a will feed into b,
    # but a will not be included in the list of activities that is passed
    # into get_fed_and_feeders
    def test_is_fed_for_child_from_previous_parent(self):

        [
            project_introduction,
            organogram,
            project_procedures,
        ] = self.get_real_test_activities()

        # project_introduction is now not a desired activity.
        # so it is as though it comes from another parent.
        activities = [organogram, project_procedures]

        # Call function to is_fed and feeder activities
        is_fed, is_feeder = get_fed_and_feeders(activities)

        # Get descriptions
        is_fed_description = list(map(lambda x: x.description, is_fed))
        is_feeder_description = list(map(lambda x: x.description, is_feeder))

        # Get the list of descriptions of the activities that are being fed.
        expected_is_fed = [project_procedures, organogram]
        expected_is_fed_description = list(
            map(lambda x: x.description, expected_is_fed)
        )

        # Get the list of descriptions of the activities that are feeders.
        expected_is_feeder = [project_introduction, project_procedures]
        expected_is_feeder_description = list(
            map(lambda x: x.description, expected_is_feeder)
        )

        self.assertEqual(expected_is_fed_description, is_fed_description)
        self.assertEqual(expected_is_feeder_description, is_feeder_description)

        # Test separate method that identifies activities from other parents.
        activities_from_previous_parents = get_activities_from_previous_parent(
            activities
        )
        self.assertEqual([project_introduction], activities_from_previous_parents)

    # Tests whether a is_feeder contains a child that is not included
    # in the incoming list of desired activities. For example,
    # suppose an activity of a child a from another parent feeds
    # into the first child b of the next parent, then a will feed into b,
    # but a will not be included in the list of activities that is passed
    # into get_fed_and_feeders
    def test_is_fed_for_child_from_next_parent(self):

        # TODO: make the order of the activity creation and storage
        # more logical/in chronological order: intro>procedures>organogram
        # in:get_real_test_activities
        [
            project_introduction,
            organogram,
            project_procedures,
        ] = self.get_real_test_activities()

        # organogram is now not a desired activity.
        # so it is as though it comes from another parent.
        activities = [project_introduction, project_procedures]

        # Call function to is_fed and feeder activities
        is_fed, is_feeder = get_fed_and_feeders(activities)

        # Get descriptions
        is_fed_description = list(map(lambda x: x.description, is_fed))
        is_feeder_description = list(map(lambda x: x.description, is_feeder))
        print(f"is_fed_description={is_fed_description}")

        # Get the list of descriptions of the activities that are being fed.
        expected_is_fed = [project_procedures, organogram]
        expected_is_fed_description = list(
            map(lambda x: x.description, expected_is_fed)
        )

        # Get the list of descriptions of the activities that are feeders.
        expected_is_feeder = [project_introduction, project_procedures]
        expected_is_feeder_description = list(
            map(lambda x: x.description, expected_is_feeder)
        )

        self.assertEqual(expected_is_fed_description, is_fed_description)
        self.assertEqual(expected_is_feeder_description, is_feeder_description)

        # Test separate method that identifies activities from other parents.
        activities_from_previous_parents = get_activities_from_next_parent(activities)
        self.assertEqual([organogram], activities_from_previous_parents)

    def test_is_feeder_description(self):

        [
            project_introduction,
            organogram,
            project_procedures,
        ] = self.get_real_test_activities()
        activities = [project_introduction, organogram, project_procedures]

        # Call function to is_fed and feeder activities
        is_fed, is_feeder = get_fed_and_feeders(activities)
        is_feeder_description = list(map(lambda x: x.description, is_feeder))

        # Get the list of descriptions of the activities that are feeders.
        expected_is_feeder = [project_introduction, project_procedures]
        expected_is_feeder_description = list(
            map(lambda x: x.description, expected_is_feeder)
        )

        self.assertEqual(expected_is_feeder_description, is_feeder_description)

    def test_get_first_activities(self):

        [
            project_introduction,
            organogram,
            project_procedures,
        ] = self.get_real_test_activities()
        activities = [project_introduction, organogram, project_procedures]

        # Call function to get initial_activities
        initial_activities = get_first_activities(activities)
        initial_activities_descriptions = list(
            map(lambda x: x.description, initial_activities)
        )

        # Assert the parent autoduration is recomputed
        expected_initial_activities = [project_introduction]
        expected_initial_activities_description = list(
            map(lambda x: x.description, expected_initial_activities)
        )

        self.assertEqual(
            expected_initial_activities_description, initial_activities_descriptions
        )

    def test_get_last_activities(self):

        [
            project_introduction,
            organogram,
            project_procedures,
        ] = self.get_real_test_activities()
        activities = [project_introduction, organogram, project_procedures]

        # Call function to get_last_activities
        last_activities = get_last_activities(activities)
        last_activities_descriptions = list(
            map(lambda x: x.description, last_activities)
        )

        # Assert the parent autoduration is recomputed
        expected_last_activities = [organogram]
        expected_last_activities_description = list(
            map(lambda x: x.description, expected_last_activities)
        )

        self.assertEqual(
            expected_last_activities_description, last_activities_descriptions
        )
