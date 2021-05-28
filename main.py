from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_stack import Stack
from marketingfirm import MarketingFirm
from contestant import Contestant
from userinterface import *
from sweepstake import *
from dictionary import Dictionary

dictionary_of_contestants = {}


new_contestant = {contestant_enter_firstname(),
                  contestant_enter_lastname(),
                  contestant_enter_email_address(),
                  contestant_enter_registration_number(),
                  verify_contestant_info()}


print(contestant)

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


