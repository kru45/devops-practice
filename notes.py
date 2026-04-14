def add_note(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added!")

def view_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes found.")

def main():
    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            note = input("Enter note: ")
            add_note(note)
        elif choice == "2":
            view_notes()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
