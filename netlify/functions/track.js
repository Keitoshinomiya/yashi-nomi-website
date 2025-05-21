exports.handler = async (event, context) => {
  const params = event.queryStringParameters;
  const userId = params.user_id || "unknown";

  const slackWebhookUrl = "https://hooks.slack.com/services/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";

  const timestamp = new Date().toLocaleString("ja-JP", { timeZone: "Asia/Tokyo" });

  const payload = {
    text: `✅ ユーザー *${userId}* がリンクを開きました（${timestamp}）`,
  };

  try {
    await fetch(slackWebhookUrl, {
      method: "POST",
      body: JSON.stringify(payload),
      headers: { "Content-Type": "application/json" },
    });
  } catch (error) {
    console.error("Slack通知失敗:", error);
  }

  return {
    statusCode: 302,
    headers: {
      Location: "https://yashi-nomi.com/thanks.html", // リダイレクト先を必要に応じて変更
    },
  };
};
