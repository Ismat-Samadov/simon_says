'use client';

/**
 * Full-viewport overlay shown on game over or paused state.
 * Uses `fixed inset-0` so it always covers the entire screen correctly,
 * regardless of the board's position in the DOM.
 */

import { motion, AnimatePresence } from 'framer-motion';
import type { Phase } from '../hooks/useSimonGame';
import type { Difficulty } from '../utils/constants';

interface Props {
  phase: Phase;
  score: number;
  highScore: number;
  difficulty: Difficulty;
  isNewHighScore: boolean;
  onRestart: () => void;
  onResume?: () => void;
}

const DIFFICULTY_LABELS: Record<Difficulty, string> = {
  easy: 'Easy',
  medium: 'Medium',
  hard: 'Hard',
};

export default function EndScreen({
  phase,
  score,
  highScore,
  difficulty,
  isNewHighScore,
  onRestart,
  onResume,
}: Props) {
  const visible = phase === 'game_over' || phase === 'paused';

  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          key={phase}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          // fixed inset-0: always covers the full viewport, never clips or bleeds
          className="fixed inset-0 z-50 flex flex-col items-center justify-center px-6"
          style={{ backgroundColor: 'rgba(2, 2, 15, 0.88)', backdropFilter: 'blur(8px)' }}
        >
          {phase === 'game_over' ? (
            <motion.div
              initial={{ scale: 0.85, opacity: 0, y: 20 }}
              animate={{ scale: 1, opacity: 1, y: 0 }}
              transition={{ type: 'spring', stiffness: 260, damping: 20 }}
              className="flex flex-col items-center gap-4 w-full max-w-sm"
            >
              {/* Title */}
              <div
                className="text-5xl sm:text-6xl font-black tracking-tight"
                style={{ color: '#ef4444', textShadow: '0 0 40px #ef4444, 0 0 80px #ef444460' }}
              >
                GAME OVER
              </div>

              {/* Score card */}
              <div className="w-full rounded-2xl border border-white/10 bg-white/5 p-5 flex flex-col items-center gap-2">
                <span className="text-xs font-semibold uppercase tracking-widest text-white/40">
                  Your Score
                </span>
                <span className="text-6xl font-extrabold text-white tabular-nums">
                  {score}
                </span>

                {isNewHighScore ? (
                  <motion.span
                    initial={{ scale: 0.8, opacity: 0 }}
                    animate={{ scale: [1, 1.12, 1], opacity: 1 }}
                    transition={{ delay: 0.3, duration: 0.5 }}
                    className="text-yellow-400 font-bold text-sm px-4 py-1.5 rounded-full border border-yellow-400/40 bg-yellow-400/10"
                    style={{ textShadow: '0 0 12px #eab308' }}
                  >
                    🏆 New High Score!
                  </motion.span>
                ) : (
                  <span className="text-white/40 text-sm">
                    Best ({DIFFICULTY_LABELS[difficulty]}): <strong className="text-white/60">{highScore}</strong>
                  </span>
                )}
              </div>

              {/* Buttons */}
              <div className="flex gap-3 w-full">
                <motion.button
                  onClick={onRestart}
                  whileHover={{ scale: 1.04 }}
                  whileTap={{ scale: 0.96 }}
                  className="flex-1 py-4 rounded-2xl text-lg font-extrabold bg-violet-600 hover:bg-violet-500 text-white transition-colors"
                  style={{ boxShadow: '0 0 24px 4px #7c3aed80' }}
                >
                  ▶ Play Again
                </motion.button>
              </div>
            </motion.div>
          ) : (
            /* ── Paused ────────────────────────────────────────── */
            <motion.div
              initial={{ scale: 0.85, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ type: 'spring', stiffness: 300, damping: 20 }}
              className="flex flex-col items-center gap-5 w-full max-w-xs"
            >
              <div className="text-4xl font-black text-white tracking-widest">
                ⏸ PAUSED
              </div>

              <div className="flex gap-3 w-full">
                {onResume && (
                  <motion.button
                    onClick={onResume}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.96 }}
                    className="flex-1 py-3 rounded-xl font-bold bg-green-600 hover:bg-green-500 text-white transition-colors"
                    style={{ boxShadow: '0 0 16px 3px #22c55e60' }}
                  >
                    Resume
                  </motion.button>
                )}
                <motion.button
                  onClick={onRestart}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.96 }}
                  className="flex-1 py-3 rounded-xl font-bold bg-white/10 hover:bg-white/20 border border-white/20 text-white/80 transition-colors"
                >
                  ↩ Menu
                </motion.button>
              </div>
            </motion.div>
          )}
        </motion.div>
      )}
    </AnimatePresence>
  );
}
