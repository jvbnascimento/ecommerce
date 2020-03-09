$(document).ready(function() {
    let menu_quantidade_itens = $("#lista-produtos").children().children().children("div[name='menu-quantidade-itens']");

    // DIMINUIR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function() {
        $(this).children().eq(0).click(function() {
            let quantidade_itens = $(this).parent().children().eq(1);

            console.log("valor antigo: " + quantidade_itens.val());

            if (quantidade_itens.val() > 1) {
                quantidade_itens.val(parseInt(quantidade_itens.val()) - 1);
            }

            console.log("valor atual: " + quantidade_itens.val());
        });
    });

    // AUMENTAR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function() {
        $(this).children().eq(2).click(function() {
            let quantidade_itens = $(this).parent().children().eq(1);

            console.log("valor antigo: " + quantidade_itens.val());

            quantidade_itens.val(parseInt(quantidade_itens.val()) + 1);

            console.log("valor atual: " + quantidade_itens.val());
        });
    });
});