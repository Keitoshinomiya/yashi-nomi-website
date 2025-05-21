exports.handler = async (event, context) => {
  // URLのクエリパラメータから user_id を取得
  const params = event.queryStringParameters;
  const userId = params.user_id || "unknown_user"; // user_idがなければ "unknown_user" とする

  // あなたのSlack Webhook URL
  const slackWebhookUrl = "https://hooks.slack.com/services/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"; 

  // 日本時間に整形したタイムスタンプ
  const timestamp = new Date().toLocaleString("ja-JP", { timeZone: "Asia/Tokyo" });

  // Slackに送信するメッセージ内容
  const slackMessage = {
    text: `🔔 クリック通知: ユーザー「${userId}」がリンクを開きました。\n⏰ 日時: ${timestamp}`,
  };

  try {
    // Slackに通知を送信
    const response = await fetch(slackWebhookUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(slackMessage),
    });

    if (!response.ok) {
      console.error(`Slack通知エラー: ${response.status} ${response.statusText}`);
    }
  } catch (error) {
    console.error("Slack通知処理中にエラー:", error);
  }

  // リダイレクト先のURLをトップページに変更
  const redirectUrl = "https://yashi-nomi.com/"; 

  return {
    statusCode: 302, 
    headers: {
      Location: redirectUrl,
    },
  };
};
