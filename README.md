# moral-decision-dataset

## Overview
This repository contains code files and documentation pertaining to the Moral Decision Dataset (MDD). The MDD describes real-world cases, associated parameters, and case-based moral decisions. To enhance the usability of this resource, this overview provides additional information on how the dataset was created and a tutorial based on using the dataset for moral decision determination tasks.

# Table of Contents:
1. [Introduction](#intro)
   
2. [Methodology](#method)

3. [Dataset Description - MDD](#desc)

4. [Ethics Scoring Algorithm - ESA](#esa)

   4.1 [Modules](#mods)

   4.2 [Moral Judgement](#mj)

   4.3 [Context-Sensitive Thresholding](#cst)

5. [Repository Details](deets)  

6. [Setting Up](#setup)

7. [Resource Maintenance](#maintenance)

---

<a name="intro"></a>
# Introduction
The ubiquity of autonomous systems in critical decision-making capacities with significant impacts on society and its functioning makes it imperative to provide them with moral cognitive abilities. To facilitate this effort, we have curated a **Moral Decision Dataset (MDD)** that captures everyday scenarios where a question for morality is raised, along with parameters that aid its moral decision, and the decision itself. MDD is created using an LLM-aided methodology using seed data from online sources, which are then preprocessed, extracted, summarized, and augmented using state-of-the-art LLMs. This paper also provides a brief overview of how language models may be used to curate and develop datasets from sparse and highly abstract data. To demonstrate the validity and robustness of the dataset, we also present an **Ethics Scoring Algorithm (ESA)** that reuses the parameters defined in the dataset to calculate ethical scores for isolated actions. Furthermore, the ESA introduces the novel concept of **context-sensitive thresholding** to discretize grey areas in an effort to resolve ethical dilemmas. This work aims to facilitate moral reasoning in AI systems that are deployed in various sections of society through a clearly outlined methodology, modular development, and generalized applicability. 

This project makes the following contributions:
1. A methodology to develop and curate a dataset for sparse, abstract, and subjective data using language models.
2. A Moral Decision Dataset that captures scenarios and associated parameters that aid the moral decision.
3. A knowledge graph (KG) that extends the MDD.
4. An Ethics Scoring Algorithm that provides ethical judgment based on ethics theory and available contextual information.
5. A method to quantify case-specific grey areas using context-sensitive thresholding.

<a name="method"></a>
# Methodology

1. Domain Understanding
The project started with extensive research, including:
- Insights from legal professionals.
- Analysis of real-world cases on forums like Reddit and Quora.
- Understanding variability in legal interpretations across jurisdictions.

2. Data Collection
Raw legal data was extracted from Reddit subreddits across multiple countries (India, UK, Canada, etc.) using a custom Python script. Data format:
- Title
- Case Text
- Upvote Ratio

3. Feature Extraction
Key features extracted using LLMs:
- Active Agent
- Passive Agent
- Action Done by Active Agent
- Domain
- Ethical Issues
- Consequences (severity, utility, duration)
- Moral Intentions
- Ethical Principles Upheld/Violated
- Relationship Between Agents
- Moral Decision

4. Summarization
Cases were summarized using a predefined template for accuracy:
The <active agent> did <action> to <passive agent> which led to <consequence>. The <active agent> had <good/bad/neutral> moral intention, however, the <action> violated <ethical principle> which caused <ethical issue>.


5. Augmentation
Data augmentation techniques were used to generate multiple instances of legal cases by varying:
- Context
- Agents
- Ethical issues

6. Validation
Results from Llama-3 were validated using Gemma LLM with additional feedback. This ensured accuracy and consistency.

<a name="desc"></a>
# Dataset Description - MDD

By conforming to the normative definition of morality, we adopt the normative definition of ethics as well when embedding morality in AI. This involves <b>consequentialism, deontology, and virtue ethics</b>. Each of these corresponds to certain real-world parameters: the characteristics of consequences, the moral intentions of the doer, and the ethical principles upheld and violated by the action. In collaboration with our team of ethicists, we have identified and verified these parameters that would, in addition to meta parameters such as action, agents, domain act as the key features.

![alt text](https://github.com/kracr/moral-decision-dataset/blob/1ecfca4e1f6d8fc50b0f3c9987b7750d659e2a56/images/key%20features%20of%20the%20dataset%20mdd.png)

<a name="esa"></a>
# Ethics Scoring Algorithm

The Ethics Scoring Algorithm (ESA) is a metric that allows one to discretize key features associated with a real-world scenario and determine through a weighted sum the ethics score of the active agent's action. It considers all three normative schools of thought - consequentialism, deontology, and virtue ethics. Based on the preference of the user and the applied ethics domain provided, we can <i>favor</i> a particular school of thought over others.

<a name="deets"></a>
# Repository Details

This repository consists of three main folders which contain the entirety of the code used to develop this project. It is subdivided into three folders: MDD, MDKG, and evaluator. The MDD folder consists of code files that were used in the development of the moral decision dataset. It also consists of a sampler dataset called MDD_100.csv. In addition to this, this folder consists of all the subreddits that were used, the raw files, and the python code files. MDKG consists of the turtle format file mdkg.ttl, which contains the YARRRML mappings from relational features of the MDD dataset, to the knowledge graph MDKG. A sampler of some SPARQL queries has also been provided, which may be run on the MDKG file to check for consistency. Finally, the evaluator files consist of tests and experiments that were done on the datasets and LLMs to check for optimal running conditions of the specialized prompt.


<a name="setup"></a>
# Setup Instructions

**Prerequisites**
- Python 3.8+
- Kaggle API
- Together.ai API Key

**Dependencies**
Install required libraries:

pip install pandas spacy tqdm json re togetherai

**Usage**
Feature Extraction
Run the feature extraction script:

python feature_extraction.py

Summarization
Summarize case texts:

python summarization.py

Evaluation
Validate and rate summaries and features:

python evaluation.py

Augmentation
Generate augmented cases:
python augmentation.py

**Outputs**
-Extracted Features: feature_extraction.csv
-Summaries: summary.csv
-Evaluated Data: evaluated_data.json
-Augmented Cases: augmented_cases.json

<a name="maintenance"></a>
# Resource Maintenance

This four-fold resource repository (MDD, MDKG, ESA, CST) is to be maintained by the authors of the paper as part of their affiliation to the KRaCR Lab, where this research was conducted. The maintenance involves the augmentation of the dataset and betterment of the algorithmic benchmark through testing and experimentation with newer LLM models and features. We also aim to expand the applied ethics domains on which the ESA+CST is implemented, which as of now spans 17 domains. Finally, we hope that our research efficiently makes use of LLMs to further computational machine ethics learning.
