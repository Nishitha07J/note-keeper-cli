import argparse
import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(content):
    notes = load_notes()
    new_id = max([note["id"] for note in notes], default=0) + 1
    notes.append({"id": new_id, "content": content})
    save_notes(notes)
    print(f'Note added: "{content}"')

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        print(f'[{note["id"]}] {note["content"]}')

def delete_note(note_id):
    notes = load_notes()
    filtered = [note for note in notes if note["id"] != note_id]
    if len(filtered) == len(notes):
        print(f"Error: No note with ID {note_id}")
        return
    save_notes(filtered)
    print(f"Note [{note_id}] deleted.")

def main():
    parser = argparse.ArgumentParser(description="Note Keeper CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new note")
    parser_add.add_argument("content", help="Content of the note")

    # List command
    parser_list = subparsers.add_parser("list", help="List all notes")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a note by ID")
    parser_delete.add_argument("id", type=int, help="ID of the note to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.content)
    elif args.command == "list":
        list_notes()
    elif args.command == "delete":
        delete_note(args.id)

if __name__ == "__main__":
    main()
