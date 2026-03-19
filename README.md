# MCP Student Sandbox

Bu depo, temel Python kod kalitesi, hata ayıklama ve güvenlik pratikleri için hazırlanmış küçük modüllerden oluşur.

## Proje Özeti

Depodaki modüller eğitim amaçlıdır ve bazı dosyalar kasıtlı olarak sorunlu örnekler içerebilir.

- `mystery_module.py`: İkinci dereceden denklem çözücüsü (bu README'nin ana konusu)
- `spaghetti_logic.py`: Refactor edilmiş, modüler veri işleme örneği
- `secret_leak.py`: Güvenlik riski gösteren örnek (hardcoded secret)
- `failing_calculator.py`: Şu an boş durumda
- `test_failing_calculator.py`: Hesaplayıcı için birim test örnekleri

---

## mystery_module.py Ne İşe Yarar?

`mystery_module.py`, şu formdaki ikinci dereceden denklemi çözer:

\[
a x^2 + b x + c = 0
\]

Dosyada bulunan `fn_x(a, b, c)` fonksiyonu, diskriminant değerini hesaplayarak reel kökleri döndürür.

### Mevcut Kod Davranışı

1. Diskriminant hesaplanır:  \(d = b^2 - 4ac\)
2. Eğer \(d < 0\) ise reel kök yoktur ve `None` döner.
3. Eğer \(d >= 0\) ise iki reel kök tuple olarak döner:

\[
x_1 = \frac{-b + \sqrt{d}}{2a}, \quad x_2 = \frac{-b - \sqrt{d}}{2a}
\]

---

## Fonksiyon Sözleşmesi (API)

### `fn_x(a, b, c)`

**Girdi:**
- `a` (`int` | `float`): \(x^2\) katsayısı
- `b` (`int` | `float`): \(x\) katsayısı
- `c` (`int` | `float`): sabit terim

**Çıktı:**
- `tuple[float, float]`: Reel kökler
- `None`: Reel kök yoksa (yani `d < 0`)

---

## Kullanım Örnekleri

```python
from mystery_module import fn_x

# x^2 - 5x + 6 = 0  -> kökler: 2 ve 3
print(fn_x(1, -5, 6))
# Çıktı: (3.0, 2.0)

# x^2 + 1 = 0 -> reel kök yok
print(fn_x(1, 0, 1))
# Çıktı: None
```

---

## Sınır Durumlar ve Riskler

### 1) `a = 0` durumu

Fonksiyon ikinci dereceden denklem varsaydığı için `a = 0` olduğunda formül geçersiz hale gelir ve `ZeroDivisionError` oluşur.

### 2) Karmaşık kök desteği yok

`d < 0` olduğunda `None` döner. Karmaşık kökleri (`complex`) hesaplamaz.

### 3) İsimlendirme okunabilirliği

`fn_x`, `a`, `b`, `c`, `d` isimleri kısa olduğu için niyet netliği düşer. Eğitim amaçlı olabilir, ancak üretim kodu için daha açıklayıcı isimler önerilir.

---

## Önerilen İyileştirmeler

1. Fonksiyon adını `solve_quadratic` olarak güncelle.
2. `a == 0` için açık bir `ValueError` fırlat.
3. İsteğe bağlı olarak karmaşık kök desteği ekle (`cmath.sqrt`).
4. Tip ipuçları ve docstring ekle.
5. Birim testlerle sözleşmeyi garanti altına al.

Örnek hedef imza:

```python
def solve_quadratic(coeff_a: float, coeff_b: float, coeff_c: float) -> tuple[float, float] | None:
    ...
```

---

## Hızlı Doğrulama

Aşağıdaki gibi basit bir test dosyasıyla davranış doğrulanabilir:

```python
import unittest
from mystery_module import fn_x


class TestMysteryModule(unittest.TestCase):
    def test_two_real_roots(self):
        self.assertEqual(fn_x(1, -5, 6), (3.0, 2.0))

    def test_no_real_root(self):
        self.assertIsNone(fn_x(1, 0, 1))


if __name__ == "__main__":
    unittest.main()
```

---

## Not

Bu depo bir öğrenme/sandbox ortamı olduğu için bazı dosyalar üretim kalitesinden uzak veya kasıtlı olarak riskli bırakılmış olabilir. Bu README, özellikle `mystery_module.py` dosyasının görevini açık hale getirmek amacıyla hazırlanmıştır.
