import type { Metadata } from "next";
import { Space_Mono } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";

const spaceMono = Space_Mono({
  variable: "--font-space-mono",
  subsets: ["latin"],
  weight: ["400", "700"],
});

export const metadata: Metadata = {
  title: "Roulette",
  description: "Talk to your local LLM",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${spaceMono.variable} antialiased`}
      >
        <Navbar />
        {children}
      </body>
    </html>
  );
}
