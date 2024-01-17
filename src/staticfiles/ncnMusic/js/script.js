const wrapper = document.querySelector(".wrapper");
const fileName = document.querySelector(".file-name");
const uploadBtn = document.querySelector("#upload-btn");
const idImageBtn = document.getElementById('id_image');
const customBtn = document.querySelector("#custom-btn");
const cancelBtn = document.querySelector("#cancel-btn i");
const img = document.querySelector("img");
let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
customBtn.addEventListener("click",function(){
  idImageBtn.click();
});

idImageBtn.addEventListener("change", function(){
  const file = this.files[0];
  if(file){
    const reader = new FileReader();
    reader.onload = function(){
      const result = reader.result;
      img.src = result;
      wrapper.classList.add("active");
      uploadBtn.disabled = false;
      uploadBtn.style.cursor = 'pointer';
    }
    cancelBtn.addEventListener("click", function(){
      img.src="";
      wrapper.classList.remove("active");
      uploadBtn.disabled = true;
      uploadBtn.style.cursor = 'not-allowed';
    })
    reader.readAsDataURL(file);
  }
  if(this.value){
    let valueStore = this.value.match(regExp);
    fileName.textContent = valueStore;
  }
});
