var btnRelNav = document.querySelectorAll(".btnRelNav");

btnRelNav.forEach((item) => {
    item.onclick = () => {
        var role = item.dataset.role;

        if (!item.classList.contains("active")) {
            document.querySelectorAll(".btnRelNav").forEach((innerItem)=>{
                innerItem.classList.remove("active");
                innerItem.style.borderBottomColor = "rgba(0,0,0,0.1)";
            });
            item.style.borderBottomColor = "#ffcc44";
            item.classList.add("active");
        }

        if(role == "sortByTurma"){
            document.getElementById("mediaPorCurso").style.display = "none";
            document.getElementById("cursoForm").style.display = "none";
            document.getElementById("turmaForm").style.display = "block";
            document.getElementById("mediaTurma").style.display = "block";
        }else{
            document.getElementById("mediaPorCurso").style.display = "block";
            document.getElementById("cursoForm").style.display = "block";
            document.getElementById("turmaForm").style.display = "none";
            document.getElementById("mediaTurma").style.display = "none";
        }
    }
})