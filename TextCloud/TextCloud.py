from wordcloud import WordCloud
import jieba
import PIL
#python image library图像处理库
import numpy as np
#矩阵数值计算库
import matplotlib.pyplot as plt
#图表库

temp=[]
file=open('example.txt','r').read()
words=list(jieba.cut(file))
for word in words:
    if len(word)>1:#去除标点及空格
        temp.append(word)
txt=r' '.join(temp)#以' '连接列表中各项为str

backdrop=np.array(PIL.Image.open('example.png'))
cloud=WordCloud(font_path='example.ttf',
                background_color='white',
                margin=5,width=1800,height=800,
                mask=backdrop,
                max_words=2000,
                max_font_size=60,
                random_state=42)
cloud=cloud.generate(txt)
cloud.to_file('output.jpg')
plt.imshow(cloud)
plt.axis('off')
plt.show()
