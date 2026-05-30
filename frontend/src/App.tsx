import { useState } from "react"
import ChatAssistant from "@/components/chat-assistant"
import FinancialGraphs from "@/components/financial-graphs"
import MiniFinanceGame from "@/components/mini-finance-game"
import StreakDisplay from "@/components/streak-display"
import FinancialProfiler from "@/components/financial-profiler"

export default function App() {
  const [activeTab, setActiveTab] = useState<"chat" | "graphs" | "game" | "profiler">("chat")
  const [currentStreak, setCurrentStreak] = useState(12)
  const [bestStreak] = useState(42)

  return (
    <main className="min-h-screen bg-background flex flex-col">
      <header className="sticky top-0 z-50 border-b border-border/50 bg-background/80 backdrop-blur-md">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div>
            <h1 className="text-2xl sm:text-3xl font-bold bg-gradient-to-r from-purple-400 via-blue-400 to-cyan-400 bg-clip-text text-transparent">
              FinanceFlow
            </h1>
            <p className="text-xs text-muted-foreground mt-1">Tu asistente financiero inteligente</p>
          </div>
          <StreakDisplay currentStreak={currentStreak} bestStreak={bestStreak} />
        </div>
      </header>

      <div className="border-b border-border/50 bg-background/50 backdrop-blur">
        <div className="max-w-6xl mx-auto px-4 flex gap-8">
          {[
            { id: "chat", label: "Asistente", icon: "💬" },
            { id: "profiler", label: "Mi Perfil", icon: "🎯" },
            { id: "graphs", label: "Conceptos", icon: "📊" },
            { id: "game", label: "Juego", icon: "🎮" },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as "chat" | "graphs" | "game" | "profiler")}
              className={`px-4 py-4 font-medium transition-all border-b-2 text-sm sm:text-base ${
                activeTab === tab.id
                  ? "border-cyan-400 text-cyan-400"
                  : "border-transparent text-muted-foreground hover:text-foreground"
              }`}
            >
              <span className="mr-2">{tab.icon}</span>
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 max-w-6xl mx-auto w-full px-4 py-8">
        {activeTab === "chat" && <ChatAssistant onStreakUpdate={setCurrentStreak} />}
        {activeTab === "profiler" && <FinancialProfiler />}
        {activeTab === "graphs" && <FinancialGraphs />}
        {activeTab === "game" && <MiniFinanceGame onStreakUpdate={setCurrentStreak} />}
      </div>
    </main>
  )
}
