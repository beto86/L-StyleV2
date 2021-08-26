//global
var base_path = "/static/img/perguntas/";
var questionFirstImg = true;

document.getElementsByTagName("body")[0].onload = () => {
    var button = document.getElementsByClassName('btn-next')[0];
    var questionBox = document.getElementsByClassName('question-self')[0];
    var heroImg = document.getElementsByClassName('hero-img')[0];

    button.onclick = () => {
        questionBox.classList.add("question-slide");
        heroImg.classList.add("fade-toggle");
        heroImg.style.animationDuration = "2s";
        setTimeout(()=>{
            questionBox.classList.remove("question-slide");
            heroImg.classList.remove("fade-toggle");
        }, 2000);
    }
}

function radioSetValue(element) {
    var parent = element.parentElement;
    var value = element.innerHTML;
    var active = parent.getElementsByClassName("custom-radio-active")[0];
    var photo = base_path+parent.dataset.photo+".svg";
    var photoTag = document.getElementsByClassName("hero-img")[0];

    if (active != null) {
        active.classList.remove("custom-radio-active");
    }

    element.classList.add("custom-radio-active");

    parent.dataset.value = value;
    photoTag.style.animationDuration = "1s";
    photoTag.classList.add("fade-toggle");
    
    setTimeout(()=>{
        photoTag.src = photo;
    }, 500);
    setTimeout(()=>{
        photoTag.classList.remove("fade-toggle");
    }, 1000);
}