// MathPractice K5 — Payment & Access Configuration
// Central config for pricing, LemonSqueezy checkout URLs, and access rules

// ==========================================
// LemonSqueezy Configuration
// ==========================================
export const LEMONSQUEEZY_CONFIG = {
  storeId: 'MATHPRACTICE_K5', // Your LemonSqueezy store ID
  successUrl: 'https://mathpracticek5.com/success/',
  cancelUrl: 'https://mathpracticek5.com/cancel/',
  billingUrl: 'https://mathpracticek5.lemonsqueezy.com/billing',
};

// ==========================================
// Plan Pricing (Variant IDs from LemonSqueezy)
// Replace placeholder IDs with your actual variant IDs
// ==========================================
export const PRICING = {
  monthly: {
    id: 'premium-monthly',
    variantId: 'MONTHLY_VARIANT_ID',
    name: 'Premium Monthly',
    price: '$9.99',
    period: '/month',
    description: 'Full access to all worksheets. Cancel anytime.',
    features: [
      'All 1000+ worksheets across K-5',
      'All answer keys included',
      'All difficulty levels',
      'Unlimited printing',
      'Cancel anytime',
    ],
  },
  yearly: {
    id: 'premium-yearly',
    variantId: 'YEARLY_VARIANT_ID',
    name: 'Premium Yearly',
    price: '$49.99',
    period: '/year',
    description: 'Best value — save 58%.',
    features: [
      'All 1000+ worksheets across K-5',
      'All answer keys included',
      'All difficulty levels',
      'Unlimited printing',
      '2 months free vs monthly',
    ],
  },
  lifetime: {
    id: 'lifetime',
    variantId: 'LIFETIME_VARIANT_ID',
    name: 'Lifetime Access',
    price: '$79',
    period: 'one-time',
    description: 'One payment. Forever access.',
    features: [
      'All 1000+ worksheets across K-5',
      'All answer keys included',
      'All difficulty levels',
      'Unlimited printing',
      'All future worksheets included',
    ],
  },
};

/**
 * Build a LemonSqueezy checkout URL for a given plan.
 * @param planKey 'monthly' | 'yearly' | 'lifetime'
 * @returns Full checkout URL with success/cancel redirects
 */
export function getCheckoutUrl(planKey: 'monthly' | 'yearly' | 'lifetime'): string {
  const plan = PRICING[planKey];
  if (!plan) return '/pricing/';
  const params = new URLSearchParams({
    embed: '0',
    'checkout[success_url]': `${LEMONSQUEEZY_CONFIG.successUrl}?plan=${planKey}`,
    'checkout[cancel_url]': LEMONSQUEEZY_CONFIG.cancelUrl,
    'checkout[custom][plan]': planKey,
  });
  return `https://mathpracticek5.lemonsqueezy.com/checkout/buy/${plan.variantId}?${params.toString()}`;
}

// ==========================================
// Access Rules
// ==========================================
export const FREE_WORKSHEETS_PER_TOPIC = 2;

/**
 * Determines which worksheets are free vs premium.
 * @param worksheetIndex - 0-based worksheet index
 * @returns 'free' | 'premium'
 */
export function getAccessLevel(worksheetIndex: number): 'free' | 'premium' {
  return worksheetIndex < FREE_WORKSHEETS_PER_TOPIC ? 'free' : 'premium';
}
