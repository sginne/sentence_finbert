import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sentence-finbert",
    packages=['sentence_finbert'],
    version="0.0.1",
    author="Timo Junolainen",
    author_email="sigin@norsula.com",
    description="Based in finbert_embedding by ahijeet3922, includes RNN for more sophisticated sentence vectorizing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sginne/sentence_finbert.git",
    download_url="",
    install_requires=[
          'torch>=1.1.0',
          'pytorch-pretrained-bert==0.6.2',
          'tensorflow',
      ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
