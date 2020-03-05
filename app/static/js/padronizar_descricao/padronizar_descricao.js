$(document).ready(function () {
    let altura_maxima_descricao = 0;
    
    let lista_produtos = "";

    if ($("#lista-produtos").children().length > 1) {
        lista_produtos = $("#lista-produtos").children();
    }
    else {
        lista_produtos = $("#lista-produtos").children().children().children().children();
    }

    lista_produtos.each(function () {
        $(this).children().children("div").children("h5").each(function () {
            if ($(this).parent().height() > altura_maxima_descricao) {
                altura_maxima_descricao = $(this).parent().height();
            }
        });
    });

    lista_produtos.each(function () {
        $(this).children().children("div").children("h5").each(function () {
            $(this).parent().css("height", altura_maxima_descricao + "px");
        });
    });
});