from django.core.management.base import BaseCommand
from main.models import Blog

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        if Blog.objects.exists():
            self.stdout.write(self.style.WARNING('Community/Blog data already exists. Skipping population.'))
            return
        
        # Create sample blog entries
        Blog.objects.create(
            timestamp='2023-10-01',
            name = "PyCon Nambia 2024",
            description="PyCon Namibia is part of a global series of conferences focused on Python programming, bringing together individuals from all backgrounds to learn, collaborate, and drive innovation.",
            body="""
            <p><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/pynam.jpeg" style="height:500px; width:500px" /></p>

            <p>Location: Windhoek Namibia</p>

            <p>Role: Speaker</p>

            <p>Talk Title: Creating Games in Python</p>

            <p>At&nbsp;<strong>PyCon Namibia 2024</strong>, held in&nbsp;<strong>Windhoek, Namibia</strong>, I participated as a&nbsp;<strong>speaker</strong>&nbsp;and presented a talk titled&nbsp;<strong>&quot;Creating Games in Python.&quot;</strong>&nbsp;In my talk, I shared my experience developing a Pygame-based game called&nbsp;<em>Space Battle,</em>&nbsp;where players control a spaceship with the mouse and fire lasers at obstacles. I discussed the fundamentals of game design and demonstrated how Python can be used to create engaging, interactive games. I also conducted a hands-on workshop, guiding participants in building&nbsp;<em>Space Battle</em>&nbsp;while introducing them to essential game design principles and showcasing Pygame as a beginner-friendly tool for game development.</p>
            """,
            image="blog/pynam1.jpeg",
            slug="pycon-nambia-2024",
            is_active=True
        )

        Blog.objects.create(
                timestamp='2023-10-01',
                name = "Black Python Devs Leadership Summit 2024",
                description="The Black Python Devs Leadership Summit is a premier event that brings together Black Python developers from around the world to share knowledge, foster community, and promote diversity in the tech industry.",
                body="""
                <p><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/bpd-sum.jpeg" style="height:500px; width:500px" /></p>

                <p>Location: Durham, North Carolina, USA</p>

                <p>Role: Speaker</p>

                <p>Talk Title: Building a Python Community in Zimbabwe</p>

                <p>At the&nbsp;<strong>Black Python Devs Leadership Summit</strong>&nbsp;in&nbsp;<strong>Durham, North Carolina, USA</strong>, I participated as a&nbsp;<strong>speaker</strong>, delivering a talk titled&nbsp;<strong>&quot;Building a Python Community in Zimbabwe.&quot;</strong></p>

                <p>Drawing on ideas from Malcolm Gladwell&rsquo;s book&nbsp;<em>Outliers,</em>&nbsp;I emphasized the importance of providing Zimbabweans with opportunities to develop their skills and the concept of the&nbsp;<strong>10,000-hour rule.</strong>&nbsp;My talk explored the critical question:&nbsp;<em>Where can Zimbabweans get their 10,000 hours?</em></p>

                <p>I shared my efforts to create these opportunities by organizing&nbsp;<strong>workshops</strong>&nbsp;and&nbsp;<strong>events</strong>&nbsp;that focus on&nbsp;<strong>hands-on Python programming, discussions, and networking.</strong>&nbsp;I highlighted a workshop held in&nbsp;<strong>Dzivarasekwa, Harare</strong>&nbsp;and outlined my vision for a future project,&nbsp;<strong>&quot;PyCreate Zim,&quot;</strong>&nbsp;which aims to offer a structured, month-long program to help participants actively develop their skills and grow the Python community in Zimbabwe.</p>
                """,
                image="blog/bpd-summit-card-deck.jpg",
                slug="black-python-devs-leadership-summit",
                is_active=True
        )

        Blog.objects.create(
            timestamp = '2023-10-01',
            name = "Pycon Zimbabwe / Django Girls Harare 2024",
            description = "PyCon Zimbabwe is a premier Python conference in Zimbabwe, fostering community, collaboration, and innovation among Python developers and enthusiasts.",
            body = """
            <p><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/pyzim.JPG" style="height:326px; width:500px" /></p>

            <p>Location: Harare, Zimbabwe</p>

            <p>Role: Organizer</p>

            <p>Team: Django Girls Workshop, Program Committee&nbsp;</p>

            <p>At&nbsp;<strong>PyCon Zimbabwe 2024</strong>, held in&nbsp;<strong>Harare, Zimbabwe</strong>, I served as an&nbsp;<strong>organizer</strong>&nbsp;on the&nbsp;<strong>Program Committee</strong>&nbsp;and as the&nbsp;<strong>lead organizer</strong>&nbsp;for the&nbsp;<strong>Django Girls Workshop.</strong></p>

            <p>The conference, held in&nbsp;<strong>November 2024</strong>, marked our first gathering since 2019, and our theme,&nbsp;<strong>&quot;Bridging Gaps and Building Bridges,&quot;</strong>&nbsp;reflected our commitment to rebuilding and reconnecting the Python community in Zimbabwe.</p>

            <p>The event spanned&nbsp;<strong>three days</strong>&nbsp;and featured diverse sessions, including a&nbsp;<strong>Django Girls Workshop</strong>, which I led. This workshop was a key initiative to promote&nbsp;<strong>diversity</strong>&nbsp;in our Python community, providing an inclusive space for new developers, particularly women, to learn and engage with Python and Django.</p>

            <p><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/IMG_0585.jpg" style="height:375px; width:500px" /></p>
            """,
            image="blog/zimpy.jpeg",
            slug = "pycon-zimbabwe-django-girls-harare-2024",
            is_active = True
        )

        Blog.objects.create(
            timestamp = '2023-10-01',
            name = "DjangoCon US 2024",
            description = "DjangoCon US is the premier conference for Django developers, offering a platform for knowledge sharing, networking, and collaboration within the Django community.",
            body = """
            <p><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/djcon-org.jpeg" style="height:333px; width:500px" /></p>

            <p>Location: Durham, North Carolina, USA</p>

            <p>Role: Organizer</p>

            <p>Teams: Programs, Hackathon</p>

            <p>At&nbsp;<strong>DjangoCon US 2024</strong>, held in&nbsp;<strong>Durham, North Carolina, USA</strong>, I contributed as an&nbsp;<strong>organizer</strong>, working on the&nbsp;<strong>Programs</strong>&nbsp;and&nbsp;<strong>Hackathon</strong>&nbsp;teams.</p>

            <p>In my role, I helped shape the conference&#39;s schedule and curated sessions highlighting diverse perspectives and cutting-edge developments in the Django ecosystem. Additionally, I co-organized the&nbsp;<strong>Hackathon</strong>, providing attendees with a collaborative environment to work on Django-related projects, exchange ideas, and build solutions. This role allowed me to foster innovation and engagement within the Django community while creating hands-on learning and networking opportunities. Here are some interviews I conducted at the conference. Check them out below.</p>

            <p><a href="https://youtu.be/FcDVSUh-Njk?si=C3tLNVoQVrWRbkXi"><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/interview1.jpg" style="height:281px; width:500px" /></a></p>

            <p><a href="https://youtu.be/f2gqngd4KP4?si=4qPKsdXftSSU4pYo"><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/interview2.jpg" style="height:375px; width:500px" /></a></p>

            <p>&nbsp;</p>
            """,
            image = "blog/dj-us.jpg",
            slug = "djangocon-us-2024",
            is_active = True 
        )

        Blog.objects.create(
            timestamp = '2023-10-01',
            name = "PyCon Nigeria 2024",
            description = "PyCon Nigeria is a premier Python conference in Nigeria, fostering community, collaboration, and innovation among Python developers and enthusiasts.",
            body = """
            <p><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/pynigeria.jpeg" style="height:500px; width:500px" /></p>

            <p>Location: Lagos, Nigeria</p>

            <p>Role: Speaker</p>

            <p>Talk Title: Food of Love: Python&#39;s Insights into my Life&#39;s Soundtrack / Empowering African Developers: Building an NBA fan Community with Django</p>

            <p>At&nbsp;<strong>PyCon Nigeria 2024</strong>, held in&nbsp;<strong>Lagos, Nigeria</strong>, I was scheduled to participate as a&nbsp;<strong>speaker</strong>, presenting two talks:</p>

            <ol>
                <li>
                <p><strong>&quot;Food of Love: Python&#39;s Insights into my Life&#39;s Soundtrack&quot;</strong>&nbsp;&ndash; This talk showcased my Django project,&nbsp;<em>Food of Love</em>, which analyzes lyrical content in musicians&#39; catalogs and generates word cloud visualizations of recurring themes. I planned to discuss how Python and data visualization can provide unique insights into music, blending technology with personal creativity.</p>
                </li>
                <li>
                <p><strong>&quot;Empowering African Developers: Building an NBA Fan Community with Django&quot;</strong>&nbsp;&ndash; This talk centered on my Django application,&nbsp;<em>ShotGeek</em>, which delivers NBA stats and player comparisons. I aimed to share how I used Django to create a user-centric platform for basketball enthusiasts while highlighting opportunities for African developers to engage in open-source communities and build impactful applications.</p>
                </li>
            </ol>

            <p>Unfortunately, I was unable to attend PyCon Nigeria 2024, but I remain proud of my contributions to the program.</p>

            <p>&nbsp;</p>
            """,
            image = "blog/pynigcon.jpg",
            slug = "pycon-nigeria-2024",
            is_active = True
        )

        Blog.objects.create(
            timestamp = "2023-10-01",
            name = "GitHub Constellation 2024",
            description = "GitHub Constellation is a premier conference that brings together developers, open-source enthusiasts, and industry leaders to explore the latest trends in software development and collaboration.",
            body = """
            <p><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/conferences/GITHUB-6_Original.jpg" style="height:750px; width:500px" /></p>

            <p>Location: Johannesburg, South Africa</p>

            <p>Role: Speaker</p>

            <p>Talk Title: All In Africa Panel</p>

            <p>At&nbsp;<strong>GitHub Constellation 2024</strong>, held in&nbsp;<strong>Johannesburg, South Africa</strong>, I participated as a&nbsp;<strong>panelist</strong>&nbsp;on the&nbsp;<strong>&quot;All In Africa&quot; Panel.</strong></p>

            <p>During the panel, I addressed several key questions, including:</p>

            <ol>
                <li>
                <p><strong>Sharing my background</strong>&nbsp;&ndash; I spoke about my journey as a developer and community organizer, highlighting what inspired me to advocate for the GitHub&nbsp;<strong>All In Africa</strong>&nbsp;program in Southern Africa.</p>
                </li>
                <li>
                <p><strong>Challenges addressed by the program</strong>&nbsp;&ndash; I discussed the program&#39;s potential to tackle barriers such as limited access to resources, mentorship, and global tech opportunities, which often hinder the growth of African developers.</p>
                </li>
                <li>
                <p><strong>The program&rsquo;s future role</strong>&nbsp;&ndash; I shared my vision for how initiatives like GitHub All In Africa can evolve to further support tech talent in the region by fostering collaboration, creating more accessible learning paths, and driving innovation tailored to Africa&#39;s unique needs.</p>
                </li>
            </ol>

            <p>The panel was an enriching experience, emphasizing the importance of building ecosystems that empower African developers to thrive.</p>
            """,
            image = "blog/githubcon.png",
            slug = "github-constellation-2024",
            is_active = True
        )

        Blog.objects.create(
            timestamp = "2023-10-01",
            name = "PyCon Namibia 2025",
            description = "PyCon Namibia is a premier Python conference in Namibia, fostering community, collaboration, and innovation among Python developers and enthusiasts.",
            body = """
            <h1>Coming in February 2025</h1>

            <p>Location: Windhoek Namibia</p>

            <p>Role: Speaker</p>

            <p>Talk Title: Designing for Users: Building a User-Centric Django App for NBA fans</p>
            """,
            image = "blog/nam2.jpg",
            slug = "pycon-namibia-2025",
            is_active = True
        )

        Blog.objects.create(
            timestamp = "2023-10-01",
            name = "DjangoCon Africa 2025",
            description = "DjangoCon Africa is a premier conference for Django developers in Africa, offering a platform for knowledge sharing, networking, and collaboration within the Django community.",
            body = """
            <h1>Coming in August 2025</h1>

            <p>Location: Tanzania</p>

            <p>Role: Organizer</p>

            <p>Teams: Design, Sponsorship</p>
            """,
            image = "blog/djconAfri.jpg",
            slug = "djangocon-africa-2025",
            is_active = True
        )

        Blog.objects.create(
            timestamp = "2023-10-01",
            name = "Stanford Code In Place 2023",
            description = "Stanford Code In Place is an introductory programming course offered by Stanford University, designed to teach the fundamentals of coding using Python.",
            body = """
            <p><a href="https://digitalcredential.stanford.edu/check/7CE65D067CCE717EBF28C62A1AC5063CF71466C77DC93667102BCB313696FD67UlE0eWpLU0dmaVJmMmM3Ykx0THY5MkVCYVVFMHlLL1ZrYVY1MGljNEkwYXhCWUN3"><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/cip-cert.png" style="height:443px; width:600px" /></a></p>

            <p>Location: Remote</p>

            <p>Role: Section Leader</p>

            <p>In&nbsp;<strong>2023</strong>, I served as a&nbsp;<strong>Section Leader</strong>&nbsp;for&nbsp;<strong>Stanford Code in Place</strong>, a program designed to teach programming fundamentals through Stanford&#39;s CS106A course.</p>

            <p>As a section leader, I supported students by facilitating&nbsp;<strong>weekly discussion sections</strong>, answering questions, and providing guidance on coding assignments. I helped create a collaborative learning environment by encouraging problem-solving, fostering discussions on programming concepts, and offering personalized assistance to ensure students gained a strong foundation in Python programming. I also collaborated with the teaching team to ensure that course content was accessible and engaging for students at various skill levels.</p>

            <p>This role allowed me to contribute to developing emerging programmers and further my passion for teaching and community-driven learning.</p>
                        """,
            image = "blog/codein.jpg",
            slug = "stanford-code-in-place-2023",
            is_active = True
        )

        Blog.objects.create(
            timestamp = "2023-10-01",
            name = "Teaching Python Podcast",
            description = "The 'Teaching Python Podcast,' is the go-to podcast for anyone interested in the intersection of education and coding. Hosted by Kelly Paredes and Sean Tibor,",
            body = """
            <p><a href="https://www.teachingpython.fm/144"><img alt="" src="https://my-world-boogie.s3.eu-north-1.amazonaws.com/myworld_images/pod.png" style="height:345px; width:600px" /></a></p>

            <p>Location: Remote</p>

            <p>Role: Guest on the <em><strong>Teaching Python Podcast with&nbsp;Kelly Paredes and&nbsp;Sean Tibor</strong></em></p>

            <p>&nbsp;</p>

            <p>I had the privilege of being a guest on the <strong>Teaching Python</strong> podcast with Sean and Kelly, where I shared my experiences building Python communities in Zimbabwe.</p>

            <p>During the episode, we discussed my journey as a community organizer, highlighting the initiatives I&rsquo;ve led, and Python programming events aimed at fostering a vibrant tech ecosystem in the region. I spoke about the challenges we face, including limited access to resources, connectivity issues, and the need to create sustainable opportunities for learning and collaboration.</p>

            <p>We also explored the resilience and creativity of the Zimbabwean tech community, as well as the role of global partnerships and local events in overcoming these barriers. It was an inspiring conversation about the power of Python and community in driving change and empowering new developers in Africa. <em><strong><a href="https://www.teachingpython.fm/144">Check out the episode.</a></strong></em></p>
            """,
            image = "blog/teach.jpeg",
            slug = "teaching-python-podcastt",
            is_active = True
        )

        self.stdout.write(self.style.SUCCESS('Community/Blog data populated successfully.'))