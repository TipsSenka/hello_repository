// じゃんけんゲームのJavaScriptコード
// プレイヤーの手を選択する関数
// clickのイベントリスナーを追加して、プレイヤーが手を選択したときにこの関数が呼び出されるようにするjqueryを使って、ボタンがクリックされたときにプレイヤーの手を取得し、コンピュータの手をランダムに生成して、勝敗を判定するコードを追加する

// 手辞書
var hands = {
    "gu": "グー",
    "pa": "パー",
    "ch": "チョキ"
};

$(".li_player_hand").click(function () {
    // プレイヤーの手を取得
    var playerHand = $(this).data("hand");
    console.log("プレイヤーの手: " + playerHand);
    // クリックしたliのクラスにactiveを追加
    $(".li_player_hand").removeClass("active");
    $(this).addClass("active");
    // プレイヤーの手を表示
    // 
    $("#player_choice").text("お前の手: " + hands[playerHand]);
});
// 決定ボタンがクリックされたときの処理
$("#btn_decide").click(function () {
    // プレイヤーの手を取得 
    var playerHand = $(".li_player_hand.active").data("hand");
    if (!playerHand) {
        alert("ボタンすら押せんのかクズ！");
        return;
    }
    // コンピュータの手をランダムに生成
    var aiHand = Object.keys(hands)[Math.floor(Math.random() * Object.keys(hands).length)];
    $("#ai_choice").text("AIの手: " + hands[aiHand]);
    $("#img_ai").attr("src", "../画像/" + aiHand + ".png");

    // 勝敗を判定
    var result = $("#result");
    // あいこ
    if (playerHand === aiHand) {
        result.text("あいこ");
    }else if (
        (playerHand === "gu" && aiHand === "ch") ||
        (playerHand === "pa" && aiHand === "gu") ||
        (playerHand === "ch" && aiHand === "pa")
    ) {
        result.text("お前のバカ");
    } else {
        result.text("お前のアホ");
    }
});