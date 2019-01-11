### 数据采集和统计（结构化和非结构化的分析）
##### 数据采集时间截止到2018年12月28日，数据条数为15万条，平台为智联和51_job，算是给要找工作的自己一个方向
####  结构化分析：对采集的数据进行全国性的统计
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/cl.png)
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/dc.png)
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/edu.png)
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/exp.png)
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/LDA4.png)
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/money.png)
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/salary.png)
![cl](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/analysis_result/type.png)
### 非结构化分析：对科技类人才招聘需求挖掘
###
>#### 主题挖掘作用：用于主题发现与热点分析，主题挖掘任务的本质是将输入的文本流划分到不同的主题类中，并且在必要时候建立新的主题类。
#### 招聘主题挖掘技术能从复杂的数据中识别出招聘单位的需求，通过词权的方式对文本关键字进行提取，并利用主题模型对主题进行聚类，以达到提炼需求的目的。本文对招聘主题挖掘进行了问题描述和任务框架梳理，通过智联招聘信息采集、文本预处理、主题挖掘算法和主题建模四个方面进行主题挖掘。
### 
### 处理框架为 
![框架](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/pic/处理路线.png)
### 相似度计算结果为
![相似度计算](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/pic/相似度效果.png)
### 基于词频的LDA主题聚类为 
![聚类3](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/pic/LDA-3.png)
![聚类4](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/pic/LDA4.png)
### 基于词权的LDA主题聚类为 
![聚类3](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/pic/tf-idf-lda3.png)
![聚类4](https://github.com/CarryChang/zhilian-51job-analysis/blob/master/pic/TF-IDF+LDA4.png)
结论：基于词频的可视化LDA的方法得出来的主题关键字无法反应低频信息，造成词频关键信息缺失，而使用TF-IDF的方法进行向量化之后，既考虑频次又考虑权重，能反应低频关键信息，弥补了频次带来的的误差。
