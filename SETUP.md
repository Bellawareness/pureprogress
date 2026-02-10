# Setup Guide - Firebase, Authentication & Hosting

---

## 🔐 Firebase Setup (Database & Authentication)

### Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **"Add project"**
3. Enter project name: `habit-tracker` (or your choice)
4. Disable Google Analytics (not needed)
5. Click **"Create project"**

### Step 2: Set Up Realtime Database

1. In your Firebase project, click **"Realtime Database"** in the left menu
2. Click **"Create Database"**
3. Choose location closest to you
4. Select **"Start in test mode"** (we'll secure it later)
5. Click **"Enable"**

### Step 3: Get Your Firebase Config

1. Click the ⚙️ gear icon → **"Project settings"**
2. Scroll down to **"Your apps"**
3. Click the **</>** (Web) icon
4. Register app name: `habit-tracker-app`
5. Copy the `firebaseConfig` object

It will look like this:
```javascript
const firebaseConfig = {
  apiKey: "AIzaSyC...",
  authDomain: "habit-tracker-xxxxx.firebaseapp.com",
  databaseURL: "https://habit-tracker-xxxxx-default-rtdb.firebaseio.com",
  projectId: "habit-tracker-xxxxx",
  storageBucket: "habit-tracker-xxxxx.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef"
};
```

### Step 4: Update Your index.html

1. Open `index.html`
2. Find the Firebase config section (around line 15)
3. Replace the placeholder with YOUR actual config from Step 3

### Step 5: Test It!

1. Open `index.html` in your browser
2. Open browser console (F12 or right-click → Inspect → Console)
3. Look for: `✓ Connected to Firebase with user: [user-id]`
4. Make a change (add an activity, track water, etc.)
5. Open the app on another device or browser
6. You should see the same data! ✅

### Step 6: Secure Your Database

Once everything works, secure your database:

1. Go to Firebase Console → Realtime Database
2. Click **"Rules"** tab
3. Replace the rules with:

```json
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    }
  }
}
```

4. Click **"Publish"**

This ensures each user can only read/write their own data.

---

## 🔑 Email/Password Authentication Setup

### Step 1: Enable Email/Password

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click your **"habit-tracker"** project
3. In left menu, click **"Authentication"**
4. Click the **"Sign-in method"** tab
5. Find **"Email/Password"** in the list
6. Click on it
7. Toggle **"Enable"** to ON
8. Click **"Save"** ✅

### How to Use Your New Login System

#### First Time Setup:
1. Open your habit tracker on any device
2. Click **"Sign Up"** tab
3. Enter your email and password (min 6 characters)
4. Click **"Create Account"**
5. ✅ Your account is created!

#### On Other Devices:
1. Open your habit tracker on iPad, phone, etc.
2. Click **"Login"** tab
3. Enter the same email/password
4. Click **"Login"**
5. ✅ All your data appears automatically!

#### Sharing with Family/Friends:

**Option 1: Shared Account** (Everyone sees the same data)
- Give them your email/password
- They login and see your shared habit tracker

**Option 2: Separate Accounts** (Private data)
- They click "Sign Up" and create their own account
- Each person has their own private habit tracker

### What Changed

| Feature | Before (Anonymous) | After (Email/Password) |
|---------|-------------------|----------------------|
| Multiple Devices | ❌ Each device = different account | ✅ Same account on ALL devices |
| Sync | ❌ Manual upload/download | ✅ Automatic sync |
| Account Loss | ❌ Lose account if clear cookies | ✅ Never lose your account |
| Sharing | ❌ Not possible | ✅ Easy sharing |

---

## 🌐 Firebase Hosting Setup (Custom Domain)

### Prerequisites
- Custom domain name (e.g., myhabittracker.com)
- Firebase account (you already have this)
- 15 minutes

### Step 1: Install Firebase CLI

Open Terminal and run:

```bash
npm install -g firebase-tools
```

If you don't have Node.js/npm installed:
1. Download from: https://nodejs.org/
2. Install the LTS version
3. Then run the command above

### Step 2: Login to Firebase

```bash
firebase login
```

This will open your browser to authenticate with your Firebase account.

### Step 3: Prepare Your Project Files

Create a clean folder structure:

```bash
cd /Users/elysian/Downloads/Organize
mkdir habittracker-deploy
cd habittracker-deploy
```

Copy your files into this folder:
- `index.html` (from templates folder)
- `manifest.json`
- `service-worker.js`
- `icon-192.png`
- `icon-512.png`

**IMPORTANT**: Rename `templates/index.html` to just `index.html` in the root folder.

### Step 4: Initialize Firebase Hosting

In your `habittracker-deploy` folder:

```bash
firebase init hosting
```

Answer the prompts:
1. **Select a Firebase project**: Choose your existing project
2. **What do you want to use as your public directory?** → Press Enter (default "public")
3. **Configure as a single-page app?** → `y` (Yes)
4. **Set up automatic builds?** → `n` (No)
5. **File public/index.html already exists. Overwrite?** → `n` (No)

### Step 5: Move Your Files to Public Folder

```bash
# Move all your files into the public folder
mv index.html public/
mv manifest.json public/
mv service-worker.js public/
mv icon-192.png public/
mv icon-512.png public/
```

### Step 6: Deploy to Firebase

```bash
firebase deploy --only hosting
```

✅ Your app is now live! Firebase will give you a URL like:
`https://your-project-name.web.app`

Test this URL to make sure everything works.

### Step 7: Connect Your Custom Domain

#### Option A: Domain from Namecheap/GoDaddy/etc.

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Select your project
3. Click **Hosting** in left sidebar
4. Click **Add custom domain** button
5. Enter your domain: `myhabittracker.com`
6. Firebase will show you DNS records to add

**Add these DNS records at your domain registrar:**

**For root domain (myhabittracker.com):**
- Type: `A`
- Name: `@`
- Value: (IP address Firebase provides)

**For www subdomain:**
- Type: `A`
- Name: `www`
- Value: (IP address Firebase provides)

**SSL Certificate:**
Firebase automatically provisions SSL (HTTPS) - usually takes 24-48 hours.

#### Option B: Buy Domain Through Cloudflare (Recommended)

If you haven't bought a domain yet, Cloudflare Registrar offers:
- At-cost pricing (~$10/year)
- Instant DNS updates
- Free SSL
- Better security

1. Buy domain at [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/)
2. In Cloudflare DNS settings, add:
   - Type: `A`, Name: `@`, Value: (Firebase IP)
   - Type: `A`, Name: `www`, Value: (Firebase IP)
3. Set Proxy status to "DNS only" (gray cloud)
4. In Firebase Console, add your domain

### Step 8: Verify Everything Works

After DNS propagates (5 minutes to 48 hours), test:

1. **Visit your domain** → Should load your habit tracker
2. **Test login** → Firebase Auth should work
3. **Install PWA** → Click install prompt on mobile
4. **Test offline** → Turn off wifi, app should still load
5. **Check notifications** → Allow notifications for daily reminder

---

## 🔄 Future Updates

Whenever you make changes:

```bash
# 1. Update your files in the public folder
# 2. Deploy changes
firebase deploy --only hosting

# Your site updates in ~30 seconds!
```

---

## 📊 Monitor Usage

Free tier limits (very generous):
- **Storage**: 10 GB
- **Bandwidth**: 360 MB/day (~10 GB/month)
- **Custom domains**: Unlimited

Check usage at: Firebase Console → Hosting → Usage tab

---

## 🐛 Troubleshooting

### Firebase not connecting
- Check console for errors
- Verify your firebaseConfig is correct
- Make sure Realtime Database is enabled

### Data not syncing
- Open console and look for sync messages
- Check Firebase Console → Realtime Database to see if data is there
- Try refreshing the page

### Permission denied
- Check database rules
- Make sure you're authenticated (check console for user ID)

### Domain not connecting?
- Wait 24-48 hours for DNS propagation
- Use [WhatsMyDNS.net](https://whatsmydns.net) to check DNS propagation
- Make sure proxy is OFF in Cloudflare (if using)

### PWA install not showing?
- Make sure you're using HTTPS (not HTTP)
- Check that `manifest.json` and `service-worker.js` are loading
- Open DevTools → Application → Manifest to debug

### Firebase Auth not working?
- Check Firebase Console → Authentication → Settings → Authorized domains
- Add your custom domain to the list

---

## 💰 Costs Summary

- **Firebase Hosting**: $0/month (free tier)
- **Firebase Auth**: $0/month (free tier)
- **Firebase Database**: $0/month (free tier, up to 1GB)
- **Custom Domain**: ~$10-12/year
- **SSL Certificate**: $0 (included)

**Total: ~$10/year** 🎉

---

## 📞 Need Help?

- Firebase Docs: https://firebase.google.com/docs
- Firebase Hosting: https://firebase.google.com/docs/hosting
- Firebase Support: https://firebase.google.com/support
- Community: https://stackoverflow.com/questions/tagged/firebase

---

**You're all set! Your habit tracker is ready to deploy with Firebase, authentication, and a custom domain.** 🚀 | **Date:** February 9, 2026
