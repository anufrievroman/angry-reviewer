# Angry Reviewer

Stylistic corrector for academic writing and scientific papers. An easy to use web app is hosted at 
[AngryReviewer.com](https://www.angryreviewer.com).

![screenshot](https://github.com/anufrievroman/Angry-Reviewer/blob/master/static/screenshot.png)

The rules used by Angry Reviewer are based on various journal guidelines, articles, books, and lectures on modern academic writing. But, the main source is the book *The Craft of Scientific Writing* by Michael Alley. The alghorithm knows hundreds of rules, most of which are stylistic. For the spell check you should rely on your text editor and other services.

## Running offline version

To run standalone version on your computer, you need to install python 3. Then, just download this repository (you only need two files `plocessing.py` and `rules.py`):

```
git clone https://github.com/anufrievroman/Angry-Reviewer
```

Put your text into `your_text.txt` file and run the `processing.py` file:

```
python processing.py
```

The suggestions should be generated in your python console.

## Main priciples

- Don't hype. Avoid words like novel, highly, clearly, greatly. Better still, avoid all adverbs.
- Don't use clichés. Avoid overused expressions like holy grail, paradigm shift, in a nutshell.
- Don't use "very" very often. Usually, there is a better word for it.
- Be concise. Avoid phrases like by means of, despite the fact that, in order to.
- Avoid negatives. For example, use "unable" instead of "not able".
- Avoid redundancy. For example, use "investigate" instead of "conduct an investigation of".
- Use active voice. Although not always possible, most of the text should be in active voice.
- Avoid inappropriate language. Keep words like "really, actually, pretty much" for social networks.
- Avoid rare words and latinisms. Non credo all readers know the meaning.
- Keep abbreviations to minimum. Abbreviations are hard to read, consider just spelling it out.

Beside these and many smaller rules, Angry Reviewer checks for typical typographic mistakes like spaces between a number and its units, references to Figures and Supplementary materials, chemical elements, abbreviations. If you supply LaTeX text, it can also check your references for self-citation, overcitation, number of references, length of abstract and title, and other LaTeX specific issues.

## Literature

To learn more about the rules used by Angry Reviewer, see the literature:

### Books

- The Craft of Scientific Writing by Michael Alley
- On writing well: the classic guide to writing nonfiction by William Zinsser
- Science research writing for non-native speakers of English by Hilary Glasman-Deal
 
### Articles

- [Elements of Style](https://www.nature.com/articles/nphys724) - Nature Physics 3, 581 (2007)
- [How to Write With Style](https://www.novel-writing-help.com/prose-writing.html) - Article in Novel Writing Help blog
- [The Elements of Style](https://faculty.washington.edu/heagerty/Courses/b572/public/StrunkWhite.pdf) - Collection of rules by Strunk, W., Jr. and White, E.B.

## Support

I am not a professional developer and work on open-source projects in my free time. If you'd like to support the development, consider donations via [buymeacoffee](https://www.buymeacoffee.com/angryprofessor) or cryptocurrencies:

- BTC `bc1qpkzmutdqfxkce34skt09vll97s5smpa0r2tyzj`
- ETH `0x6f1Ce9cA181458Fc153a5f7cBF88044736C3b00C`
- BNB `0x40f22c372758E35C905458cAF8BB17f51ac133d1`
- LTC `ltc1qtu33qyv2xlzxda5mmrmk943zpksq8q75tuh85p`
