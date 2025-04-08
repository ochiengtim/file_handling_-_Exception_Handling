import os

def transform_text(text, mode):
    if mode == "1":
        return text.upper()
    elif mode == "2":
        return text.lower()
    elif mode == "3":
        return text.title()
    else:
        return text

def get_transformation_choice():
    print("\nChoose a transformation:")
    print("  [1] UPPERCASE")
    print("  [2] lowercase")
    print("  [3] Title Case")
    choice = input("Your choice (1/2/3): ").strip()
    return choice

def process_file():
    print("=" * 40)
    filename = input("📂 Enter the filename to read from: ").strip()

    if not os.path.exists(filename):
        print(f"❌ Error: File '{filename}' not found.")
        return

    if not os.access(filename, os.R_OK):
        print(f"🔒 Error: No read permission for '{filename}'.")
        return

    transform_choice = get_transformation_choice()

    base_name = os.path.basename(filename)
    new_filename = f"modified_{base_name}"

    if os.path.exists(new_filename):
        overwrite = input(f"⚠️ File '{new_filename}' already exists. Overwrite? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("❌ Operation cancelled by user.")
            return

    try:
        line_count = 0

        with open(filename, 'r') as file, open(new_filename, 'w') as new_file:
            for line in file:
                modified_line = transform_text(line, transform_choice)
                new_file.write(modified_line)
                line_count += 1

        print(f"\n✅ Success! {line_count} lines processed.")
        print(f"📝 Modified content written to '{new_filename}'.")

    except PermissionError:
        print(f"🔒 Error: Permission denied when accessing '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file()
