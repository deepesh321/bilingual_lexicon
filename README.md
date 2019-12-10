# bilingual_lexicon
Information Retrieval using random indexing

Prerequisites:
Django (pip3 install django)
Numpy (pip3 install numpy)
Open folder '​ bilingual_lexicon-master​ '
Run the following commands:
1. python3 manage.py makemigrations
2. python3 manage.py migrate
3. python3 manage.py runserver
Open the link given on terminal
http://127.0.0.1:8000/
1. Choose the English file in Lang1 field
2. Choose the corresponding translated(​ Hindi/Bengali​ ) file in Lang2
3. Wait for a few seconds.
Constraints:
Both English and Hindi/Bengali file should have the same number of lines.
Example: Line 5 in the Hindi/Bengali file should be an exact translation of line 5 of the
English file.
Each English line should terminate with '.' and the Hindi/Bengali line should terminate
with '|'.

You can use the above dataset.
