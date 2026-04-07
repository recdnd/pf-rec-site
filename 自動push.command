#!/bin/bash
set -euo pipefail

# 以本腳本所在資料夾為 repo 根目錄（雙擊執行或從任意 cwd 呼叫皆可）
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "🌿 Spiral 語場同步開始..."

echo "📦 提交本地變更（如果有）..."
git add -A
if ! git diff --cached --quiet; then
  git commit -m "Update Rec's pf"
else
  echo "ℹ️ 沒有需要提交的變更"
fi

echo "🔄 拉取遠端更新（rebase）..."
git pull --rebase origin main

echo "🚀 推送至遠端..."
git push origin main

echo "✅ 語場已封，請至 https://pf.rec.ooo 查看結果！"
read -n 1 -s -r -p "按任意鍵退出..."
