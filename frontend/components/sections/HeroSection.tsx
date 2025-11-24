"use client";

import { SendHorizontal } from "lucide-react";
import { useState } from "react";

export default function HeroSection() {
  const [input, setInput] = useState("");

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      // Handle send message here
      console.log("Send:", input);
      setInput("");
    }
  };

  return (
    <section className="flex flex-col items-center justify-center min-h-screen px-4">
      <h1
        className="text-[12rem] font-bold tracking-tighter cursor-default"
        style={{
          WebkitTextFillColor: 'transparent',
          WebkitTextStroke: '1px rgba(255, 255, 255, 0.7)',
        }}
      >
        Roulette
      </h1>

      <div className="w-full max-w-3xl relative z-10">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Say Anything"
          rows={1}
          className="w-full bg-transparent border border-white/20 rounded-3xl px-6 py-3.5 pr-14 text-white placeholder-gray-500 focus:outline-none focus:border-white/20 transition-colors resize-none overflow-hidden"
          style={{
            minHeight: '56px',
            maxHeight: '200px',
          }}
          onInput={(e) => {
            const target = e.target as HTMLTextAreaElement;
            target.style.height = '56px';
            target.style.height = target.scrollHeight + 'px';
          }}
        />
        <button className="absolute right-2 top-1.5 p-3 bg-white/10 hover:bg-white/20 rounded-full transition-colors">
          <SendHorizontal className="w-5 h-5 text-white" />
        </button>
      </div>
    </section>
  );
}
