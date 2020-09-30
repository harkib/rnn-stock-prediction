# rnn-stock-prediction

**Goal:** Use the time series data form the pre-market and perdict if the stock will go up, down, or stay realitivly the same from open to close. 

**Approach:** We use a lstm-rnn with a fully connected layer at the end to produce a class label (Pos, Neu, Neg). We use several different class definitons  based on percent change. We use the last two year of data for all stocks in the NASDEQ100.

**Findings:** Our model is woefully ineffective at finding any pattern in the pre-market to perdict market performance. Given any class deffinition the model simply only perdicts the class with most samples. If the number of samples is perfectly balanced, the model seems to randomly select one or sometime two class to always perdict. 

![ConfutionMatrix](/Results/ConfusionMatrix.png) ![ValidationLoss](/Results/ValidationLoss.png)
