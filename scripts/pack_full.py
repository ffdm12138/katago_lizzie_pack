"""打包全部文件为发行版 zip（含权重，解压即用）"""
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
    ZIP_NAME,
    "katago_lizzie_pack_git.zip",
    ".gitignore",
}

def main():
    total_files = 0
    total_bytes = 0

    kwargs = dict(
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    )

    with zipfile.ZipFile(ZIP_PATH, "w", **kwargs) as zf:
        for root, dirs, files in os.walk(ROOT):
            rel = Path(root).relative_to(ROOT)
            if rel.parts and rel.parts[0] in EXCLUDE_DIRS:
                dirs.clear()
                continue

            for f in sorted(files):
                if f in EXCLUDE_FILES:
                    continue
                fpath = Path(root) / f
                arcname = str(rel / f) if str(rel) != "." else f
                zf.write(fpath, arcname)
                total_files += 1
                total_bytes += fpath.stat().st_size

    raw_mb = total_bytes / 1024 / 1024
    zip_mb = os.path.getsize(ZIP_PATH) / 1024 / 1024
    ratio = (1 - zip_mb / raw_mb) * 100 if raw_mb else 0
    print(f"Done: {ZIP_NAME}")
    print(f"  Files:     {total_files}")
    print(f"  Raw size:  {raw_mb:.1f} MB")
    print(f"  Zipped:    {zip_mb:.1f} MB  ({ratio:.0f}% compression)")

if __name__ == "__main__":
    main()
