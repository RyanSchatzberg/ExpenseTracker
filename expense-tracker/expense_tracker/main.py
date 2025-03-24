import argparse
from . import tracker

def cli():
    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparsers = parser.add_subparsers(dest="command")

    #Add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    #Update
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description")
    update_parser.add_argument("--amount", type=float)

    #Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    #List
    subparsers.add_parser("list")

    #Summary
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int, required=False)

    args = parser.parse_args()
    tracker.handle_command(args)