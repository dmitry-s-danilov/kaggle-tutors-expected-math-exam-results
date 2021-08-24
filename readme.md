# [Tutors - expected math exam results][1]
## Predict average math exam results for students of the tutors

### Overview

#### Description

In this competition your task will be to predict
the mean math exam result (from 0 to 100 points)
for students of tutors in _test.csv_.
You will be given two datasets:
_train.csv_ (contains all features and the target) and
_test.csv_ (only features).

Ваша задача этом соревновании -
предсказать средний балл на экзамене по математике,
который получают ученики репетиторов из датасета _test.csv_.
Вам будут даны два датасета:
_train.csv_ (содержит признаки и целевую переменную) и
_test.csv_ (только признаки).


#### Evaluation

The evaluation metric is
[Coefficient of determination][2.1]

Метрика для оценки –
[Коэффициент детерминации][2.2]

### Data

- submission_example.csv
- train.csv
- test.csv

### Rules

You can only use these imports:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
```

[1]: https://www.kaggle.com/c/tutors-expected-math-exam-results
[2.1]: https://en.wikipedia.org/wiki/Coefficient_of_determination
[2.2]: https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%8D%D1%84%D1%84%D0%B8%D1%86%D0%B8%D0%B5%D0%BD%D1%82_%D0%B4%D0%B5%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8
