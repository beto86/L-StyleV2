//global
var base_path = "/static/img/perguntas/";
var questionFirstImg = true;
var scrollCount = 0;
var anterior = 1;
var completas = 1;

document.getElementsByTagName("body")[0].onload = () => {
    var button = document.querySelectorAll('.btn-next');
    var questionaryForm = document.getElementById('questionaryForm');
    var allow = 0;

    button.forEach((item) => {
        item.onclick = () => {
            changeQuestion(item, "button");
        }
    });

    questionaryForm.onsubmit = function (e) {
        e.preventDefault();
        var opt = document.querySelectorAll('.questoes .opcoes');
        var noResponse = [];
        var resp = [];

        opt.forEach((item) => {
            if (item.dataset.respondido == "false") {
                noResponse.push(item.dataset.questao);
            }
        })

        document.querySelectorAll('#questao12 .opcoes').forEach((item) => {
            questao = item.dataset.questao;

            if (item.dataset.respondido == "true") {
                item.querySelectorAll('input').forEach((input) => {
                    if (input.checked) {
                        resp.push(input.value);
                    }
                })
                allow += 1;
            }
        });

        let hasDuplicate = resp.some((val, i) => resp.indexOf(val) !== i);

        // Se sim, avisa o usuário
        if (hasDuplicate) {
            document.getElementsByClassName('btn_enviar')[0].setAttribute("disabled", true);

            setTimeout(() => {
                document.getElementsByClassName('btn_enviar')[0].removeAttribute("disabled");
            }, 3800);
            msgError("error", "Você não pode atribuir a mesma nota para mais de uma opção");
        } else {

            if (allow == 4) {
                if (document.querySelector('#nav12 .done') == null) {
                    document.getElementById('nav12').innerHTML += '<span class="done"><i class="fas fa-check"></i></span>';
                    document.getElementById('footerInfo').innerHTML = completas + " de 12 completa";
                    completas++;
                }

                if (document.querySelector('#nav12 .question-times') != null) {
                    document.querySelector('#nav12 .question-times').remove();
                }
            }

            var semRepetidos = noResponse.filter(function (el, i) {
                return noResponse.indexOf(el) === i;
            });

            if (semRepetidos.length >= 1) {
                semRepetidos.forEach((item) => {
                    var className = '#nav' + item;

                    if (document.querySelector(className + ' .question-times') != null) {
                        document.querySelector(className + ' .question-times').remove();
                    }

                    document.querySelector(className).innerHTML += '<span class="question-times"><i class="fas fa-times"></span>';
                });

                msgError("error", "Existem campos sem resposta");

            } else {
                questionaryForm.submit();
            }
        }
    }

    changeNavDot("nav1");
    document.getElementById("questao1").classList.remove("d-none");

    /*pre-set*/
    document.getElementsByClassName('page-footer')[0].remove();
    document.getElementsByClassName('main-menu')[0].remove();
}

function changeQuestion(element, source = "") {
    var questionBox = document.getElementsByClassName('question-self')[0];
    var heroImg = document.getElementsByClassName('hero-img')[0];
    var ordem = element.getAttribute("ordem");
    var navTab = 'nav' + element.getAttribute('questao');
    var allow = 0;
    var numControl = element.getAttribute('questao');
    var cover = document.getElementsByClassName('protected')[0];
    var resp = [];
    var questao = 0;
    var target = element.offsetTop;

    document.getElementsByClassName('question-nav')[0].scrollTop = target;

    if (source == "") {
        numControl = document.getElementsByClassName('nav-active')[0].parentElement.getAttribute('questao');
    }

    document.querySelectorAll('#questao' + numControl + ' .opcoes').forEach((item) => {
        questao = item.dataset.questao;

        if (item.dataset.respondido == "true") {
            item.querySelectorAll('input').forEach((input) => {
                if (input.checked) {
                    resp.push(input.value);
                }
            })
            allow += 1;
        }
    });

    let hasDuplicate = resp.some((val, i) => resp.indexOf(val) !== i);

    // Se sim, avisa o usuário
    if (hasDuplicate) {
        if (source == "") {
            cover.style.display = 'block';

            setTimeout(() => {
                cover.style.display = 'none';
            }, 3800);
        } else {
            element.setAttribute("disabled", true);

            setTimeout(() => {
                element.removeAttribute("disabled");
            }, 3800);
        }
        msgError("error", "Você não pode atribuir a mesma nota para mais de uma opção");

    } else {
        /*Animação do card de pergunta(direito)*/
        questionBox.classList.remove("question-slide");
        heroImg.classList.remove("fade-toggle");
        questionBox.classList.add("question-slide");
        heroImg.classList.add("fade-toggle");
        cover.style.display = 'block';

        if (allow == 4) {
            if (source == "") {
                navTab = 'nav' + numControl;
            }

            if (document.querySelector('#' + navTab + ' .done') == null) {
                document.getElementById(navTab).innerHTML += '<span class="done"><i class="fas fa-check"></span>';
                document.getElementById('footerInfo').innerHTML = completas + " de 12 completa";
                completas++;
            }

            if (document.querySelector('#' + navTab + ' .question-times') != null) {
                document.querySelector('#' + navTab + ' .question-times').remove();
            }
        }

        heroImg.style.animationDuration = "2s";

        anterior = ordem;

        setTimeout(() => {

            if (ordem <= 12) {
                var atual = "questao" + ordem;
                var prox = (source != "button") ? atual : "questao" + (parseInt(ordem) + 1);

                if (source == "button") {
                    changeNavDot('nav' + (parseInt(ordem) + 1));
                } else {
                    changeNavDot('nav' + ordem);
                }

                document.querySelectorAll('.questoes').forEach((item) => {
                    item.classList.add("d-none");
                })

                if (source == "button") {
                    document.getElementById(prox).classList.remove("d-none");
                } else {
                    document.getElementById(atual).classList.remove("d-none");
                }
            }
        }, 1000);
        setTimeout(() => {
            questionBox.classList.remove("question-slide");
            heroImg.classList.remove("fade-toggle");
            cover.style.display = 'none';
        }, 2000);
    }
}

function msgError(state, msg) {
    var classChosen = (state == "error") ? "error" : "success";
    var element = document.getElementsByClassName('validation-msg')[0];

    element.style.display = 'flex';

    element.classList.remove('success');
    element.classList.remove('error');
    element.classList.remove('validation-in');
    element.classList.remove('validation-out');

    element.classList.add(classChosen);
    element.classList.add('validation-in');
    element.getElementsByClassName('msg')[0].innerHTML = msg;

    setTimeout(() => {
        element.classList.remove('validation-in');
        element.classList.add('validation-out');
    }, 3000);
    setTimeout(() => {
        element.style.display = 'none';
    }, 3800);
}

function changeNavDot(element) {
    var elementExist = document.getElementsByClassName('active-circle')[0];
    var element = document.getElementById(element);

    if (elementExist != null) {
        elementExist.remove();
    }

    document.querySelectorAll('.question-nav p').forEach((item) => {
        item.classList.remove('nav-active');
    });

    element.getElementsByTagName('p')[0].classList.add('nav-active');
    element.innerHTML += '<div class="active-circle"><div></div></div>';
}

function radioSetValue(element) {
    var parent = element.parentElement;
    var value = element.innerHTML;
    var active = parent.getElementsByClassName("custom-radio-active")[0];
    var photo = base_path + parent.dataset.photo + ".svg";
    var photoTag = document.getElementsByClassName("hero-img")[0];
    var idValue = element.id;
    idValue = idValue.substring(3, idValue.length);

    parent.querySelectorAll('input').forEach((input) => {
        input.checked = false;
    });

    document.getElementById('input' + idValue).checked = true;
    element.parentElement.parentElement.parentElement.dataset.respondido = "true";

    if (active != null) {
        active.classList.remove("custom-radio-active");
    }

    element.classList.add("custom-radio-active");

    parent.dataset.value = value;
    photoTag.style.animationDuration = "1s";
    photoTag.classList.add("fade-toggle");

    setTimeout(() => {
        photoTag.src = photo;
    }, 500);
    setTimeout(() => {
        photoTag.classList.remove("fade-toggle");
    }, 1000);
}

function expand(element) {
    var pageWidth = document.getElementsByTagName('body')[0].clientWidth;
    var questionList = document.getElementsByClassName('question-info')[0];
    var controle = element.dataset.state;

    if (pageWidth <= 1000) {
        if (controle == "hidden") {
            questionList.style.height = "400px";
            element.dataset.state = "visible";
            element.innerHTML = 'Esconder <i class="fas fa-eye-slash color-custom-primary"></i>';
        } else {
            questionList.style.height = "60px";
            element.dataset.state = "hidden";
            element.innerHTML = 'Expandir <i class="fas fa-expand-arrows-alt color-custom-primary"></i>';
        }
    }
}

