import Navbar from "@/components/Navbar";
import ChatInterface from "@/components/ChatInterface";

export default function Home() {
  return (
    <div className="min-h-screen bg-black">
      <Navbar />
      <main className="min-h-screen">
        <ChatInterface />
      </main>
    </div>
  );
}
