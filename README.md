# image_processing [Hafta hafta tutulan notlar]

# Hafta2 
-- liste yapısına göz attık ardından numpy kütüphanesinde array oluşturduk np.array fonksiyonunu kullandık. Fonksiyona array gönderip ekrana bastırdık. Daha sonra matplotlib kütüphanesini kullanarak resimleri okuttuk, aslında resimlerde 3 boyutlu array yapısındadır. Daha sonra resmin RGB değerlerini belli oranda arttırıp ya da azaltıp resmi gösterdik. Daha sonra resmi 4/1 oranında kücülten fonksiyonu yazıp bir resmi ard arda 4/1 oranında kücültüp sonuçları gördük.

# Hafta3 
-- Resimdeki pixel lerin ne kadar tekrar ettiğini bulmak için histogram yapısı oluşturduk. Pixel lerin sıklıklarını hesapladık.Daha sonra x ve y değişkenleri tanımlayıp histogram keys ve değerlerini histogram grafiği üzerinde gösterdik.

# Hafta4 
-- Resimde yeterli yada yetersiz sayıda pixel olabilir. Bu durumda array lar üzerinde daha iyi çalışmak için Python daki MNIST data yı local olarak temin ettik. Daha sonra train_data üzerinde herhangi bir satırdaki pixeli, resme atadık. O resmin shape 2 boyutlu hale getirdik ve gösterdik. Daha sonra my_pdf adında varyans ve ortalama ile veri ilişkisini hesaplayan fonksiyonu tanımladık. Daha sonra train_data üzerinde ortalama ve varyansı bulan fonksiyonu yazdık. Dönen sonuç ile my_pdf fonksiyonunu çalıştırıp train_data içindeki pixellerin birbiriyle olan ilişki oranını gösterdik.

# Hafta5 
-- Hafta4 teki ortalama ve varyans fonksiyonunu tekrar yazdık. Daha sonra paintte cizdiğimiz 1-10 kadar herhangi bir sayı resmini okuttuk. Daha sonra bu resmin boyutunu 2 yapıp sütün pixel adetini 784 çıkardık. Daha sonra 1-10 a kadar bütün sütun pixel değerleri için (784) tane ortalama ve varyansı bulduk. my_pdf fonksiyonuna ekleyerek devam ettik. En son my_pdf dönen ilişki değerlerini topladığımız pdf değişkenini ekrana yazdık. En son ise bu ekrana yazdığımız 10 pdf değerini liste içine atayıp bu listedeki max değeri hesaplayan fonksiyon yazdık.

# Hafta6 
-- Bir resim yükleyip boyutlarını shape fonksiyonu ile bulduk. Daha sonra bu boyut değerlerine göre np.array oluşturduk. Np.array bütün elemanları 0 olan dizidir. Daha sonra mean filter uygulamak için fonksiyon yazdık. Fonksiyonda her bir pixel değerin çevresindeki pixel leri /9 bölüp ortalamasını aldık. Bu sayede resme mean filter uygulayarak (yumuşatma) daha yumuşak ve güzel görünüm elde ettik.

# Hafta7 
-- Matris tanımını yapıp matris nedir detaylı gösterdik. x ve y matrisleri oluşturup bu iki matris için sigma değerlerini bulduk. Daha sonra bu matrislerin covaryansını bulan fonksiyon yazdık.Daha sonra my_pdf benzer fonksiyon olan multivariate_normal fonksiyonu ile bu matrislerin ortalama ve konvaryansı arasındaki ilişkiyi gösterdik.Daha sonra 10 tane boy değeri için bu ilişkileri multivariate_normal fonksiyonuna hesaplattık.

# Hafta8 
-- İnternetten örnek kuş resmi upload ettik. Daha sonra bu RGB resmi 90 derece döndüren rotate fonksiyonunu yazdık. Bu fonksiyondaki mantık satır ve sütunların yer değiştirmesinden ibaret. Daha sonra döndürdüğümüz bu RGB resmi gray_level dönüştüren fonksiyonu yazdık. Gray_level dönüştürmek demek RGB değerlerin ortalamasını almak demektir. Bundan sonrada yüklediğimiz RGB resmininin bütün pixellerini 0-1 lere yani binary olarak dönüştüren fonksiyonu yazdık.

# Hafta10 
-- Vektörün tanımını yapıp ardından nasıl temsil edileceğini gösterdik. Aslında vektörler tek satırlık matrislerdir. Vektörler üzerinde aritmetik işlemler yapıldı. Daha sonra iki vektörü toplamak için iki farklı şekilde işlem yapan fonksiyon yazdık.Python random kütüphanesi kullanarak random sayı üretildi. Bu üretilen sayılarla yeni random vektör yaratan fonksiyon yazdık. Daha sonra iki vektörün orta noktasını bulan my_center adlı fonksiyon ve iki vektör arası uzaklığı bulan my_distance adlı fonksiyonları yazdık.


# Hafta11 --
-- Yapay sinir ağları için python da Perceptron olarak adlandırılan yapıyı tanımladık. Class perceptron yapısını initalize ettik. Daha sonra eğitilecek girdileri yazıp perceptronları oluşturduk. Burada işlemi AND ile ya da OR ile yapmak mümkündür. Perceptronları tek tek kontrol etmek için farklı threshold girdileri yazıp initalize fonksiyonunu test ettim. Sonuçları gözlemleyip farklı threshold girdileri yapının farklı olduğunu gözlemledim.

# Hafta12 --
-- sklearn.datasets  python kütüphanesini kullanarak kullanacağımız mnist_data yı çektik. x ve y değişkenlerine data ve targets hedeflerini atamasını yaptık. Bu atama çektiğimiz data içindeki her bir değeri kapsıyor. Daha sonra train_test verilerine bu kütüphanenin reshape fonksiyonlarını uyguladık. Daha sonra cmap değerini binary şekilde ayarladıktan sonra sigmoid gösterimi yaptık. Ardından öğrenme oranı (learning_rate) belirleyip bu yapay ağın yani sigmoidlerin output  verilerini hesapladık. Burdaki kullandığımız her bir yaklaşımı (epoch) gösterip ardından bu kütühanenin classificiton_report fonksiyonunu kullanıp ayrıntıları rapor olarak gösterdik.


# Hafta13--
-- Convansional Neural Network tanımlaması yapıp CNN yapısını pythonda initalize ettik. Yani CCN oluşturmak için class yapısının içine gerekli fonksiyonları yazdık (örnek : __init__). MNIST daha python kütüphanesini import ettik burda hazır data ve images ler bulunuyor. Daha sonra SOFTMAX yönteminin önce initalize sonra diğer fonksiyonlarını yazdık ve SOFTMAX class yapısını tamamladık. Son olarak POOLİNG class yapısını initalize ettik ve konvensional sinir ağ yapımızı test ettik. Step ve avarage kısımlarının nasıl oluştuğunu gördük.


#                                         DERS SONU..
