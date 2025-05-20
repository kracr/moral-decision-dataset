#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install rouge-score nltk')


# In[2]:


# Define reference summaries and extracted features (ground-truth)
references = [
    {"summary": "A hospital mistakenly reported a living person as deceased to a funeral home, resulting in the funeral home informing the person’s husband about her death. The individual discovered the error, and while the funeral home apologized, the hospital provided no clear resolution. Friends have suggested seeking legal advice.",
     "features": "Hospital staff,The person mistakenly reported as deceased,Incorrectly reporting the individual as deceased to a funeral home,Healthcare,Emotional distress caused to the individual and her family,Loss of trust in the healthcare institution,Moderate,Negative,negligence,None,Confidentiality/privacy,Hospital staff providing medical records information about the individual to a third party"},
    
    {"summary": "The user's husband received a call claiming he failed to appear for jury duty, leading to a demand for $8,000 or two nights in jail. The situation arose because a new tenant allegedly signed the jury summons. However, it was later revealed to be a scam. Thanks to advice from others, they stopped communicating with the scammers, and the bank’s fraud alert team is now assisting in recovering the lost money.",
     "features": "Scammers, husband,Fraudulent phone call claiming missed jury duty and demanding payment,Legal,Fraud,Financial Loss, Severe,Negative, short term,Malicious,None,Fairness,Scaamers impersonating legal authorities"}

]


# ### LLM1 - Llama 3.0

# In[3]:


# Define candidate summaries and extracted features (predicted/generated)
candidates = [
    {"summary": "The funeral home did contact the husband with condolences to the wrong person which led to emotional distress. The funeral home had bad moral intention, however, the contact violated privacy ethical principle which caused invasion of privacy.",
     "features": "Hospital/Funeral Home,Husband/Wife,Providing incorrect information,Healthcare , Miscommunication,Emotional distress,High,Harmful,Long term,Negligence,None,Respect for life, Stranger to acquaintance"},
    
    {"summary": "The scammers did scam to the husband which led to financial loss. The scammers had bad moral intention, however, the scam violated trust ethical principle which caused financial issue.",
     "features": "Scammers/New Tenant,Husband,Signing jury summons,Justice/Legal,Identity theft,Financial loss,Severe, Harmful,Immediate and long-term,Malicious, None,fairness in justice,Stranger"}
    
    
]


# In[5]:


from rouge_score import rouge_scorer
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction




# Initialize ROUGE scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
smooth = SmoothingFunction().method1  # Smoothing function for BLEU

# Store results
summary_bleu_scores = []
feature_bleu_scores = []

print("\n===== Evaluation Results =====")
for i, (ref, cand) in enumerate(zip(references, candidates), 1):
    # ROUGE Scores for Summaries
    summary_rouge = scorer.score(ref["summary"], cand["summary"])
    feature_rouge = scorer.score(ref["features"], cand["features"])

    # BLEU Scores (Tokenized input)
    summary_bleu = corpus_bleu([[ref["summary"].split()]], [cand["summary"].split()], smoothing_function=smooth)
    feature_bleu = corpus_bleu([[ref["features"].split()]], [cand["features"].split()], smoothing_function=smooth)

    summary_bleu_scores.append(summary_bleu)
    feature_bleu_scores.append(feature_bleu)

    print(f"\nExample {i}:")
    print(f"Reference Summary: {ref['summary']}")
    print(f"Candidate Summary: {cand['summary']}")
    print(f"ROUGE-1: {summary_rouge['rouge1'].fmeasure:.4f}, ROUGE-2: {summary_rouge['rouge2'].fmeasure:.4f}, ROUGE-L: {summary_rouge['rougeL'].fmeasure:.4f}")
    print(f"BLEU Score (Summary): {summary_bleu:.4f}")

    print(f"\nReference Features: {ref['features']}")
    print(f"Candidate Features: {cand['features']}")
    print(f"ROUGE-1: {feature_rouge['rouge1'].fmeasure:.4f}, ROUGE-2: {feature_rouge['rouge2'].fmeasure:.4f}, ROUGE-L: {feature_rouge['rougeL'].fmeasure:.4f}")
    print(f"BLEU Score (Features): {feature_bleu:.4f}")

# Compute Average Scores
avg_summary_bleu = sum(summary_bleu_scores) / len(summary_bleu_scores)
avg_feature_bleu = sum(feature_bleu_scores) / len(feature_bleu_scores)

print("\n===== Average Scores =====")
print(f"Average BLEU Score (Summaries): {avg_summary_bleu:.4f}")
print(f"Average BLEU Score (Features): {avg_feature_bleu:.4f}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




