AI: str = "AI"
USER: str = "USER"

SYSTEM_MESSAGE = {
    "role": "system",
    "content": "you are a helpful assistant. answer similar a human.",
}

MODELS: list[str] = ["Model_1", "Model_2", "Model_3", "Model_4", "Model_5"]

STREAMLIT_STYLE: str = """
<style>
    @import url('https://fonts.cdnfonts.com/css/iransansx');

    html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
        font-family: 'IRANSansX', tahoma !important;
    }

    div.e121c1cl0 {
        margin-right: 10px !important;
    }

    [role=radiogroup], pre {
        direction: ltr;
        text-align: left;
    }

    .block-container, section, input, textarea {
        direction: rtl;
        text-align: justify;
    }
</style>
"""

ABOUT: str = """
<p style="direction: rtl; text-align: justify;">
    توسعه دهنده: امیر وزیری
</p>

<hr />

<p style="direction: ltr; text-align: left;">
    Version: 3.1
    <br>
    📞 +98-912-108-7461
    <br />
    📧 amirVaziry7@Gmail.com
    <br />
    🌐 <a href='amirvaziry7.com'>amirvaziry7.com</a>
</p>
"""

SETTINGS: str = "تنظیمات"
PAGE_TITLE: str = "Chatbot امیر وزیری"
SELECTED_MODEL: str = "مدل انتخاب شده:"
SELECT_YOUR_MODEL: str = "لطفا مدل خود را انتخاب نمایید:"
PAGE_HEADER: str = "👋 به Chatbot امیر وزیری خوش آمدید!"
USER_PROMPT_PLACEHOLDER: str = "لطفا سوال خودتان را اینجا بنویسید..."
ERROR_YOU_DID_NOT_SPECIFY_MODEL_NAME: str = (
    "لطفا برای انجام عملیات، مدل خود را انتخاب نمایید!"
)