package com.example.car;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private final String TAG = "MainActivity";
    private Button email = null;
    private Button weChat = null;
    private Button phone = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        email = findViewById(R.id.email);
        weChat = findViewById(R.id.wechat);
        phone = findViewById(R.id.phone);
        email.setOnClickListener(this);
        weChat.setOnClickListener(this);
        phone.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.email:
                Toast.makeText(this,"邮件app",Toast.LENGTH_SHORT).show();
                Intent goEmail = new Intent(this, EmailActivity.class);
                startActivity(goEmail);
                break;
            case R.id.wechat:
                Toast.makeText(this,"微信app",Toast.LENGTH_SHORT).show();
                break;
            case R.id.phone:
                Toast.makeText(this,"电话app",Toast.LENGTH_SHORT).show();
                break;
            default:
                break;
        }
    }
}
