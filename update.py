import argparse as ap
import subprocess as su
import time
import os
import env


def execute(command: str) -> str:
    get = command.split()
    return su.check_output(get).decode("utf-8")


parser = ap.ArgumentParser()
parser.add_argument(
    "-r", "--reset", help='로드할 git 버전을 선택합니다. 예시 입력: HEAD~1', required=False)
parser.add_argument(
    "-l", "--login", help="자동 로그인 설정을 켜거나 끕니다. 켰을 때에는 실행 후에 적용됩니다. 예시 입력: false 혹은 true", required=False)
parser.add_argument("-n", "--noPull", help="pull 없이 서버를 재시작합니다.",
                    required=False, action="store_true")
parser.add_argument("-k", "--kill", help="서버를 재시작없이 종료합니다.",
                    required=False, action="store_true")
args = parser.parse_args()
if args.login:
    if args.login == "true":
        os.system("git config credential.helper store")
    elif args.login == "false":
        os.system("git config --unset credential.helper")
worktree = "sudo git " + \
    (f" reset {args.reset} --hard" if args.reset else "pull")

params = execute(f"ps -e").split("\n")[1:]
token = True
for i in params:
    param = [j for j in i.split() if j]
    if len(param) == 4:
        if param[3] == env.PROC_NAME and os.getpid() != int(param[0]):
            result = f"kill {param[0]}"
            print(result)
            os.system(result)
            if token:
                token = False
            time.sleep(0.5)

if not args.noPull:
    os.system(worktree)
    time.sleep(0.5)
if not args.kill:
    file_dir = os.path.abspath(__file__)
    path = os.path.dirname(file_dir)
    os.system(
        f"nohup python3 -u {path}/app.py &")