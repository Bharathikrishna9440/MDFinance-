package com.example.network

import android.app.DownloadManager
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log
import android.widget.Toast

class UpdateDownloadReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == DownloadManager.ACTION_DOWNLOAD_COMPLETE) {
            val id = intent.getLongExtra(DownloadManager.EXTRA_DOWNLOAD_ID, -1L)
            val sharedPrefs = context.getSharedPreferences("weekly_finance_prefs", Context.MODE_PRIVATE)
            
            // Critical check: Only process update installation if the user is signed in
            val isLoggedIn = sharedPrefs.getBoolean("is_logged_in", false)
            if (!isLoggedIn) {
                Log.i("UpdateDownloadReceiver", "User is not logged in. Discarding update install.")
                return
            }

            val savedDownloadId = sharedPrefs.getLong("enqueued_download_id", -1L)
            val latestCode = sharedPrefs.getLong("downloading_version_code", -1L)

            if (id == savedDownloadId && id != -1L && latestCode != -1L) {
                Log.i("UpdateDownloadReceiver", "Persisted Update download completed! Delegating to FirebaseUpdateManager for v$latestCode...")
                FirebaseUpdateManager.onDownloadComplete(context, id, latestCode)
            }
        }
    }
}
