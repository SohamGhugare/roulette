export default function Footer() {
  return (
    <footer className="fixed bottom-4 left-1/2 -translate-x-1/2 z-50">
      <p className="text-white/40 text-xs font-medium">
        © {new Date().getFullYear()} Roulette. All rights reserved.
      </p>
    </footer>
  );
}
