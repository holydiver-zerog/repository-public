<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>お問い合わせフォーム</title>
  </head>
  <body>
    <form action="testenq" method="post" お名前: <input type="text" name="name">
      <br />
      お問い合わせの種類:
      <select name="qtype">
        <option value="company">会社について</option>
        <option value="product">製品について</option>
        <option value="support">アフターサポートについて</option></select
      ><br />
      お問い合わせ内容:
      <textarea name="body"></textarea><br />
      <input type="submit" />
    </form>
  </body>
</html>
