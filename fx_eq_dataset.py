import numpy as np

class FXEQDataset:
    def __init__(self, path, train_split=0.65):
        # Load data
        self.data = np.loadtxt(path, delimiter=',', skiprows=1)
        
        # Dataset size
        self.dataset_size = self.data.shape[0]
        
        # Chronological split
        split_idx = int(self.dataset_size * train_split)
        self.train_imgs = self.data[:split_idx]
        self.test_imgs = self.data[split_idx:]
        
        # Reshape into (batch, 3, 4, 1)
        self.train_imgs = self.train_imgs.reshape((-1, 3, 4, 1))
        self.test_imgs = self.test_imgs.reshape((-1, 3, 4, 1))
        
        # Define x_dim for BGAN
        self.x_dim = (3, 4, 1)

        # Dummy labels
        self.train_labels = np.zeros((self.train_imgs.shape[0], 1))
        self.test_labels = np.zeros((self.test_imgs.shape[0], 1))

    def get_train_data(self):
        return self.train_imgs, self.train_labels

    def get_test_data(self):
        return self.test_imgs, self.test_labels
    
    def next_batch(self, batch_size, class_id=None):
        """
        Returns a batch of images from the training set.
        """
        idx = np.random.randint(0, self.train_imgs.shape[0], batch_size)
        return self.train_imgs[idx], np.zeros((batch_size, 1))  # returning dummy labels
