#Motion Detection from Web Cam

import cv2, pandas, time
first_frame = None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=['Start','End'])
video = cv2.VideoCapture(0)
while True:
	status=0
    check, frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
    cnts, hierarchy = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
		status=1
		status_list.append(status)
		status_list=status_list[-2:]
		if status_list[-1] == 1 and status_list[-2] == 0:
			times.append(datetime.now())
		if status_list[-2] == 0 and status_list[-2] == 0:
			times.append(datetime.now())
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
		
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('delta_frame', delta_frame)
    cv2.imshow('thresh_delta', thresh_delta)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
