# myHateSpeech
myHateSpeech: Myanmar hate speech datasets and experiments.

Today, social media platforms, especially Facebook, are widely used by Myanmar people for communication, information sharing, and news updates in their native language. However, this has also led to a rise in harmful content, including hate speech, disinformation, and misinformation.

To address this issue, **the Language Understanding Lab, Myanmar** is actively developing Myanmar-language hate speech corpora and conducting NLP experiments, such as hate speech keyword extraction and hate speech classification.

This repository (**myHateSpeech**) will share:

- Work-in-progress hate speech datasets
- Experimental logs & results
- Related academic publications

*Note: Datasets may vary in format and size across releases.*

## Hate Speech Tags  

We defined **9 distinct classes** to reflect a comprehensive approach to understanding and addressing harmful speech in online communication. Below are the definitions and examples for each hate speech tag:

**1. Abusive Hate Speech (ab)**  
Sentences that use abusive language, criticize minorities, promote hate speech/crimes, or misrepresent facts while blaming minority groups.  

*In Myanmar:* မကောင်းဆိုးဝါးအကောင် လာဘ်ပိတ် တယ်  
*In English:* "You're a monster who brings bad luck."  

**2. Religious Hate Speech (re)**  
Sentences that include disrespectful language, unfair generalizations, or offensive remarks about a religion or its followers.  

*In Myanmar:* သီလရှင်လောဘပင်လယ်ဝ  
*In English:* "The Buddhist nun’s greed is boundless."  

**3. Racist Hate Speech (ra)**  
Sentences that discriminate against individuals or groups based on race, claim racial superiority, or advocate unequal treatment.  

*In Myanmar:* တိုင်းရင်းသားထဲမှာ ဗမာ လူမျိုး က အယုတ်မာဆုံး  
*In English:* "Burmese people are the meanest among all ethnic groups."  

**4. Body-Shaming Speech (bo)**  
Sentences that mock or discriminate based on physical appearance, body movements, disabilities, or health conditions (e.g., autism, cancer).  

*In Myanmar:* အနောက် က ဖက်တီး ဘာ ဖြစ် နေ တာ လဲ  
*In English:* "What’s wrong with the fatty at the back?"  

**5. Political Hate Speech (po)**  
Sentences expressing hostility toward political ideologies, parties, or individuals based on their political views.  

*In Myanmar:* ဒီ နိုင်ငံရေးစနစ်ကြီးက ချီးထုပ် ပါ ကွာ  
*In English:* "This political system is shit."  

**6. Sexist Speech (se)**  
Sentences promoting hate based on gender (including orientation) or containing sexual abuse content.  

*In Myanmar:* အဲ့ဒီ စောက်ခြောက် က ဘယ်သူ လဲ  
*In English:* "Who is that fucking gay?"  

**7. Lethal Speech (le)**  
Sentences wishing harm, misfortune, or negative events upon someone (e.g., curses, violent threats).  

*In Myanmar:* ဖမ်းခံရပါစေ  
*In English:* "I hope you get arrested."  

**8. Educational Hate Speech (ed)**  
Sentences mocking or discriminating based on educational background, intelligence, achievements, or choices.  

*In Myanmar:* ဆယ်တန်းတောင်မအောင် တဲ့ ငတုံး က များ  
*In English:* "An idiot who didn’t even pass 10th grade."  

**9. No Hate Speech (no)**  
Neutral sentences without hateful or discriminatory content.  

*In Myanmar:* အပေါ် က စာကြောင်း တွေ က ဥပမာ ပြ ဖို့ ပဲ သုံး သင့် ပါ တယ်  
*In English:* "The above sentences should only be used as examples."  

## Corpus Building, Annotation, and Format

We manually collected hate speech sentences from **Facebook** (the most widely used social platform in Myanmar). The corpus is annotated at both **word/phrase-level** and **sentence-level**:

### Word/Phrase-Level Annotation  
- If a word/phrase constitutes hate speech, we annotate it with a slash (`/`) followed by its hate speech class.  
  **Example (Myanmar):** မအေလိုး`/ab`  
  **English:** "motherfucker`/ab`"  
- Phrases composed of multiple words (without spaces) are annotated as a single unit.  
  **Example (Myanmar):** ကျက်သရေမရှိ`/ab`  
  **English:** "lacking grace`/ab`"  
- For words/phrases with multiple hate speech classes, we use pipe-separated tags (`|`).  
  **Example (Myanmar):** စောက်ခွက်`/ab|bo`  
  **English:** "fucking face`/ab|bo`"  

### Sentence-Level Annotation  
Each sentence receives **one tab-separated label** based on its overall meaning.  

### Examples:

```
ခွေးရူးကောင်းစားတစ်မွန်းတည့်/ab ab
အသံ လေး ရော ရုပ် လေး ရော က ဆဲ ချင် စရာ လေး နော် ဖော်လော်မော်/ab လေး 🤧🤧 bo
မေး ပါ ဦး မယ် နင် တို့ အကယ်ဒမီ က ဘယ်သူ တွေ ကို ပေး မှာ လဲ no
ဦးနှောက်ကဂုတ်ကပ်/ed နေ တော့ ဘယ် နားလည် မ လဲ $ကောင်မ/ab ရဲ့ ed
ဥာဏ်ရည်နိမ့်/ed|ab ဖော်လော်မော်မ/ab အောက်တန်းစား/ab က အောက်တန်းစား/ab ပဲ အဆင့် တက် မ လာ နိုင် ဘူး ab
ဒီလောက်ကြီးတဲ့နို့ကြီး/se ရှိ နေ တာ ကို မ ခိုင်နှင်းဝေ ဆီ တစ် ခါ လောက် သွား လှူ သင့် တာ ပေါ့ 😂 😂 😂 😂	se
ဘယ် နား လှ တာ လဲ စောက်ခွက်/ab|bo က တောရုပ်/ra|bo နဲ့ တိုက်ဂေါမ/ra ချစ် စရာ လည်း မ ကောင်း	bo
ဘာ မ ဟုတ် တာ တဲ့ လား 🤌 ကိုယ့် ဘာသာ လုပ် မယ် ဆို တခြား စကား မ ပြော တတ် ဘူး လား လူ အခွင့်ရေး လူငယ် တိုင်း ဆုံးရှုံး နေ ရ တဲ့ ချိန် ဖင်အရမ်းမယားပြပါနဲ့/ab 👌	po
ဦးနှောက်ကပညာမဲ့မှန်းသိသာလိုက်တာ/ed ဘာ မ ဟုတ် တဲ့ ဟာမ/ab က ခွေးစကား/ab တွေ ပြော တာ ဆို တော့ 🙃	ed
ခွေးသူတောင်းစားမ/ab မွေးကတည်းကအသေလေးမွေးခဲ့ရမှာ/le	le
```

## Version Information of the myHateSpeech Corpus

We manually collected hate speech sentences from **Facebook** between **January 2023 and August 2023**, preserving all original content including emojis.  
### Version 0.9  
[`myHateSpeech_ver0.9.txt`](https://github.com/ye-kyaw-thu/myHateSpeech/blob/main/corpus/version0.9/myHateSpeech_ver0.9.txt)  

**Technical Details:**  
- **Encoding:** UTF-8  
- **Format:** Plain text (with original emojis preserved)
- **Size:** 10,140 sentences  
- **Structure:** `hate-speech_tagged_Myanmar_sentence<TAB>sentence_level_hatespeech_tag`  

### Version 1.0  
Version 1.0 is a manually corrected version of Version 0.9 with annotation errors fixed. For detailed changes, please refer to [this file](https://github.com/ye-kyaw-thu/myHateSpeech/blob/main/corpus/version1.0/diff_ver0.9_and_ver1.0.txt).  

[`myHateSpeech_ver1.0.txt`](https://github.com/ye-kyaw-thu/myHateSpeech/blob/main/corpus/version1.0/myHateSpeech_ver1.0.txt)  

**Technical Details:**  
- **Encoding:** UTF-8  
- **Format:** Plain text (with original emojis preserved) 
- **Size:** 10,140 sentences  
- **Structure:** `hate-speech_tagged_Myanmar_sentence<TAB>sentence_level_hatespeech_tag`

## License

Creative Commons Attribution-NonCommercial-Share Alike 4.0 International (CC BY-NC-SA 4.0) License  
[Details Info of License](https://creativecommons.org/licenses/by-nc-sa/4.0/)  

## Experiments

### Hate Speech Generation Experiment  

The lack of publicly available hate speech corpora for Myanmar (a low-resource language) presents significant challenges. Using the developing myHateSpeech corpus (v0.9), we conducted **automatic hate speech generation experiments**.  

Our work-in-progress results were presented at:  
📌 **5th NLP/AI R&D Workshop** (27 November 2023)  
📍 Co-located with iSAI-NLP-AIoT 2023, Thailand  

🔍 *Explore the experiment:*  
[`Experiment with myHateSpeech (version 0.9)`](https://github.com/ye-kyaw-thu/myHateSpeech/tree/main/corpus/version0.9/experiment)  

---

### Hate Speech Classification via Lexicon-Based Filtering  

With **myHateSpeech v1.0**, we propose:  
- Building a **hate speech dictionary** from annotated data  
- Using **fastText models** to compare:  
  - Classifiers trained on unfiltered long sentences  
  - Classifiers trained on lexicon-filtered short sentences  

**Key Result:**  
✅ Achieved **0.771 accuracy** through lexicon-enhanced filtering  

📄 *Published at:*  
**JCSSE 2024** (June 19–22, 2024, Phuket, Thailand)  

🔍 *Explore the experiment:*  
[`Experiment with myHateSpeech (version 1.0)`](https://github.com/ye-kyaw-thu/myHateSpeech/tree/main/corpus/version1.0/experiment)  

## Citation

If you use the **myHateSpeech (Version 0.9 or 1.0)** corpus in your research, we would appreciate it if you cite the following reference:  

Nang Aeindray Kyaw, Ye Kyaw Thu, Hutchatai Chanlekha, Thazin Myint Oo, Okumura Manabu and Thepchai Supnithi, "Enhancing Hate Speech Classification in Myanmar Language Through Lexicon-Based Filtering", the 21st International Joint Conference on Computer Science and Software Engineering (JCSSE 2024), June 19-22, Phuket, Thailand, pp. 325-332 [[Paper-Link]](https://ieeexplore.ieee.org/document/10613636)  

## To Do

- We will continue expanding the myHateSpeech corpus  
- We plan to conduct automatic hate speech generation and classification experiments with the extended corpus  

## References

[1] nanoGPT: [https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)   

