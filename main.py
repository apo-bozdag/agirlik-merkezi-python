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


# Kütlelerin listesi (örneğin kilogram cinsinden)
masses = [50, 30, 20]  # Kütleler
# Her kütlenin (x, y, z) koordinatları (örneğin metre cinsinden)
coordinates = [(2, 3, 4), (5, 6, 7), (8, 9, 10)]  # Koordinatlar

center_of_mass = calculate_center_of_mass(masses, coordinates)
print(f"The center of mass is at: {center_of_mass}")

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
ax.text(center_of_mass[0], center_of_mass[1], center_of_mass[2], 'Center of Mass', color='r', size=12, zorder=1)

# Eksen etiketlerini ve başlıkları ayarla
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Ağırlık Merkezi ve Kütle Konumları')

# Grafiği göster
plt.show()