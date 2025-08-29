import argparse
import os
import os.path
import obsidianhtml
import sys

parser = argparse.ArgumentParser(description="Converts an Obsidian vault folder into a static website using obsidianhtml")
parser.add_argument("-i", help="Path to obsidianhtml's config.yml config file", default="/mnt/workspace/vault_obsidian/config.yml")
parser.add_argument("--max-depth", help="Maximum recursion depth", default=5)
parser.add_argument("vault_folder", help="Path to vault folder")
args = parser.parse_args()

def process_folder(folder):
	files = os.listdir(folder)
	links = []
	for file in files:
		abspath = os.path.join(folder, file)
		if os.path.isdir(abspath):
			links += process_folder(abspath)
			continue
		if os.path.isfile(abspath) and file.endswith(".md"):
			link = abspath[:-3].replace(root, '').lstrip('/')
			links.append(f"[[{link}]]")
	return links

print("Building index node")
root = args.vault_folder
os.makedirs(os.path.join(root, ".obsidian"), exist_ok=True)
links = process_folder(root)
with open(os.path.join(root, "entry.md"), "w") as entry_note:
	for link in links[:-1]:
		entry_note.write(link + "\n")
	entry_note.write(links[-1])

print("Converting Obsidian notes into HTML")
sys.argv = ["obsidianhtml", "convert", "-i", args.i]
obsidianhtml.main()
