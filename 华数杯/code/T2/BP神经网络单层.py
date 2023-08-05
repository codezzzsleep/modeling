import torch
import torch.nn as nn
import torch.optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np


class MyDataset(Dataset):
    def __init__(self, X, y=None):
        if y is None:
            self.X = X
        else:
            self.X = X
            self.y = y

    def __getitem__(self, item):
        return self.X[item], self.y[item]

    def __len__(self):
        return len(self.X)


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.linear1 = nn.Linear(8, 3)

    def forward(self, X):
        return self.linear1(X)


df = pd.read_excel("../dataset/demo_train.xlsx")
train_fea = torch.tensor(df.iloc[:-20, 1:9].to_numpy(), dtype=torch.float32)

train_lab = torch.tensor(df.iloc[:-20, 9].to_numpy(), dtype=torch.long)
test_fea = torch.tensor(df.iloc[-20:, 1:9].to_numpy(), dtype=torch.float32)

batch_size = 16
shuffle = True

train_dataset = MyDataset(train_fea, train_lab)
train_dataloader = DataLoader(dataset=train_dataset,
                              batch_size=batch_size,
                              shuffle=shuffle)
model = MyNet()

criterion = torch.nn.CrossEntropyLoss(reduction='mean')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
train_dataset = []
test_dataset = []
print(model(train_fea[179]))
print(train_lab[179])
for epoch in range(1000):
    loss_record = []
    for X, y in train_dataloader:
        # print(X)
        # print(y)
        pred = model(X)
        # print(pred)
        loss = criterion(pred, y)
        # print(loss)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss_record.append(loss.item())
        # print("===================================================================")
    mean_train_loss = sum(loss_record) / len(loss_record)
    print(f"Epoch {epoch + 1:03d}: Train Loss: {mean_train_loss:.4f}")
model.eval()
pred = model(test_fea)
print(pred)
_, pred_test = torch.max(pred, 1)
print(pred_test)
print(model(train_fea[179]))
print(train_lab[179])