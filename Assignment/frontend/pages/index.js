import { useState } from "react";

export default function Home() {
  const [resume, setResume] = useState("");
  const [enhanced, setEnhanced] = useState("");

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);
    const res = await fetch("http://127.0.0.1:8000/upload_resume/", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setResume(data.parsed_text);
  };

  const handleEnhance = async () => {
    const res = await fetch("http://127.0.0.1:8000/enhance_resume/", {
      method: "POST",
      body: JSON.stringify({ skills: ["Python"], experience: [{ description: resume }] }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await res.json();
    setEnhanced(data.enhanced_resume);
  };

  return (
    <div>
      <h1>AI Resume Builder</h1>
      <input type="file" onChange={handleUpload} />
      <button onClick={handleEnhance}>Enhance Resume</button>
      <h2>Original Resume</h2>
      <pre>{resume}</pre>
      <h2>Enhanced Resume</h2>
      <pre>{enhanced}</pre>
    </div>
  );
}
