"""Updates the new  generated thesaurus with the old one."""

# Reads the new thesaurus
new_thesaurus = {}
with open("thesauri/descriptors.the.txt", "r", encoding="utf-8") as f:
    for line in f:
        if not line.startswith(" "):
            key = line.strip()
        else:
            value = line.strip()
            new_thesaurus[value] = key

# update the keys with the
with open("descriptors.the.txt", "r", encoding="utf-8") as f:
    for line in f:
        if not line.startswith(" "):
            key = line.strip()
        else:
            value = line.strip()
            if value in new_thesaurus.keys():
                new_thesaurus[value] = key

with open("thesauri/descriptors.the.txt", "w", encoding="utf-8") as f:
    for key, value in new_thesaurus.items():
        f.write(f"{value}\n")
        f.write(f"    {key}\n")

print("Done!")
