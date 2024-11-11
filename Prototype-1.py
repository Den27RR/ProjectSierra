import cv2

# Menghubungkan ke webcam
cap = cv2.VideoCapture(0)

# Memeriksa apakah webcam terbuka
if not cap.isOpened():
    print("Tidak dapat menghubungkan ke webcam")
    exit()

# Menampilkan video dari webcam
while True:
    ret, frame = cap.read()  # Membaca frame dari webcam
    if not ret:
        print("Tidak dapat membaca frame")
        break

    cv2.imshow('Webcam', frame)  # Menampilkan frame

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan webcam dan menutup jendela
cap.release()
cv2.destroyAllWindows()