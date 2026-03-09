'use client';

/**
 * A single Simon Says colored button.
 * Lights up with a neon glow when active; dims when inactive.
 */

import { motion } from 'framer-motion';
import type { ButtonConfig } from '../utils/constants';

interface Props {
  config: ButtonConfig;
  /** Whether this button is currently lit (CPU showing or player pressing it) */
  isActive: boolean;
  /** Whether the player can interact right now */
  isInteractive: boolean;
  /** Called when the player presses this button */
  onPress: () => void;
  /** Which corner of the 2×2 grid this button occupies */
  corner: 'tl' | 'tr' | 'bl' | 'br';
  /** Show color name + key hint label */
  showLabel?: boolean;
}

/** Outer corner radius per grid position (large outer, small inner) */
const CORNER_RADIUS: Record<Props['corner'], string> = {
  tl: 'rounded-tl-[44%] rounded-tr-xl rounded-bl-xl rounded-br-md',
  tr: 'rounded-tr-[44%] rounded-tl-xl rounded-br-xl rounded-bl-md',
  bl: 'rounded-bl-[44%] rounded-br-xl rounded-tl-xl rounded-tr-md',
  br: 'rounded-br-[44%] rounded-bl-xl rounded-tr-xl rounded-tl-md',
};

export default function SimonButton({
  config,
  isActive,
  isInteractive,
  onPress,
  corner,
  showLabel = false,
}: Props) {
  return (
    <motion.button
      aria-label={`${config.label} button${isActive ? ' (active)' : ''}`}
      aria-pressed={isActive}
      // Never use `disabled` — it causes browsers to apply opacity:0.5
      // which kills the glow effect. Block clicks via onClick guard instead.
      onClick={() => { if (isInteractive) onPress(); }}
      whileTap={isInteractive ? { scale: 0.92 } : undefined}
      transition={{ type: 'spring', stiffness: 400, damping: 18 }}
      className={[
        'w-full h-full select-none outline-none',
        'relative flex items-center justify-center',
        'focus-visible:ring-4 focus-visible:ring-white/50',
        CORNER_RADIUS[corner],
        isInteractive ? 'cursor-pointer' : 'cursor-default',
      ].join(' ')}
      style={{
        // Inline transition so it always applies regardless of Tailwind version
        transition: 'background-color 0.12s ease, box-shadow 0.12s ease',
        backgroundColor: isActive ? config.activeColor : config.baseColor,
        // Active: bright outer glow + tighter inner glow for neon effect
        // Inactive: plain inset shadow
        boxShadow: isActive
          ? `0 0 0 2px ${config.glowColor}40,
             0 0 20px 4px ${config.glowColor},
             0 0 50px 12px ${config.glowColor}60,
             inset 0 0 20px 4px ${config.glowColor}30`
          : 'inset 0 3px 6px rgba(0,0,0,0.6)',
      }}
    >
      {/* Gloss sheen */}
      <span className="absolute inset-0 rounded-[inherit] bg-gradient-to-br from-white/15 to-transparent pointer-events-none" />

      {/* Color name + keyboard key */}
      {showLabel && (
        <span className="relative z-10 flex flex-col items-center gap-1 pointer-events-none select-none">
          <span
            className="text-xs sm:text-sm font-bold uppercase tracking-widest drop-shadow-md"
            style={{ color: isActive ? '#fff' : `${config.activeColor}dd` }}
          >
            {config.label}
          </span>
          <kbd
            className="text-[10px] sm:text-xs font-mono px-1.5 py-0.5 rounded border"
            style={{
              color: isActive ? '#ffffffcc' : `${config.activeColor}88`,
              borderColor: isActive ? '#ffffff40' : `${config.activeColor}33`,
              backgroundColor: 'rgba(0,0,0,0.35)',
            }}
          >
            {config.key.toUpperCase()}
          </kbd>
        </span>
      )}
    </motion.button>
  );
}
