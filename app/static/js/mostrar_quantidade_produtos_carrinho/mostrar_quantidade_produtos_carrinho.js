$(document).ready(function() {
    // SELECIONAR A DIV CORRESPONDENTE AO MENU DE CONTROLE DE QUANTIDADE DE ITENS SELECIONADOS
    let input_quantidade_produto = $("#lista-produtos-carrinho").children().children().children("div").children().children("div[name='menu-quantidade-itens']");

    // TRANSFORMAR O COOKIE EM UMA LISTA 
    let cookie = document.cookie
    cookie = cookie.replace("\"", "")
    cookie = cookie.replace("\"", "")

    cookie = cookie.split("=")[1].split("\\073");

    // PERCORRER LISTA 
    input_quantidade_produto.each(function() {
        cookie.forEach(element => {
            if (element != "") {
                item = element.split("_")
                if (parseInt($(this).children("input[type='hidden']").val()) == parseInt(item[0])) {
                    $(this).children("input[type='text']").val(item[1]);

                    $(this).children("button").eq(0).css("border-top-left-radius", "5px");
                    $(this).children("button").eq(0).css("border-bottom-left-radius", "5px");

                    $(this).children("button").eq(1).css("border-top-right-radius", "5px");
                    $(this).children("button").eq(1).css("border-bottom-right-radius", "5px");
                }
            }
        });
    });
});