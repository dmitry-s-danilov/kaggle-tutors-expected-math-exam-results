# [Kaggle competition. Tutors - expected math exam results][1]
## Predict average math exam results for students of the tutors

### Overview

#### Description

In this competition your task will be to predict
the mean math exam result (from 0 to 100 points)
for students of tutors in _test.csv_.
You will be given two datasets:
_train.csv_ (contains all features and the target) and
_test.csv_ (only features).

#### Evaluation

The evaluation metric is
[Coefficient of determination][2]

### Data

- train.csv
- test.csv
- submission_example.csv

### Rules

You can only use these imports:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
```

---

[1]: https://www.kaggle.com/c/tutors-expected-math-exam-results
[2]: https://en.wikipedia.org/wiki/Coefficient_of_determination
