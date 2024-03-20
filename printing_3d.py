import cv2

base_img_path = 'images/no_Defect.jpg'
defect_img_path = 'images/small_Defect.jpg'

base_img = cv2.imread(base_img_path, cv2.IMREAD_GRAYSCALE)
defect_img = cv2.imread(defect_img_path, cv2.IMREAD_GRAYSCALE)

if base_img is None or defect_img is None:
    print("Error: Could not load images.")
    exit()

defect_img = cv2.resize(defect_img, (base_img.shape[1], base_img.shape[0]))
diff = cv2.absdiff(base_img, defect_img)
threshold = 60
mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
highlighted_img = cv2.cvtColor(defect_img, cv2.COLOR_GRAY2BGR)
highlighted_img[mask == 255] = [0, 255, 255]

cv2.imshow('Defect Highlighted Image', highlighted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
