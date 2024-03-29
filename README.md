
## Fazal Mahmud Niloy

### Instructions to run this project
please run:
1. [question_1.py](question_1.py) to test the **first problem**
   - For [question_1.py](question_1.py) the unknown data-points with their class can also be visualized by **"un-commenting"** the `render_graph(dataSet_red, dataSet_blue, dataset_unknown, nearest_dataset)` line. After running the program by giving input from console by setting dimension (*2, 4 or 8; although the program runs for any dimension of data*) output files will be generated as [output_2D.txt](output_2D.txt), [output_4D.txt](output_4D.txt) & [output_8D.txt](output_8D.txt).

2. [question_2.py](question_2.py) to test the **second problem**
   - For [question_2.py](question_2.py) change the parameter of `dataset = io.read_multi_dim_data("datasets/K-means/data_4c_2d.txt")` to change the dataset for clustering and `initial_points = [(0.02, 0.82), (-0.004, 4.3), (3.8955, 2.392), (0.1, 2.1)]` to change the points according to the files dimensions and number of centers. Initial points takes input as a list of tuples.

### Datasets used:

###1.  Nearest Neighbour Classifier
| id | file name | count|
| ----------- | ----------- | ----------- |
| 1 | red_2d.txt| 90 samples
| 2 | blue_2d.txt| 90 samples
| 3 | unknown_2d.txt| 20 samples  
| 4 | red_4d.txt| 65 samples
| 5 | blue_4d.txt| 65 samples
| 6 | unknown_4d.txt| 20 samples  
| 7 | red_8d.txt| 40 samples
| 8 | blue_8d.txt| 40 samples
| 9 | unknown_8d.txt| 20 samples

###2.  K-means Clustering
| id | file name | description|
| ----------- | ----------- | ----------- |
| 1 | data_2c_2d.txt | 200 samples, 2 clusters, 2 dimensions
| 2 | data_4c_2d.txt | 200 samples, 4 clusters, 2 dimensions
| 3 | data_2c_4d.txt | 400 samples, 2 clusters, 4 dimensions
| 4 | data_4c_4d.txt | 400 samples, 4 clusters, 4 dimensions
