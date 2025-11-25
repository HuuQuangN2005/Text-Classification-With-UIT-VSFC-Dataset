# Text-Classification-With-UIT-VSFC-Dataset


## Getting Started

Một trong những repo dùng để luyện tập NLP của tôi

### Data

- Bộ dataset được sử dụng ở đây là bộ UIT-VSFC Dataset.
- Ngoài ra tôi còn sử dụng 1 vài bộ data hỗ trợ, tất cả được để ở link dưới đây:
    + [UIT-VSFC Dataset](https://drive.google.com/drive/folders/1xclbjHHK58zk2X6iqbvMPS2rcy9y9E0X)
    + [vietnamese-stopwords](https://github.com/stopwords/vietnamese-stopwords)
    + synonym_vi được generate bằng ChatGPT

- Cấu trúc thư mục data:

```
    data/
        UUIT-VSFC/
            train/
            dev/
            test/
        synonym_vi.csv
        vietnamese-stopwords.txt
```

### Installing

Để clone và chạy repo, bạn cần [Git](https://git-scm.com). Từ command line:

```bash
# Clone this repository
$ git clone https://github.com/HuuQuangN2005/Text-Classification-With-UIT-VSFC-Dataset.git

# Go into the repository
$ cd Text-Classification-With-UIT-VSFC-Dataset

# Install dependencies
$ python -m venv venv
$ .\venv\Scripts\Activate
$ pip install -r requirements.txt

```

### Citation

"""\
@InProceedings{8573337,
  author={Nguyen, Kiet Van and Nguyen, Vu Duc and Nguyen, Phu X. V. and Truong, Tham T. H. and Nguyen, Ngan Luu-Thuy},

  booktitle={2018 10th International Conference on Knowledge and Systems Engineering (KSE)},
  title={UIT-VSFC: Vietnamese Students’ Feedback Corpus for Sentiment Analysis},
  year={2018},
  volume={},
  number={},
  pages={19-24},
  doi={10.1109/KSE.2018.8573337}
}

"""