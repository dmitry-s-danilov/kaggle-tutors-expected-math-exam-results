from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='competition',
    version='0.0.1',

    author='Dmitry S. Danilov',
    author_email='dmitry.s.danilov@gmail.com',

    description='Predict average math exam results for students of the tutors within the Kaggle competition',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/dmitry-s-danilov/kaggle-tutors-expected-math-exam-results',
    project_urls={
        'Bug Tracker': 'https://github.com/dmitry-s-danilov/kaggle-tutors-expected-math-exam-results/issues',
        'Kaggle Competition': 'https://www.kaggle.com/c/tutors-expected-math-exam-results',
    },

    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='machine-learning, prediction-competition, python',

    license='MIT License',
    license_files=['LICENSE.txt'],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    data_files=[
        (
            'data',
            [
                'data/train.csv',
                'data/test.csv',
                'data/submission_example.csv',
            ]
        )
    ],

    python_requires=">=3.9",
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
    ],
)
