from math import sqrt


class CollisionDetection:
    #put in self, we could probably make this into a module and not a class? Something to think about.
    velocity_A = []
    velocity_B = []
    vector_position_A = []
    vector_position_B = []
    radius_A = 200
    radius_B = 200
    def determine_collision(self, p_a, potential_intruder):
        """
        Determines whether two aircraft will collide.
        :param p_a: the primary aircraft
        :param potential_intruder: the aircraft being compared to the primary aircraft
        :return: True if the planes will collide, False if they will not
        """

        raise Exception("Not Yet Implemented.")

        # TUC interval will be set inside the plane object which the caller has access to.
        pass

    #vector 2 minus vector 1
    def vector_subtraction(self, matrix_A, matrix_B):
        return [b-a for a, b in zip(matrix_A, matrix_B)]

    def dot_product(self,vector1, vector2):
        return sum(p*q for p,q in zip(vector1, vector2))

    def multiple_vector(self,int_var, vector):
        return [i*int_var for i in vector]

    def calculate_b_in_algo(self):
        return 2*(self.dot_product(self.vector_subtraction(self.velocity_A, self.velocity_B),
                       self.vector_subtraction(self.vector_position_A, self.vector_position_B)))

    def calculate_a_in_algo(self):
        return self.dot_product(self.vector_subtraction(self.velocity_A, self.velocity_B),
                        self.vector_subtraction(self.velocity_A, self.velocity_B))

    def calculate_c_in_algo(self):
        return (self.dot_product(self.vector_subtraction(self.vector_position_A, self.vector_position_B),
                self.vector_subtraction(self.vector_position_A, self.vector_position_B))) - \
               (self.radius_A+self.radius_B)**2

    def calculate_a_b_c_of_algo(self):
        # u = b*b-4*a*c
        #if postivive have to do roots
        return self.calculate_b_in_algo()**2-4*self.calculate_a_in_algo()*self.calculate_c_in_algo()

    def check_negative_root(self, u):
        if(self.calculate_a_in_algo() != 0 and u >=0):
            return ((-self.calculate_b_in_algo()-sqrt(u))/(2*self.calculate_a_in_algo()))
        else:
            print("Exiting neg root: dividing result by 0 or sqrt is negative")

    def check_positive_root(self, u):
        if(self.calculate_a_in_algo() != 0 and u >=0):
            return ((-self.calculate_b_in_algo()+sqrt(u))/(2*self.calculate_a_in_algo()))
        else:
            print("Exiting pos root: dividing result by 0 or sqrt is negative")