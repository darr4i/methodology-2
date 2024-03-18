# methodology-2

This console application is a Markdown to HTML converter written in Python. Below is an English description of how the program works:

## 1. File Reading:
   - The script begins by attempting to open and read the contents of a specified Markdown file (`input_file`) in UTF-8 encoding.

## 2. Text Conversion:
   - The Markdown content is then processed to convert various Markdown syntax elements to HTML tags. The following conversions are applied:
     - **Bold Text:** `**text**` becomes `<b>text</b>`.
     - **Italic Text:** `_text_` becomes `<i>text</i>`.
     - **Monospaced Text:** `` `text` `` becomes `<tt>text</tt>`.
     - **Preformatted Text:** ``` ```text``` ``` becomes `<pre>text</pre>`.

## 3. Paragraph Formatting:
   - The script uses regular expressions to convert line breaks into HTML paragraph tags (`<p>`). It ensures that consecutive lines separated by a single newline are considered separate paragraphs.

## 4. HTML Output:
   - The converted HTML content is wrapped in a `<p>` tag and stored in the variable `html_text`.

## 5. File Writing (Optional):
   - If an output file (`output_file`) is specified, the HTML content is written to that file. If no output file is provided, the HTML content is printed to the console.

## 6. Error Handling:
   - The script includes error handling to address potential issues, such as file not found errors (`FileNotFoundError`) or general exceptions. Error messages are displayed, and the script exits with a status code of 1 in case of an error.

## 7. Running tests
   - To run the test, you need to copy the repository to your machine in the folder C:\\lab1 and write the command python -m unittest test_markdown_to_html.py in the terminal.
