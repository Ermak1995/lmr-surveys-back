function render_surveys(surveys) {
    let count = cnt;
    for (let survey of surveys) {
      let obj = JSON.parse(JSON.stringify(survey.survey))
      obj = JSON.parse(JSON.stringify(obj))
      const newDiv = document.createElement("div");
      newDiv.classList.add("surv");

      const surv_info = document.createElement("div")
      surv_info.classList.add("surv-info")

      const newSpan1 = document.createElement("span");
      const newSpan2 = document.createElement("span");
      const newButton = document.createElement("a");
          
      newSpan1.classList.add("surv-info-item");
      newSpan2.classList.add("surv-info-item");
      newSpan2.classList.add("surv-info-topic");
      newButton.classList.add("button");
      newButton.classList.add("surv-button");

      newSpan1.innerText = obj.title;
      newSpan2.innerText = obj.topic;
      newButton.innerHTML = "Пройти";
      newButton.setAttribute("href", "pass.html?uuid=" + survey["uuid"]);
      newButton.setAttribute("type", "button");
      const surveysElement = document.querySelector(".surveys");
      surveysElement.appendChild(newDiv);

      surv_info.appendChild(newSpan1);
      surv_info.appendChild(newSpan2);
      newDiv.appendChild(surv_info);
      newDiv.appendChild(newButton);
    } 
}

fetch(
    'http://127.0.0.1:8000/surveys/'
)
.then(res => res.json())
.then(surveys => {
    const numSurveys = surveys.length;
    window.cnt = numSurveys;
    let text = "Количество опросов: " + cnt;
    document.getElementById("bc").textContent = text;

    render_surveys(surveys)
})
.catch(res => console.error(res));





// Get the button:
let mybutton = document.getElementById("button-up");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 