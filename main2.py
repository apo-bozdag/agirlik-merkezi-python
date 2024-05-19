import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_center_of_mass(masses, coordinates):
    # Tüm kütlelerin toplamını hesapla
    total_mass = sum(masses)

    # Toplam kütle sıfırsa, hata mesajı ver
    if total_mass == 0:
        raise ValueError("Toplam kütle sıfır olamaz.")

    # Ağırlık merkezinin başlangıç değerleri
    center_of_mass = [0, 0, 0]

    # Her kütle ve koordinat için
    for i in range(len(masses)):
        # Üç eksen için (x, y, z)
        for j in range(3):
            # Ağırlık merkezi hesaplamasında kullanılan toplama işlemi
            center_of_mass[j] += masses[i] * coordinates[i][j]

    # Toplam kütle ile bölerek ağırlık merkezini bulun
    center_of_mass = [x / total_mass for x in center_of_mass]

    # Ağırlık merkezini (x, y, z) tuple olarak döndür
    return tuple(center_of_mass)

# Kullanıcıdan römorkun boyutlarını al
short_side = float(input("Römorkun kısa kenar uzunluğunu girin (m): "))
long_side = float(input("Römorkun uzun kenar uzunluğunu girin (m): "))
height = float(input("Römorkun yüksekliğini girin (m): "))

# Kullanıcıdan yüklerin sayısını al
num_loads = int(input("Yük sayısını girin: "))

# Yüklerin kütlelerini ve koordinatlarını al
masses = []
coordinates = []
for i in range(num_loads):
    mass = float(input(f"Yük {i + 1} kütlesini girin (kg): "))
    x = float(input(f"Yük {i + 1} x koordinatını girin (m): "))
    y = float(input(f"Yük {i + 1} y koordinatını girin (m): "))
    z = float(input(f"Yük {i + 1} z koordinatını girin (m): "))
    masses.append(mass)
    coordinates.append((x, y, z))

center_of_mass = calculate_center_of_mass(masses, coordinates)
print(f"Ağırlık merkezi: {center_of_mass}")

# 3D grafik oluştur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Her kütlenin koordinatını grafiğe ekle
for mass, coord in zip(masses, coordinates):
    # Kütlenin konumunu çiz ve nokta büyüklüğünü kütleye göre ayarla
    ax.scatter(coord[0], coord[1], coord[2], s=mass * 10, alpha=0.6)
    # Kütle değerini noktaya etiket olarak ekle
    ax.text(coord[0], coord[1], coord[2], f'{mass} kg', size=10, zorder=1)

# Ağırlık merkezini grafiğe ekle
ax.scatter(center_of_mass[0], center_of_mass[1], center_of_mass[2], color='r', s=100)
# Ağırlık merkezi noktasına etiket ekle
ax.text(center_of_mass[0], center_of_mass[1], center_of_mass[2], 'Ağırlık Merkezi', color='r', size=12, zorder=1)

# Eksen etiketlerini ve başlıkları ayarla
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Ağırlık Merkezi ve Kütle Konumları')

# Grafiği göster
plt.show()
