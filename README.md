# srt_translator
translate english to cn

# 格式问题
1. 加载字幕不显示：尝试将字幕文件的编码格式改为 UTF-8 with BOM（带有字节顺序标记的 UTF-8 编码），这是一种常见的在不同平台上都能良好显示的编码格式。`with codecs.open(output_filepath, "w", encoding="utf-8-sig") as f:`在这个修改后的代码中，我使用了 `codecs.open` 来打开文件，指定了编码格式为 "utf-8-sig"，这会在文件开头添加字节顺序标记（BOM），以确保兼容性。
2. 字母格式：
![Pasted image 20240122212055](https://github.com/nicecanoe/srt_translator/assets/31350782/2ece2782-720d-4b7d-923c-b739ea8f3100)
	下面是修改后的代码，将文件写入时的编码格式修改为 UTF-8 with BOM：
	`f"{i}\n{original.start} --> {original.end}\n{original.text}\n{translated}\n\n"`
