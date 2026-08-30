// 運用ドキュメント・設定ファイルを公開URLから遮断する（Cloudflare Pages Functions）
// Functions は静的アセットより先に評価されるため、リポジトリ直下に置かれた
// 運用ドキュメントでも確実に404にできる（_headers の noindex は検索避けであって非公開ではない）。
// ※ ここに列挙したパス以外は一切触らない（context.next() でそのまま静的配信）。
const DENY = new Set([
  "/README.md",
  "/AFF_SLOTS.md",
  "/vercel.json",
]);

export async function onRequest(context) {
  const path = new URL(context.request.url).pathname;
  if (DENY.has(path)) {
    return new Response("Not Found", {
      status: 404,
      headers: { "content-type": "text/plain; charset=utf-8", "x-robots-tag": "noindex" },
    });
  }
  return context.next();
}
