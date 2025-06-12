from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "title": "Herbalife Shake ile Güne Zinde Başla",
        "image": "shake.jpg",
        "content": "Herbalife Shake ile dengeli ve besleyici bir kahvaltı yaparak gün boyunca enerjik kalabilirsin. Lezzetli ve düşük kalorili bu shake'ler, sağlıklı yaşamın anahtarıdır."
    },
    {
        "title": "Termo Complete ile Yağ Yakımını Destekle",
        "image": "thermo.jpg",
        "content": "Termo Complete, içerdiği kafein ve bitkisel özlerle metabolizmanı hızlandırarak yağ yakımını destekler. Diyetine ek olarak kullanabilirsin."
    },
    {
        "title": "Bitki Çayı ile Vücudunu Arındır",
        "image": "cay.jpg",
        "content": "Herbalife bitki çayı, sindirimi destekler ve toksinleri atmaya yardımcı olur. Sıcak ya da soğuk içerek günlük rutininin bir parçası haline getirebilirsin."
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
