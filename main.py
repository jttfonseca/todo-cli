import argparse
from src.task import Task
from src.todolist import TodoList
from src.persistence import load_from_file, save_to_file, DEFAULT_PATH


def build_parser():
    p = argparse.ArgumentParser(description="Simple To-Do CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")

    add_p = sub.add_parser("add")
    add_p.add_argument("description", nargs="+", help="Task description")

    comp_p = sub.add_parser("complete")
    comp_p.add_argument("index", type=int)

    rm_p = sub.add_parser("remove")
    rm_p.add_argument("index", type=int)

    sub.add_parser("save")
    sub.add_parser("load")

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    # Load (or start new)
    todo = load_from_file(DEFAULT_PATH)

    if args.cmd == "list":
        todo.list_tasks()

    elif args.cmd == "add":
        desc = " ".join(args.description)
        todo.add(Task(desc))
        print(f"➕ Added: {desc}")
        save_to_file(todo, DEFAULT_PATH)

    elif args.cmd == "complete":
        todo.complete(args.index)
        save_to_file(todo, DEFAULT_PATH)

    elif args.cmd == "remove":
        todo.remove(args.index)
        save_to_file(todo, DEFAULT_PATH)

    elif args.cmd == "save":
        save_to_file(todo, DEFAULT_PATH)

    elif args.cmd == "load":
        todo = load_from_file(DEFAULT_PATH)
        todo.list_tasks()


if __name__ == "__main__":
    main()
