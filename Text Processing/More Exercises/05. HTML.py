title = input()
content = input()

print("<h1>")
print(f"    {title}")
print("</h1>")


print("<article>")
print(f"    {content}")
print("</article>")



while True:
    comments = input()

    if comments == "end of comments":
        break

    print("<div>")
    print(f"    {comments}")
    print("</div>")
