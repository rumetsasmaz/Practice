import os

class BaseModule:

    def __init__(self , target):
        self.target = target

    def run(self):

        raise NotImplementedError()

class LogAnalyzerModule(BaseModule):

    def __init__(self , filename):

        super().__init__(filename)

    def read_lines(self):

        lines = []

        with open(self.target, "r") as file:

            for line in file:
                lines.append(line.strip())
        return lines

    def count_failed(self , lines):
        counts = {}

        for line in lines:
            if line.startswith("FAILED"):
                parts = line.split()
                ip = parts[-1]
                counts[ip] = counts.get(ip , 0) + 1
        return counts

    def run(self):
        print(f"[*] Starting Log Analysis: {self.target}")

        try:

            lines = self.read_lines()
            counts = self.count_failed(lines)

            for ip , count in counts.items():
                if count >= 3:
                    print(f"[!] SUSPICIOUS: {ip} -> {count} failed attempts")

                else:
                    print(f"[+] {ip} -> {count} failed attempts")
        except FileNotFoundError:
            print(f"[-] File not found: {self.target}")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    LogAnalyzerModule(os.path.join(base_dir , "test_logs.txt")).run()
    print("-" * 40)
    LogAnalyzerModule(os.path.join(base_dir , "yok.txt")).run()
