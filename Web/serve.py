import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

class H(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        path = path.split("?")[0]
        if path.endswith(".js.gz") or path.endswith(".js"):
            return "application/javascript"
        if path.endswith(".wasm.gz") or path.endswith(".wasm"):
            return "application/wasm"
        if path.endswith(".data.gz") or path.endswith(".data"):
            return "application/octet-stream"
        return super().guess_type(path)

    def end_headers(self):
        p = self.path.split("?")[0]
        if p.endswith(".gz"):
            self.send_header("Content-Encoding", "gzip")
        if p.endswith(".br"):
            self.send_header("Content-Encoding", "br")
        # 禁用浏览器缓存：每次请求都重新校验，避免测试时加载到旧的 index.html / 旧构建文件
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

if __name__ == "__main__":
    print("目录:", ROOT)
    print("index.html:", os.path.exists(os.path.join(ROOT, "index.html")))
    print("打开这个: http://127.0.0.1:8765/")
    ThreadingHTTPServer(("127.0.0.1", 8765), H).serve_forever()