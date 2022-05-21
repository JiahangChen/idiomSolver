package com.ahren.idiomsolver

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {

    private val mainFragment = MainFragment()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val fragmentManager = supportFragmentManager.beginTransaction()
        fragmentManager.add(R.id.main_fragment, mainFragment, "main")
        fragmentManager.commitAllowingStateLoss()
    }
}