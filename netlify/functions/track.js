exports.handler = async (event, context) => {
  const params = event.queryStringParameters;
  const userId = params.user_id || "unknown_user";

  // Netlifyの環境変数からWebhook URLを読み込む
  const slackWebhookUrl = process.env.SLACK_WEBHOOK_URL; 

  // Webhook URLが設定されていない場合のエラーハンドリングを追加
  if (!slackWebhookUrl) {
    console.error("Slack Webhook URLが環境変数に設定されていません。");
    // ユーザーには通常のエラーページか、何も表示しないリダイレクトが適切かもしれません
    return {
      statusCode: 302, // または 500 Internal Server Error
      headers: {
        Location: "https://yashi-nomi.com/error.html", // エラーページにリダイレクトする例
      },
      // body: "設定エラーが発生しました。", // またはエラーメッセージを返す
    };
  }

  const timestamp = new Date().toLocaleString("ja-JP", { timeZone: "Asia/Tokyo" });

  const slackMessage = {
    text: `🔔 クリック通知: ユーザー「${userId}」がリンクを開きました。\n⏰ 日時: ${timestamp}`,
  };

  try {
    const response = await fetch(slackWebhookUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(slackMessage),
    });

    if (!response.ok) {
      const responseText = await response.text();
      console.error(`Slack通知エラー: ${response.status} ${response.statusText}`, responseText);
    }
  } catch (error) {
    console.error("Slack通知処理中にエラー:", error);
  }

  const redirectUrl = "https://yashi-nomi.com/"; 

  return {
    statusCode: 302, 
    headers: { Location: redirectUrl },
  };
};
