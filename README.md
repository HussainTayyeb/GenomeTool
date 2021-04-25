# GenomeTool
Start Tool with i.e:

Initialize DB:
python Tool/main.py --table init 

Reinitialize DB
python Tool/main.py --table reinit 

Execute with Filter:
python Tool/main.py --taxid 134629 --chunk 5 --filter filtermax --parameter 238  --filter filtermin --parameter 235  --fileName max1

Execute without Filter:
python Tool/main.py --taxid 134629 --chunk 5 --fileName max1

the .db file couldnt be commited to the github due to the size of the db file

Please download it from the followed link and add it outside of the 'Tool'-file

Link: https://drive.google.com/file/d/1awHbX_s_Nq3ZEpNi9YPSnTwdeqck9dO-/view?usp=sharing