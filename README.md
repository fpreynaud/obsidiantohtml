# Install dependencies

```bash
pip install -r requirements.txt
```

# Configuration

## Generate config.yml file

```bash
obsidianhtml export default-config -o config.yml
```

## Change relevant paths in config.yml

obsidianhtml needs an entry point note that contains links to other notes. This entry point is specified with the *obsidian_entrypoint_path_str* option
The *convert_vault_to_site.py* script will create a file named "entry.md" in the folder that will be converted. This file will simply be a list of wikilinks of all .md files under the obsidian folder.
Of course, you also have the option to manually create a note that will be a more beautiful table of contents.

Also, by default, the output of obsidianhtml will be created under a folder named output, in the directory it was run from. Change the following options if that's not what you want:

- md_folder_path_str
- md_entrypoint_path_str
- html_output_folder_path_str
- module_data_folder

# Usage

```bash
python3 convert_vault_to_site.py vault_folder -i config.yml
```

> [!NOTE]
> The script creates a .obsidian folder in `vault_folder` because it's needed by obsidianhtml
