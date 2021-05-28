from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager
from marketingfirm import MarketingFirm


def choose_stack_or_queue():
    manager_type = input("Please enter 'stack' for stack manager type or 'queue' for queue manager type")
    if manager_type == "stack":
        manager_type = SweepstakesStackManager()
    elif manager_type == "queue":
        manager_type = SweepstakesQueueManager
    marketingfirm = MarketingFirm(manager_type)
    return marketingfirm
