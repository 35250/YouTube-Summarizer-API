# 📺 YouTube Video Summarizer API using FastAPI

This project is a YouTube Video Summarizer built using **FastAPI**, a Python web framework. It takes a YouTube video URL and returns a **topic label** and a **summary** of the content.

---

## 🚀 Project Goal

To develop a Python-based API using **FastAPI** that fetches a transcript of a YouTube video and summarizes its content into a concise topic and description.

---

## 🧠 Skills & Technologies Used

- **Python** – Core language used throughout the project
- **FastAPI** – Python framework to create the API
- **OpenRouter API** – Integrated for content analysis (access tied to personal Google account)
- **API integration**, **JSON formatting**, **error handling**, **YouTube transcript extraction**

---

## 🔧 How It Works

1. User submits a YouTube video URL.
2. If the video has a transcript (subtitles), it extracts it.
3. The content is passed through OpenRouter API.
4. The API returns a **topic label** and **summarized content**.

---

## ⚠️ Limitations & Precautions

This API has a few usage limitations due to the current implementation and platform constraints:

- ❌ **Will not work for users other than the developer** because:
  - The OpenRouter API is **authenticated via a personal Google account** on `hosting.com`.
  - Other users will not have access to this session/token.

- ⚠️ Works **only for videos that have accessible transcripts**. It may fail for:
  - Videos where **captions are disabled** by the owner
  - **YouTube Shorts**
  - **Music videos** or videos with no spoken content
  - **Very short videos** (no transcript available)

---

## ✅ Working Example

**Video URL:** `https://youtube.com/shorts/DEuIqiWCG6M?si=Atd83GPhlWTGSZlF`
📸 `Sample_Output_Success.jpg`

---

## ❌ Sample Error Output

📸 `Sample_Output_Error.jpg` – shows graceful error when a video without captions is used  
This proves the limitation is due to video content, not the code.

---



✅ Positive Output (Successful Summary)

{
  "topic_name": "Tax Implications of Flipping a Home",
  "topic_summary": "The video discusses the varying tax implications of flipping a house and distinguishes between it as a short-term investment and a continuous business, as well as the difference in tax rates applied for each."
}



❌ Negative Output (Graceful Error Handling)

{
  "Error": "Transcript not found. This may happen if the video has no captions or is restricted."
}



🙏 Final Note
This project was developed during a remote internship. It helped me:

Learn FastAPI

Work with real-world API limitations

Build a functional backend microservice

I’ve shared this project for recruiters and collaborators to view my learning, structure, and problem-solving process.



## 🧑‍💻 Author
**Ayan Dey**  
B.Tech CSE (AI/ML), 2nd Year  LinkedIn: (www.linkedin.com/in/ayandey212105242)
GitHub: (https://github.com/35250) 


---

Feel free to fork this project, give a ⭐ star, or connect with me for collaboration or job/internship opportunities!



