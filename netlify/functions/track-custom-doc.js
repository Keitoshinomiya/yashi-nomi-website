exports.handler = async (event, context) => {
  const params = event.queryStringParameters;

  // 必須パラメータ: 実際の資料URL
  const targetUrl = params.target_url;
  // オプションパラメータ: 誰がクリックしたか
  const userId = params.user_id || "unknown_user"; 

  // target_url が指定されていない場合はエラーまたはデフォルトページへ
  if (!targetUrl) {
    console.error("target_url が指定されていません。");
    return {
      statusCode: 400, // Bad Request
      body: "Error: target_url parameter is missing.",
    };
    // または、特定のフォールバックページにリダイレクト
    // return {
    //   statusCode: 302,
    //   headers: { Location: "https://yashi-nomi.com/link-error.html" },
    // };
  }

  // Slack Webhook URLを環境変数から取得
  const slackWebhookUrl = process.env.SLACK_WEBHOOK_URL; 

  if (!slackWebhookUrl) {
    console.error("Slack Webhook URLが環境変数に設定されていません。");
    // Slack通知が設定されていなくても、リダイレクトは実行する
  }

  const timestamp = new Date().toLocaleString("ja-JP", { timeZone: "Asia/Tokyo" });

  // Slackに送信するメッセージ内容
  const slackMessage = {
    text: `📄 資料閲覧通知:\nユーザー: *${userId}*\n資料URL: ${targetUrl}\n日時: ${timestamp}`,
  };

  // Slack通知 (エラーが発生してもリダイレクトは試みる)
  if (slackWebhookUrl) {
    try {
      await fetch(slackWebhookUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(slackMessage),
      });
    } catch (error) {
      console.error("Slack通知処理中にエラー:", error);
    }
  }

  // 実際の資料URLにリダイレクト
  return {
    statusCode: 302,
    headers: {
      Location: targetUrl, // 受け取ったtarget_urlにリダイレクト
    },
  };
};
