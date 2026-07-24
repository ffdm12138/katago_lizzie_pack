"""打包 git 跟踪的文件为轻量 zip（配置/文档/主题/音效）"""
import subprocess, zipfile, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIP_NAME = "katago_lizzie_pack_git.zip"
ZIP_PATH = ROOT / ZIP_NAME

def main():
    files = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.strip().splitlines()

    if not files:
        print("No tracked files found.")
        return

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            fpath = ROOT / f
            if fpath.is_file():
                zf.write(fpath, f)

    size = os.path.getsize(ZIP_PATH)
    print(f"Done: {ZIP_NAME} ({len(files)} files, {size / 1024:.1f} KB)")

if __name__ == "__main__":
    main()
