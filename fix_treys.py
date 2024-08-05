import os

treys_init_path = '/opt/render/project/src/.venv/lib/python3.11/site-packages/treys/__init__.py'

with open(treys_init_path, 'a') as f:
    f.write('\nfrom .card import Card\n')

print("Fixed treys import issue.")
