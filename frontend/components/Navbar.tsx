import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="fixed top-6 left-1/2 -translate-x-1/2 z-50 w-[95%] max-w-[1400px]">
      <div className="flex items-center justify-between px-8 py-4 rounded-full backdrop-blur-md bg-white/10 border border-white/20 shadow-lg">
        <Link href="/" className="text-white font-semibold text-lg tracking-tighter cursor-pointer">
          Roulette
        </Link>
        <button className="text-white font-medium text-sm hover:text-gray-300 transition-colors">
          Connect
        </button>
      </div>
    </nav>
  );
}
