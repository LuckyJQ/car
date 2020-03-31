package com.example.car;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;

import java.util.ArrayList;
import java.util.List;

public class EmailListActivity extends AppCompatActivity {

    private List<Message> msgList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_email_list);

        initMsgs();
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        LinearLayoutManager layoutManager = new LinearLayoutManager(this);
        recyclerView.setLayoutManager(layoutManager);
        MessageAdapter adapter = new MessageAdapter(msgList);
        recyclerView.setAdapter(adapter);
    }

    private void initMsgs() {
        for (int i = 0;i<20;i++){
            Message msg1 = new Message("邮件一：内容内容内容内容内容内容内容内容内容", R.drawable.apple_pic);
            msgList.add(msg1);
            Message msg2 = new Message("邮件二：内容内容内容内容内容内容内容内容内容", R.drawable.banana_pic);
            msgList.add(msg2);
        }
    }
}
