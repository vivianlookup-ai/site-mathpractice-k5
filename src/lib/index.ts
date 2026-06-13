// MathPractice K5 — Central Library Barrel Export
// Import from '@/lib' to access all shared logic with a single import.
// Future: extract into @mathpracticek5/core-logic npm package.

export {
  grades,
  getGrade,
  getTopic,
} from './grades';

export type {
  Topic,
  GradeData,
} from './grades';

export {
  LEMONSQUEEZY_CONFIG,
  PRICING,
  FREE_WORKSHEETS_PER_TOPIC,
  getCheckoutUrl,
  getAccessLevel,
} from './payment';
