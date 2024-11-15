from langchain_community.chat_models import ChatTongyi
from langchain.prompts import ChatPromptTemplate

def generate_script(subject, length):
    model = ChatTongyi(model='qwen-max', api_key='sk-eefb42c8cd9b4d0ea02de46351c172a6')

    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", "给'{subject}'这个餐厅评价想一个吸引人的标题")
        ]
    )

    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """
             你喜欢吃美食，你经常去各个美味的餐厅打卡，现在你需要给{subject}这个餐厅想一段{length}字数的文章，来表达你对这个餐厅的赞美，通常需要从环境，服务和美食的口味三个方面来评价。
             整体内容的表达方式要轻松有趣，吸引年轻人。
             尽量以叙述的口吻来表达，给人身临其境的感觉。
             """
             )
        ]
    )

    # 创建链式调用
    title_chain = title_template | model
    script_chain = script_template | model

    # 传递参数并获取结果
    title = title_chain.invoke({'subject': subject}).content
    script = script_chain.invoke({'subject': subject, 'length': length}).content

    return title, script





