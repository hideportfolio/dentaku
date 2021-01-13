import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for v in lines:
        stack = []
        line = v.split()
        try:
            for element in line:
                if element.isdecimal():
                    stack.append(int(element))
                else:
                    if element == "++":
                        stack.append(stack.pop() + 1)
                    elif element == "+":
                        stack.append(stack.pop() + stack.pop())
                    elif element == "-":
                        stack.append((stack.pop() * -1 + stack.pop()))
                    elif element == "*":
                        stack.append(stack.pop() * stack.pop())
                    elif element == "@":
                        x, y, z = [stack.pop() for e in range(3)]
                        stack.append(x * y + y * z + z * x)
                    else:
                        raise ValueError()
            if len(stack) == 1:
                print(stack[0])
            else:
                raise ValueError()
        except:
            print("invalid")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
