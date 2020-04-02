$(document).ready(function () {
    let menu_quantidade_itens = null;

    // VERIFICA SE EXISTE O ID ESPECIFICADO PARA
    // RECUPERAR O ITEM CORRETO
    if ($("#lista-produtos").length > 0) {
        menu_quantidade_itens = $("#lista-produtos").
            children().
            children().
            children("div[name='menu-quantidade-itens']");
    }
    else {
        menu_quantidade_itens = $("#lista-produtos-carrinho").
            children().
            children("div").
            children("div").
            children().
            children("div[name='menu-quantidade-itens']");

        // CALCULA O PRECO ATUAL DOS PRODUTOS
        // COM BASE NA QUANTIDADE DE ITENS ESCOLHIDOS NO CARRINHO
        let preco_total = 0;

        menu_quantidade_itens.each(function () {
            let campo_preco_atual = $(this).parent().
                parent().
                parent().
                children("div").
                children("div").
                children("h3");

            let preco = campo_preco_atual.text().
                split("R$ ")[1].
                replace(",", ".");

            let quantidade_atual = $(this).
                children("input[type='text']");

            let resultado = (
                (parseFloat(preco) * parseInt(quantidade_atual.val()))
            ).toFixed(2);

            campo_preco_atual.text("R$ " +
                resultado.toString().replace(".", ",")
            );

            preco_total += parseFloat(resultado);
        });

        var h5_carrinho_compras = $("#carrinho_compras").children().
            eq(1).
            children().
            children().
            eq(1).
            children().
            children().
            eq(1).
            children("h5");

        h5_carrinho_compras.text(preco_total.toFixed(2).toString().replace(".", ","));
    }

    // DIMINUIR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function () {
        $(this).children("button").eq(0).click(function () {
            let quantidade_itens = $(this).
                parent().
                children("input[type='text']");

            if (quantidade_itens.val() > 1) {
                quantidade_itens.val(parseInt(quantidade_itens.val()) - 1);

                if ($("#lista-produtos-carrinho").length >= 1) {
                    let h3_preco_atual = $(this).parent().
                        parent().
                        parent().
                        parent().
                        children("div").
                        children("div").
                        children("h3");

                    let preco_atual = h3_preco_atual.
                        text().
                        split("R$ ")[1].
                        replace(",", ".");

                    let r_preco_total = (
                        parseFloat(
                            h5_carrinho_compras.text().replace(",", ".")
                        ) -
                        parseFloat(preco_atual)
                    );

                    let r_preco_atual = (
                        parseFloat(preco_atual) -
                        (
                            parseFloat(preco_atual) /
                            (parseInt(quantidade_itens.val()) + 1)
                        )
                    ).toFixed(2);

                    h3_preco_atual.text("R$ " +
                        r_preco_atual.toString().replace(".", ",")
                    );

                    let novo_resultado = (
                        parseFloat(r_preco_total) +
                        parseFloat(r_preco_atual)
                    ).toFixed(2);

                    h5_carrinho_compras.text(
                        novo_resultado.toString().
                            replace(".", ",")
                    );

                    gerar_novo_cookie({
                        componente: $(this),
                        quantidade: quantidade_itens
                    });
                }
            }
        });
    });

    // AUMENTAR QUANTIDADE DE PRODUTOS
    $(menu_quantidade_itens).each(function () {
        $(this).children("button").eq(1).click(function () {
            let quantidade_itens = $(this).
                parent().
                children("input[type='text']");

            quantidade_itens.val(parseInt(quantidade_itens.val()) + 1);

            if ($("#lista-produtos-carrinho").length >= 1) {
                let h3_preco_atual = $(this).parent().
                    parent().
                    parent().
                    parent().
                    children("div").
                    children("div").
                    children("h3");

                let preco_atual = h3_preco_atual.
                    text().
                    split("R$ ")[1].
                    replace(",", ".");

                let r_preco_total = (
                    parseFloat(
                        h5_carrinho_compras.text().replace(",", ".")
                    ) -
                    parseFloat(preco_atual)
                );

                let r_preco_atual = (
                    parseFloat(preco_atual) +
                    (
                        parseFloat(preco_atual) /
                        (parseInt(quantidade_itens.val()) - 1)
                    )
                ).toFixed(2);

                h3_preco_atual.text("R$ " +
                    r_preco_atual.toString().replace(".", ",")
                );

                let novo_resultado = (
                    parseFloat(r_preco_total) +
                    parseFloat(r_preco_atual)
                ).toFixed(2);

                h5_carrinho_compras.text(
                    novo_resultado.toString().
                        replace(".", ",")
                );

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
        let cookie = document.cookie.
            split("carrinho_compras=")[1].
            replace("\"", "").
            replace("\"", "").
            split("\\073");

        let id_produtos = [];
        let quantidade_produtos = [];

        cookie.forEach(element => {
            if (element != "") {
                let item = element.split("_");

                id_produtos.push(item[0]);
                quantidade_produtos.push(item[1]);
            }
        });

        if (id_produtos.indexOf($(opcoes.componente).
            parent().
            children("input[type='hidden']").val()) != null
        ) {
            let indice = id_produtos.indexOf($(opcoes.componente).
                parent().
                children("input[type='hidden']").
                val()
            );

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