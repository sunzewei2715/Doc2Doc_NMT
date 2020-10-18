# Doc2Doc_NMT
The repository for the paper: Capturing Longer Context for Document-level Neural Machine Translation—A Multi-resolutional Approach

### Training sets
The training sets can be downloaded from [here](https://drive.google.com/drive/folders/1cmYG2960L1dfttKivl7ZyXY3N9kdzyFQ?usp=sharing).

### Test sets
The test sets are organized in sentences(sent/del) and documents(doc) respectively with the same content. The labeled tokens and their positions are in the testsets/doc/en.candidates.

### Calculate TCP
As is mentioned in the paper, we provide the python script of calculating TCP, as:

    python3 tcp.py python tcp.py --hypotheses_dir your_hypothesis_or_rootpath

It is equivalent to

    python3 tcp.py python tcp.py --reference ./testsets/doc/en.tok --candidates ./testsets/doc/en.candidates --hypotheses_dir your_hypothesis_or_rootpath

