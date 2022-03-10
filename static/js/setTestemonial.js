function trocarTestemonial(numero){
    var div_testemonial = document.getElementById("testemonial"+numero);
    var testemonial_descricao = document.getElementById("testemonialD"+numero);

    for (var i = 1; i < 5; i++){
        var remove_testemonial = document.getElementById("testemonial"+i).classList.remove('testemonials-item-active');
        var remove_testemonialD = document.getElementById("testemonialD"+i).classList.add('hidden');
    }
    div_testemonial.classList.add('testemonials-item-active');
    testemonial_descricao.classList.remove('hidden');

}

function dataAutomatica() {
    let data = new Date();

    var ano = data.getFullYear();

    let documento_data = document.getElementsByClassName('inner_date');

    for(let i in documento_data){
        documento_data[i].innerHTML = ano;
    }
}