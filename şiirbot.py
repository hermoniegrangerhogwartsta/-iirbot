import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot aktif!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

threading.Thread(target=run_flask, daemon=True).start()
import telebot
from telebot import types
from telebot.types import BotCommand
import random

TOKEN = "8943756743:AAE0bKuw0RSoaFs1vFi9Qx1Ke3nMIQxiiHs"
bot = telebot.TeleBot(TOKEN)

# Telegram Sol Alt "Menü" Tuşu Komut Listesi
bot.set_my_commands([
    BotCommand("start", "🤖 Botu Başlat ve Karşıla"),
    BotCommand("menu", "📜 Şiir Kategorileri Menüsü"),
    BotCommand("yardim", "❓ Bot Nasıl Kullanılır?")
])

# 21 Adet Şiirlik Zengin Veritabanı
siirler = {
    'mutlu': [
        {
            'sair': "Nâzım Hikmet",
            'siir': "Yaşamak şaka değil,\nBüyük bir ciddiyetle yaşayacaksın...\nYani bütün işin gücün yaşamak olacak!",
            'giris': "Ne güzel işte, neşen daim olsun dostum! Bak senin bu güzel enerjine şu satırlar çok yakışır:",
            'yorum': "Nâzım'ın dediği gibi; hayat her şeye rağmen yaşamaya ve gülümsemeye değer. Bugün bu neşenin tadını çıkar!"
        },
        {
            'sair': "Orhan Veli Kanık",
            'siir': "Beni bu güzel havalar mahvetti,\nBöyle havada istifa ettim\nEvkaftaki memuriyetimden.\nTütüne böyle havada alıştım,\nBöyle havada aşık oldum...",
            'giris': "İçinin cıvıl cıvıl olduğunu hissetmemek imkansız! Bak Orhan Veli de tam o modu anlatıyor:",
            'yorum': "Orhan Veli'nin dediği gibi; bazen güzel bir an, insanın içindeki tüm kasveti dağıtmaya yeter."
        },
        {
            'sair': "Cahit Sıtkı Tarancı",
            'siir': "Gökyüzünün başka rengi de varmış!\nGeç farkettim taşın sert olduğunu.\nSu insanı boğar, ateş yakarmış!\nHer doğan günün bir dert olduğunu...",
            'giris': "Hayatın güzelliğini fark ettiğin o tatlı anlardasın! Bak sana ne döküldü mısralardan:",
            'yorum': "Cahit Sıtkı gibi etrafındaki güzelliklerin farkına varman harika bir duygu."
        },
        {
            'sair': "Can Yücel",
            'siir': "Gülümsemek bir eylemdir,\nVe her eylem bir devrimdir aslında.\nGülümse ki dünya değişsin...",
            'giris': "Yüzündeki tebessüm buraya kadar yansıdı valla! Al bak bu satırlar senin için:",
            'yorum': "Can Yücel'in dediği gibi, senin bir tek gülüşün bile ortamın havasını değiştirmeye yeter."
        }
    ],
    'yalniz': [
        {
            'sair': "Attilâ İlhan",
            'siir': "Gözlerin gözlerime değince felaketim olurdu ağlardım\nBeni sevmiyordun bilirdim bir sevdiğin vardı duyardım\nNe zaman seni düşünsem yaşamak kurak bir çöl gibi gelirdi...",
            'giris': "Seni çok iyi anlıyorum dostum... Bak şair de tam olarak senin bu kırgın ve hüzünlü halini özetlemiş:",
            'yorum': "Attilâ İlhan'ın da dediği gibi; hayat hep gülmeyi gerektirmez. Bazen hüzün de insana dâhildir."
        },
        {
            'sair': "Cahit Zarifoğlu",
            'siir': "Bize ağır gelen kendimizdir...\nGeceye söylenecek söz çoktur ama\nSessizlik en güzel cevaptır bazen.",
            'giris': "Seni çok iyi anlıyorum dostum... O içinin yalnızlığını hissettim, bak şair ne diyor:",
            'yorum': "Zarifoğlu'nun dediği gibi hayat her zaman kalabalık olmak zorunda değil. Yalnızlığını bir çay gibi demlemek gerekir bazen."
        },
        {
            'sair': "Ümit Yaşar Oğuzcan",
            'siir': "Ben seni unutmak için sevseydim\nSana olan sevgimi kalbime gömerdim.\nOysa ben seni yaşamak için sevdim...",
            'giris': "Seni çok iyi anlıyorum dostum... İçindeki o sızıyı duydum, al bak bu mısralar senin için:",
            'yorum': "Ümit Yaşar'ın dediği gibi; derin sevgilerin hüznü de derin olur. Yalnız değilsin."
        },
        {
            'sair': "Ahmet Hamdi Tanpınar",
            'siir': "Ne içindeyim zamanın,\nNe de büsbütün dışında;\nYekpare, geniş bir anın\nParçalanmaz akışında.",
            'giris': "Seni çok iyi anlıyorum dostum... Zamanın durduğu o yalnızlık anında şu satırlara tutun:",
            'yorum': "Tanpınar'ın hissettirdiği gibi; bazen kendi iç dünyamızda kaybolmak en büyük sığınaktır."
        }
    ],
    'hissizlik': [
        {
            'sair': "Edip Cansever",
            'siir': "Görüyorsun ya bir duyguyu düşünmek başka,\nBir duyguyla yaşamak başka...\nBen hangisindeyim bilmiyorum, içim bomboş.",
            'giris': "Anlıyorum seni, bazen insan ne hissettiğini bile bilemez... Bak şair de tam bu boşluğu kaleme almış:",
            'yorum': "Edip Cansever'in dediği gibi; hiçbir şey hissedememek de bir duygudur. Ruh bazen dinlenmek ister."
        },
        {
            'sair': "Turgut Uyar",
            'siir': "Her şeyi eksik anlatıyorum sanki,\nYada hiç anlatamıyorum.\nBir duygu var içimde ama adı yok...",
            'giris': "Kelimelerin tükendiği, duygunun bile karıştığı o andasın... Bak sana tam da bu hali anlatan mısralar:",
            'yorum': "Turgut Uyar'ın dediği gibi; bazen duygunun adı olmaz. Kendini zorlama, akışına bırak."
        },
        {
            'sair': "Sezai Karakoç",
            'siir': "Büyülenmiş bir akşamın ortasındayım,\nNe geceyim ben ne de gündüzüm.\nAdı konulmamış bir fırtınayım...",
            'giris': "İçindeki o belirsizliği, tanımı olmayan boşluğu hissettim. Al dostum şu satırları:",
            'yorum': "Sezai Karakoç'un dediği gibi; ruh bazen ne gece olur ne gündüz. Bu duraksama geçicidir."
        },
        {
            'sair': "İsmet Özel",
            'siir': "Gözlerim kapanıyor ama uykudan değil,\nİçimdeki o derin suskunluktan...\nBir şey söyleyememekten.",
            'giris': "Sessizliğin ve hissizliğin ne demek olduğunu çok iyi anlıyorum. Bak şu satırları oku:",
            'yorum': "İsmet Özel'in altını çizdiği gibi; bazen en büyük çığlıklar suskunlukta saklıdır."
        }
    ],
    'kavusamama': [
        {
            'sair': "Ahmed Arif",
            'siir': "Seni bağırabilsem seni,\nDipsiz kuyulara,\nAkan yıldıza,\nBir anlayan çıksa beni...\nSeni bir kavuşsam ah!",
            'giris': "Vah be dostum... Kavuşamamanın ve o büyük aşkın sancısını hissettim. Bak şair nasıl haykırmış:",
            'yorum': "Ahmed Arif'in dediği gibi; kavuşamamak sevgiyi azaltmaz, aksine içindeki ateşi daha da kor yapar."
        },
        {
            'sair': "Cemal Süreya",
            'siir': "Şimdi sen kalkıp gidiyorsun ya, herkes sana benzeyecek.\nAklımda kalışın, yüreğimde duruşun gibi değil...",
            'giris': "O büyük aşkın ve mesafelerin ağırlığını aldım... Al bak bu satırlar tam senin için:",
            'yorum': "Cemal Süreya'nın dediği gibi; özlem insanı olgunlaştırır. Kalbinde taşıdığın sevgi çok kıymetli."
        },
        {
            'sair': "Özdemir Asaf",
            'siir': "Seni bulmaktan önce aramak isterim.\nSeni sevmekten önce anlamak isterim.\nSana her gün yeniden başlamak isterim.",
            'giris': "Aşkın o tutkulu ve vazgeçilmeyen halini hissettim! Bak Özdemir Asaf senin için ne diyor:",
            'yorum': "Özdemir Asaf'ın dediği gibi; gerçek aşk bitmez, her gün yeniden başlar."
        },
        {
            'sair': "Abdurrahim Karakoç",
            'siir': "Lambada titreyen alev olsam,\nGideceğin yollara ışık tutsam.\nMihriban'ım desem sana,\nSessizce içimden ağlasam...",
            'giris': "Sevip de kavuşamayanların ahını duydum sanki... Bak şu efsane mısralara:",
            'yorum': "Karakoç'un Mihriban'da dediği gibi; 'Ayrılıktan zor belletme ölümü.' Sevginin en arı halidir bu."
        },
        {
            'sair': "Yahya Kemal Beyatlı",
            'siir': "Artık demir almak günü gelmişse zamandan,\nMeçhule giden bir gemi kalkar bu limandan.\nHiç yolcusu yokmuş gibi sessizce alır yol...",
            'giris': "Ayrılığın ve imkansızlığın o derin hüznü... Bak Yahya Kemal nasıl dile getirmiş:",
            'yorum': "Yahya Kemal'in dediği gibi; bazen kabullenmek ve sessizce izlemek gerekir."
        }
    ],
    'genel': [
        {
            'sair': "Cemal Süreya",
            'siir': "İki çay söylemiştik orda, biri açık,\nKeşke yalnız bunun için sevseydim seni.",
            'giris': "Satırlarının arkasındaki o samimi duyguyu aldım dostum. Bak bu mısralar seni anlatıyor sanki:",
            'yorum': "Cemal Süreya'nın dokunduğu gibi; hayat bazen küçük bir detayda gizlidir. İçindeki hisleri akışına bırak."
        },
        {
            'sair': "Aşık Veysel",
            'siir': "Uzun ince bir yoldayım,\nGidiyorum gündüz gece.\nBilmiyorum ne haldeyim,\nGidiyorum gündüz gece...",
            'giris': "Hayat yolculuğundaki o tatlı yorgunluğu hissettim dostum. Bak Veysel baba ne diyor:",
            'yorum': "Aşık Veysel'in dediği gibi; hepimiz bir yoldayız. Önemli olan yolda yürürken kalbi temiz tutmak."
        },
        {
            'sair': "Mevlana",
            'siir': "Gel, ne olursan ol yine gel,\nİster kafir, ister mecusi, ister puta tapan ol yine gel,\nBizim dergahımız, umutsuzluk dergahı değildir...",
            'giris': "İçindeki o samimiyeti aldım dostum. Sana Mevlana'nın şu kucaklayan sözleriyle cevap vereyim:",
            'yorum': "Mevlana'nın dediği gibi; kapı hiçbir zaman kapalı değildir. Umudunu asla kaybetme."
        },
        {
            'sair': "Bedri Rahmi Eyüboğlu",
            'siir': "Seni düşünürken bir çakıl taşı ısınır içimde,\nBir kuş havalanır avuçlarımdan.\nSeni düşünürken ben, insan olduğumu hatırlarım...",
            'giris': "Kalbinden geçen o güzel kırıntıları hissettim. Al bak şu mısralar senin için:",
            'yorum': "Bedri Rahmi'nin dediği gibi; insanı insan yapan içindeki sevgidir."
        }
    ]
}

# Butonlu Menü Yapısı
def ana_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b1 = types.InlineKeyboardButton("🎲 Rastgele Şiir", callback_data="kat_genel")
    b2 = types.InlineKeyboardButton("💔 Aşk & İmkansızlık", callback_data="kat_kavusamama")
    b3 = types.InlineKeyboardButton("🌧️ Yalnızlık & Hüzün", callback_data="kat_yalniz")
    b4 = types.InlineKeyboardButton("🌀 Hissizlik & Boşluk", callback_data="kat_hissizlik")
    b5 = types.InlineKeyboardButton("☀️ Mutluluk & Umut", callback_data="kat_mutlu")
    markup.add(b1, b2, b3, b4, b5)
    return markup

# Komut Dinleyicileri
@bot.message_handler(commands=['start', 'menu'])
def karsilama(mesaj):
    metin = (
        "Selam dostum! 📜\n\n"
        "İçini dökebileceğin, muhabbet edebileceğin bir dost köşesine geldin.\n"
        "Bana o an ne hissettiğini yazabilirsin (Örn: 'Üzgünüm', 'Çok mutluyum', 'Hissizim')...\n\n"
        "Veya aşağıdaki **menüden** istediğin kategoriye tıklayarak mısralara ulaşabilirsin!"
    )
    bot.reply_to(mesaj, metin, reply_markup=ana_menu())

@bot.message_handler(commands=['yardim'])
def yardim_mesaji(mesaj):
    metin = (
        "📖 **Nasıl Kullanılır?**\n\n"
        "1. Bana içinden geldiği gibi nasıl hissettiğini yazabilirsin. Ben durumunu analiz eder, tam o anki haline uygun şiiri fırlatırım!\n"
        "2. `/menu` yazarak veya sol alttaki **Menü** butonuna basarak kategori butonlarını açabilirsin.\n"
        "3. İster hissettiğin bir kelime yaz, ister kategorilerden seç; mısralar her zaman seninle!"
    )
    bot.reply_to(mesaj, metin, parse_mode="Markdown")

# Buton Tıklamaları
@bot.callback_query_handler(func=lambda call: True)
def buton_tiklama(call):
    kategori = call.data.replace("kat_", "")
    secilen_liste = siirler.get(kategori, siirler['genel'])
    veri = random.choice(secilen_liste)
    
    cevap = (
        f"{veri['giris']}\n\n"
        f"📖 *{veri['sair']}*\n"
        f"_\"{veri['siir']}\"_\n\n"
        f"💭 {veri['yorum']}"
    )
    bot.send_message(call.message.chat.id, cevap, parse_mode="Markdown", reply_markup=ana_menu())

# Duygu Analizi ve Mesaj Cevapları
@bot.message_handler(func=lambda mesaj: True)
def siir_analiz(mesaj):
    girdi = mesaj.text.lower()
    
    if any(k in girdi for k in ['mutlu', 'sevinç', 'keyif', 'harika', 'güzel', 'süper', 'iyiyim', 'gülüyorum', 'neşeli']):
        secilen_liste = siirler['mutlu']
    elif any(k in girdi for k in ['bilmiyorum', 'bilmiom', 'hissiz', 'duygusuz', 'boşluk', 'hiçbir şey', 'hissedemiyorum', 'anlamsız']):
        secilen_liste = siirler['hissizlik']
    elif any(k in girdi for k in ['üzgün', 'üzgünüm', 'kırgın', 'kötü', 'yalnız', 'gece', 'hüzün', 'karanlık', 'efkar', 'ağlıyorum']):
        secilen_liste = siirler['yalniz']
    elif any(k in girdi for k in ['kavuşam', 'imkansız', 'ayrıldık', 'ayrı', 'özledim', 'hasret', 'aşk', 'aşık', 'seviyorum']):
        secilen_liste = siirler['kavusamama']
    else:
        secilen_liste = siirler['genel']
        
    veri = random.choice(secilen_liste)
    
    cevap = (
        f"{veri['giris']}\n\n"
        f"📖 *{veri['sair']}*\n"
        f"_\"{veri['siir']}\"_\n\n"
        f"💭 {veri['yorum']}"
    )
    
    bot.reply_to(mesaj, cevap, parse_mode="Markdown", reply_markup=ana_menu())

print("Komut Menülü & Dev Şiir Botu Aktif!")
bot.infinity_polling()
