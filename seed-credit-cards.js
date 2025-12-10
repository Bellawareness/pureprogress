// Run this in browser console or load as script to seed initial credit card data
const creditCards = [
  {
    id: '1-chase',
    name: 'Chase Sapphire',
    last4: '0000',
    limit: 35000,
    apr: 0,
    balance: 911.98,
    minPayment: 40,
    createdAt: new Date().toISOString()
  },
  {
    id: '2-bofa',
    name: 'Bank of America',
    last4: '1111',
    limit: 25000,
    apr: 25.6,
    balance: 7022.08,
    minPayment: 222,
    createdAt: new Date().toISOString()
  },
  {
    id: '3-bofa-ul',
    name: 'Bank of America Unlimited',
    last4: '2222',
    limit: 30000,
    apr: 23.2,
    balance: 7235.81,
    minPayment: 210,
    createdAt: new Date().toISOString()
  },
  {
    id: '4-apple',
    name: 'Apple',
    last4: '3333',
    limit: 15000,
    apr: 26.6,
    balance: 2926.12,
    minPayment: 100,
    createdAt: new Date().toISOString()
  },
  {
    id: '5-paypal',
    name: 'PayPal',
    last4: '4444',
    limit: 10000,
    apr: 0,
    balance: 2145.2,
    minPayment: 53,
    createdAt: new Date().toISOString()
  },
  {
    id: '6-citi',
    name: 'Citi Card',
    last4: '5555',
    limit: 18000,
    apr: 23.3,
    balance: 3681.12,
    minPayment: 111.02,
    createdAt: new Date().toISOString()
  },
  {
    id: '7-priceline',
    name: 'Priceline',
    last4: '6666',
    limit: 15000,
    apr: 19.9,
    balance: 2562.43,
    minPayment: 70.15,
    createdAt: new Date().toISOString()
  },
  {
    id: '8-carnival',
    name: 'Carnival',
    last4: '7777',
    limit: 20000,
    apr: 23.6,
    balance: 3872.53,
    minPayment: 113.11,
    createdAt: new Date().toISOString()
  },
  {
    id: '9-ulta',
    name: 'Ulta',
    last4: '8888',
    limit: 5000,
    apr: 0,
    balance: 100,
    minPayment: 20,
    createdAt: new Date().toISOString()
  }
];

// Save to localStorage
localStorage.setItem('creditCards', JSON.stringify(creditCards));
console.log('✅ Credit cards seeded successfully!', creditCards);
