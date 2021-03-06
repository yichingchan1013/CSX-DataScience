# 107-2 Data Science & Programming

## Introduce Myself 
I am Yiching :smiley: A passionate learner in data analytics. This is the weekly report of my progress in the course *Data Science & Prgramming*. 

## Projects Overview
1. [project 1 - Keywords Analysis](https://github.com/yichingchan1013/CSX-DataScience/tree/master/project1): Words clouds of certain topics (豬瘟、台大校長遴選) based on the news articles scraped from Liberty Times Net .  
2. [project 2 - Data Mining](https://github.com/yichingchan1013/CSX-DataScience/tree/master/project2): 91APP Customer behavior anaylsis with data visualization.
3. [project 3 - Text Analytics](https://github.com/yichingchan1013/CSX-DataScience/blob/master/project3/Zootopia%20text%20analytics.ipynb): Keywords analysis and Senetiment analysis on Zootopia screenplay.
4. [project 4 (final project) - Customer Relationship Management](https://github.com/yichingchan1013/CSX-DataScience/blob/master/project4(final%20project)/Final%20Presentation.pdf): A) predict customer segmentation based on their first transation records to customize future promotions. B) predict customer chrun to improve customer retention. C)Analyze the effects of promotions and Ecoupon on different customer segmentation.



### Reference
- [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [visualize Python](http://pythontutor.com/visualize.html?fbclid=IwAR2q1rmTpHAJmxUOhD_p00Wm4HTITX7EGCxy-o7U_pns0liWl0sEx7cODtc#mode=edit)
- [Selecting the Perfect Visualization for Your Data](https://www.techprevue.com/decision-tree-perfect-visualisation-data/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

# Progress Report 

## week 1 (2/21)
   - Course Introduction
   - Github Introduction & Setup 

To-Do:
   - [x] create README.md 
   - [x] add GitHub link at NTU COOL
   - [x] upload homework0 to Github before 3/7 10pm
   - [x] check out more info. at COOL

## week 2 (2/28) no class- Homework0
To-Do:
   - [x] [HW0](https://github.com/yichingchan1013/myGithub/tree/master/hw0)
   - draw Flow chart of the sample code 
   - Crawl news articles from 自由時報生活版 to make wordclouds


## week 3 (3/07)
   - Introduction to open data sources
   - Determine our own topic on EDA (91APP)


## week 4 (3/14) 選定一種領域資料集，提出對資料的看法與問題定義流程說明
   - Introduction to data visualization 
   - practice EDA in group 
   
Self-taught: Data Visualization from Coursera [IBM Data Science Professional Certificate Specialization](https://www.coursera.org/specializations/ibm-data-science-professional-certificate)
   - IBM data analysis:
      - [X] Data Wrangling 
      - [X] Exploratory Data Analysis
   - IBM data visualization:
      - [X] Introduction to Matplotlib and Line Plots
      - [X] Area Plots, Histograms, and Bar Plots
      - [X] Pie Charts, Box Plots, Scatter Plots, and Bubble Plots
      - [ ] Waffle Charts, Word Clouds, and Regression Plots
      - [ ] Generating Maps with Python
   - work on [IBM Developer Skills Network Labs](https://labs.cognitiveclass.ai/tools/jupyterlab/)



## week 5 (3/21) 資料預處理 & 視覺化，進行 EDA，提出對資料更深刻的理解。
   - case study: 台北市長候選人臉書經營方式的影響分析 (question defined,sentiment analysis,LDA) 
   - practice EDA in group 
   
Self-taught: review python fundamentals @ ccClub problem sets

## week 6 (3/28) 
   - presentation of 南山理賠服務
   - presentation of 南山理賠再購資料分析
   - case study: 韓國瑜 & 陳其邁 2018 年 9 月臉書資料文本分析 (LDA、DTM & 共現性圖)

## week 7 (4/4) spring break

To-Do:
   - [X] [hw1-3](https://github.com/yichingchan1013/myGithub/blob/master/hw1-3/91APP%20%E5%AE%A2%E6%88%B6%E5%88%86%E6%9E%90-Copy1.ipynb) EDA & preliminary results (submit by 4/10)
   
  
## week 8 (4/11)   
   - hw1-3  peer sharing 
   - Introduction to Maching Learning & Deep Learning
   
To-Do:
   - [X] group set up 
   
## week 9 (4/18) 對文字資料進行預處理。	
   - Introduction to TF-IDF(文字向量化，假設出現越多次越重要), Word2vec(文字向量化，大量訓練), PCA（降維）, Kmeans clustering（未標記標準答案）, SVM（有標記標準答案）
   - case study: 數據唐詩（基本假設：唐詩用字精練，字詞出現越多次表示重要度越高，沒有贅詞的問題）
   - group discussion: 針對屬性去做客戶分類

To-Do:
   - [X] 91APP 針對屬性再做EDA，找出可用來分群的x,y。下週討論主題大方向和分工
 
## week 10 (4/25) 使用 NER 對文本進行重點動態標註。  
   - Introduction to NER & statistics

To-Do:
   - [X] 討論分析的大方向：有無生日禮&開卡禮對使用者行為的影響、界定VIP客戶作為最後預測的目標、促銷活動的效果（暫定）
   - [X] EDA based on attriubes in datasets (instead of 'time trend')

Self-taught:
   - Machine Learning from [Machine Learning A-Z™: Hands-On Python & R In Data Science](https://www.learningcrux.com/course/machine-learning-a-z-hands-on-python-r-in-data-science): done Classifiers' section
   - Machine Learning from coursera [by Prof.Andrew Ng](https://www.coursera.org/learn/machine-learning/home/welcome) : Linear regression with one variable
   
   
## week 11 (5/2) 將文字標記分類透過共現性與關聯分析進行視覺化。  
   - Introduction to Apriori algorithm （關聯性分析）
      - 共現性：看不出先後，且運算高效率。關聯性：可以看出先後，運算量大。
      - 實務上：先用共現性畫出heatmap，再挑出關聯性高的項目進行關聯性分析。
   - 實習經驗分享：野村證券

To-Do:
   - [X] [hw4-6](https://github.com/yichingchan1013/CSX-DataScience/blob/master/hw4-6/Zootopia%20text%20analytics-Copy2.ipynb)
   - 題目：文字探勘《動物方程式》，分析角色重要用字與情緒走向 
      
## week 12 (5/9)
   - hw4-6 peer sharing part1
   - 確定各組名單與題目

To-Do:
   - [X] 確定期末專案的主題與發展方向 (pitch on 5/16)
   
Self-taught:
   - 《Data Science for Business》 chap1-5
## week 13 (5/16) Pitch in group
   - pitch in group part1
   - talk: 矽谷的溫度 
## week 14 (5/23)
   - pitch in group part1 

To-Do:
   - [X] 期末專案進度：baseline model 把資料格式化，從首購訂單預測所屬客群

## week 15 (5/30)
   - Recap 專案觀摩：從客服聯繫紀錄找出潛在銷售機會、投資人實際投資行為與風險屬性評估之落差
   - pattern hunter 產品介紹

To-Do:
   - [X] 期末專案進度：rolling window，定義問題＋模型訓練
   - [ ] 期末專案進度: 驗證promotion/ecoupon的效果
   - [X] 6/6 把進度放上github由老師決定期末報告組別
   
  
## week 16 (6/6) 努力做專案
   - 專案進度討論
   
## week 17 (6/13) Final Demo
   - final project [顧客消費行為預測與折扣優惠影響之探討](https://github.com/yichingchan1013/CSX-DataScience/tree/master/final%20project)  


