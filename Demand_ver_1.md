#Demand *ver.1*
##Introduction to the *Project Vtuber* (temp)
The whole project is based on the MVC model, which consist four parts.Front end, 
control, business logic and data base.

+ It is welcomed to add your own thought and any useful information below each demand.
+ !!We haven't name our project yet.
+ ver.1 is the origin version of this project. The **MAJOR** change will be recorded below:

> 2020/10/17 ver.1 : file created.
##Front end
The front end will will mostly likely to be a web page to get the text from the user, 
generate the figure and voice of the Vtuber.
###IO
+ The front end will have some code to get input text from the 
[damuji](https://www.danmuji.org).
+ DDL: N/A
+ Contributor: N/A
###Visual
+ The figure (or the 'skin') of the vtuber will based on live2D and js, for more details see
[Live2D](https://www.cnblogs.com/liuzhou1/p/10813828.html) 
> This is the best solution I could thought so far, if there's any idea,please tell me. 
*(by Wb)*
> And we need a good painter :P
+ DDL: N/A
+ Contributor: N/A
###Voice
+ The voice part will generate the output text to speech. Maybe with subtitle?
+ The actual code may be in the serve, see Control -voiceGenerator
> Honestly I don't know much of the this part. Probably vocaliod? Or something else? I'm not sure.
*(by Wb)*
+ DDL: N/A
+ Contributor: N/A

##Control
The control part will receive the input text and do the basic analyze *(alternative)*, receive the output of 
the business logic part and deliver it to each other. Also it will be connected to the data base.
###Framework
+ The framework of the control will probably be the [spring boot](https://spring.io/projects/spring-boot). Which
means it will be written in java. 
> Since I've written one *(by Wb)*
###WebController
+ This will be the controller of the Web part. To control the figure, emotion (if possible) of the vtuber
 and transmit voice file. 
+ Since it's a server, it is possible to be deployed on the school wifi. 
 **So it may become a possible way to collect data and train the algorithm**
+ DDL: N/A
+ Contributor: N/A
###TextAnalyze *(alternative)*
+ Using the [jieba Segmenter](https://www.cnblogs.com/bky-lzw/p/7799238.html) or others to process the raw input.
+ This can be embed in the business part.
+ DDL: N/A
+ Contributor: N/A
###VoiceGenerator
+ This will convert the returned text to sound file
+ DDL: N/A
+ Contributor: N/A
###DataBaseControl
+ It is most likely we will use myBatis to operate our database, if more technical details are needed, please note below.
> Note Here
+ DDL: N/A
+ Contributor: N/A

##DataBase
+ Maintainer:
I strongly recommended [sqlite](https://sqlite.org/index.html), since it's light weighted and easy to learn. The 
database will be used to store the component of the language and some frequent used phrases. Maybe even short-term
memory (if we have enough time and energy).
###Component
+ It will store everything we need to assemble a sentence. From words to phrases. It may be made up of several parts. 
One possible solution is to use the existing NLP data base.
+ If we collect enough fixed phases, the performance of our vtuber will be much better.
###ShortTermMem *(alternative)*
+ Surprisingly we have enough time to do this. The major purpose of this is to help our lovely Miss.AI to remember what 
she has said and what others have told her one minute ago.
> I don't how to realize it, or through which way. Just forget for now (by Wb)

##A.I.Kernel (Business logic)
+ DDL: N/A
+ Contributor: N/A
Finally we come to 'heart' of our AI. Depends on the method we use, we will face many complete different problems. If we
use DeepLearning, then dataset is needed. If we use profession system, huge amount work will be ahead. Since we haven't
decide which method will use. The detail of the part can't be written.
> //TODO


>written by Wb 2020/10/17