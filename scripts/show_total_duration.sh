#!/usr/bin/env bash

if [ -z $1 ]; then
    echo "specify dir name"
    return 1
fi

dir_name=$1
total_seconds=0
file_count=0

# ./files ディレクトリ内の wav ファイルを検索
for file in "${dir_name}"/*.wav; do
    # ファイルが存在しない場合はスキップ
    [ -e "$file" ] || continue

    # ffprobe を使用して再生時間を取得(秒単位)
    duration=$(ffprobe -v error -show_entries format=duration \
               -of default=noprint_wrappers=1:nokey=1 "$file" 2>/dev/null)

    # 取得に成功した場合のみ加算
    if [ -n "$duration" ]; then
        total_seconds=$(echo "$total_seconds + $duration" | bc)
        file_count=$((file_count + 1))
        echo "$(basename "$file"): ${duration}秒"
    fi
done

# 結果を表示
if [ $file_count -eq 0 ]; then
    echo "WAVファイルが見つかりませんでした。"
    exit 1
fi

echo "---"
echo "ファイル数: $file_count"
echo "合計時間: ${total_seconds}秒"

# 時:分:秒形式に変換
hours=$(echo "$total_seconds / 3600" | bc)
minutes=$(echo "($total_seconds % 3600) / 60" | bc)
seconds=$(echo "$total_seconds % 60" | bc)

printf "合計時間: %d時間%d分%.2f秒\n" $hours $minutes $seconds