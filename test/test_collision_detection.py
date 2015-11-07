import unittest
from computation_package.collision_detection import CollisionDetection
from plane_controller import plane

_author_ = 'group'


# plane.PlaneObject( id_code, loc_x, loc_y, loc_z, vec_x, vec_y, vec_z)
# determine_collision(self, p_a, potential_intruder):

class TestCollisionDetection(unittest.TestCase):
    def setUp(self):
        self.a_id_code = "0011"
        self.b_id_code = "0022"

    # same_direction_same_speed_not_touching
    def test_same_direction_same_speed_not_touching(self):  # 1
        plane_a_location, plane_a_velocity = [0, 0, 0], [100, 100, 100]
        plane_b_location, plane_b_velocity = [300, 200, 200], [100, 100, 100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # same_direction_same_speed_boundry_touching
    def test_same_direction_same_speed_boundry_touching(self):  # 2
        plane_a_location, plane_a_velocity = [0, 0, 0], [100, 100, 100]
        plane_b_location, plane_b_velocity = [400, 0, 0], [100, 100, 100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # same_direction_same_speed_intruding
    def test_same_direction_same_speed_intruding(self):  # 3
        plane_a_location, plane_a_velocity = [0, 0, 0], [100, 100, 100]
        plane_b_location, plane_b_velocity = [300, 200, 170], [100, 100, 100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Cases 4 - 7 assume same direction different speed
    def test_plane_A_catching_up_B(self):  # 4
        plane_a_location, plane_a_velocity = [0, 0, 0], [100, 100, 0]
        plane_b_location, plane_b_velocity = [400, 400, 0], [50, 50, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_not_catching_up_to_B(self):  # 5
        plane_a_location, plane_a_velocity = [0, 0, 0], [100, 100, 0]
        plane_b_location, plane_b_velocity = [400, 400, 0], [200, 200, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Non-moving aircraft A (non-rotary), with aircraft B moving towards the aircraft
    def test_non_moving_A_with_B_moving_pos_X(self):  # 6
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-500, 0, 0], [10, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_with_B_moving_neg_X(self):  # 7
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [500, 0, 0], [-10, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_with_B_moving_pos_Y(self):  # 8
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [0, -500, 0], [0, 20, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_with_B_moving_neg_Y(self):  # 9
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [0, 500, 0], [0, -20, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_with_B_moving_pos_Z(self):  # 10
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [0, 0, -500], [0, 0, 30]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def ttest_non_moving_A_with_B_moving_neg_Z(self):  # 11
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [0, 0, 500], [0, 0, -30]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Non-moving aircraft A and aircraft B coming from different quadrants.
    def test_non_moving_A_positive_x_y_z_quadrant(self):  # 12
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [500, 500, 500], [-10, -10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_negative_x_y_z_quadrant(self):  # 13
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-500, -500, -500], [10, 10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_B_coming_negative_x_positive_y_z_quadrant(self):  # 14
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-500, 500, 500], [10, -10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_B_coming_negative_y_positive_x_z_quadrant(self):  # 15
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [500, -500, 500], [-10, 10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_B_coming_negative_z_positive_x_y_quadrant(self):  # 16
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [500, 500, -500], [-10, -10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_B_coming_negative_x_z_positive_y_quadrant(self):  # 17
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-500, 500, -500], [10, -10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_B_coming_negative_y_z_positive_x_quadrant(self):  # 18
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [500, -500, -500], [-10, 10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_B_coming_negative_x_y_positive_z_quadrant(self):  # 19
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-500, -500, 500], [10, 10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Two aircraft moving along the same axis:
    def test_moving_2_planes_toward_on_pos_Z_axis(self):  # 20
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 10]
        plane_b_location, plane_b_velocity = [0, 0, 500], [0, 0, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_toward_on_neg_Z_axis(self):  # 21
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, -10]
        plane_b_location, plane_b_velocity = [0, 0, -500], [0, 0, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_toward_on_pos_Y_axis(self):  # 22
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 10, 0]
        plane_b_location, plane_b_velocity = [0, 500, 0], [0, -10, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_toward_on_neg_Y_axis(self):  # 23
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, -10, 0]
        plane_b_location, plane_b_velocity = [0, -500, 0], [0, 10, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_toward_on_pos_x_axis(self):  # 24
        plane_a_location, plane_a_velocity = [0, 0, 0], [10, 0, 0]
        plane_b_location, plane_b_velocity = [500, 0, 0], [-10, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_toward_on_neg_x_axis(self):  # 25
        plane_a_location, plane_a_velocity = [0, 0, 0], [-10, 0, 0]
        plane_b_location, plane_b_velocity = [-500, 0, 0], [10, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Both aircraft are in same quadrant:
    def test_moving_2_planes_pos_x_y_z_quadrant_collision(self):  # 26
        plane_a_location, plane_a_velocity = [50, 50, 10], [20, 20, 20]
        plane_b_location, plane_b_velocity = [500, 500, 500], [-10, -10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_neg_x_y_z_quadrant_collision(self):  # 27
        plane_a_location, plane_a_velocity = [-50, -50, -10], [-20, -20, -20]
        plane_b_location, plane_b_velocity = [-500, -500, -500], [10, 10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_neg_y_pos_x_z_quadrant_collision(self):  # 28
        plane_a_location, plane_a_velocity = [50, -50, 10], [20, -20, 20]
        plane_b_location, plane_b_velocity = [500, -500, 500], [-10, 10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_neg_x_z_pos_y_quadrant_collision(self):  # 29
        plane_a_location, plane_a_velocity = [-50, 50, -10], [-20, 20, -20]
        plane_b_location, plane_b_velocity = [-500, 500, -500], [10, -10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_neg_z_pos_x_y_quadrant_collision(self):  # 30
        plane_a_location, plane_a_velocity = [50, 50, -10], [20, 20, -20]
        plane_b_location, plane_b_velocity = [500, 500, -500], [-10, -10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_neg_x_y_pos_z_quadrant_collision(self):  # 31
        plane_a_location, plane_a_velocity = [-50, -50, 10], [-20, -20, 20]
        plane_b_location, plane_b_velocity = [-500, -500, 500], [10, 10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_neg_y_z_pos_x_quadrant_collision(self):  # 32
        plane_a_location, plane_a_velocity = [50, -50, -10], [20, -20, -20]
        plane_b_location, plane_b_velocity = [500, -500, -500], [-10, 10, 10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_moving_2_planes_neg_x_pos_y_z_quadrant_collision(self):  # 33
        plane_a_location, plane_a_velocity = [-50, 50, 10], [-20, 20, 20]
        plane_b_location, plane_b_velocity = [-500, 500, 500], [10, -10, -10]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Start out in different quadrants
    def test_plane_A_neg_x_y_z_quadrant_towards_plane_B_pos_x_y_z_quadrant(self):  # 34
        plane_a_location, plane_a_velocity = [-400, -700, -300], [100, 100, 100]
        plane_b_location, plane_b_velocity = [700, 400, 800], [-100, -100, -100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_pos_x_y_z_quadrant_towards_plane_B_neg_x_y_z_quadrant(self):  # 35
        plane_a_location, plane_a_velocity = [400, 700, 300], [-100, -100, -100]
        plane_b_location, plane_b_velocity = [-700, -400, -800], [100, 100, 100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_neg_x_pos_y_z_quadrant_towards_plane_B_neg_y_z_pos_x_quadrant(self):  # 36
        plane_a_location, plane_a_velocity = [-400, 700, 300], [100, -100, -100]
        plane_b_location, plane_b_velocity = [700, -400, -800], [-100, 100, 100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_neg_y_z_pos_x_quadrant_towards_plane_B_neg_x_pos_y_z_quadrant(self):  # 37
        plane_a_location, plane_a_velocity = [400, -700, -300], [-100, 100, 100]
        plane_b_location, plane_b_velocity = [-700, 400, 800], [100, -100, -100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_neg_y_pos_x_z_quadrant_towards_plane_B_neg_x_z_pos_y_quadrant(self):  # 38
        plane_a_location, plane_a_velocity = [400, -700, 300], [-100, 100, -100]
        plane_b_location, plane_b_velocity = [-700, 400, -800], [100, -100, 100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_neg_x_z_pos_y_quadrant_towards_plane_B_neg_y_pos_x_z_quadrant(self):  # 39
        plane_a_location, plane_a_velocity = [-400, 700, -300], [100, -100, 100]
        plane_b_location, plane_b_velocity = [700, -400, 800], [-100, 100, -100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_neg_z_pos_x_y_quadrant_towards_plane_B_neg_x_y_pos_z_quadrant(self):  # 40
        plane_a_location, plane_a_velocity = [400, 700, -300], [-100, -100, 100]
        plane_b_location, plane_b_velocity = [-700, -400, 800], [100, 100, -100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_plane_A_neg_x_y_pos_z_quadrant_towards_plane_B_neg_x_y_pos_z_quadrant(self):  # 41
        plane_a_location, plane_a_velocity = [-400, -700, 300], [100, 100, -100]
        plane_b_location, plane_b_velocity = [700, 400, -800], [-100, -100, 100]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Test plane touches edge:
    def test_non_moving_A_plane_B_close_to_plane_edge(self):  # 42
        plane_a_location, plane_a_velocity = [-400, 401, 0], [100, 0, 0]
        plane_b_location, plane_b_velocity = [0, 0, 0], [0, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_plane_B_grazing_plane_A_edge(self):  # 43
        plane_a_location, plane_a_velocity = [-400, 400, 0], [100, 0, 0]
        plane_b_location, plane_b_velocity = [0, 0, 0], [0, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_non_moving_A_plane_B_entering_plane_A_edge(self):  # 44
        plane_a_location, plane_a_velocity = [-400, 399, 0], [100, 0, 0]
        plane_b_location, plane_b_velocity = [0, 0, 0], [0, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Test cross in past
    def test_cross_paths_in_past1(self):  # 45
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [401, 0, 0], [100, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_cross_paths_in_past2(self):  # 46
        plane_a_location, plane_a_velocity = [200, 100, 100], [9999, 9999, 9999]
        plane_b_location, plane_b_velocity = [-100, -100, -100], [-9999, -9999, -9999]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_cross_paths_in_past3(self):  # 47
        plane_a_location, plane_a_velocity = [-200, -100, -100], [-9999, -9999, -9999]
        plane_b_location, plane_b_velocity = [100, 100, 100], [9999, 9999, 9999]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_cross_paths_in_past4(self):  # 48
        plane_a_location, plane_a_velocity = [400, 400, 400], [400, 0, 0]
        plane_b_location, plane_b_velocity = [-400, 1200, 400], [0, 400, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_cross_paths_in_past5(self):  # 49
        plane_a_location, plane_a_velocity = [-400, -400, -400], [-400, 0, 0]
        plane_b_location, plane_b_velocity = [400, -1200, -400], [0, -400, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_cross_in_past6(self):  # 50
        plane_a_location, plane_a_velocity = [50, 150, 40], [-70, -420, -90]
        plane_b_location, plane_b_velocity = [350, 20, 840], [110, -440, 370]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_collision_beginning(self):  # 51
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [400, 0, 0], [100, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_edge1(self):  # 52
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [0, 0, 0], [100, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_edge2(self):  # 53
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-399, 0, 0], [100, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_edge3(self):  # 54
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-400, 0, 0], [100, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_edge4(self):  # 55
        plane_a_location, plane_a_velocity = [0, 0, 0], [0, 0, 0]
        plane_b_location, plane_b_velocity = [-401, 0, 0], [100, 0, 0]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    # Random tests, hit or misses depending on whether the algorithm detects they were hit in the past
    def test_random_points_1(self):  # 56
        plane_a_location, plane_a_velocity = [922, -973, -729], [7, 30, 375]
        plane_b_location, plane_b_velocity = [721, -470, -50], [66.6938748861153, -152.15410351277828,
                                                                162.9989590441641]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_2(self):  # 57
        plane_a_location, plane_a_velocity = [892, 473, 19], [-247, -155, -645]
        plane_b_location, plane_b_velocity = [-234, -875, -135], [-116.51520559668512, -22.561532552033437,
                                                                  -626.3886936272655]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_3(self):  # 58
        plane_a_location, plane_a_velocity = [-577, 331, 814], [256, 443, 940]
        plane_b_location, plane_b_velocity = [191, 451, 511], [-596.5978391630134, 229.3418302813451,
                                                               1144.5013910164269]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_4_hit_past_1(self):  # 59
        plane_a_location, plane_a_velocity = [97, -666, -541], [647, 17, 380]
        plane_b_location, plane_b_velocity = [-3, -517, -804], [683.1518470283609, 10.013600114151117,
                                                                388.3171427212487]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_5_hit_past_2(self):  # 60
        plane_a_location, plane_a_velocity = [138, 721, 881], [428, 967, 977]
        plane_b_location, plane_b_velocity = [242, 667, 645], [415.0613107671489, 1008.3443173187657,
                                                               1007.1902748766527]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_6_hit_past_3(self):  # 61
        plane_a_location, plane_a_velocity = [-79, 645, -409], [221, 550, 302]
        plane_b_location, plane_b_velocity = [-279, 746, -298], [286.1493300824687, 578.0142119354615,
                                                                 309.38359074267976]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_7_hit_past_4(self):  # 62
        plane_a_location, plane_a_velocity = [-528, 828, -218], [305, 869, 943]
        plane_b_location, plane_b_velocity = [-354, 719, -95], [212.42247572305172, 979.6673853425588, 861.772976783827]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_8_hit_past_5(self):  # 63
        plane_a_location, plane_a_velocity = [392, 961, -105], [536, 980, 377]
        plane_b_location, plane_b_velocity = [344, 825, -96], [533.670023347531, 1127.3710232686612, 336.2254085817933]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertFalse(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_9(self):  # 64
        plane_a_location, plane_a_velocity = [526, 300, 937], [249, 894, 197]
        plane_b_location, plane_b_velocity = [331, -224, -853], [355.7580592596675, 1168.8298687698198,
                                                                 1343.2064605649434]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_10(self):  # 65
        plane_a_location, plane_a_velocity = [-115, 638, -649], [594, 626, 404]
        plane_b_location, plane_b_velocity = [-531, 945, 744], [630.2134364559457, 606.4731470090487,
                                                                120.32808109509146]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_11(self):  # 66
        plane_a_location, plane_a_velocity = [-423, -393, 129], [867, 507, 707]
        plane_b_location, plane_b_velocity = [479, 997, -616], [761.3139710461941, 333.9994256337078, 801.17458389141]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_12(self):  # 67
        plane_a_location, plane_a_velocity = [-331, -627, -708], [514, 637, 783]
        plane_b_location, plane_b_velocity = [-764, 994, -810], [551.157171920058, 395.47838251962366,
                                                                 783.6518802091239]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_13(self):  # 68
        plane_a_location, plane_a_velocity = [380, 334, -829], [521, 684, 142]
        plane_b_location, plane_b_velocity = [387, 615, -477], [523.0612614187343, 608.8432375015374, 50.67026329300751]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def test_random_points_14(self):  # 69
        plane_a_location, plane_a_velocity = [293, -870, 81], [999, 263, 48]
        plane_b_location, plane_b_velocity = [-277, -15, -990], [1090.0561667337115, 36.170515948336984,
                                                                 282.24372663557847]
        plane_a = self.plane_helper(self.a_id_code, plane_a_location, plane_a_velocity)
        plane_b = self.plane_helper(self.b_id_code, plane_b_location, plane_b_velocity)
        self.assertTrue(CollisionDetection().determine_collision(plane_a, plane_b), "Not implemented yet")

    def plane_helper(self, id_code, location_vector, velocity_vector):
        return plane.PlaneObject(id_code,
                                 location_vector[0], location_vector[1], location_vector[2],
                                 velocity_vector[0], velocity_vector[1], velocity_vector[2])

# if __name__ == '__main__':
#     unittest.main
