J542（2026-11-16）BJ 戦略エンジンの自己検査
1) python3 check_transcription.py   … woo_tables.py の転記が WoO 画像（woo_images/、2026-11-16 取得）の色と一致するか（1820セル）
2) python3 gen_expected.py          … 全85ルール×610セルの期待値 expected.json を作る
3) node verify_engine.js ../index.html expected.json [-v]   … ページの decide() と突合。食い違い0で終了コード0
出典: https://wizardofodds.com/games/blackjack/strategy/{1-deck,2-decks,4-decks,european}/ ・ /games/blackjack/surrender/
JSを触ったら 2→3 を回して mismatch=0 を確認してから push すること。
