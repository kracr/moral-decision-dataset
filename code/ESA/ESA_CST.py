import numpy as np
import pandas as pd
from statistics import mean, variance

#value of characteristics of consequence
sev = [-0.82, 0.2, 0.4, -0.5] #[mild, intermediate, significant] [0, 0.5, 1]
ut = -0.76 #[good, neutral, bad] [0, 0.5, 1]
dur = -0.60 #[short term, medium term, long term] [0, 0.5, 1]

cq = [sev, ut, dur]

#value of moral intention
mi = 0.99 #[good moral int, bad moral int, no moral int]

#value of ethical principle
beneficence = 0.48 #[upheld, violated]
nonmaleficence = -0.72 #[upheld, violated]
responsibility = -0.91 #[upheld, violated]

ep = [beneficence, nonmaleficence, responsibility]

ep = mean(ep)
round(ep,2)

choice = 'cons'
#choice = 'deon'
#choice = 'virt'

#if-conditions

def et(choice):
    w = []
    if choice == 'cons':
        w = [1, 0.5, 0.5]
    elif choice == 'deon':
        w = [0.5, 1, 0.5]
    elif choice == 'virt':
        w = [0.5, 0.5, 1]
    else:
        w = [1, 1, 1]
    return w

def ej(cq, mi, ep, weights):
    j=0
    
    #calculating the weighted sum
    
    #calculating using weights
    sev = cq[0]*weights[0]
    ut = cq[1]*weights[0]
    dur = cq[2]*weights[0]
    
    mi = mi*weights[1]
    
    ep = ep*weights[2]
    
    #calculating judgement using sum
    j = sev+ut+dur+mi+ep
    return j

weights = et(choice)
judgement = ej(cq, mi, ep, weights)
judgement

#grey area default values
thr_defaults = {
    "Bioethics": 0.4,  # Broad scope; ethical disagreements on genetics, AI in medicine, etc.
    "Medical Ethics": 0.2,  # Patient-centered with clear guidelines; some dilemmas remain.
    "Research Ethics": 0.3,  # Some clear-cut rules (e.g., no plagiarism), but emerging AI issues create ambiguity.
    "Animal Ethics": 0.45,  # Ethical treatment of animals varies across cultures and industries.
    "Corporate Ethics": 0.5,  # Business ethics differ based on laws, globalization, and industry norms.
    "Environmental Ethics": 0.35,  # Climate action is urgent, but economic and policy trade-offs exist.
    "AI & Data Ethics": 0.4,  # Balancing privacy, bias, and fairness in AI is difficult.
    "Neuroethics": 0.3,  # Ethics of brain enhancement, neuroprivacy, and consciousness studies.
    "Tech & Cyber Ethics": 0.45,  # Issues like online privacy, misinformation, and cyberwarfare have evolving norms.
    "Legal Ethics": 0.25,  # Strong professional codes but grey areas in advocacy and confidentiality.
    "Media & Journalism Ethics": 0.35,  # Objectivity, sensationalism, and political biases create grey zones.
    "Military Ethics": 0.2,  # Rules of war exist (e.g., Geneva Conventions), but moral dilemmas arise in conflicts.
    "Political Ethics": 0.5,  # Corruption, lobbying, and governance transparency vary by system.
    "Sports Ethics": 0.4,  # Issues like doping, fairness, and commercialization create moral debates.
    "Educational Ethics": 0.3,  # Student rights, academic integrity, and AI in learning present ethical dilemmas.
    "Sexual Ethics": 0.35,  # Consent is clear-cut, but cultural norms create grey areas.
    "Religious Ethics": 0.5,  # Varies by belief system; moral relativism is a factor.
}

#based on standards 
#things may be debatable
#disclaimer: footnote: there are broader standards on which people agree whereas some require more debate/research. There might be disagreements. 
#Privacy and bias have some common agreement however, there is a lack of regulation
#why are there variations? there is no way to resolve some of these concerns
#cautionary suggestion: 
#moral advisor papers
#how do you want an AI to give advice? Should it give advice based on my values?
#does it give me like a 'correct' solution
#contradictory opinion?
#we have a theoretical understanding of ethics but requires a clear cut framework
#clarify why we chose this model?
#any agent's reasoning, how does it take certain parameters into account?
#use case? why going in a particular use case?

get_ipython().system('pip install scipy')
from scipy.stats import entropy

p = [sev, ut, dur, mi, round(ep,2)]

p = [0.3, 0.6, 0.4]

#try entropy
ent = entropy(p, base=2)
print("Entropy:", ent)

#try variance
var = variance(p)
var

grey_area = thr_defaults[domain] + var
grey_area
#context-sensitive thresholding 

domain = "Medical Ethics"

def place_judgement(judgement, grey_area):
    ans = ""
    if judgement < -1*grey_area:
        ans = "morally wrong"
    elif judgement > grey_area:
        ans = "morally right"
    elif judgement > -1*grey_area and judgement < grey_area:
        ans = "morally grey"
    return ans

ans = place_judgement(judgement, grey_area)
print(ans)

#-1________________________-g______0______g__________________________+1
# domain, context : context-sensitive thresholding


