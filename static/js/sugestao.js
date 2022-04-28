var btnHide = document.getElementsByClassName("btnHide")[0];
var btnShow = document.getElementsByClassName("btnShow")[0];
var bottomMenu = document.getElementsByClassName("bottomMenu")[0];
var isFirstTime = true;

//navigation
var navigation = [
    {
        "titulo": "Instruções iniciais",
        "icon": "fas fa-play",
        "id": "initial",
        "state": true,
        "body": Inicio
    },
    {
        "titulo": "Divergente",
        "icon": "fas fa-brain",
        "id": "divergente",
        "state": false,
        "body": Divergente
    },
    {
        "titulo": "Convergente",
        "icon": "fas fa-shapes",
        "id": "convergente",
        "state": false,
        "body": Convergente
    },
    {
        "titulo": "Assimilador",
        "icon": "fas fa-atom",
        "id": "assimilador",
        "state": false,
        "body": Assimilador
    },
    {
        "titulo": "Acomodador",
        "icon": "fas fa-flask",
        "id": "acomodador",
        "state": false,
        "body": Acomodador
    }
]

window.onload = () => {
    btnHide.onclick = () => {
        bottomMenu.style.transform = 'translateX(100%)';
        setTimeout(() => {
            btnShow.style.display = "block";
        }, 800);
    }

    btnShow.onclick = () => {
        bottomMenu.style.transform = 'translateX(0%)';
        btnShow.style.display = "none";
    }

    startContent();
    document.getElementById("initial").click();

    setTimeout(() => {
        document.getElementById("loadingElement").remove();
    }, 500)
}

function startContent() {
    let menu = document.getElementById("menuList");
    let realContent = document.getElementById("realContent");

    html = "";
    contentHtml = "";

    navigation.forEach((nav) => {
        active = (nav.state) ? "active" : "";
        html += `
                <li id=${nav.id} class="${active}" onclick=setMenu(${nav.id})>
                    <i class="${nav.icon}"></i>
                    <p>${nav.titulo}</p>
                </li>
            `;

        contentHtml += `
                <div id=${nav.id + "Content"} class="maincomponent" style="display: none;">
                    ${gerarConteudo(nav.body.text)}
                </div>`;
    })

    menu.innerHTML = html;
    realContent.innerHTML = contentHtml;
}

function gerarConteudo(contents) {
    let html = "";

    contents.forEach((item) => {
        html += `
            <div class="component">
                <div class="title bg-color-custom-primary">
                    <h1>${item.titulo}</h1>
                    <button><i class="fas fa-minus"></i></button>
                </div>
                <div class="information textComponent">
                    ${item.corpo}
                </div>
            </div>
                `;
    })

    return html;
}

function setMenu(obj) {
    var selected = navigation.filter((item) => {
        return item.state == true
    })

    if ((selected[0].id != obj.id) || isFirstTime == true) {
        isFirstTime = false;
        attStatus(obj.id);
    }
}

function attStatus(id) {
    let selectedId = id + "Content";

    navigation.forEach((item) => {
        item.state = false;
        document.getElementById(item.id).classList.remove('active');

        if (item.id == id) {
            item.state = true;
            document.getElementById(item.id).classList.add('active');
        }
    })

    document.querySelectorAll(".maincomponent").forEach((item) => {
        item.style.display = "none";
    })

    document.getElementById(selectedId).style.display = "block";
}

function resphandle(respIsHidden) {
    let menu = document.getElementsByClassName("asideMenu")[0];
    let respMenu = document.getElementsByClassName("btnResp")[0];


    menu.style.transition = "transform 0.8s";

    if (respIsHidden) {
        respMenu.style.display = "none";
        menu.style.transform = "translateX(0)";
        menu.style.overflowY = "auto";
    }else{
        menu.style.transform = "translateX(-100%)";

        setTimeout(()=>{
            respMenu.style.display = "flex";
            menu.style.overflowY = "initial";   
        }, 800);
    }
}