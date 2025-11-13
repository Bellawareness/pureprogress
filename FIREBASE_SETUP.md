# Firebase Setup Instructions

Follow these steps to enable cloud sync for your habit tracker:

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **"Add project"**
3. Enter project name: `habit-tracker` (or your choice)
4. Disable Google Analytics (not needed)
5. Click **"Create project"**

## Step 2: Set Up Realtime Database

1. In your Firebase project, click **"Realtime Database"** in the left menu
2. Click **"Create Database"**
3. Choose location closest to you
4. Select **"Start in test mode"** (we'll secure it later)
5. Click **"Enable"**

## Step 3: Get Your Firebase Config

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

## Step 4: Update Your index.html

1. Open `index.html`
2. Find this section near the top (around line 15):
```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  // ... etc
};
```
3. Replace it with YOUR actual config from Step 3

## Step 5: Test It!

1. Open `index.html` in your browser
2. Open browser console (F12 or right-click → Inspect → Console)
3. Look for: `✓ Connected to Firebase with user: [user-id]`
4. Make a change (add an activity, track water, etc.)
5. Open the app on another device or browser
6. You should see the same data!

## Step 6: Secure Your Database (Important!)

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

## How It Works

- **Anonymous Authentication**: Each device/browser gets a unique user ID
- **Automatic Sync**: Every time you save data (localStorage), it syncs to Firebase
- **Cross-Device**: Open on any device and your data appears
- **Offline First**: Still works without internet, syncs when connected

## Troubleshooting

**"Firebase not connecting"**
- Check console for errors
- Verify your firebaseConfig is correct
- Make sure Realtime Database is enabled

**"Data not syncing"**
- Open console and look for sync messages
- Check Firebase Console → Realtime Database to see if data is there
- Try refreshing the page

**"Permission denied"**
- Check database rules (Step 6)
- Make sure you're authenticated (check console for user ID)

## Need Help?

- Firebase Docs: https://firebase.google.com/docs/database
- Check browser console for error messages
- Make sure you completed all steps above

---

**All set!** Your habit tracker now syncs across all your devices! 🎉
