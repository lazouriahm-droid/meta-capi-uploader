import gradio as gr

def hello():
    return "✅ Meta CAPI Uploader يعمل بنجاح"

with gr.Blocks(title="Meta CAPI Uploader") as demo:
    gr.Markdown("# Meta Conversions API Uploader")
    gr.Markdown("إذا ظهر زر الاختبار فهذا يعني أن التطبيق يعمل.")

    btn = gr.Button("اختبار")
    output = gr.Textbox(label="النتيجة")

    btn.click(
        fn=hello,
        inputs=[],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()