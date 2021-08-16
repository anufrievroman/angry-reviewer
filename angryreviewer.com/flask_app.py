from flask import Flask, request

from processing import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def corrector_page():
    errors = ""
    text = None
    if request.method == "POST":
        text = str(request.form["text"])
        text_split = text.split('\r\n')
        result = main(text_split)
        return '''
            <html>
                <head>
                    <link rel="stylesheet" href="/static/style.css">
                    <link rel="shortcut icon" href="static/favicon.ico">
                    <meta property="og:site_name" content="Angry Reviewer">
                    <meta property="og:url" content="https://www.angryreviewer.com">
                    <meta property="og:title" content="Angry Reviewer - Academic style editor">
                    <meta property="og:description" content="Free academic style corrector for modern scientific writing.!">
                    <meta property="og:image" content="/static/logo_big.png">
                    <meta property="twitter:image" content="/static/logo_big.png">
                </head>
                <body>
                <div class="content">
                    <div class="header">
                        <img src="/static/logo.png" alt="Angry Reviewer">
                        <a href="/" class="logo"><h1>Angry Reviewer</h1></a>
                        <div class="header-right">
                        <a class="active" href="/">Corrector</a>
                        <a href="/rules">Rules</a>
                        <a href="/about">About</a>
                        </div>
                    </div>
                    <div class="container">
                    <p><b>Reviewer's suggestions for your text:</b></p>
                    <p>{result}</p>
                    <br>
                    <p><a href="/" class="buttons">Back</a> <a href="https://buymeacoffee.com/angryprofessor" class="buttons">Buy me a coffee</a></p>
                    <br>
                    <br>
                    </div>
                </div>
                </body>
            </html>
        '''.format(result=result)

    return '''
        <html>
            <head>
                <link rel="stylesheet" href="/static/style.css">
                <link rel="shortcut icon" href="static/favicon.ico">
                <meta property="og:site_name" content="Angry Reviewer">
                <meta property="og:url" content="https://www.angryreviewer.com">
                <meta property="og:title" content="Angry Reviewer - Academic style editor">
                <meta property="og:description" content="Free academic style corrector for modern scientific writing.!">
                <meta property="og:image" content="/static/logo_big.png">
                <meta property="twitter:image" content="/static/logo_big.png">
            </head>
            <body>
            <div class="content">
                <div class="header">
                    <img src="/static/logo.png" alt="Angry Reviewer">
                    <a href="/" class="logo"><h1>Angry Reviewer</h1></a>
                    <div class="header-right">
                    <a class="active" href="/">Corrector</a>
                    <a href="/rules">Rules</a>
                    <a href="/about">About</a>
                    </div>
                </div>
                <div class="container">
                <div class="nicetext">
                <p>Free academic style corrector for modern scientific writing. To get style suggestion for your abstacts, papers, theses, and applications, paste the text below:</p>
                <form method="post" action=".">
                    <textarea id="subject" name="text" placeholder="Paste your text here..." style="height:300px">Despite the fact that quantity of new scientific output clearly increased significantly in the past years, it is known that the quality of academic writing has been declining as never before. Click the button below to check this text!</textarea>
                    <p><input type="submit" class="block" value="Check" /></p>

                </form>
                </div>
                </div>
            </div>
            </body>
        </html>
    '''.format(errors=errors)


@app.route("/rules")
def rules_page():
    return '''
        <html>
            <head>
                <link rel="stylesheet" href="/static/style.css">
                <link rel="shortcut icon" href="static/favicon.ico">
                <meta property="og:site_name" content="Angry Reviewer">
                <meta property="og:url" content="https://www.angryreviewer.com">
                <meta property="og:title" content="Angry Reviewer - Academic style editor">
                <meta property="og:description" content="Free academic style corrector for modern scientific writing.!">
                <meta property="og:image" content="/static/logo_big.png">
                <meta property="twitter:image" content="/static/logo_big.png">
            </head>
            <body>
            <div class="content">
                <div class="header">
                    <img src="/static/logo.png" alt="Angry Reviewer">
                    <a href="/" class="logo"><h1>Angry Reviewer</h1></a>
                    <div class="header-right">
                    <a href="/">Corrector</a>
                    <a class="active" href="/rules">Rules</a>
                    <a href="/about">About</a>
                    </div>
                </div>
                <div class="container">
                <div class="nicetext">
                <p>The rules used by Angry Reviewer are based on journal guidelines, articles, books, and lectures on modern academic writing. The alghorithm knows hundreds of rules, most of which are stylistic. For the spellcheck you should rely on your text editor and other services.</p>
                <h2>Main priciples</h2>
                <ul>
                <li> <i>Don't hype.</i> Avoid words like novel, highly, clearly, greatly. Better still, avoid all advebs.</li>
                <li> <i>Don't use cliches.</i> Avoid overused expressions like holy grail, paradigm shift, in a nutshell.</li>
                <li> <i>Don't use "very" very often.</i> Usually, there is a better word for it.</li>
                <li> <i>Be concise.</i> Avoid phrases like <i>by means of, despite the fact that, in order to</i>.</li>
                <li> <i>Avoid negatives.</i> For example, use "unable" instead of "not able".</li>
                <li> <i>Avoid redundancy.</i> For example, use "investigate" instead of "conduct an investigation of".</li>
                <li> <i>Use active voice.</i> Although not always possible, most of the text should be in active voice.</li>
                <li> <i>Avoid inapproprite language.</i> Keep words like "really, actually, pretty much" for social networks.</li>
                <li> <i>Avoid rare words and latinisms.</i> Non credo all readers know the meaning.</li>
                <li> <i>Keep abbreviations to minimum.</i> Abbreviations are hard to read, consider just spelling it out.</li>
                </ul>
                <p>Beside these and many smaller rules, Angry Reviewer checks for typical typographic mistakes like spaces between a number and its units, references to Figures and Supplementary materials, chemical elements, abbreviations and other details. Full list of rules can be found the the source code in the <a href="https://github.com/anufrievroman/Angry-Reviewer">github repository</a>.</p>
                <h2>Literature</h2>
                <p>To learn more about the rules used by Angry Reviewer, see the literature below.
                <h3>Books</h3>
                <ul>
                <li><i>The Craft of Scientific Writing</i> by Michael Alley</li>
                <li><i>On writing well: the classic guide to writing nonfiction</i> by William Zinsser</li>
                <li><i>Science research writing for non-native speakers of English</i> by Hilary Glasman-Deal</li>
                </ul>
                <h3>Articles</h3>
                <ul>
                <li><i>Elements of Style</i> - <a href="https://www.nature.com/articles/nphys724">Nature Physics 3, 581 (2007)</a></li>
                <li><i>How to Write With Style</i> - <a href="hhttps://www.novel-writing-help.com/prose-writing.html">Article in Novel Writing Help blog</a></li>
                <li><i>The Elements of Style</i> - <a href="https://faculty.washington.edu/heagerty/Courses/b572/public/StrunkWhite.pdf">Collection of rules by Strunk, W., Jr. and White, E.B.</a></li>
                </ul>
                </div>
                <p><a href="https://buymeacoffee.com/angryprofessor" class="buttons">Buy me a coffee</a></p>
                <br>
                <br>
                </div>
            </div>
            </body>
        </html>
    '''

@app.route("/about")
def about_page():
    return '''
        <html>
            <head>
                <link rel="stylesheet" href="/static/style.css">
                <link rel="shortcut icon" href="static/favicon.ico">
                <meta property="og:site_name" content="Angry Reviewer">
                <meta property="og:url" content="https://www.angryreviewer.com">
                <meta property="og:title" content="Angry Reviewer - Academic style editor">
                <meta property="og:description" content="Free academic style corrector for modern scientific writing.!">
                <meta property="og:image" content="/static/logo_big.png">
                <meta property="twitter:image" content="/static/logo_big.png">
            </head>
            <body>
            <div class="content">
                <div class="header">
                    <img src="/static/logo.png" alt="Angry Reviewer">
                    <a href="/" class="logo"><h1>Angry Reviewer</h1></a>
                    <div class="header-right">
                    <a href="/">Corrector</a>
                    <a href="/rules">Rules</a>
                    <a class="active" href="/about">About</a>
                    </div>
                </div>
                <div class="container">
                <h2>Author</h2>
                <p>The Angry Reviewer is a free and open-source project. These alghoritms were gathered and implemented by Dr. Roman Anufriev based on <a href="/rules">articles, books</a>, and lectures on scintific writing as well as his experience in academia.</p>
                <h2>Privacy</h2>
                <p>This website does not save or store your text, as you can verify in the source code. If you still worry about privacy of your super secret project, you can download the python code of this alghorithm with the link below, verify it, and run it locally on your computer.</p>
                <h2>Contacts</h2>
                <p>For suggestions and issues regarding the alghorithm, feel free to open an issue on github. If you wish to discuss this website or some of the rules, you can find current contacts of the author with the link below.
                <p><a href="https://github.com/anufrievroman/Angry-Reviewer" class="buttons">Soucre code</a> <a href="https://anufrievroman.com" class="buttons">Author</a> <a href="https://buymeacoffee.com/angryprofessor" class="buttons">Buy me a coffee</a></p>
                <br>
                <br>
                </div>
            </div>
            </body>
        </html>
    '''
