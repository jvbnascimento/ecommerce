function adicionar_carrinho(produto) {
    $.ajax({
        type: "POST",
        data: JSON.stringify(produto),  
        url: "http://localhost:8080/adicionar_carrinho/produto/",
        dataType: "json",
        contentType: "application/json; charset=UTF-8"
    });
}

$(document).ready(function() {
    botao_adicionar_carrinho = $('#lista-produtos').children().children().children("div").children("form").children("button[name='botao-adicionar-carrinho']");
    
    botao_adicionar_carrinho.each(function() {
        $(this).click(function(event) {
            event.preventDefault();

            let id_produto = $(this).parent().children("input").val();
            let quantidade = $(this).parent().parent().parent().children("div[name='menu-quantidade-itens']").children("input").val();

            let dados = { produto_id: parseInt(id_produto), quantidade_itens: parseInt(quantidade) };

            adicionar_carrinho(dados);

            $(this).parent().parent().parent().children("div[name='menu-quantidade-itens']").children("input").val(1);
        });
    });
});