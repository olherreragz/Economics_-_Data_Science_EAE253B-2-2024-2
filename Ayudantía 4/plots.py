import pandas as pd
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO


data = {
    "Date": [
        "1996-02-01", "1996-03-01", "1996-04-01", "1996-05-01", "1996-06-01",
        "1996-07-01", "1996-08-01", "1996-09-01", "1996-10-01", "1996-11-01",
        "1996-12-01", "1997-01-01", "1997-02-01", "1997-03-01", "1997-04-01",
        "1997-05-01", "1997-06-01", "1997-07-01", "1997-08-01", "1997-09-01",
        "1997-10-01", "1997-11-01", "1997-12-01", "1998-01-01", "1998-02-01",
        "1998-03-01", "1998-04-01", "1998-05-01", "1998-06-01", "1998-07-01",
        "1998-08-01", "1998-09-01", "1998-10-01", "1998-11-01", "1998-12-01",
        "1999-01-01"
    ],
    "Close": [
        30.25, 30.375, 30.625, 31.5, 27.125,
        27.875, 27.0, 25.125, 26.125, 30.0,
        28.75, 26.875, 28.25, 23.75, 22.375,
        25.25, 21.875, 22.8125, 22.75, 24.6875,
        20.5625, 16.5625, 18.625, 19.375, 19.3125,
        21.625, 22.4375, 19.25, 19.25, 16.375,
        13.0, 20.0, 21.375, 20.0, 19.5,
        19.0625
    ],
    "Cambio_porcentual_precio": [
        2.978723, 0.413223, 0.823045, 2.857143, -13.888889,
        2.764977, -3.139013, -6.944444, 3.980100, 14.832536,
        -4.166667, -6.521739, 5.116279, -15.929204, -5.789474,
        12.849162, -13.366337, 4.285714, -0.273973, 8.516484,
        -16.708861, -19.452888, 12.452830, 4.026846, -0.322581,
        11.974110, 3.757225, -14.206128, 0.000000, -14.935065,
        -20.610687, 53.846154, 6.875000, -6.432749, -2.500000,
        -2.243590
    ],
    "Cambio_porcentual_volumen": [
        13.186201, -21.330563, -4.790901, -22.275734, 23.368903,
        -21.279871, -21.909063, 4.444228, 8.637587, 79.097358,
        -40.430633, 13.14455, 20.994707, -29.948258, 8.466894,
        -16.213591, 23.544107, 26.610251, -38.992938, 39.056754,
        8.148720, -22.167234, 91.333449, 10.753125, -28.742750,
        -0.881602, 11.429905, -38.991282, 24.089131, -43.013848,
        49.215671, 107.184446, 2.308426, -45.749561, -0.967447,
        -17.265971
    ]
}


df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

correlation = df['Cambio_porcentual_precio'].corr(df['Cambio_porcentual_volumen'])

print(f"Correlación entre Cambio porcentual precio and Cambio porcentual volumen: {correlation:.4f}")

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], color='tab:blue', label='Close Price', linewidth=2)
plt.title('Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Cambio_porcentual_precio'], color='tab:orange', label='Cambio porcentual precio', linewidth=2)
plt.plot(df['Date'], df['Cambio_porcentual_volumen'], color='tab:red', label='Cambio porcentual volumen', linewidth=2)
plt.title('Cambio Porcentual Precio and Volumen Over Time')
plt.xlabel('Date')
plt.ylabel('Cambio porcentual (%)')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid()
plt.legend()

plt.ylim(-100, 100)
plt.show()

image_urls = [
    "https://www.bytetree.com/content/images/2024/02/2024-02-22-atlas-pulse-90-1.png",
    "https://followthemoney.com/wp-content/uploads/2014/11/usd-gold.png",
    "https://sdbullion.com/media/opti_image/webp/wysiwyg/Blog/Real_Interest_Rates_vs_Gold_vs_Interest_Rates_Chart_SD_Bullion_SDBullion.com.webp"
]

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

for ax, url in zip(axs, image_urls):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    ax.imshow(img)
    ax.axis('off') 

plt.tight_layout()
plt.show()

