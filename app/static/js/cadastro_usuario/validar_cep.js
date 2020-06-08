function validar_cep(cep) {
    $.ajax({
        type: "GET", 
        url: "https://viacep.com.br/ws/" + cep + "/json/",
        dataType: "json",
        contentType: "application/json; charset=UTF-8",

        success: function(resposta) {
            $("#inputLogradouro").val(resposta.logradouro);
            $("#inputComplemento").val(resposta.complemento);
            $("#inputBairro").val(resposta.bairro);
            $("#inputCidade").val(resposta.localidade);
            $("#inputEstado").val(resposta.uf);

            $("#inputLogradouro").prop("readonly", true);
            $("#inputBairro").prop("readonly", true);
            $("#inputCidade").prop("readonly", true);
            $("#inputEstado").prop("readonly", true);
        }
    })
}

$(document).ready(function() {
    let tempo_sem_digitar = 0;
    
    setInterval(() => {
        if ($("#inputCep").is(":focus")) {
            $("#inputCep").keydown(() => {
                tempo_sem_digitar = 0;
            });
            
            tempo_sem_digitar += 1;

            if (tempo_sem_digitar >= 1) {
                if ($("#inputCep").val().trim().length == 9) {
                    validar_cep($("#inputCep").val());
                }
            }
        }
    }, 500);
});