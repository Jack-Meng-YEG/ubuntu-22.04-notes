# rm_usage.py - basic rm command examples

# 1) Remove a single file
# $ rm file.txt
# $ rm test.py

# 2) Remove multiple files
# $ rm a.txt b.txt c.txt
# $ rm *.log

# 3) Ask for confirmation before each removal (-i)
# $ rm -i file.txt
# $ rm -i *.txt

# 4) Remove an empty directory (use rmdir, not rm)
# $ rmdir empty_dir

# 5) Remove a directory and its contents recursively (-r)
# WARNING: this is dangerous; always double-check the path.
# $ rm -r mydir
# $ rm -r folder/subfolder

# 6) Force removal without prompts (-f)
# WARNING: do NOT use -rf carelessly. It can delete many files permanently.
# $ rm -f file.txt
# $ rm -rf mydir   # dangerous: recursive and forced removal

# 7) Common safe pattern: combine -r and -i for interactive recursive deletion
# $ rm -ri mydir
# # rm will ask you before deleting each file or directory
