import unittest


class TestPublicAPIAsManager(unittest.TestCase):

    def test_fetch_list_of_teams(self):
        self.skipTest('TODO')

    def test_fetch_list_of_stations(self):
        self.skipTest('TODO')

    def test_fetch_list_of_routes(self):
        self.skipTest('TODO')

    def test_update_team(self):
        self.skipTest('TODO')

    def test_update_own_station(self):
        self.skipTest('TODO')

    def test_update_other_station(self):
        self.skipTest('TODO')

    def test_update_route(self):
        self.skipTest('TODO')

    def test_create_team(self):
        self.skipTest('TODO')

    def test_create_station(self):
        self.skipTest('TODO')

    def test_create_route(self):
        self.skipTest('TODO')

    def test_delete_team(self):
        self.skipTest('TODO')

    def test_delete_station(self):
        self.skipTest('TODO')

    def test_delete_route(self):
        self.skipTest('TODO')

    def assign_user_to_station(self):
        self.skipTest('TODO')

    def assign_user_to_two_stations(self):
        # should fail: integrity error
        self.skipTest('TODO')

    def unassign_user_from_station(self):
        self.skipTest('TODO')

    def assign_team_to_route(self):
        self.skipTest('TODO')

    def assign_team_to_two_routes(self):
        # should fail
        self.skipTest('TODO')

    def unassign_team_from_route(self):
        self.skipTest('TODO')

    def assign_role_to_user(self):
        self.skipTest('TODO')

    def unassign_role_from_user(self):
        self.skipTest('TODO')

    def assign_station_to_route(self):
        self.skipTest('TODO')

    def assign_station_to_two_routes(self):
        # should *pass*. A station can be on multiple routes!
        self.skipTest('TODO')

    def unassign_station_from_route(self):
        self.skipTest('TODO')

    def advance_team_state(self):
        self.skipTest('TODO')


class TestPublicAPIAsStationManager(unittest.TestCase):

    def test_fetch_list_of_teams(self):
        self.skipTest('TODO')

    def test_fetch_list_of_stations(self):
        self.skipTest('TODO')

    def test_fetch_list_of_routes(self):
        self.skipTest('TODO')

    def test_update_team(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_update_own_station(self):
        self.skipTest('TODO')

    def test_update_other_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_update_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_create_team(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_create_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_create_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_delete_team(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_delete_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_delete_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_user_to_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_user_to_two_stations(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_user_from_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_team_to_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_team_to_two_routes(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_team_from_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_role_to_user(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_role_from_user(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_station_to_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_station_to_two_routes(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_station_from_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def advance_team_state(self):
        self.skipTest('TODO')

    def advance_team_state_on_other_stations(self):
        # should fail: access denied
        self.skipTest('TODO')


class TestPublicAPIAsAnonymous(unittest.TestCase):

    def test_fetch_list_of_teams(self):
        self.skipTest('TODO')

    def test_fetch_list_of_stations(self):
        self.skipTest('TODO')

    def test_fetch_list_of_routes(self):
        self.skipTest('TODO')

    def test_update_team(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_update_own_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_update_other_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_update_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_create_team(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_create_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_create_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_delete_team(self):
        # should fail
        self.skipTest('TODO')

    def test_delete_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def test_delete_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_user_to_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_user_to_two_stations(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_user_from_station(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_team_to_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_team_to_two_routes(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_team_from_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_role_to_user(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_role_from_user(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_station_to_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def assign_station_to_two_routes(self):
        # should fail: access denied
        self.skipTest('TODO')

    def unassign_station_from_route(self):
        # should fail: access denied
        self.skipTest('TODO')

    def advance_team_state(self):
        # should fail: access denied
        self.skipTest('TODO')

    def advance_team_state_on_other_stations(self):
        # should fail: access denied
        self.skipTest('TODO')
