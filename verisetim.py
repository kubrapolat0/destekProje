from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import pandas as pd


class MetinSınıfı:
    def __init__(self):
        self.data = {
            'text': [
                'futbol, basketbol, voleybol, ragbi, tenis, atletizm, yüzme, hentbol, kayak, koşu, güreş, golf, triatlon, masa tenisi,'
                'amerikan futbolu, sörf, okçuluk, bisiklet, buz pateni, paten, jimnastik',
                'yapay-zeka, programlama, kodlama, siber güvenlik, yazılım, internet, bilgisayar, veri madenciliği,'
                'robotik, donanım, bulut bilişim, otomasyon, python, makine, makine öğrenme',
                'seyahat, turistik, tatil, macera, gezi, doğa, kamp, plaj, deniz, gezgin, maceracı, keşif',
                'borsa, para, vergi, ekonomi, faiz, yatırım, şirket, enflasyon, gelir, borç, piyasa, ticaret, döviz',
                'resim, sergi, sinema, opera, dans, edebiyat, enstrüman, heykel, müzik, tiyatro',
                'öğrenci, öğretmen, sınav, vize, final, büt, üniversite, kitap, makale, öğrenim, akademisyen, proje, okul, ödev'
            ],
            'category': ['Spor', 'Teknoloji', 'Seyahat', 'Ekonomi', 'Sanat', 'Eğitim']
        }

        self.df = pd.DataFrame(self.data)

        # modelin eğitilmesi
        self.model = make_pipeline(TfidfVectorizer(), SVC(kernel='linear', C=1.0))
        self.model.fit(self.df['text'], self.df['category'])

    def predict_category(self, text):
        text_lower = text.lower()

        # girilen kelimelerin hangi sınıfta olduğuna bak
        categories = []
        for index, row in self.df.iterrows():
            if text_lower in row['text']:
                categories.append(row['category'])

        if not categories:
            return "Bu kelime verisetimde bulunmuyor, üzgünüm.\n Başka bir kelime yazmayı dene!"

        return ', '.join(categories)





