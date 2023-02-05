from PIL import Image
import requests
import streamlit as st
import streamlit_lottie as st_lottie


img_icon = Image.open("images/logo.png")

st.set_page_config(page_title="Asim Ismail", page_icon=img_icon, layout="wide")
st.markdown("<script>window.scrollTo(0,0);</script>", unsafe_allow_html=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style?", unsafe_allow_html=True)


local_css("style/style.css")

#         LOAD ASSETS

lottie_ai = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_9azkhcpb.json"
)

img_instagram = Image.open("images/instagram.png")
img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_sudoku = Image.open("images/Sudoku.png")
img_pathfinder = Image.open("images/PathFinder.png")
img_portfolio = Image.open(
    "images/a-simple-artificial-intelligence-website-landing-page-revolutionary-website-state-of-art-technolo-923482858.png"
)

# Header

left_column, right_column = st.columns(2)
with left_column:
    st.title("Hi, My name is Asim Ismail")
with right_column:
    st.empty()

# Home Page
with st.container():
    st.write("---")
    st.write("##")
    st.header("A Computer Science Graduate From Pakistan.")
    st.write(
        "Take a look around and find out more about me and the projects I am working on."
    )
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            As a programmer attempting to transition into an AI developer,
            I'm like a caterpillar trying to transform into a butterfly, it's a big metamorphosis, but I'm excited to see the outcome!
            I'm like a chef trying to become a baker, it's a whole new recipe, but I'm ready to knead the dough!
            I'm like a rock climber trying to scale a mountain, it's a steep ascent, but I'm equipped with determination and algorithms!
            Join me on this exciting adventure as I strive to become an AI developer. It will take a lot of hard work and determination, but I'm hoping to reach my goal. Wish me luck, because I'll need it.
            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/watch?v=jwSBE1EIevA)")
    with right_column:
        st_lottie.st_lottie(lottie_ai, height=350, key="ai")

    # Projects Page
    with st.container():
        st.write("---")
        st.header("Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_sudoku, width=380)
            with text_column:
                st.subheader("Soduko Game")
                st.write(
                    """ 
                This is a pygame project that uses BackTracking to solve a board of 
                soduko puzzle The player can choose to solve the puzzle themselves or 
                have the machine solve it for them, and they can also observe the 
                Backtracking process in real-time. Great work on this project! 
                It is like a fun and educational tool for learning about algorithms and solving puzzles.
                """
                )
                st.markdown(
                    "[Project On GitHub](https://github.com/screwhorn/SudokuPygame)"
                )

        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_pathfinder, width=380)
            with text_column:
                st.subheader("Path Finder")
                st.write(
                    """ 
                Nearest Path Finder Between Two Points. This is a Machine Learning Algorithm 
                that finds the nearest path between two points A-B using a specific algorithm. 
                The user can place obstructions using their mouse cursor, but the AI will 
                eventually find a path. The user can observe the process in real-time if they 
                choose to, or they can simply let the AI find and display the path using blue lines.
                """
                )
                st.markdown(
                    "[Watch Video...](https://www.youtube.com/watch?v=jwSBE1EIevA)"
                )

        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_portfolio, width=380)
            with text_column:
                st.subheader("This Portfolio")
                st.write(
                    """ 
                I have created this portfolio using almost exclusively the Python programming language 
                and several tools such as Streamlit and Lottie Files. My goal is to create something in 
                Python that is typically created using HTML, CSS, Bootstrap, and other web development programming languages.
                This portfolio is a work in progress, and I will be making continual updates and upgrades as I learn new concepts
                and techniques that I can incorporate into it. As time passes, I hope to make my portfolio a showcase of my skills 
                and abilities as a programmer.
                """
                )
                st.markdown(
                    "[Project On GitHub](https://github.com/screwhorn/csportfolio)"
                )


# Contacts Page
with st.container():
    st.write("---")
    st.header("Contact Form")
    st.write("##")

    contact_form = """ 
    <form action="https://formsubmit.co/iasim1999@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
     """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.write("##")
        st.write("Email: iasim1999@gmail.com")
        st.write("Phone Number: (+92) 348-6464-500")
        st.markdown(
            """
    <link href="https://use.fontawesome.com/releases/v5.14.0/css/all.css" rel="stylesheet">
    <style>
    .icon {
        display: inline-block;
        width: 70px;
        height: 70px;
        margin: 20px;
        transition: transform 1s;
        font-size: 40px;
        text-align: center;
    }

    </style>
    <a href="https://www.instagram.com/aso._.oom/">
    <i class="icon fab fa-instagram"></i>
    </a>
    <a href="https://www.linkedin.com/in/asim-ismail-865998a1/">
    <i class="icon fab fa-linkedin"></i>
    </a>
    <a href="https://github.com/screwhorn">
    <i class="icon fab fa-github"></i>
    </a>
    """, unsafe_allow_html=True)