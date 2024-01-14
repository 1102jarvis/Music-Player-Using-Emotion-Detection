document.addEventListener("DOMContentLoaded", function () {
  const openCameraBtn = document.getElementById("open-camera");
  const shutterBtn = document.getElementById("shutter-btn");
  const cameraFeed = document.getElementById("camera-feed");

  let stream;
  let mediaRecorder;
  let chunks = [];

  openCameraBtn.addEventListener("click", async () => {
      try {
          stream = await navigator.mediaDevices.getUserMedia({ video: true });
          cameraFeed.srcObject = stream;
          cameraFeed.play();
          openCameraBtn.disabled = true;
          shutterBtn.disabled = false;
      } catch (err) {
          console.error("Error accessing camera:", err);
      }
  });

  shutterBtn.addEventListener("click", () => {
      if (stream) {
          mediaRecorder = new MediaRecorder(stream);

          mediaRecorder.ondataavailable = (event) => {
              if (event.data.size > 0) {
                  chunks.push(event.data);
              }
          };

          mediaRecorder.onstop = () => {
              const blob = new Blob(chunks, { type: "video/webm" });
              const url = URL.createObjectURL(blob);
              window.open(url);
              chunks = [];
          };

          mediaRecorder.start();
          setTimeout(() => {
              mediaRecorder.stop();
              stream.getTracks().forEach((track) => track.stop());
              openCameraBtn.disabled = false;
              shutterBtn.disabled = true;
          }, 3000); // Set recording duration (in milliseconds)
      }
  });
});