$(document).ready(function () {
    let menu_quantidade_itens = null;

    if ($("#lista-produtos").length > 0) {
        menu_quantidade_itens = $("#lista-produtos").children().children().children("div[name='menu-quantidade-itens']");
    }
    else {
        menu_quantidade_itens = $("#lista-produtos-carrinho").children().children("div").children("div").children().children("div[name='menu-quantidade-itens']");
    }

    // DIMINUIR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function () {
        $(this).children("button").eq(0).click(function () {
            let quantidade_itens = $(this).parent().children("input[type='text']");

            if (quantidade_itens.val() > 1) {
                quantidade_itens.val(parseInt(quantidade_itens.val()) - 1);
            }

            if ($("#lista-produtos-carrinho").length >= 1) {
                gerar_novo_cookie({
                    componente: $(this),
                    quantidade: quantidade_itens
                });
            }
        });
    });

    // AUMENTAR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function () {
        $(this).children("button").eq(1).click(function () {
            let quantidade_itens = $(this).parent().children("input[type='text']");

            quantidade_itens.val(parseInt(quantidade_itens.val()) + 1);


            if ($("#lista-produtos-carrinho").length >= 1) {
                gerar_novo_cookie({
                    componente: $(this),
                    quantidade: quantidade_itens
                });
            }
        });
    });
});

function gerar_novo_cookie(opcoes) {
    if (document.cookie.length != 0) {
        let cookie = document.cookie.split("carrinho_compras=")[1].replace("\"", "").replace("\"", "").split("\\073");

        let id_produtos = [];
        let quantidade_produtos = [];

        cookie.forEach(element => {
            if (element != "") {
                let item = element.split("_");

                id_produtos.push(item[0]);
                quantidade_produtos.push(item[1]);
            }
        });

        if (id_produtos.indexOf($(opcoes.componente).parent().children("input[type='hidden']").val()) != null) {
            let indice = id_produtos.indexOf($(opcoes.componente).parent().children("input[type='hidden']").val());

            quantidade_produtos[indice] = opcoes.quantidade.val();

            let novoCookie = '"';
            id_produtos.forEach(element => {
                let i = id_produtos.indexOf(element);

                novoCookie += id_produtos[i] + "_" + quantidade_produtos[i] + "\\073";
            });
            novoCookie += '"';

            let data = new Date();
            data.setTime(data.getTime() + (15 * 24 * 60 * 60 * 1000));
            let expires = "expires=" + data.toUTCString();

            document.cookie = "carrinho_compras=" + novoCookie + ";" + expires;
        }
    }
}