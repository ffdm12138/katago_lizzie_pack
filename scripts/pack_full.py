"""打包项目全部文件为发行版 zip（补上权重就能解压即用）"""
import zipfile, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIP_NAME = "katago_lizzie_pack_full.zip"
ZIP_PATH = ROOT / ZIP_NAME

EXCLUDE_DIRS = {
    ".git",
    "KataGoData",     # 引擎缓存，启动后自动生成
    "gtp_logs",       # 日志
    "save",           # 用户存档
}

EXCLUDE_FILES = {
    ZIP_NAME,             # 避免递归打包
    "katago_lizzie_pack_git.zip",
    ".gitignore",
}

def main():
    total_files = 0
    total_bytes = 0

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(ROOT):
            # 跳过排除目录
            rel = Path(root).relative_to(ROOT)
            if rel.parts and rel.parts[0] in EXCLUDE_DIRS:
                dirs.clear()
                continue

            for f in files:
                if f in EXCLUDE_FILES:
                    continue
                fpath = Path(root) / f
                arcname = str(rel / f) if str(rel) != "." else f
                zf.write(fpath, arcname)
                total_files += 1
                total_bytes += fpath.stat().st_size

    size_mb = total_bytes / 1024 / 1024
    zip_mb = os.path.getsize(ZIP_PATH) / 1024 / 1024
    print(f"Done: {ZIP_NAME}")
    print(f"  Files:  {total_files}")
    print(f"  Raw:    {size_mb:.1f} MB")
    print(f"  Zipped: {zip_mb:.1f} MB")

if __name__ == "__main__":
    main()
