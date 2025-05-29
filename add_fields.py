import os, json

inp  = "dataset/music/data.jsonl"
outp = "dataset/music/data_prepped.jsonl"

with open(inp, "r", encoding="utf-8") as fin, open(outp, "w", encoding="utf-8") as fout:
    for line in fin:
        item = json.loads(line)
        # key 已经存在，如果没有再添加
        if "key" not in item:
            fn = os.path.basename(item["path"])
            item["key"] = os.path.splitext(fn)[0]
        # 新增 start 和 end
        item["start"] = 0.0
        item["end"]   = item["duration"]
        fout.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Wrote {outp}")
