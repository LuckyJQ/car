package com.example.car;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class EmailActivity extends AppCompatActivity implements View.OnClickListener {

    private Button login = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_email);

        login = findViewById(R.id.login);
        login.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        if(v.getId() == R.id.login){
            Toast.makeText(this, "授权成功", Toast.LENGTH_SHORT).show();
            Intent goEmailList = new Intent(this, EmailListActivity.class);
            startActivity(goEmailList);
        }
    }
}
