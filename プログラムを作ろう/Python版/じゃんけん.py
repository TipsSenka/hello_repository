# じゃんけんプログラム Python版
# まずは、必要なモジュールをインポートします
import random
# プレイヤーの手を入力する関数を定義します
def get_player_choice():
    while True:
        choice = input("じゃんけんの手を入力してください（グー、チョキ、パー）：")
        if choice in ["グー", "チョキ", "パー"]:
            return choice
        else:
            print("無効な入力です。もう一度入力してください。")

# コンピュータの手をランダムに選ぶ関数を定義します
def get_computer_choice():
    return random.choice(["グー", "チョキ", "パー"])

# 勝敗を判定する関数を定義します
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "引き分け"
    elif (player_choice == "グー" and computer_choice == "チョキ") or \
         (player_choice == "チョキ" and computer_choice == "パー") or \
         (player_choice == "パー" and computer_choice == "グー"):
        return "プレイヤーの勝ち"
    else:
        return "コンピュータの勝ち"

# メインのゲームループを定義します
def main():
    print("じゃんけんゲームへようこそ！")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"プレイヤーの手: {player_choice}")
        print(f"コンピュータの手: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(f"結果: {result}")
        
        play_again = input("もう一度プレイしますか？（はい/いいえ）：")
        if play_again.lower() != "はい":
            print("ゲームを終了します。ありがとうございました！")
            break
# プログラムのエントリーポイントを定義します
if __name__ == "__main__":
    main()
