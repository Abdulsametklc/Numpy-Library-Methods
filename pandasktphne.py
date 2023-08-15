import pandas as pd

veri = {"isim":["Abdulsamet","Betül","Mehmet","Tuğra","Selim","Mete"], #veri seti
      "Glukoz":[90,140,55,88,180,77], #mg/dL
      "Kilo":[80,100,77,88,55,55], #kg
      "Hastalik":[0,1,0,0,1,0]} # 0: Sağlıklı, 1: Hastalıklı

df = pd.DataFrame(veri) #veri setini dataframe'e çevirme
df.head(veri) #ilk 5 satırı gösterme
df.tail(veri)#son 5 satırı gösterme
df.columns #sütun isimlerini gösterme
df.info() #veri seti hakkında bilgi verir
df.dtypes #sütunların veri tiplerini gösterir
df.describe() #sayısal sütunların istatistiksel bilgilerini gösterir
df.shape #satır ve sütun sayısını gösterir