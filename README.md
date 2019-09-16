## DrawSth: a package for statistic graphs making in GUI


### What is it？

DrawSth is a user friendly  package, which aims to make statistic graphs and calculate relative evaluation metrics of classifiers. 

### What DrawSth can do ?

 It's capable of drawing four different charts including *receiver operating characteristic (ROC) curve*, *precision-recall (PR) curve*, *Enrichment curve* and *log-scaled area under the receiver-operating characteristic (logAUC) curve.* 

#### ROC(SE-SP) curve

The ROC curve reflects the relationship between the true and false positive rates,The AUC is commonly used in machine learning studies as an accuracy metric and is deﬁned as the area under the ROC curve. The ROC curve was plotted for each compound in prediction order. The possible values of the AUC range from 0 to 1, and the AUC values corresponding to ideal and random prediction are 1 and 0.5, respectively. 

#### P-R curve

Similar to the ROC curve, P-R curve is introduced to characterize of precision and recall on the whole sample set. The area under the P-R curve indicates the possibility of the model to achieve high precision and recall rate at the same time to a certain extent. Therefor, the larger the AUC of P-R curve, the better the model performs.

#### Enrichment curve

xxxxx

#### LogAUC curve

LogAUC was introduced to tackle the early enrichment problem by computing the percentage of the ideal area that lies under the semilog enrichment curve. Formally, we define LogAUC<sub>λ</sub>, where the log area computations run from λ to 1.0, and in this paper we refer to LogAUC<sub>0.001</sub> as simply LogAUC<sub>λ</sub>.

### How to use DrawSth?

DrawSth is based on the Python environment, so you should download the package and open the file [drawsth.py](https://github.com/kotori-y/DrawSth/blob/master/drawsth/drawsth.py) in your Spyder or Python3. Click on button run and then a graphical user interface will appear. Firstly,  select  the data file.



















