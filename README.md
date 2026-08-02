# BJ Trainer — ブラックジャック・トレーナー（勝負ラボ）

ブラックジャックの基本戦略とカードカウンティングを学べる練習ツール。単一HTML・外部依存ゼロ・仮想チップのみ（実際の金銭を賭ける賭博の勧誘・助長はしません）。

## 公開
- 新（本番）: https://bj.shoubu-lab.com  … Cloudflare Pages（このリポジトリを接続）
- 旧: https://fujiken1016.github.io/bj-trainer/ … GitHub Pages（移行案内あり）

## 構成
- `index.html` … アプリ本体（ルール / ストラテジー / 実践 / カウンティング）＋法務ページ導線フッター
- `privacy.html` `disclaimer.html` `operator.html` `contact.html` … 法務・情報ページ（広告審査要件）
- `legal.css` … 上記ページ共通スタイル
- `robots.txt` `sitemap.xml` … SEO
- `_headers` … Cloudflare Pages セキュリティヘッダ
- `404.html` … 404ページ

## デプロイ
Cloudflare Pages にこのリポジトリを接続（ビルドコマンドなし・出力ディレクトリ=ルート）。`main` への push で自動デプロイ。

## 移行案内の有効化
`index.html` 末尾のスクリプト内 `MIGRATION_ACTIVE` を `true` にすると、旧URL（github.io）でのみ新URLへの案内バナー＋自動遷移が有効になる（新ドメイン側では無効）。ドメイン稼働確認後に切り替えること。

## 注意
仮想チップで戦略を学ぶ学習ツール。オンラインカジノ等へのリンク・アフィリエイト広告は掲載しない（ギャンブル隔離ドメイン shoubu-lab.com のポリシー）。
