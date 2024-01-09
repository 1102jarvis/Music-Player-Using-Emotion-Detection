import cv2
import numpy as np
import time
import spotify
from keras.models import load_model

now = time.time()
#future = now+random.randint(20,50)
future = now+25
model=load_model('model_file.h5')

video=cv2.VideoCapture(0)
''' happy_songs = ['Mast kalandar-Mika Singh']
sad_songs = ['kabhi jo badal barse']
fear_songs = ['hanuman chalisa']
disgust_songs  = ['besabriyan']
surprise_songs = ['bulleya']
neutral_songs = ['uff teri adaa']
angry_songs = ['yalgaar'] '''

happy_songs_uri = 'spotify:playlist:0TB1scqYXu8vaFwxiOaT1j'
sad_songs_uri = 'spotify:playlist:6eq5Zviu57AxTT02x0F3pE'
neutral_songs_uri = 'spotify:playlist:1QbJym8B3Xb6rpXdk7MBiJ'

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

labels_dict={0:'Happy',1:'Neutral',2:'Sad'}

while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= faceDetect.detectMultiScale(gray, 1.3, 3)
    for x,y,w,h in faces:
        sub_face_img=gray[y:y+h, x:x+w]
        resized=cv2.resize(sub_face_img,(48,48))
        normalize=resized/255.0
        reshaped=np.reshape(normalize, (1, 48, 48, 1))
        result=model.predict(reshaped)
        label=np.argmax(result, axis=1)[0]
        text = labels_dict[label]
        print(labels_dict[label])
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
        cv2.putText(frame, labels_dict[label]+text, (x, y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(30)& 0xff
    if time.time() > future:
        try:
            cv2.destroyAllWindows()
            
            if text == 'Happy':
                #spotify.play_song(random.choice(happy_songs))
                spotify.play_from_playlist(happy_songs_uri)

            if text == 'Sad':
                #spotify.play_song(random.choice(sad_songs))
                spotify.play_from_playlist(sad_songs_uri)
                    
            if text == 'Neutral':
                spotify.play_from_playlist(neutral_songs_uri)
                
            break
            
        except Exception as e:
            print(e)
            print('Please stay focus in Camera frame atleast 15 seconds & run again this program:)')
            break
    k=cv2.waitKey(1)
    if k==ord('q'):
      break

video.release()
cv2.destroyAllWindows()