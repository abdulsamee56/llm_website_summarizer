# Website Summarizer

**Website Summarizer** is a lightweight Python-Django application that allows users to enter a URL of a website and generates a concise summary of the website's content. The app uses OpenAI's GPT API for summarization and BeautifulSoup for extracting content from the given URL.

---

## Current Features

### Summarize Website Content
- Users can paste the URL of a website, and the app fetches the content of the webpage (excluding images, scripts, etc.).
- The extracted text is summarized using OpenAI's GPT API to generate a concise and meaningful summary.

### Supports Static HTML Websites
- Works well with websites that serve static content.

### Simple and Intuitive Interface
- Users can enter a URL and instantly receive a summary.

---

## Future Enhancements

### Job Posting Summarizer and ATS Keyword Extractor
- Extend the app to summarize job descriptions from popular job posting websites.
- Extract key skills and keywords (e.g., Python, SQL, Agile) required for ATS (Applicant Tracking Systems).
- Allow users to paste job links for automatic analysis.

### Handle JavaScript-Heavy Websites
- Incorporate headless browsers like Selenium or Playwright to process dynamic content.

### Support File Uploads
- Enable users to upload HTML or text files containing job descriptions or web content for summarization.

### Store Summaries and Keywords
- Add functionality to save summaries and keywords in a database for future reference.

### Improve UI and UX
- Enhance the app's interface with a responsive design using frameworks like Bootstrap or TailwindCSS.
