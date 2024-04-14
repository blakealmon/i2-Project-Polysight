import streamlit as st
import openai
import trafilatura


st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.title(':blue[Polysight]')

url = st.text_input('Enter URL - Takes some time (Make sure to press enter)')


#url = 'https://www.cnn.com/2024/04/07/politics/supreme-court-5th-circuit/index.html'
downloaded = trafilatura.fetch_url(url)
article_content = trafilatura.extract(downloaded)
print(article_content)



if article_content is None:
    article_content = ""
else:

    #image = st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcm9ndGR3cjM1cnpoMzR5dzNuYzFlMG4xdHA1b25rdXM0azlldjMxdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/zlcIBNopQj8Yx5QgpR/giphy.gif)")

    # Define your OpenAI API key
    openai.api_key = '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'

    response = openai.ChatCompletion.create( model="gpt-4", messages=[{"role": "user", "content": "You are to be given an article and then you must first say if the article leans to the right or the left or neutral politically then give it a rating from 0.00 - 1.00 on how biased it is toward the side and include what the bias is by saying 'I would rate it [bias] on it being leaning to the direction politically (1.00 being max)' (you must paraphrase). [DO NOT USE I or any pronouns and sound robotic] Then take a deep breath and give reasoning behind your choice. Do not make the reasoning long. Make sure the reasoning is like around 2 sentences and in bullet points. Make sure that there is a line indent between reasoning and bias. and Here is the article : " + article_content}] ) # print(response)

 

    x = "" + response.choices[0].message.content
    st.write(x)




