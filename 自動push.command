#!/bin/bash

echo "🚀 pf.rec.ooo 同步開始..."
cd /Users/matleyentacle/Documents/pf_rec || exit

echo "🔄 更新 Git 狀態..."
git add .

# 檢查是否有更改
if git diff --staged --quiet; then
    echo "ℹ️  沒有更改需要提交"
else
    git commit -m "Update pf.rec.ooo resume site"
    echo "📤 推送到 GitHub..."
    git push origin main
    echo "✅ 已推送，請至 https://pf.rec.ooo 查看結果！"
fi

read -n 1 -s -r -p "按任意鍵退出..."
