import HeroSection from "@/components/sections/HeroSection";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <div className="min-h-screen bg-black">
      <main className="min-h-screen">
        <HeroSection />
      </main>
      <Footer />
    </div>
  );
}
