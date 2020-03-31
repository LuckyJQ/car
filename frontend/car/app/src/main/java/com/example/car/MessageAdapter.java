package com.example.car;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

import androidx.recyclerview.widget.RecyclerView;

public class MessageAdapter extends RecyclerView.Adapter<MessageAdapter.ViewHolder>{

    private List<Message> myMsgList;

    static class ViewHolder extends RecyclerView.ViewHolder {
        View msgView;
        ImageView msgImage;
        TextView msgName;

        public ViewHolder(View view) {
            super(view);
            msgView = view;
//            msgImage = (ImageView) view.findViewById(R.id.msg_image);
            msgName = (TextView) view.findViewById(R.id.msg_name);
        }
    }

    public MessageAdapter(List<Message> msgList) {
        myMsgList = msgList;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.msg_item, parent, false);
        final ViewHolder holder = new ViewHolder(view);
        holder.msgView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int position = holder.getAdapterPosition();
                Message msg = myMsgList.get(position);
                Toast.makeText(v.getContext(), "you clicked view " + msg.getName(), Toast.LENGTH_SHORT).show();
            }
        });
//        holder.msgImage.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                int position = holder.getAdapterPosition();
//                Message msg = myMsgList.get(position);
//                Toast.makeText(v.getContext(), "you clicked image " + msg.getName(), Toast.LENGTH_SHORT).show();
//            }
//        });
        return holder;
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        Message msg = myMsgList.get(position);
//        holder.msgImage.setImageResource(msg.getImageId());
        holder.msgName.setText(msg.getName());
    }

    @Override
    public int getItemCount() {
        return myMsgList.size();
    }

}