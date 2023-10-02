import cv2

def take_pic():
    cam = cv2.VideoCapture(1)
    
    cv2.namedWindow("check image")
    
    img_counter = 0
    
    
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("check_img", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "test.jpg"
            img_name = img_name.format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    
    cam.release()
    
    cv2.destroyAllWindows()
