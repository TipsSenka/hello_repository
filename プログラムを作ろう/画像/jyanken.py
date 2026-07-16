import random

#ユーザーにグー、チョキ、パーを選択させる
def get_user_choice():
    while True:
        user_input = input("グー、チョキ、パーのいずれかを入力してください: ")
        if user_input in ["グー", "チョキ", "パー"]:
            return user_input
        else:
            print("無効な入力です。もう一度試してください。")

#コンピュータの選択をランダムに決定する
def get_computer_choice():
    return random.choice(["グー", "チョキ", "パー"])

#ユーザーとコンピュータの選択を比較して勝敗を決定する
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == "グー" and computer_choice == "チョキ") or \
         (user_choice == "チョキ" and computer_choice == "パー") or \
         (user_choice == "パー" and computer_choice == "グー"):
        return "ユーザーの勝ち"
    else:
        return "コンピュータの勝ち"

#メインのゲームループ
def main():
    print("じゃんけんゲームへようこそ！")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"コンピュータの選択: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"結果: {result}")

        play_again = input("もう一度プレイしますか？ (はい/いいえ): ")
        if play_again.lower() != "はい":
            print("ゲームを終了します。")
            break

if __name__ == "__main__":
    main()