Execute to initialize local Taxonomy database:
python Tool/main.py --table init 

Execute to reinitialize local Taxonomy  database:
python Tool/main.py --table reinit 

Execute WITHOUT Filter:
python Tool/main.py --taxid 134629 --chunk 5 --fileName TestFile

Execute WITH Filter minimum:
python Tool/main.py --taxid 134629 --chunk 5 --filter filtermin --parameter 235 --fileName TestFile

Execute WITH Filter maximum:
python Tool/main.py --taxid 134629 --chunk 5 --filter filtermax --parameter 238 --fileName TestFile

Execute WITH Filter minimum and maximum:
python Tool/main.py --taxid 134629 --chunk 5 --filter filtermax --parameter 238 --filter filtermin --parameter 235  --fileName TestFile

The .db file couldn't be uploaded to github due it's size.
Please download it from the following link and save it in the parent directory of the 'Tool'-directory.
Link: https://drive.google.com/file/d/1awHbX_s_Nq3ZEpNi9YPSnTwdeqck9dO-/view?usp=sharing
