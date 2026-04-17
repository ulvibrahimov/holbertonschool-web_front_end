#!/usr/bin/python3
import os

head_base = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{}</title>
    <meta name="description" content="Techium is a digital agency">
    <link rel="icon" type="image/x-icon" href="./favicon.ico">
    <link rel="icon" type="image/png" href="./favicon.png">
  </head>"""

lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!"
lorem_short_1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Id Sextilius factum negabat. Quo tandem modo? At eum nihili facit; Quae contraria sunt his, malane?"
lorem_short_2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Tum mihi Piso: Quid ergo? Tum ille: Ain tandem? Non autem hoc: igitur ne illud quidem. Sed quod proximum fuit non vidit. Nos commodius agimus. An nisi populari fama?"
lorem_short_3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Non igitur bene. Quid enim est a Chrysippo praetermissum in Stoicis? Pugnant Stoici cum Peripateticis. Prioris generis est docilitas, memoria; Apparet statim, quae sint officia, quae actiones."

# -------------------------------------------------------------
# FINAL INDEX PAGE (Tasks 20-25, 27, 29)
# -------------------------------------------------------------
final_index = head_base.format("Homepage - Techium") + f"""
  <body>
    <header>
      <div>
        <div>
          <a href="/"><span>Techium</span></a>
        </div>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#works">Works</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#latest_news">Latest news</a></li>
            <li><a href="#testimonials">Testimonials</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <main>
      <h1>Homepage</h1>
      <section>
        <div>
          <h2>We help you build your brand!</h2>
          <a href="#">Get started</a>
        </div>
      </section>
      <section>
        <div>
          <header>
            <h2>Services</h2>
            <p>We work with you</p>
          </header>
          <div>
            <h3><a href="#">Design & Concept</a></h3>
            <h3><a href="#">Digital Strategy</a></h3>
            <h3><a href="#">Content Strategy</a></h3>
            <h3><a href="#">UX Design</a></h3>
            <h3><a href="#">Web Development</a></h3>
            <h3><a href="#">Social Media</a></h3>
          </div>
        </div>
      </section>
      <section>
        <div>
          <header>
            <h2>Works</h2>
            <p>Take a look in our portfolio</p>
          </header>
          <div>
            <article>
              <h3><a href="#">Interior Design</a></h3>
            </article>
            <article>
              <h3><a href="#">Web Development</a></h3>
            </article>
            <article>
              <h3><a href="#">Personal Brand</a></h3>
            </article>
          </div>
        </div>
      </section>
      <section>
        <div>
          <header>
            <h2>About Us</h2>
            <p>Everything about us</p>
          </header>
          <div>
            <h3>Who are we</h3>
            <p>{lorem}</p>
            <h3>Our culture</h3>
            <p>{lorem}</p>
            <h3>How we work</h3>
            <p>{lorem}</p>
            <a href="about.html">Learn more about us</a>
          </div>
        </div>
      </section>
      <section>
        <div>
          <header>
            <h2>Latest news</h2>
          </header>
          <div>
            <article>
              <p>Career</p>
              <h3><a href="#">Hoc loco tenere se Triarius non potuit.</a></h3>
              <p>{lorem_short_1}</p>
            </article>
            <article>
              <p>Digital Life</p>
              <h3><a href="#">Ut alios omittam, hunc appello, quem ille unum secutus est.</a></h3>
              <p>{lorem_short_2}</p>
            </article>
            <article>
              <p>Social</p>
              <h3><a href="#">Bestiarum vero nullum iudicium puto.</a></h3>
              <p>{lorem_short_3}</p>
            </article>
          </div>
        </div>
      </section>
      <section>
        <div>
          <header>
            <h2>Testimonials</h2>
            <p>We are more than a digital company</p>
          </header>
          <div>
            <article>
              <blockquote>I am completely blown away. Thanks to Techium, we've just launched our 5th website!</blockquote>
              <cite>Yuri Y.</cite>
            </article>
            <article>
              <blockquote>Thank you so much for your help. Techium company is awesome!</blockquote>
              <cite>Dorrie S.</cite>
            </article>
            <article>
              <blockquote>I love your system. Definitely worth the investment. I'd be lost without Techium company.</blockquote>
              <cite>Sven H.</cite>
            </article>
          </div>
        </div>
      </section>
      <section>
        <div>
          <header>
            <h2>Contact</h2>
            <p>We like to know new people</p>
          </header>
          <div>
            <p>{lorem_short_1}</p>
            <a href="contact.html">Get in touch</a>
          </div>
        </div>
      </section>
    </main>
    <footer>
      <div>
        <ul>
          <li><a href="https://www.facebook.com/HolbertonSchool/">Facebook</a></li>
          <li><a href="https://twitter.com/holbertonschool">Twitter</a></li>
          <li><a href="https://www.instagram.com/holbertonschool/">Instagram</a></li>
        </ul>
      </div>
      <hr>
      <p>© 2020 Techium, made with ♥ by students at Holberton School.</p>
      <div>
        <ul>
          <li><a href="#">Terms of Use</a></li>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Cookie Policy</a></li>
        </ul>
      </div>
    </footer>
  </body>
</html>"""

# -------------------------------------------------------------
# FINAL STYLEGUIDE PAGE (Tasks 26, 28, 30)
# -------------------------------------------------------------
final_styleguide = head_base.format("Styleguide - Techium") + """
  <body>
    <header></header>
    <main>
      <section>
        <header>
          <h2>Headings</h2>
        </header>
        <h1>Heading level 1</h1>
        <h2>Heading level 2</h2>
        <h3>Heading level 3</h3>
        <h4>Heading level 4</h4>
        <h5>Heading level 5</h5>
        <h6>Heading level 6</h6>
      </section>
      <section>
        <header>
          <h2>Paragraph</h2>
        </header>
        <h2>Heading with a subtitle</h2>
        <p>This is my subtitle</p>
        <p>Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet. Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh in adipiscing blandit tempus accumsan.</p>
      </section>
      <section>
        <header>
          <h2>Lists</h2>
        </header>
        <div>
          <h3>Unordered</h3>
          <ul>
            <li>Dolor pulvinar etiam magna etiam.</li>
            <li>Sagittis adipiscing lorem eleifend.</li>
            <li>Felis enim feugiat dolore viverra.</li>
          </ul>
          <h3>Ordered</h3>
          <ol>
            <li>Dolor pulvinar etiam magna etiam.</li>
            <li>Sagittis adipiscing lorem eleifend.</li>
            <li>Felis enim feugiat dolore viverra.</li>
          </ol>
          <h3>Definition</h3>
          <dl>
            <dt>Definition List title</dt>
            <dd>Definition text.</dd>
            <dt>Startup</dt>
            <dd>A startup company or startup is a company or temporary organization designed to search for a repeatable and scalable business model.</dd>
            <dt>Water</dt>
            <dd>A colorless, transparent, odorless liquid that forms the seas, lakes, rivers, and rain and is the basis of the fluids of living organisms.</dd>
          </dl>
        </div>
      </section>
      <section>
        <header>
          <h2>Horizontal rule</h2>
        </header>
        <div>
          <hr>
        </div>
      </section>
      <section>
        <header>
          <h2>Blockquotes</h2>
        </header>
        <div>
          <h3>Inline quote</h3>
          <q>Stay hungry. Stay foolish.</q>
        </div>
        <div>
          <h3>Blockquote</h3>
          <blockquote>I will be the leader of a company that ends up being worth billions of dollars, because I got the answers. I understand culture. I am the nucleus. I think that’s a responsibility that I have, to push possibilities, to show people, this is the level that things could be at.</blockquote>
          <cite>Kanye West, Musician</cite>
        </div>
      </section>
    </main>
    <footer></footer>
  </body>
</html>"""

# Generate all intermediate Index files needed for the checker
index_files = ["20-index.html", "21-index.html", "22-index.html", "23-index.html", "24-index.html", "25-index.html", "27-index.html", "29-index.html"]
for file in index_files:
    with open(file, "w") as f:
        f.write(final_index)

# Generate all intermediate Styleguide files needed for the checker
styleguide_files = ["26-styleguide.html", "28-styleguide.html", "30-styleguide.html"]
for file in styleguide_files:
    with open(file, "w") as f:
        f.write(final_styleguide)

print("All final HTML files generated successfully!")
