#じゃんけんプログラムpython版
#まずは、必要なモジュールをインポートします
import random

#手順を示します
#1. ユーザーが手を選ぶ（グー、チョキ、パー）
#2. コンピュータがランダムで手を選ぶ
#3. 勝敗を判定する
#4. 結果を表示する
#5. 必要に応じてリセットや再戦の機能を追加する
#6. デザインやスタイルを整える
#7. 追加機能（スコアの記録、アニメーションなど）を検討する
#8. コードの整理や最適化を行う
#9. テストを行い、バグを修正する

#ユーザーの手を取得する関数
def get_user_hand():
    user_hand = input("グー、チョキ、パーのいずれかを入力してください: ")
    return user_hand

#コンピュータの手をランダムに選ぶ関数
def get_computer_hand():
    hands = ['グー', 'チョキ', 'パー']
    computer_hand = random.choice(hands)
    return computer_hand

#勝敗を判定する関数
def determine_winner(user_hand, computer_hand):
    if user_hand == computer_hand:
        return '引き分け'
    elif (user_hand == 'グー' and computer_hand == 'チョキ') or \
         (user_hand == 'チョキ' and computer_hand == 'パー') or \
         (user_hand == 'パー' and computer_hand == 'グー'): 
        return 'ユーザーの勝ち'
    else:
        return 'コンピュータの勝ち'

#結果を表示する関数
def show_result(user_hand, computer_hand):
    result = determine_winner(user_hand, computer_hand)
    print(f"あなたの手: {user_hand}\nコンピュータの手: {computer_hand}\n結果: {result}")
        
#ゲームを終了するかどうかを確認する関数
def ask_to_continue():
    answer = input("もう一度プレイしますか？ (y/n): ")
    return answer.lower() == 'y'

#メインのゲームループ
def main():
    while True:
        user_hand = get_user_hand()
        computer_hand = get_computer_hand()
        show_result(user_hand, computer_hand)
        
        if not ask_to_continue():
            print("ゲームを終了します。")
            break
