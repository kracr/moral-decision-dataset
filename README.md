# moral-decision-dataset

## Overview
This repository contains code files and documentation pertaining to the Moral Decision Dataset (MDD). The MDD describes real-world cases, associated parameters, and case-based moral decisions. To enhance the usability of this resource, this overview provides additional information on how the dataset was created and a tutorial based on using the dataset for moral decision determination tasks.

#Table of Contents:
1. [Introduction](#intro)
   
2. [Methodology](#method)

3. [Dataset Description - MDD](#desc)

   3.1 [Dataset Features](#features)

   3.2 [Moral Decision - Y](#moraldecision)

5. [Ethics Scoring Algorithm - ESA](#esa)

   4.1 [Modules](#mods)

   4.2 [Moral Judgement](#mj)

   4.3 [Context-Sensitive Thresholding](#cst)

6. [Resource Specifications](#stats)

7. [Repository Details](deets)  

8. [Setting Up](#setup)

9. [Tutorial](#tut)

10. [_A Cautionary Tale!_](#beware)

11. [Resource Maintenance](#maintenance)

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

<a name="setup"></a>
#Setup Instructions

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



