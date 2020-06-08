$(document).ready(function() {
    setInterval(() => {
        if ($("#inputTelefone").val().trim().length != 0) {
            if ($("#inputTelefone").val().trim().length == 14) {
                let ddd = $("#inputTelefone").val().split(" ")[0];
                let telefone = $("#inputTelefone").val().split(" ")[1];
                let novo_telefone = ddd + " 9" + telefone;
                
                $("#inputTelefone").val(novo_telefone);
            }
        }
    }, 500);
});