$(document).ready(function() {
    let menu_quantidade_itens = null;
    
    if ($("#lista-produtos").length > 0) {
        menu_quantidade_itens = $("#lista-produtos").children().children().children("div[name='menu-quantidade-itens']");
    }
    else {
        menu_quantidade_itens = $("#lista-produtos-carrinho").children().children("div").children("div").children().children("div[name='menu-quantidade-itens']");
    }

    // DIMINUIR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function() {
        $(this).children("button").eq(0).click(function() {
            let quantidade_itens = $(this).parent().children("input[type='text']");

            if (quantidade_itens.val() > 1) {
                quantidade_itens.val(parseInt(quantidade_itens.val()) - 1);
            }
        });
    });

    // AUMENTAR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function() {
        $(this).children("button").eq(1).click(function() {
            let quantidade_itens = $(this).parent().children("input[type='text']");

            quantidade_itens.val(parseInt(quantidade_itens.val()) + 1);
        });
    });
});