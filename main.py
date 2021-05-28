from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_stack import Stack
from marketingfirm import *
from contestant import Contestant
from userinterface import *
import sweepstake
from dictionary import Dictionary


#want to preface this for whoever is grading...
# feel like i'm getting close to the correct function here. really want to make this work and re-submit asap
dictionary_of_contestants = {}


new_contestant = {contestant_enter_firstname(),
                  contestant_enter_lastname(),
                  contestant_enter_email_address(),
                  contestant_enter_registration_number(),
                  verify_contestant_info()}


dictionary_of_contestants.update(new_contestant)
print(dictionary_of_contestants)





# dict_object = Dictionary()
# dict_object.add(1, "contestant")
#
# print(dict_object)
#
# contestant_one = Contestant("Caitlin", "Jones", "blah@test.com", 5565)
# contestant_two = Contestant("Billy", "Bob", "bbob@yahoo.com", 4702)
# contestant_three = Contestant("Joe", "Horton", "horton@aol.com", 8951)
#
# dictionary_of_contestants = {
#     "1": contestant_one,
#     "2": contestant_two,
#     "3": contestant_three
# }
#
# print(dictionary_of_contestants)
#


