var btnResp = document.getElementById("btnResp");
var respMenu = document.getElementsByClassName("menu-itens")[0];
var controller = false;

btnResp.onclick = () => {

    if(controller == false){
        respMenu.style.transition = "transform 0.8s";
        respMenu.style.transform = "translateY(0)";
        btnResp.setAttribute("disabled", true);
        controller = true;
    }else{
        controller = false;
        respMenu.style.transition = "transform 0.8s";
        respMenu.style.transform = "translateY(-105%)";
        btnResp.setAttribute("disabled", true);
    }

    setTimeout(()=>{
        btnResp.removeAttribute("disabled");
    }, 800);
}