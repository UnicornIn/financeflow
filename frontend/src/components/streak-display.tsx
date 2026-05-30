interface StreakDisplayProps {
  currentStreak: number
  bestStreak: number
}

export default function StreakDisplay({ currentStreak, bestStreak }: StreakDisplayProps) {
  return (
    <div className="flex gap-6">
      <div className="text-right">
        <p className="text-xs text-muted-foreground">Racha Actual</p>
        <div className="text-3xl font-bold text-cyan-400 streak-pulse flex items-center gap-2">
          <span>🔥</span>
          {currentStreak}
        </div>
      </div>
      <div className="h-12 w-px bg-border/50"></div>
      <div className="text-right">
        <p className="text-xs text-muted-foreground">Mejor Racha</p>
        <div className="text-2xl font-bold text-purple-400 flex items-center gap-2">
          <span>🏆</span>
          {bestStreak}
        </div>
      </div>
    </div>
  )
}
