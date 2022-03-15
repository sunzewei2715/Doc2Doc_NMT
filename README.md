# Doc2Doc_NMT
The repository for the paper: [Rethinking Document-level Neural Machine Translation](https://arxiv.org/abs/2010.08961)
(ACL-2022: Findings)

Other previously used titles: 

    - Capturing Longer Context for Document-level Neural Machine Translation: A Multi-resolutional Approach)

    - An Empirical Study of Document-to-document Neural Machine Translation

### Training sets
The training sets can be downloaded from [here](https://drive.google.com/drive/folders/1cmYG2960L1dfttKivl7ZyXY3N9kdzyFQ?usp=sharing).

### Test sets
The test sets are organized in sentences(sent/del) and documents(doc) respectively with the same content. The labeled tokens and their positions are in the testsets/doc/en.candidates.

### Calculate TCP
As is mentioned in the paper, we provide the python script of calculating TCP, as:

    python3 tcp.py python tcp.py --hypotheses_dir your_hypothesis_or_rootpath

It is equivalent to

    python3 tcp.py python tcp.py --reference ./testsets/doc/en.tok --candidates ./testsets/doc/en.candidates --hypotheses_dir your_hypothesis_or_rootpath

### Cititaion
If you use our data or evaluation scripts, please cite:

	@inproceedings{sun2020rethinking,
	  title={Rethinking Document-level Neural Machine Translation},
      author={Zewei Sun, Mingxuan Wang, Hao Zhou, Chengqi Zhao, Shujian Huang, Jiajun Chen, Lei Li},
	  booktitle={Findings of the Association for Computational Linguistics: ACL 2022},
	  year={2022},
	}
