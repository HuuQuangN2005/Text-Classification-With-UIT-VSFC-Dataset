import os
from collections import defaultdict
import unicodedata



class UITVSFCDataset():
    """
    A dataloader for the UIT-VSFC dataset.
    """

    def __init__(self, root_dir):
        """
        Initializes the data loader with the root directory of the dataset.

        Args:
            root_dir (str): The root directory where the dataset is stored.
        """
        self.root_dir = root_dir
        self.train_path = os.path.join(root_dir, 'train')
        self.test_path = os.path.join(root_dir, 'test')
        self.dev_path = os.path.join(root_dir, 'dev')
        self.dataset = defaultdict(dict)
    
    def __load_data_from_files(self, data_path:str):
        sents_file = os.path.join(data_path, 'sents.txt')
        sentiments_file = os.path.join(data_path, 'sentiments.txt')
        topics_file = os.path.join(data_path, 'topics.txt')
        
        with open(sents_file, 'r', encoding='utf-8') as f:
            sentences = f.readlines()
        
        with open(sentiments_file, 'r', encoding='utf-8') as f:
            sentiments = f.readlines()
        
        with open(topics_file, 'r', encoding='utf-8') as f:
            topics = f.readlines() 
        
        data = {}
        
        for idx, (sent, sentiment, topic) in enumerate(zip(sentences, sentiments, topics)):
            data[idx] = {
                'sentence': sent.strip(),
                'sentiment': sentiment.strip(),
                'topic': topic.strip()
            }
        
        return data
    
    def load_data(self):
        """
        Loads the dataset from the specified root directory.

        Returns:
            dict: A dictionary containing training, testing, and development data.
        """
        self.dataset = {
            'train': self.__load_data_from_files(self.train_path),
            'test': self.__load_data_from_files(self.test_path),
            'dev': self.__load_data_from_files(self.dev_path)
        }
        
        return self.dataset
    
    
if __name__ == "__main__":
    dataset = UITVSFCDataset(root_dir='data/UIT-VSFC').load_data()   
    print(dataset['train'][0])
