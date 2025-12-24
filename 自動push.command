#!/bin/bash
set -e

echo "🌿 Spiral 語場同步開始..."
cd ~/Documents/pf_rec

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
