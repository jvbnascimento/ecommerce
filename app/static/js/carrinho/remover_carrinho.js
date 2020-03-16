function remover_carrinho(produto) {
    $.ajax({
        type: "POST",
        data: JSON.stringify(produto),  
        url: "http://localhost:8080/remover_carrinho/produto/",
        dataType: "json",
        contentType: "application/json; charset=UTF-8",

        success: function(resposta) {
            $("#icone-carrinho-compras").children("span").text(resposta);

            window.location.href = window.location.href;
        }
    })
}

$(document).ready(function() {
    botao_remover_carrinho = $('#lista-produtos-carrinho').children().children().children("div").children("div").children("div[name='menu-quantidade-itens']").children("a");
    
    botao_remover_carrinho.each(function() {
        $(this).click(function(event) {
            event.preventDefault();

            let id_produto = $(this).parent().children("input").val();

            let dados = { produto_id: parseInt(id_produto)};

            remover_carrinho(dados);
        });
    });
});