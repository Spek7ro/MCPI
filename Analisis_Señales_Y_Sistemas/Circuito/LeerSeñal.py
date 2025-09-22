import serial
import numpy as np
import matplotlib.pyplot as plt

# Configurar puerto serial
arduino = serial.Serial('COM3', 9600)
samples = 1024  # número de muestras a capturar
data = []

print("Capturando datos...")

while len(data) < samples:
    try:
        value = int(arduino.readline().decode().strip())
        data.append(value)
    except:
        pass

arduino.close()
print("Datos capturados.")

# Convertir a numpy array
signal = np.array(data)

# Graficar señal en el dominio del tiempo
plt.figure(figsize=(10,4))
plt.plot(signal, label="Señal capturada")
plt.title("Señal de LED captada por LDR")
plt.xlabel("Muestra")
plt.ylabel("Intensidad (ADC 0-1023)")
plt.legend()
plt.show()

# --- Análisis en frecuencia (FFT) ---
fft_signal = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), d=0.001)  # asumiendo muestreo ~1kHz

plt.figure(figsize=(10,4))
plt.plot(freqs[:len(freqs)//2], np.abs(fft_signal)[:len(freqs)//2])
plt.title("Espectro de frecuencia (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.show()
