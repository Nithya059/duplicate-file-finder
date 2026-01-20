import os
import hashlib
import argparse
from collections import defaultdict

def hash_file(path, chunk_size=8192):
    sha = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                sha.update(data)
        return sha.hexdigest()
    except Exception:
        return None

def find_duplicates(folder):
    hashes = defaultdict(list)

    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            file_hash = hash_file(path)
            if file_hash:
                hashes[file_hash].append(path)

    return {h: paths for h, paths in hashes.items() if len(paths) > 1}

def main():
    parser = argparse.ArgumentParser(description="Duplicate File Finder")
    parser.add_argument("folder", help="Folder to scan")
    parser.add_argument("--delete", action="store_true", help="Delete duplicate files")

    args = parser.parse_args()

    folder = args.folder
    delete_mode = args.delete

    if not os.path.isdir(folder):
        print("❌ Invalid folder path")
        return

    duplicates = find_duplicates(folder)

    if not duplicates:
        print("✅ No duplicate files found.")
        return

    print("\n🔁 DUPLICATE FILES FOUND:\n")

    for h, files in duplicates.items():
        print(f"Hash: {h}")
        for f in files:
            print(f"   {f}")
        print()

    if delete_mode:
        print("⚠️ DELETE MODE ENABLED")
        confirm = input("Type YES to permanently delete duplicates: ")

        if confirm == "YES":
            deleted = 0
            for files in duplicates.values():
                for f in files[1:]:
                    try:
                        os.remove(f)
                        deleted += 1
                        print(f"🗑 Deleted: {f}")
                    except Exception as e:
                        print(f"❌ Failed to delete {f}: {e}")

            print(f"\n✅ Deleted {deleted} duplicate files.")
        else:
            print("❌ Deletion cancelled.")

if __name__ == "__main__":
    main()