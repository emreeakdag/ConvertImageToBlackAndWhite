# Modülü ekleyelim
from PIL import Image

# Resimi açalım
image = Image.open("test_image.jpg")

# Görüntüyü gri tonlamalı hale getirelim.
image = image.convert("L")

# Gri tonlamalı resmi kayıt edelim.
image.save("grayscale_image.jpg")