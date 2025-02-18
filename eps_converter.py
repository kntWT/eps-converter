import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def select_and_convert_images():
    # Tkinterのルートウィンドウを作成（非表示）
    root = tk.Tk()
    root.withdraw()

    # ファイル選択ダイアログを表示（複数選択可能）
    file_paths = filedialog.askopenfilenames(
        title="画像ファイルを選択してください",
        filetypes=[("画像ファイル", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
    )
    
    if not file_paths:
        # print("ファイルが選択されませんでした。")
        return

    # 最初に選択されたファイルのディレクトリをデフォルト保存先に設定
    default_dir = os.path.dirname(file_paths[0])

    # 保存先フォルダを選択
    save_folder = filedialog.askdirectory(
        title="EPSファイルの保存先フォルダを選択してください",
        initialdir=default_dir
    )

    if not save_folder:
        # print("保存先フォルダが選択されませんでした。")
        return

    for file_path in file_paths:
        try:
            # 画像を開く
            with Image.open(file_path) as img:
                # RGBに変換（必要な場合）
                if img.mode in ("RGBA", "P"):  
                    img = img.convert("RGB")
                
                # 元のファイル名を取得し、拡張子を変更
                base_name = os.path.basename(file_path)
                file_name_without_ext = os.path.splitext(base_name)[0]
                save_path = os.path.join(save_folder, f"{file_name_without_ext}.eps")
                
                # EPS形式で保存
                img.save(save_path, format="EPS")
                print(f"保存しました: {save_path}")
        except Exception as e:
            print(f"エラーが発生しました（{file_path}）: {e}")

if __name__ == "__main__":
    select_and_convert_images()